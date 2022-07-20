a = [20,23,4,5,6,8,23,20,4,40]

dupa_items = set()
unique_items = []
for x in a:
    if x not in dupa_items:
        unique_items.append(x)
        dupa_items.add(x)
        # sorted(dupa_items)
print(dupa_items)
