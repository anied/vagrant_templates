import os

print "~~~~~Python Provision File Executing~~~~~"

### RETAINED FOR QUICK DEBUGGING PURPOSES
# cwd = os.getcwd()
# contents = os.listdir(cwd)

# print "PYTHON CURRENT WORKING DIRECTORY:"
# print cwd
# print "DIRECTORY CONTENTS:"
# print contents

print "...changing to vagrant dir..."
os.chdir("/home/vagrant")
os.chdir("/vagrant")

print "...fetching apache_edited contents..."
with open('apache_edited.txt', 'r') as src_file:
    apache_contents = src_file.read()

print "...changing to apache dir..."
os.chdir("/etc/apache2")

print "...writing edited apache contents to file..."
with open('apache2.conf', 'w') as apache_file:
    apache_file.write(apache_contents)

print "~~~~~Python Provision File Exiting~~~~~"
