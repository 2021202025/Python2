import re
fhand = open('Sorcery.txt')
for line in fhand:
    line=line.rstrip()
    if re.search('if' ,line):
        print(line)