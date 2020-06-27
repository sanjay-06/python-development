#!/usr/bin/env python3
import re
import sys
import operator
import csv

users={}
errors={}

f=open("syslog.log")
for line in f:
    line=line.strip()
    username=(re.search(r"\((.*)\)",line)).group(1)
    msg=(re.search(r"(ERROR|INFO)",line)).group(1)
    if (username not in users):
          user_count = {'INFO': 0, 'ERROR': 0}
        users.update(sub)
          users[username] = user_count
    users[username][msg]+=1

    if msg=="ERROR":
        err=(re.search(r"ERROR (.*) ",line)).group(1)
        if (err not in errors):
            errors[err]=0
        errors[err]+=1
f.close()


users2=[]
errors2=[]
for key in sorted(users.keys()):
    users2.append([key,users[key]["INFO"],users[key]["ERROR"]])

for key, value in sorted(errors.items(), key=lambda item: item[1],reverse=True):
    errors2.append([key, value])

users2.insert(0,["Username","INFO","ERROR"])
errors2.insert(0,["Error","Count"])

fe=open("error_message.csv","w")
fu=open("user_statistics.csv","w")

writer1=csv.writer(fe)
writer2=csv.writer(fu)
writer1.writerows(errors2)
writer2.writerows(users2)

fe.close()
fu.close()
