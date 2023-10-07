import json

with open('data.json', 'r') as f:
    data = json.loads(f.read())

like = data['like']
dislike = data['dislike']

like += 1

data['like'] = like

json_data = json.dumps(data, indent=4)

with open('data.json', 'w') as f:
    f.write(json_data)