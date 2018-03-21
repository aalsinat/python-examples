from configparser import ConfigParser
from os import path

configfile_name = "config.ini"
# ---------------------------
# Load the configuration file
# ---------------------------
with open(configfile_name) as f:
    config = ConfigParser(allow_no_value=True)
    config.read_file(f)

# List all contents
print("List all contents")
for section in config.sections():
    print("Section: %s" % section)
    for options in config.options(section):
        print("x %s:::%s:::%s" % (options,
                                  config.get(section, options),
                                  str(type(options))))

# Print some contents
print("\nPrint some contents")
print(config.get('other', 'use_anonymous'))  # Just get the value
print(config.getboolean('other', 'use_anonymous'))  # You know the datatype?

# ---------------------
# Writing configuration
# ---------------------

# Check if there is already a configuration file
if not path.isfile(configfile_name):
    # Create the configuration file as it doesn't exist yet
    cfgfile = open(configfile_name, 'w')

    # Add content to the file
    Config = ConfigParser.ConfigParser()
    Config.add_section('mysql')
    Config.set('mysql', 'host', 'localhost')
    Config.set('mysql', 'user', 'root')
    Config.set('mysql', 'passwd', 'my secret password')
    Config.set('mysql', 'db', 'write-math')
    Config.add_section('other')
    Config.set('other',
               'preprocessing_queue',
               ['preprocessing.scale_and_center',
                'preprocessing.dot_reduction',
                'preprocessing.connect_lines'])
    Config.set('other', 'use_anonymous', True)
    Config.write(cfgfile)
    cfgfile.close()
