import os
import sys
import string
import json
from scraper import Scraper
from console_progress import print_progress
from time import sleep

categories = {"POLITICS", "TRAVEL", "BUSINESS", "SPORTS", "TECH", "SCIENCE"}
cat_mapping = {
    "POLITICS": 0,
    "TRAVEL": 0,
    "BUSINESS": 0,
    "SPORTS": 0,
    "TECH": 0,
    "SCIENCE": 0
}

def create_folders(): 

    current_directory = os.getcwd() 
    dataset_path = os.path.join(current_directory, "data")

    dirs = os.listdir(dataset_path)
    
    for cat in categories:
        
        if cat not in dirs:
            path = os.path.join(dataset_path, cat)
            os.mkdir(path)

def format_filename(s):
    """
    Take a string and return a valid filename constructed from the string.
    Uses a whitelist approach: any characters not present in valid_chars are
    removed. Also spaces are replaced with underscores.
    
    Note: this method may produce invalid filenames such as ``, `.` or `..`
    When I use this method I prepend a date string like '2009_01_15_19_46_32_'
    and append a file extension like '.txt', so I avoid the potential of using
    an invalid filename.

    Taken from: https://gist.github.com/seanh/93666
 
    """

    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    return filename

def print_to_file(cat: str, title: str, content: str): 
    current_directory = os.getcwd() 
    dataset_path = os.path.join(current_directory, "data")
    topic_location = os.path.join(dataset_path, cat)
    write_location = os.path.join(topic_location, (format_filename(title) + ".txt"))

    with open(write_location, mode="w", encoding="utf-8") as f:
        f.write(content)

def print_problematic_file(cat: str, url: str, problem: str): 
    current_directory = os.getcwd() 
    dataset_path = os.path.join(current_directory, "data")
    write_location = os.path.join(dataset_path, ("problematic_files_" + cat + ".csv"))

    with open(write_location, "a", encoding="utf-8") as myfile:
        myfile.write(cat + "," + url + "," + problem + "\n")

create_folders()

# Get each line of the json file
with open("./business.json", "r") as f:
    lines = f.readlines()

scraper = Scraper()

for i, line in enumerate(lines):


    # Load in json line as a dictionary
    json_line = json.loads(line)

    curr_category = json_line["category"]
    curr_heading = json_line["headline"]
    curr_link = json_line["link"]

    print("#%d" % i)
    print("TOPIC:   %s" % curr_category)
    print("Link:    %s" % curr_link)
    print("Heading: %s" % (curr_heading + "\n"))
        
    # Set up the web client to read
    try:
        scraper.update_web_client(curr_link)
    except Exception as e:
        # Link is invalid
        old_val = cat_mapping[curr_category]
        new_val = old_val + 1
        cat_mapping[curr_category] = new_val
        print_problematic_file(curr_category, curr_link, "LINK")
        print("Finished problematic: LINK")
        continue
    
    if curr_category == "TRAVEL":
        link_text = scraper.get_text_travel()
    else:
        link_text = scraper.get_text()

    if link_text != "":
        
        print_to_file(curr_category, curr_heading, link_text)
        print("Finished writing\n")
        
    else:
        print("PROBLEM")
        old_val = cat_mapping[curr_category]
        new_val = old_val + 1
        cat_mapping[curr_category] = new_val
        print_problematic_file(curr_category, curr_link, "TEXT")
        print("Finished problematic: TEXT\n")
            


print("Finished!\n")
for keys, values in cat_mapping.items():
    print("%s        -> %d" % (keys, values))
