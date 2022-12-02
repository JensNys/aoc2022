
#takes A,B,Y,X,Y,Z. returns corresponding move. rock=1, paper=2, scissors=3
def move(letter):
    dict = {'A':0,'B':1,'C':2,'X':0,'Y':3,'Z':6}
    return dict[letter]
#returns the amount of points gained from a round
def points(string):
    winningpts= move(string[2])
    if winningpts==3:#draw (play the same)
        charpts=move(string[0])+1
    if winningpts==0:#lose (play worse)
        charpts=((move(string[0])-1)%3) + 1
    if winningpts==6:#lose (play worse)
        charpts=((move(string[0])+1)%3) + 1
    return winningpts + charpts


file = open("input.txt","r")
lines = file.readlines()
for i in range(len(lines)):
    lines[i]=lines[i][:-1]


pts = 0
for s in lines:
    pts += points(s)
print(pts)