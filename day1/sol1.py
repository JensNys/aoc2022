


file = open("input1.txt","r")
lines = file.readlines()
print(lines)

for i in range(len(lines)):
    lines[i]=lines[i][:-1]
    if lines[i]!='':
        lines[i] = int(lines[i])
print(lines)

tmp=0
maxi=0
for i in range(len(lines)):
    if lines[i] != '':
        tmp += lines[i]
    else:
        maxi = max(tmp,maxi)
        tmp=0


print(maxi)











