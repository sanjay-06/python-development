import csv
file=open("file.txt")
print(file.readline())
with open("file.txt") as file:
    for line in file:
        print(line.upper().strip())
with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"],row["users"]))
users=[{"name":"sanjay","username":"sol","department":"Development"}]
keys=["name","username","department"]
with open ("file.csv","w") as files:
    file_w=csv.DictWriter(files,filenames=keys)
    file_w.writeHeader()
    file_w.writerows(users)
