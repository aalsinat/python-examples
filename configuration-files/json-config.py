import json

# You can read it like this:

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
print(data)

# Writing JSON files is also easy. Just build up the dictionary and use:

with open('config.json', 'w') as outfile:
    json.dump(data, outfile)
