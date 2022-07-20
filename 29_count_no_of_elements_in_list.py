def count_in_list(li,min,max):
    ctr = 0
    for x in li:
        if min <= x <= max:
            ctr += 1
    return ctr
list1 = [10,20,30,40,40,30,30,80,90]
print(count_in_list(list1,20,100))

list2 = ["a","b","c","d","e","f","g","h"]
print(count_in_list(list2,"a","e"))

