import random
while True:
    
    num=random.randint(1,6)
    if num==6:
        print("congratulation ...you got ", num)
    else:
        print("you got ",num)
    ch=input("roll again ? , (y/n")
    if ch=="n":
        break;
print("Thanks for playing ")

