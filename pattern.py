integer = int(input("Enter a integer"))
length = int(input("input length"))
def star():
    for i in range(length):
        for j in range(i + 1):
        
            print("*",end=" ")
        print()

def moon():
    for i in range(length):
        for j in range(length + 1- i -1):
            print(" ", end=" ")
        for j in range(0,i + 1):
            print("*",end=" ")
        print()


if integer > 10:
    print(star( ))
else:
    print(moon( ))