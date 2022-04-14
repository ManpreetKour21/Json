# import json
# f=open("file.json",mode="r")
# data=json.load(f)
# print(data)

# import json
# f=open("file.json",mode="r")
# data=json.load(f)
# print(data)

import json
python_obj = {
  "name": "David",
  "class":"I",
  "age": 6  
}
print(type(python_obj))
j_data = json.dumps(python_obj)
print(j_data)



