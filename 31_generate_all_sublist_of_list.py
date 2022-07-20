from itertools import combinations
def sub_list(my_list):
    subs = []
    for i in range(0,len(my_list)+1):
        temp = [list(x) for x in combinations(my_list,i)]
        if len(temp)>0:
            subs.extend(temp)
    return subs

l1 = [10,20,30,40,50]
l2 = ["X","Y","Z","L"]
print("Orginal numbers")
print(l1)
print("s")
print(sub_list(l1))
print("Sublist of the said list:")
print(sub_list(l1))
print("combination of alphabetical letters")
print(sub_list(l2))