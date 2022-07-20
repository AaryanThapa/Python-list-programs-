import random
print("Enter your guess")
input = input()
Things = ["Snake","Gun","Water"]
rand = random.choice(Things)
print(rand)
if input == rand:
    print("GAME TIE!!")
elif input == "Snake" and  rand == "Water":
    print("Congrats YOU WIN!!")
elif input == "Gun" and rand == "Water":
    print("YOU LOOSE")
elif input == "Water" and rand == "Gun":
    print("Congrats YOU WIN!!")
elif input == "Snake" and rand == "Gun":
    print("YOU LOOSE")
elif input == "Gun" and rand == "Snake":
    print("Congrats YOU WIN!!")
elif input == "Water" and rand == "Snake":
    print("YOU LOOSE")