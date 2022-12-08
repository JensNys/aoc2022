



def main(args):
    file = open(args, "r")
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    print(lines)
    visible=[]
    for i in range(len(lines)):
        visible.append([])
        for j in range(len(lines[0])):
            visible[i].append(False)




    #visible from the left
    for i in range(len(lines)):
        max = -1
        for j in range(len(lines[0])):
            if int(lines[i][j]) >max:
                max = int(lines[i][j])
                visible[i][j]=True


    #visible from right
    for i in range(len(lines)):
        max=-1
        for j in range(len(lines[0])-1,-1,-1):
            if int(lines[i][j]) >max:
                max = int(lines[i][j])
                visible[i][j]=True

    #visible from up
    for i in range(len(lines)):
        max = -1
        for j in range(len(lines[0])):
            if int(lines[j][i]) >max:
                max = int(lines[j][i])
                visible[j][i]=True


    # visible from up
    for i in range(len(lines)):
        max = -1
        for j in range(len(lines[0])-1,-1,-1):
            if int(lines[j][i]) > max:
                max = int(lines[j][i])
                visible[j][i] = True
    print(visible)

    sum=0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if visible[i][j]:
                sum+=1

    print(sum)







if __name__ == '__main__':
    main('input.txt')