import random 
comp = random.randint(0, 2)
user = int(input("press 0 for Stone, 1 for paper, 2 for Scissor:  "))

if user > 2:
    print("invalid input")
else:
    def func(comp,user):
        if comp == user:
            return 0
        elif(comp == 0 and user == 1):
            return 1
        elif(comp == 2 and user == 0):
            return 1
        elif(comp == 1 and user == 2):
            return 1
        else:
            return -1
    a = func(comp, user)


    if user == 0:
        print("you chose: Stone")
    elif user == 1:
        print("you choose: paper")
    else:
        print("you choose: Scissor")


    if comp == 0:
        print("Computer choose: Stone")
    elif comp == 1:
        print("Computer choose: paper")
    else:
        print("computer choose: Scissor")


    if(a == 0):
        print("Its a draw")
    elif(a == 1):
        print("you win")
    else:
        print("you Loose")


