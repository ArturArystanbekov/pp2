import re
txt=input()
word=re.findall(r'a.*b$', txt)
print(word)