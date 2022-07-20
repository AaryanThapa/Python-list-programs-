list1 = [10,10,10,0,0]
list2 = [10,10,10,0,0]
list3 = [10,10,10,0,1]

# print("Compare list1 and list2")
# print("".join(map(str, list2)))
# print( "".join(map(str,list1)))
# print("Compare list1 and list3")
# print("".join(map(str,list3)))
# print("".join(map(str,list1 * 2)))
if list1 == list2:
    print("Compare list1 and list2")
    print("True")
if list1 == list3:
    print("Compare list1 and list3")
    print("True")
else:
    print("False")
