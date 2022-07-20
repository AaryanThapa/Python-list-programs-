def last(n):return n[-1]


def sort_list_last(tuples):
    return sorted(tuples, key=last)
print(sort_list_last([(2,19),(2,6),(4,7),(2,9)]))