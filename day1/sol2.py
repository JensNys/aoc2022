import heapq

# converting input
file = open("input1.txt","r")
lines = file.readlines()


for i in range(len(lines)):
    lines[i]=lines[i][:-1]
    if lines[i]!='':
        lines[i] = int(lines[i])


#actual code
tmp=0
maxi=0
elves = []
for i in range(len(lines)):
    if lines[i] != '':
        tmp += lines[i]
    else:
        heapq.heappush(elves,-tmp)
        tmp=0

biggest=abs(heapq.heappop(elves))
bigger=abs(heapq.heappop(elves))
big=abs(heapq.heappop(elves))
their_sum = big+bigger+biggest
print("the 3 biggest elves are {}, {} and {}. their sum is {}".format(big,bigger,biggest,their_sum))












