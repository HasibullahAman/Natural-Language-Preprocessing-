import re

text = "Hello Hasib, I know you love me but I don't love you Hasibjan"


for i in re.finditer('Hasib',text):
    changetoTuple = i.span()


    print(changetoTuple)