import re

with open("plik.tex") as file:
        data = file.read()
        
print("TEST\n")

# print("dane z pliku\n")
# print(data)

pattern = r"\\begin\{regex\}\s*% (.*?), (.*?), (.*?)\n(.*?)\\end\{regex\}"

# print("\nWYNIKI\n")
wyniki = re.findall(pattern,data, re.DOTALL)
for i in wyniki:
    for j in range(0,4):
        print(i[j])
# print(wyniki)

# print("\ndalsza zabawa\n")

file.close()