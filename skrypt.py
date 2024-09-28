import re

with open("plik.tex") as file:
        data = file.read()
        
pattern = r"\\begin\{regex\}\s*% (.*?)\n(.*?)\\end\{regex\}"

wyniki = re.findall(pattern,data, re.DOTALL)

for i in wyniki:
    for j in i[0].split(', '):
        print(j)
    print(i[1])

file.close()