import csv
import json

suits = {'H' : "hearts", "S" : "spades", "C" : "clubs", "D" : "diamonds"}
out = open("cards.js", "w")

f = open('cards.csv')
reader = csv.reader(f)
out.write("var cards = [\n")
for row in reader:
    out.write("    {\n")
    card = row[0]
    filename = row[1]
    suit = suits[card[0]]
    rank = card[1:]

    with open("json/" + filename + ".json", "r") as read_file:
        data = json.load(read_file)
        text = data["Main Version"]["Statement"]
        text = text.replace("\n", "\\n")
        text = text.replace("\"", "\\\"")
        out.write('''        "rank": "{}",
        "suit": "{}",
        "text": "{}"\n'''.format(rank, suit, text))

    out.write("    },\n")

out.write("]\n")
f.close()