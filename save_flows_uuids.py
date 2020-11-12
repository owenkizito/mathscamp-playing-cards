import json
import csv
import re

cardcsv = open('cards.csv')
reader = csv.reader(cardcsv)

flows_file = open("./output/generated_flows.json", "r")
flows_json = json.load(flows_file)

flows_info = []


for row in reader:
    name_of_flow = row[1].lower().replace(" ", "-")
    flow = list(filter(lambda fl: fl["name"].replace("Content-","").replace("Puzzle-","").replace("Counting-","").replace("Funfact-","").replace("Game-","")== name_of_flow, flows_json["flows"] ))
    
    if len(flow) != 1:
        print("flow not found " + name_of_flow)
        continue
    
    curr_flow_info = {}
    curr_flow_info["flow name"] = flow[0]["name"]
    curr_flow_info["doc name"] = row[1]
    curr_flow_info["uuid"] = flow[0]["uuid"]
    curr_flow_info["card number"] = row[0]

    flows_info.append(curr_flow_info)



with open('./flows_info.json', 'w') as outfile:
    json.dump(flows_info, outfile,indent=2)



    
        