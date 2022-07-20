from multiprocessing.sharedctypes import Value


def funargs(normal,*args,**kwargs):
    print(normal)
    for items in args:
        print(items)
    print("\nNow i woukd like introduce some students who got some responsibility in our class")   
    for key,Value in kwargs.items():
            print(f"{key} is a {Value}")
hrgs = ["Saimon","Pratham",
        "Nabin","Aarya","Abhaye"]

normal = ("This is python")
kw = {"Saimon":"Class monitor","Pratham":"Class president","Nabin":"Class coordinator","Aarya":"Class controller","Abhaye":"dean of class"}
funargs(normal,*hrgs,**kw)