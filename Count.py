fhand = open('Sorcery.txt')
counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word, 0)+1

lisst=list()
for key,value in counts.items():
    lisst.append((value,key))

lisst.sort(reverse=True)
for value,key in lisst[:10]:
    print (value,key)

