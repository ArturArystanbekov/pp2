import random

def guess():
    name=str(input("Hello! What is your name?"))
    print(f"Well {name} , I am thinking of a number between 1 and 20.")
    numer=random.randint(1,20)
    taken=0
    
    while True:
        print("Take a guess")
        guess=int(input())
        taken+=1
        
        if guess<numer:
            print("Your guess is too low.")
        elif guess>numer:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! Youe guessed my number in {taken} guesses!")
            break
guess()