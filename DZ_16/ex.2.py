import json

A = {'key1': 'mishan9', 'key2': 2, 'key3': True}
B = {'key1': 'Hello', 'key2': False, 'key3': 5}
C = {}

for key, value in A.items():
    if key in B:
        if isinstance(B[key], list):
            C[key] = B[key] + [value]
        else:
            C[key] = [B[key], value]
        del B[key]
    else:
        C[key] = value

for key, value in B.items():
    C[key] = value

print(C)

with open('result.json', 'w') as f:
    json.dump(C, f)

