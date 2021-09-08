import random
import time as t


def action(choice):
    sum_h=sum_b=0
    print("Okay! Go for it!\n")
    t.sleep(1)
    for die in range(0, choice):
        #playsound("dice.mp3")
        human= random.randint(1,6)
        t.sleep(1)
        print("I got : ",human)
        sum_h+=human
    t.sleep(1)
    print("\nMy Total is : ", sum_h)
    t.sleep(1.5)
    print("\nNow it's computer's turn")
    t.sleep(1)
    for die in range(0,choice):
        #playsound("dice.mp3")
        bot= random.randint(1,6)
        t.sleep(1)
        print("Computer got : ",bot)
        sum_b+=bot
    t.sleep(1)
    print("\nComputer's Total is : ", sum_b)
    t.sleep(2)
    result= "\n**I win the Game**" if sum_h>sum_b else "\n**Computer win the Game**" if sum_h<sum_b else "**It's a tie**"
    print(result)
  
def play():
    die=0
    roll=" "
    while die==0:
        choice=int(input("How many chances you want (1,3) : "))
        if choice>0 and choice<4:
             action(choice)
             break
        else:
            print("Please enter a valid choice\n")
    print("\nDo you want to continue?")     
    while roll!="Yes":
        roll=input().lower().capitalize()
        if roll== "Yes":
            print("\n")
            play()
        else:
            print("It was nice playing with you! Bye!") 
            break
play() 
