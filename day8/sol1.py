



def main(args):
    file = open(args, "r")
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    print(lines)










if __name__ == '__main__':
    main('input.txt')