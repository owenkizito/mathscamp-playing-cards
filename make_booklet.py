import json

import csv
import json

suits = {'H' : "hearts", "S" : "spades", "C" : "clubs", "D" : "diamonds"}

out = open("booklet.md", "w")
# out.write("# Puzzles\n\n")

cardcsv = open('cards.csv')
reader = csv.reader(cardcsv)
for row in reader:
    # out.write("    {\n")
    card = row[0]
    filename = row[1]
    suit = suits[card[0]]
    rank = card[1:]

    with open("json/" + filename + ".json", "r") as read_file:
        print(filename)
        data = json.load(read_file)
        ctype = data["Metadata"]["Type"].lower().replace(" ", "") # canonical spelling
        if ctype == "counting":
            ctype == "puzzle"

        out.write("## " + card + " - " + data["Title"] + "\n\n")
        out.write(data["Main Version"]["Statement"] + "\n\n")
        if ctype == "puzzle" or ctype == "funfact":
            if "Hint" in data["Main Version"]:
                out.write("**Hint**: " + data["Main Version"]["Hint"] + "\n\n")
            out.write("**Explanation**: " + data["Main Version"]["Explanation"] + "\n\n")
        elif ctype == "game":
            out.write("**Further instructions**: " + data["Main Version"]["Further Instructions"] + "\n\n")
            out.write("**Strategy Tips**: " + data["Main Version"]["Strategy tips"] + "\n\n")
        out.write("### Extension 1\n\n")
        out.write(data["Extension 1"]["Statement"] + "\n\n")
        if ctype == "puzzle" or ctype == "funfact":
            if "Hint" in data["Extension 1"]:
                out.write("**Hint**: " + data["Extension 1"]["Hint"] + "\n\n")
            if "Explanation" in data["Extension 1"]:
                out.write("**Explanation**: " + data["Extension 1"]["Explanation"] + "\n\n")
        if "Extension 2 " in data and "Statement" in data["Extension 2 "]:
            out.write("### Extension 2\n\n")
            out.write(data["Extension 2 "]["Statement"] + "\n\n")
            if ctype == "puzzle" or ctype == "funfact":
                out.write("**Hint**: " + data["Extension 2 "]["Hint"] + "\n\n")
                out.write("**Explanation**: " + data["Extension 2 "]["Explanation"] + "\n\n")

cardcsv.close()
out.close()