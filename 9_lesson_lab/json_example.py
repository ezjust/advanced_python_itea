import json

a = {'Name': 'Anton',
     'Students': ['Andrey', 'EZ']
     }

b = json.dumps(a, indent=2)

str_json = '{"name": "EZ"}'
c = json.loads(str_json)
print(b)
print(type(c))
print(c['name'])

