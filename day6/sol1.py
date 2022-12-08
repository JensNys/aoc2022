
def main(args):
    file = open(args, "r")
    lines = file.readlines()
    str = lines[0]
    print((str))
    buffer = []
    for i in range(len(str)):
#        print(buffer)
        if len(buffer)>=14:
            buffer=buffer[1:]
        buffer.append(str[i])
        if len(buffer)==len(set(buffer)) and i>14:
            print(i+1)
            break




#1919 fout too low


if __name__ == '__main__':
    main('input.txt')