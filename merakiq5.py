# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?
# Ans.5
import json
def is_complex_num(objct):
    if 'complex' in objct:
        return complex(objct['real'], objct['img'])
    return objct

complex_object =json.loads('{"complex": true, "real": 4, "img": 5}', object_hook = is_complex_num)
simple_object =json.loads('{"real": 4, "img": 3}', object_hook = is_complex_num)
print("Complex_object: ",complex_object)
print("Without complex object: ",simple_object)