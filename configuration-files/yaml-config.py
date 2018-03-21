import yaml

# You can read it like this:

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print(section)

print(cfg['mysql'])
print(cfg['other'])

# There is a yaml.dump method, so you can write the configuration the same way. Just build up a dictionary.
