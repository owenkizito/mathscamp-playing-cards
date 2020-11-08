# -*- coding: utf-8 -*-
# This code is a modified version of md_to_json.py from the repository
# https://github.com/njvack/markdown-to-json
# Original code by Nate Vack <njvack@freshforever.net>

from __future__ import unicode_literals, absolute_import
from collections import OrderedDict 
from contextlib import contextmanager
from functools import reduce
from markdown import markdown
from shutil import copyfile
import json
import logging
import operator
import os
import sys
import re

import CommonMark

logging.basicConfig(
    format="%(message)s", stream=sys.stderr, level=logging.INFO)


# From https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


"""
This module contains a class to change a CommonMark.py AST into a nested
OrderedDict structure. Its rules:

* Headings are keys. Stuff following headings are values.
* Values are generally treated as strings, and left unchanged; in other words
  you'll generally get the markdown.
* The exception is lists -- they're turned into arrays.
* Lists must occur alone after a heading.
* You can nest lists; you'll get nested arrays.
* To increase key nesting level, use higher-numbered headers. You can't go
  past 6. That would be insane anyhow.
* You'll want to monotonically increasing heading numbers (eg, a H1 followed
  by a H2) -- if you jump, it's valid but the high-numbered headings won't be
  treated as keys.
* Content ordering is unchanged.

To use:

md = \"""
# First Heading

Foo bar baz corge

# Second Heading

* List 1
* List 2
\"""

ast = CommonMark.DocParser().parse(md)
nested = CMarkASTNester().nest(ast)

Note that you'll want to turn the nested structure into a string.

In addition, this module contains a Renderer class; this transforms the nested
structure from CMarkASTNester into an OrderedDict with strings as keys and
strings, lists, or OrderedDicts as values.
"""


class CMarkASTNester(object):
    def __init__(self):
        super(CMarkASTNester, self).__init__()

    def nest(self, ast):
        return self._dictify_blocks(ast.children, 1)

    def _dictify_blocks(self, blocks, heading_level):
        def matches_heading(block):
            return block.t == 'ATXHeader' and block.level == heading_level

        if not any((matches_heading(b) for b in blocks)):
            self._ensure_list_singleton(blocks)
            return blocks

        splitted = dictify_list_by(blocks, matches_heading)
        for heading, nests in splitted.items():
            splitted[heading] = self._dictify_blocks(nests, heading_level + 1)
        return splitted

    def _ensure_list_singleton(self, blocks):
        lists = [e for e in blocks if e.t == 'List']
        if len(blocks) > 1 and len(lists) > 0:
            l = lists[0]
            raise ContentError(
                "Error at line {0}: Can't mix lists and other content".format(
                    l.start_line))


class ContentError(ValueError):
    pass


def dictify_list_by(l, fx):
    result = OrderedDict()
    cur = None
    children = []
    for item in l:
        if fx(item):
            if cur:
                # Pop cur, children into result
                result[cur] = children
            cur = item
            children = []
            continue
        children.append(item)
    if cur:
        result[cur] = children
    return result


class Renderer(object):
    def __init__(self):
        super(Renderer, self).__init__()

    def stringify_dict(self, d):
        out = OrderedDict(
            [
                (self._render_block(k), self._valuify(v))
                for k, v in d.items()
            ])
        return out

    def _valuify(self, cm_vals):
        if hasattr(cm_vals, 'items'):
            return self.stringify_dict(cm_vals)
        if len(cm_vals) == 0:
            return ''
        first = cm_vals[0]
        if first.t == 'List':
            return self._render_List(first)
        return "\n\n".join([self._render_block(v) for v in cm_vals])

    def _render_block(self, block):
        method_name = "_render_{0}".format(block.t)
        method = self._render_generic_block
        if hasattr(self, method_name):
            method = getattr(self, method_name)
        return method(block)

    def _render_generic_block(self, block):
        if hasattr(block, 'strings') and len(block.strings) > 0:
            return "\n".join(block.strings)
        if len(block.children) > 0:
            return [self._render_block(b) for b in block.children]

    def _render_List(self, block):
        # We need to de-nest this one level -- we'll use the trick that
        # lists can be added to do this.
        list_items = [self._render_block(li) for li in block.children]
        return reduce(operator.add, list_items)

    def _render_FencedCode(self, block):
        return "```\n" + block.string_content + "```"


@contextmanager
def writable_io_or_stdout(filename):
    if filename is None:
        yield sys.stdout
        return
    else:
        try:
            f = open(filename, 'w')
            yield f
            f.close()
        except:
            logging.error("Error: Can't open {0} for writing".format(
                filename))
            sys.exit(1)


def get_markdown_ast(markdown_file):
    try:
        f = open(markdown_file, 'r')
        return CommonMark.DocParser().parse(f.read())
    except:
        logging.error("Error: Can't open {0} for reading".format(
            markdown_file))
        sys.exit(1)
    finally:
        f.close()


# For a given image path, replace it with the new (flattened)
# destination path.
def move_image_path(img_path):
    img_path = img_path.replace("images/", "")
    img_path = img_path.replace("%20", "_")
    return "images/" + img_path

# Take a Markdown string, replace all Markdown content with HTML,
# assign all HTML image tags an additional class attribute
# and change their path to a different canonical location.
def demark(data):
    # Do intermediate substitutions because the markdown conversion
    # would mess up the formatting of these otherwise
    data = re.sub(r"\\\[", "XXLaTeXStartXX", data, flags=re.MULTILINE)
    data = re.sub(r"\\\]", "XXLaTeXEndXX", data, flags=re.MULTILINE)
    data = re.sub(r"\\<", "XXUnicodeStartXX", data, flags=re.MULTILINE)
    data = re.sub(r"\\>", "XXUnicodeEndXX", data, flags=re.MULTILINE)
    data = markdown(data)
    # Now do the actual replacement: For formulas that are provided in both
    # LaTeX and Unicode, LaTeX is surrounded by these start/end comments,
    # and Unicode is commented out.
    data = re.sub("XXLaTeXStartXX", "<!-- LaTeX Start -->", data, flags=re.MULTILINE)
    data = re.sub("XXLaTeXEndXX", "<!-- LaTeX End -->", data, flags=re.MULTILINE)
    data = re.sub("XXUnicodeStartXX", "<!--", data, flags=re.MULTILINE)
    data = re.sub("XXUnicodeEndXX", "-->", data, flags=re.MULTILINE)
    image_tags = re.findall(r'<img.*?>', data)
    for tag in image_tags:
        match = re.search(r'src=\".*\"', tag)
        if match:
            img_path = match.group()[5:-1]
            new_img_path = move_image_path(img_path)
            copyfile("Markdown/" + img_path.replace("%20", " "), "json/" + new_img_path)
            path_base = os.path.splitext(os.path.basename(new_img_path))[0]
            new_tag = tag.replace(img_path, new_img_path + '" class="' + path_base)
            data = data.replace(tag, new_tag)
        else:
            raise ValueError("HTML img tag without src.")
    return data


# Take a nested structure, turn all keys to lowercase without spaces
# and demark all strings.
def pretty_parse(data):
    if type(data) is OrderedDict or type(data) is dict:
        return OrderedDict((k.strip().lower().replace(" ", "_"), pretty_parse(v)) for k,v in data.items())
    elif type(data) is list:
        return [pretty_parse(e) for e in data]
    elif type(data) is str:
        return demark(data)
    else:
        raise TypeError("Unknown field type in generated json dict.")


def unhtml_nontext(pretty_parsed):
    # Remove HTML tags from some non-html data
    if "title" in pretty_parsed:
        pretty_parsed["title"] = cleanhtml(pretty_parsed["title"])
    if "metadata" in pretty_parsed and "type" in pretty_parsed["metadata"]:
        pretty_parsed["metadata"]["type"] = cleanhtml(pretty_parsed["metadata"]["type"]).lower().replace(" ", "")
    if "main_version" in pretty_parsed and "correct_answer" in pretty_parsed["main_version"]:
        pretty_parsed["main_version"]["correct_answer"] = cleanhtml(pretty_parsed["main_version"]["correct_answer"])
    if "extension_1" in pretty_parsed and "correct_answer" in pretty_parsed["extension_1"]:
        pretty_parsed["extension_1"]["correct_answer"] = cleanhtml(pretty_parsed["extension_1"]["correct_answer"])
    if "extension_2" in pretty_parsed and "correct_answer" in pretty_parsed["extension_2"]:
        pretty_parsed["extension_2"]["correct_answer"] = cleanhtml(pretty_parsed["extension_2"]["correct_answer"])
    return pretty_parsed


def jsonify_markdown(markdown_file, outfile, indent):
    nester = CMarkASTNester()
    renderer = Renderer()
    # with writable_io_or_stdout(outfile) as f:
    with open(outfile, 'w') as f:
        ast = get_markdown_ast(markdown_file)
        nested = nester.nest(ast)
        rendered = renderer.stringify_dict(nested)
        pretty_parsed = pretty_parse(rendered)
        unhtmled = unhtml_nontext(pretty_parsed)
        json.dump(unhtmled, f, indent=indent)
        f.write("\n")
    return 0


# Clean some markdown formatting issues that result from gdocs2md.
def clean_formatting(filename):
    with open(filename, "r+") as f:
        data = f.read()
        data = re.sub(r"^> \*", "*", data, flags=re.MULTILINE)
        data = re.sub(r"^> ", "* ", data, flags=re.MULTILINE)
        data = re.sub(r"^\* 1\.", "(1.)", data, flags=re.MULTILINE)
        data = re.sub(r"^\* 2\.", "(2.)", data, flags=re.MULTILINE)
        # data = re.sub("\"", "'", data)
        f.seek(0)
        f.truncate()
        f.write(data)

if __name__ == '__main__':
    os.makedirs("json/images/", exist_ok=True)
    directory = os.fsencode("Markdown")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        basename = os.path.splitext(os.path.basename(filename))[0]
        if filename.endswith(".md"):
            print("Processing " + filename)
            fin = "Markdown/" + filename
            clean_formatting(fin)
            new_basename = basename.lower().replace(" ", "-")
            fout = "json/{}.json".format(new_basename)
            jsonify_markdown(fin, fout, indent=2)
