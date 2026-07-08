import random 

secret_number = random.randint(1, 25)
print("I am thanking of a number bet 1 and 25.")

while True:
    guess = int(input("Take a guess: "))

    if guess < secret_number: 
        print("Too slow - - - Try again.")
    elif guess > secret_number:
        print("Too high - - - Try again.")
    else:
        print(f"Correct you found it in )