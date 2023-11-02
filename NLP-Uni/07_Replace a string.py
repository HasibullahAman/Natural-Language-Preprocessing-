import re


food = 'hat rat mat pat'

regex = re.compile("[r]at")

food = regex.sub("food",food)

print(food)



myText = '''
my name is Hasibullah Aman
and I love Basira jafari
but I want to sex with Zarifa Jafari because
she is so hot
'''
regex = re.compile('\n')

newText = regex.sub(" ",myText)

print(newText)
