import sys
from indexObjClass import indexObj

text_file = sys.argv[1]
pattern_file = sys.argv[2]

s = sys.argv[1]
p = sys.argv[2]
"""

with open(text_file, "r") as f:
    s = f.readline()
f.close()

with open(pattern_file, "r") as f:
    p = f.readline()
f.close()

"""


indexArray = []

counter = 0


for i in range(len(s)):
    slic = indexObj(start=i, motherString=s)
    indexArray.append(slic)


indexArray.sort(key=lambda x: str(x))


for obj in indexArray:
    print(f"index: {obj.start}, suffix: {obj}")

matchArray = []

for i in range(len(p)):
    match = False
    if i == 0:
        for obj in indexArray:
            ind = obj.start
            if s[ind] == p[i]:
                match = True
                matchArray.append(ind)
            else:
                if match == True:
                    break
    else:
        for ind in matchArray:
            tempStr = s[ind:]
            if tempStr[i] != p[i]:
                matchArray.remove(ind)

print(matchArray)











"""

if len(found) > 0:
    print()
    print(f"Found occurrences of {pattern_file} in {text_file} starting with index 0 at:")
    print(found)
    print()
    print(f"{counter} String-comparisons needed.")
else:
    print()
    print(f"Found no occurrences of {pattern_file} in {text_file}.")

"""

