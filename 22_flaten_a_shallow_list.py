import itertools
orginal_list = [[2,3,4],[4,5,6],[7],[8,9]]
new_merged_list = list(itertools.chain(*orginal_list))
print(new_merged_list)
