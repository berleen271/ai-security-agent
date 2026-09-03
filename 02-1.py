
import json
json_str='{"id": "01112", "name": "berleen", "severity": "high"}'
dict1=json.loads(json_str)
print(dict1)
print(type(dict1))
