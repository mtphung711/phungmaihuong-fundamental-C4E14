from random import randint

number = randint(0, 100)
guess_wrong = True #flag
count = 0

while True:
    count = count + 1
    while count < 7:
        guess = int(input("Guess a number from 1 to 100 "))
        if guess > number:
            print("too large")
        elif guess < number:
            print("too small")
        else:
            print("bingo")
            guess_wrong = False
    print("you lose")
