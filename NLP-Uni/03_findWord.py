import re

mytext = "Hello Hasib, I know you love me but I don't love you Hasibjan"

finding = re.findall('Hasib',mytext)

for i in finding:
    print(i)