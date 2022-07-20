def lowest_num(num):
    low = num[0]
    for x in num:
        if low > x:
            low = x
    return low
print(lowest_num([2,3,-45,5]))
