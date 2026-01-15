"""
author: Matous Simunek
email: simunekmatous@gmail.com
"""

import random

title = """                                             
                                             
                                ___          
                                `MM          
                   /      /      MM          
            ___   /M     /M      MM   ____   
     ,M   6MMMMb /MMMMM /MMMMM   MM  6MMMMb  
    ,dM  8M'  `Mb MM     MM      MM 6M'  `Mb 
   ,dMM      ,oMM MM     MM      MM MM    MM 
  ,d MM  ,6MM9'MM MM     MM      MM MMMMMMMM 
 ,d  MM  MM'   MM MM     MM      MM MM       
,d   MM  MM.  ,MM YM.  , YM.  ,  MM YM    d9 
MMMMMMMM `YMMM9'Yb.YMMM9  YMMM9 _MM_ YMMMM9  
     MM                                      
     MM                                      
     MM                                      """


divider = "----------------------------------------------------------------"
num = 0
i = 0
won = False


def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False


def getDigits(num):
    return [int(i) for i in str(num)]

def generateNum():
    while True:
        num = random.randint(1000,9999)
        if noDuplicates(num):
            return num


def cownbull(secret, guess):
    bull_cow = [0, 0]
    num_li = getDigits(secret)
    guess_li = getDigits(guess)

    for i, j in zip(num_li, guess_li):
        if j in num_li:
            if j == i:
                bull_cow[0] += 1  # bull
            else:
                bull_cow[1] += 1  # cow
    return bull_cow


def begin():
    secret = generateNum()
    print(divider)

    while True:
        g = guess()   # get string first
        
        if g == "quit":
            print(f"The number was {secret}!")
            return  # or quit()

        guess_val = int(g) # put into int 🥺

        bull_cow = cownbull(secret, guess_val)

        print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
        print(divider)

        if bull_cow[0] == 4:
            print("You guessed right!")
            break

        if won == True:
            print(f"The number was {secret}!")
            quit



def guess():
    while True:
        g = input("")

        if g == "quit":
            return "quit"

        if not g.isdigit():
            print("not a 4 digit number or starts with 0!")
            print(divider)
            continue

        if len(g) != 4:
            print("not a 4 digit number or starts with 0!")
            print(divider)
            continue

        if g.startswith("0"):
            print("not a 4 digit number or starts with 0!")
            print(divider)
            continue

        return g




def start():
    print(title)
    print(divider)

    print("Welcome to 4attle! a Bull & Cows remake playable in the console. " \
    "Write 'start' to begin the game and write a 4 digit number. Write 'exit' to quit the game. Go ahead and guess!")
    
    print(divider)
    begin()




start()
