import json

a = '[{"name": "landing", "age": 18},{"name": "landing", "age": 18}]'

s = json.loads(a)
print(type(s))

s1 = json.dumps(a)
print(type(s1))
