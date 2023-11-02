import re

TextList = 'Hat,mat,pat,sat'

findText = re.findall('[sHmp]at',TextList)

for i in findText:
    print(i)


