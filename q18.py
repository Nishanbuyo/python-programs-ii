import json
print(dir(json))

print(json.__name__)
# print(json.__doc__)

a= json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(json.dumps({'4': 5, '6': 7}))
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))

print(json.loads(a))

# help(json)

dict1 = {'name': 'Ram', 'age': '23'}
jsondict = json.dumps(dict1)
print(jsondict, type(jsondict))

deserialized_dict = json.loads(jsondict)
print(deserialized_dict, type(deserialized_dict))
