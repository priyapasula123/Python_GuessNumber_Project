<<<<<<< HEAD
import random
number = random.randint(1, 100)
attempt = 1
guess = int(input("Guess the Number: "))
while(True):
    if(guess>number):
        guess = int(input("Guess another number. This one is too big: "))
        attempt += 1
    elif(guess<number):
        guess = int(input("Guess another number. This one is too small: "))
        attempt += 1
    else:
        print(f"Yeah thats the number. You guessed it right in {attempt} attempts")
=======
import random
number = random.randint(1, 100)
attempt = 1
guess = int(input("Guess the Number: "))
while(True):
    if(guess>number):
        guess = int(input("Guess another number. This one is too big: "))
        attempt += 1
    elif(guess<number):
        guess = int(input("Guess another number. This one is too small: "))
        attempt += 1
    else:
        print(f"Yeah thats the number. You guessed it right in {attempt} attempts")
>>>>>>> 2d08dd82da8f55e279b238f6481376d79e475029
        break