dict1={
    "name": "David", 
    "class": "I", 
    "age": 6
}

import json
f=open("dict1",mode="w")
data=json.dump(dict1,f)
print(data)
 