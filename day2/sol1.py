
#takes A,B,Y,X,Y,Z. returns corresponding move. rock=1, paper=2, scissors=3
def move(letter):
    dict = {'A':0,'B':1,'C':2,'X':0,'Y':1,'Z':2}
    return dict[letter]
#returns the amount of points gained from a round
def points(string):
    if (move(string[0])+1)%3==(move(string[2])):#win
        return 6+ move(s[2]) + 1
    if move(string[0])==move(string[2]):#draw
        return 3+ move(s[2]) + 1
    return 0 + move(s[2]) + 1#lose

file = open("input.txt","r")
lines = file.readlines()
for i in range(len(lines)):
    lines[i]=lines[i][:-1]

pts = 0
for s in lines:
    pts += points(s)
print(pts)