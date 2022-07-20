# num1 = int(input("Enter the 1st number"))
# num2 = int(input("Enter the 2nd number"))
# if num1 > num2:
#     print("first number is greater then second number ")
# elif num1 == num2:
#     print("First number is equal to second number")
# else:
#     print("Second number is greater than first number")
from collections import Counter
word = ("Aquickbrownfoxjumpsoverthelazydog")
counts=Counter(word) 
for i in word:
    print(i,counts[i])