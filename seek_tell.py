with open("read_write.txt") as f:
    a = f.read(4)
    print(a)

B = open("read_write.txt")
print(B.readline())
print(B.readline())
B.close