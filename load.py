# Q.1 Json data ko python object main convert karne ka program likho?.
# Ans.1

import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])