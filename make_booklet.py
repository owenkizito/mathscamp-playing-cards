import csv
import json
import markdown
import re

suits = {'H' : "hearts", "S" : "spades", "C" : "clubs", "D" : "diamonds"}

out = open("booklet.md", "w")
# out.write("# Puzzles\n\n")

cardcsv = open('cards.csv')
reader = csv.reader(cardcsv)
for row in reader:
    # out.write("    {\n")
    card = row[0]
    filename = row[1].lower().replace(" ", "-")
    suit = suits[card[0]]
    rank = card[1:]

    with open("json/" + filename + ".json", "r") as read_file:
        print(filename)
        data = json.load(read_file)
        ctype = data["metadata"]["type"]
        if ctype == "counting":
            ctype = "puzzle"

        out.write("## " + card + " - " + data["title"] + "\n\n")
        out.write(data["main_version"]["statement"] + "\n\n")
        if ctype == "puzzle" or ctype == "funfact":
            if "hint" in data["main_version"]:
                out.write("**Hint**: " + data["main_version"]["hint"] + "\n\n")
            out.write("**Explanation**: " + data["main_version"]["explanation"] + "\n\n")
        elif ctype == "game":
            out.write("**Further instructions**: " + data["main_version"]["further_instructions"] + "\n\n")
            out.write("**Strategy Tips**: " + data["main_version"]["strategy_tips"] + "\n\n")
        out.write("### Extension 1\n\n")
        out.write(data["extension_1"]["statement"] + "\n\n")
        if ctype == "puzzle" or ctype == "funfact":
            if "hint" in data["extension_1"]:
                out.write("**Hint**: " + data["extension_1"]["hint"] + "\n\n")
            if "explanation" in data["extension_1"]:
                out.write("**Explanation**: " + data["extension_1"]["explanation"] + "\n\n")
        if "extension_2" in data and "statement" in data["extension_2"]:
            out.write("### Extension 2\n\n")
            out.write(data["extension_2"]["statement"] + "\n\n")
            if ctype == "puzzle" or ctype == "funfact":
                out.write("**Hint**: " + data["extension_2"]["hint"] + "\n\n")
                out.write("**Explanation**: " + data["extension_2"]["explanation"] + "\n\n")

cardcsv.close()
out.close()
with open("booklet.md", "r") as bmd:
    outdata = markdown.markdown(bmd.read())
    with open("booklet.html", "w") as bhtml:
        bhtml.write(outdata)