import os
import json

categories = {"POLITICS", "TRAVEL", "BUSINESS", "SPORTS", "TECH", "SCIENCE"}

def separate(cat: str, line: str):

    current_directory = os.getcwd() 
    write_location = os.path.join(current_directory, (cat.lower() + ".json"))

    with open(write_location, mode="a") as f:
        f.write(line)

with open("./News_Category_Dataset_v2.json", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):

    print('#%d\r' % i, end='', flush=True)
    # Load in json line as a dictionary
    json_line = json.loads(line)

    curr_category = json_line["category"]
    
    if curr_category in categories:
        separate(curr_category, line)