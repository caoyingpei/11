import re
txt = open("123.txt", "r").read()
print(len(re.findall("h", txt)))