import random

print("Guess the number between 1 to 100")
secret_number = random.randint(1,100)
guess_count = 0
guess_limit = 15

while guess_count < guess_limit :
    guess = int(input("Enter your Guess :"))
    guess_count += 1
    if guess < secret_number:
        print("Number is greater than guess")
    elif guess > secret_number:
        print("Number is smaller than guess")
    else:
        print("You got the number")
        break
else:
    print("Sorry !! You failed ")
