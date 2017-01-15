import re
x= '93 is an awesome number'
y=re.findall('[0-9]+' ,x)
print(y)
z=re.findall('an*' ,x)
print(z)