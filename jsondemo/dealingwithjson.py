import json

jsonfile = open("data.json", "r")

data= json.load(jsonfile)
print(data)  # list of dictionaries

jsonfile.close()

addedobj = {"name":"yasmin", "city":"Sherbine"}

data.append(addedobj)
# convert list to string
data_to_json = json.dumps(data, indent=2)
print(data_to_json)

with open('data.json', "w") as fo:
    fo.write(data_to_json)



found = filter(lambda x: x["name"]=='yasmin', data)
print(list(found))





