import json
import json
from textwrap import indent
x = '{ "name":"John", "age":30, "city":"New York"}'
with open("x.json","w")as dict:
    json.dump(x,dict,indent=4)

