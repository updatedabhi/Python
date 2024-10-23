# fp = open("file2.txt", "w")
fp = open("file2.txt", "a")
fp.write(" Nani teri morani ko mor le gai baki jo bache the kale chor le gaye")
with open("file2.txt", "r") as fp:
    con = fp.read()
    print(con)
fp.close()