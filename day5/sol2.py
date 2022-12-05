


def parse_action(line):
    line = line[5:]

    for i in range(len(line)):
        if line[i]==" ":
            amount = line[:i]

            line = line[i + 6:]
            break
    for i in range(len(line)):
        if line[i] == " ":
            start = line[:i]

            line = line[i+4:]
            break
    end = int(line)

    return (int(amount),int(start),int(end))

def stackify(stringstack):
    r=[]
    for i in range(10):
        r.append([])
    print(r)
    for i in range(len(stringstack)-2):
        for j in range(9):
            if stringstack[i][1+4*j] != ' ':
                r[j+1].append(stringstack[i][1+4*j])
    return r
    print(r)
def main(args):
    file = open(args, "r")
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    stack = stackify(lines[:10])

    print((lines[:10]))

    print(stack)
    for i in range(10,len(lines)):
        (amount,start,finish) = parse_action(lines[i])
        print((amount,start,finish))
        buffer = stack[start][:amount]
        stack[start]= stack[start][amount:]

        stack[finish] = buffer + stack[finish]


    length = 0
    for line in stack:
        print(line)




if __name__ == '__main__':
    main('input.txt')