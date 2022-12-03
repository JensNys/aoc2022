
def find_common_type(string1, string2,string3):
    for i in range(len(string1)):
        for j in range(len(string2)):
            for k in range(len(string3)):
                if string1[i]==string2[j] and string2[j]==string3[k]:
                    return string1[i]

def priority(letter):
    if 96<ord(letter):#lowercase
        return ord(letter)-96
    else:#uppercase
        return 26 + ord(letter)-64


def main(args):
    file = open(args, "r")
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    print(lines)

    sum = 0
    for i in range(0,len(lines),3):
        sum += (priority(find_common_type(lines[i],lines[i+1],lines[i+2])))

    print(sum)


if __name__ == '__main__':
    main('input.txt')