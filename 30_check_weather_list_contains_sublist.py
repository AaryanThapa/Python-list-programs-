def check_sublist(l,s):
    sub_set = False
    if s == []:
        sub_set = True
    elif s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = False
    
    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[n+i]==s[n]):
                    n += 1
                if n == len(s):
                    sub_set = True
    return sub_set
a = [1,2,3,4,5]
b = [2,3,4]
c = [2,3]
print(check_sublist(a,b))
print(check_sublist(a,c))