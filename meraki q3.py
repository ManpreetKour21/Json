# Q.3 Python object ko json string mai convert karne ka program likho?
import json
dict={"hello":1}
json.dumps(dict)
with open("meraki3.json","w")as dict1:
    json.dump(dict,dict1,indent=1)
