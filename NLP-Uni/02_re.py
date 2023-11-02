import re

text = """
Hasibullah is 22 and Basira is 21
Qasib is 45 and Ali is 20
"""

ages = re.findall(r'\d{1,3}',text)
name = re.findall(r'[A-Z][a-z]*',text)

print(name)

mydict = {}

x = 0


for eachname in name:
    mydict[eachname] = ages[x]
    x+=1


print(mydict)