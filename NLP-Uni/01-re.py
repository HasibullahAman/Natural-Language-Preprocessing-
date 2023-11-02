import re
notext = 'my name is Hasibullah Aman and I love Basira Jafari'

# letter = re.search("H",text)
# print(letter)


# txt = "The rain in Spain"
# x = re.split("^The.*Spain$", txt)
# print(x)

res = re.findall('^H|B$h|a',notext)
print(res)