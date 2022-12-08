
def split(str):
    for i in range(len(str)):
        if str[i]==" ":
            return (str[:i],str[i+1:])



class File:
    def __init__(self, name,size):
        self.name = name
        self.size = size

    def count_size(self):
        return self.size
    def count_size_less_100000(self):
        return 0

    def smaller_to_remove(self, to_remove, arr):
        return

class Directory:
    def __init__(self,name):
        self.name = name
        self.contents = set()
    def add(self,file):
        self.contents.add(file)
        file.parent=self


    def count_size(self):
        sum=0
        for element in self.contents:
            sum += element.count_size()
        self.size = sum
        return sum

    def count_size_less_100000(self):
        if self.size<=100000:
            sum = self.size
            for element in self.contents:
                sum += element.count_size_less_100000()
            return sum
        sum=0
        for element in self.contents:
            sum += element.count_size_less_100000()
        return sum


        return self.size
    def goto(self,filename):
        for element in self.contents:
            if element.name == filename:
                return element
    def smaller_to_remove(self,to_remove,arr):
        if self.size>=to_remove:
            arr.append(self)

        for element in self.contents:
            element.smaller_to_remove(to_remove,arr)












def main(args):
    file = open(args, "r")
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
 #   lines.append("$ cd /")
    i=0
    root = Directory("/")

    while i<len(lines):
        line = lines[i]
        print(line)
        if line[0]=="$":
            #cd
            if line.__contains__("cd"):
                #
                for j in range(len(line)-1,0,-1):
                    if line[j]==" ":
                        dir = line[j+1:]
                        #print(dir)
                        break
                #dir = the name of the directory we enter
                if dir=="/":
                    wd = root
                elif dir=="..":
                    wd = wd.parent
                else:
                    wd = wd.goto(dir)
                i += 1

            #ls
            elif line.__contains__("ls"):
                new_files=[]
                for j in range(i+1,len(lines)+1):
                    if j==len(lines):
                        i=j
                        break
                    if not(lines[j][0]=="$"):
                        new_files.append(lines[j])

                    else:
                        i = j
                        break

                #newfiles bevat de strings van de gelezen files
                for file in new_files:

                    if file[:3]=="dir":
                        dir_name=file[4:]
                        wd.add(Directory(dir_name))
                    else:
                        (size, name) = split(file)
                        wd.add(File(name,int(size)))
    print(root.name)
    print(root.count_size())
    #todo: find directories with size at most 100000
    #calculate sum of their sizes
    print(root.count_size_less_100000())
    disk_space = 70000000
    required_space = 30000000
    fs_size = root.count_size()
    free_space = disk_space-fs_size
    to_remove=required_space-free_space
    dirs_smaller_to_remove=[]
    root.smaller_to_remove(to_remove,dirs_smaller_to_remove)
    print(dirs_smaller_to_remove)
    sizes=[]
    for i in range(len(dirs_smaller_to_remove)):
        sizes.append(dirs_smaller_to_remove[i].size)
    print(sizes)
    print(min(sizes))


#5693



















#1919 fout too low

#To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)
if __name__ == '__main__':
    main('input.txt')