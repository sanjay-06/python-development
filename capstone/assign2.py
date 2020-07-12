
#! /usr/bin/env python3
import os
import requests


# path = r'./data/feedback/'

#path used in assignment
path = '/data/feedback/'

files = os.listdir(path)
for file in files:
    feedback = {}
    with open(os.path.join(path, file), 'r') as f:
        lines = f.readlines()
        feedback['title'] = lines[0].strip()
        feedback['name'] = lines[1].strip()
        feedback['date'] = lines[2].strip()
        feedback['feedback'] = lines[3].strip()

    response = requests.post("http://35.226.218.5/feedback/", json=feedback)
    if not response.ok:
        raise Exception("POST failed with status code {}".format(response.status_code))
    print("Successfully added feedback")
