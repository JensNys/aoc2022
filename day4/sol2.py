
def overlaps(range1,range2):
    if range1[0]<=range2[0] and range1[1]>=range2[0]:
        return 1
    if range2[0]<range1[0] and range2[1]>=range1[0]:
        return 1
    return 0




def split(string):
    for i in range(len(string)):
        if string[i]==",":
            return (string[:i],string[i+1:])
def split_streep(string):
    for i in range(len(string)):
        if string[i]=="-":
            return (int(string[:i]),int(string[i+1:]))

def main(args):
    file = open(args, "r")
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    print(len(lines))

    sum=0
    for i in range(len(lines)):
        (str1,str2)=split(lines[i])

        sum+=(overlaps(split_streep(str1),split_streep(str2)))
    print(sum)




if __name__ == '__main__':
    main('input.txt')