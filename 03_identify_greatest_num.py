def greatest_num(num):
    max = num[0]
    for x in num:
        if x > max:
            max = x
    return max

print(greatest_num([2,3,-89,-898.00,45]))