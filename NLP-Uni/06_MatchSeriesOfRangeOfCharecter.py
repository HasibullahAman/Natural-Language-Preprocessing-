import re

TextList = 'Hat,mat,pat,sat'

findText = re.findall('[m-p]at',TextList)
for i in findText:
    print(i)


print("----------Second Part ---------")
# If I say, not between this range(m-p) I use the ^ character

findText2 = re.findall('[^m-p]at',TextList)
for i in findText2:
    print(i)