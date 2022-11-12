import os

file_object = open('./secrets.yaml', 'a')

for name, value in os.environ.items():
    if name.startswith("ST_")
        file_object.write("  {0}: {1}".format(name.replace("ST_", ""), value))

file_object.close()
