print("Enter how many rows you want")
num = int(input())
print("Type 1 , 0")
type =input()
if type =="1":
    for i in range(0,num + 1):
        print("*"*int(i))
if type=="0":
    for i in range(num,0,-1):
        print("*"*int(i))