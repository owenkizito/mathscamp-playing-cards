import json
import csv
import uuid
import re


# From https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


class UuidCollector:
    def __init__(self):
        self.uuids = dict()

    def collect_uuids(self, data):
        if type(data) is not dict:
            return
        for k,v in data.items():
            if k == "type" and v == "enter_flow":
                # We don't want replace uuids of other flows, so don't recurse
                break
            if type(v) is dict:
                self.collect_uuids(v)
            elif type(v) is list:
                for entry in v:
                    self.collect_uuids(entry)
            elif k.find('uuid') != -1:
                # We found a field whose name contains "uuid"
                # We record this uuid and assign a replacement uuid
                if v is not None:
                    self.uuids[v] = str(uuid.uuid4()) # Generate new random UUID to replace it with


uuid_collector = UuidCollector()
ftypes = ["puzzle", "funfact", "game"]
for ftype in ftypes:
    template = "template_" + ftype + ".json"
    with open(template, "r") as read_file:
        data = json.load(read_file)
        uuid_collector.collect_uuids(data)

f_replacements = open("replacements.json", "r")
replacements = json.load(f_replacements)
f_replacements.close()

container_file = open("template_container.json", "r")
container = json.load(container_file)

cardcsv = open('cards.csv')
reader = csv.reader(cardcsv)
for row in reader:
    card = row[0]
    filebase = row[1].lower().replace(" ", "-")

    # Get content specific json file to read from
    filename = "json/" + filebase + ".json"
    file = open(filename, "r")
    data = json.load(file)

    # Get type of content
    ftype = data["metadata"]["type"]
    ftype = ftype.lower().replace(" ", "") # account for different spellings of "funfact"
    ftype_raw = ftype  # the raw type distinguishes between puzzle and counting
    if ftype == "counting":
        # counting uses the same format as puzzle.
        ftype = "puzzle"

    # Get type specific flow template
    flow_fname = "template_" + ftype + ".json"
    if ftype == "puzzle" and "extension_2" not in data:
        flow_fname = "template_puzzle_1extension.json" # puzzles have two extensions by default, but can have one
    flow_template = open(flow_fname, "r").read()
    # Replace title and all UUIDs
    flow_template = flow_template.replace(replacements[ftype]["name"], "Content-" + ftype_raw.title() + "-" + filebase)
    for k,v in uuid_collector.uuids.items():
        flow_template = flow_template.replace(k, v)

    # Collect text snippets to replace in the flow
    replacement_dict = dict()
    for repl in replacements[ftype]["texts"]:
        sections = repl.split(" - ")
        # Find the data corresponding to the subsection specified in the replacement
        current_section = data
        found = True
        try:
            # Find the subsection of interest
            for s in sections:
                current_section = current_section[s.strip().lower().replace(" ", "_")]
        except KeyError:
            if ftype != "puzzle" and sections[0] != "Extension 2":
                # It's ok for puzzles not to have a second extension
                print("Section " + repl + " not found in " + filebase)
            found = False
        if found:
            # References is a list of refs rather than a string
            if type(current_section) == list:
                current_section = ''.join(current_section)
            # if sections[0] != "Extension 2":
            if len(current_section) == 0:
                print("Warning: blank answer in Section " + repl + " of " + filebase)
            elif cleanhtml(current_section)[0] == '[':
                print("Warning: template answer in Section " + repl + " of " + filebase)
            # Put content of section into the replacement dict.
            replacement_dict[repl] = current_section

    # After all the text replacements, we read flow_template as JSON.
    # Check for NRICH references and remove starting node if there aren't any.
    new_flow = json.loads(flow_template)
    if ftype == "puzzle":
        # For puzzles: We determine whether the puzzle is an NRICH puzzle.
        references = ''.join(data["additional_information"]["references"])
        # The references node should be the first node in the flow.
        assert new_flow["nodes"][0]["actions"][0]["text"] == "Additional information - References"
        if references.lower().find("nrich") != -1:
            # This puzzle is an NRICH puzzle. Fill references node with NRICH information.
            # print("NRICH PUZZLE: " + filebase)
            new_flow["nodes"][0]["actions"][0]["text"] = "The following is based on an NRICH puzzle\\n https://nrich.maths.org/"
        else:
            # Not an NRICH puzzle. Remove references node from flow and UI.
            # print("not NRICH PUZZLE: " + filebase)
            uuid_to_remove = new_flow["nodes"][0]["uuid"]
            del new_flow["nodes"][0]
            new_flow["_ui"]["nodes"].pop(uuid_to_remove)

    # # Replace all these text snippets.
    # # We do a lazy text replacement on the unparsed JSON.
    # for k,v in replacement_dict.items():
    #     flow_template = flow_template.replace(k, v)

    # For each flow node, check the text for whether it should be replaced.
    # If so, strip the target text to replace the template from images,
    # and add these images as attachments instead.
    for node in new_flow["nodes"]:
        if "actions" in node:
            for action in node["actions"]:
                if "text" not in action:
                    continue
                text = action["text"]
                for k,v in replacement_dict.items():
                    if text == k:
                        images = re.findall(r'<img.*?>', v)
                        for image in images:
                            image_filename = re.search(r'src=\".*?\"', image).group()[12:-1]
                            # print(image[4:-1])
                            action["attachments"].append("@{{fields.image_path & \"{}\"}}".format(image_filename))
                        v_stripped = re.sub(r'<img.*?>', "", v).strip()  # strip image tags and trailing whitespace
                        # We also strip Markdown formatting and replace linebreaks with \n,
                        # because RapidPro doesn't support Markdown and JSON doesn't allow linebreaks.
                        v_stripped = cleanhtml(v_stripped).replace("\n\n", "\\n").replace("\n", "\\n")
                        action["text"] = v_stripped
        if "router" in node and "cases" in node["router"]:
            for case in node["router"]["cases"]:
                if "arguments" not in case:
                    continue
                for i,arg in enumerate(case["arguments"]):
                    for k,v in replacement_dict.items():
                        if arg == k:
                            case["arguments"][i] = v



    # Add this flow to the template_container.
    container["flows"].append(new_flow)

# Save filled up template container as JSON file
generated_flows = open("generated_flows.json", "w")
json.dump(container, generated_flows, indent=2)   # ensure_ascii=False
generated_flows.close()
