from itertools import zip_longest, chain, tee
def replace2copy(lst):
    # lst1, lst2 = tee(iter(lst), 2)
    # print("lst1: ", lst1, "lst2: ", lst2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2], fillvalue="*")))

print(replace2copy([1,2,3,4]))