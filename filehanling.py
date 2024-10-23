# open() fucntion is used to readig and writing file

# file object = open(<file-name>, <access mode>)

fileptr = open("file.txt", "r")

with open("file.txt", "r") as f:
    # content = f.read()
    # content = f.read(3)
    # content = f.readline()
    # content = f.readline()
    for i in f:
        print(i)

#closes the opened file
fileptr.close()