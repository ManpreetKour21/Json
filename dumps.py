import json


data={
    "year":'harry',
    "car": ['rt','yu 67','rty'],
    "hdfg":('roti',540),
    "dfg":False
}
x=json.dumps(data)
print(x)

# print(json.dumps(None))