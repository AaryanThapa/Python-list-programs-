list1 = [1,2,3,4,5,6,7]
list2 = [1,2,3,4,5,6,7,8,9]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)