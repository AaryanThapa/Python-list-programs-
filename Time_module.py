import time 
initial = time.time()
k = 0
while(k<10):
    print("This is while loop")
    # time.sleep(2)
    k+=1
print("While loop ran in",time.time()- initial,"Seconds")

# initial2 = time.time()
# for i in range(45):
#     print("This is for loop")
#     time.sleep(2)
# print("For loop ran in",time.time() - initial2,"Seconds")