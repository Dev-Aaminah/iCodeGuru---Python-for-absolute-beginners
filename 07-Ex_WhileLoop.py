# Question_01: Counting Down from a Given Number Using a While Loop 

# Description:
#  The program asks the user to input a starting number.
#  It uses a while loop to count down from the starting number to zero.
#  Inside the loop, it prints the current number and then decrements it by 1
#  (start_number -= 1).
#   Once the number becomes less than zero, the loop stops, and it prints "Countdown finished!"
print('Question_01')
start_number = int(input("Please Enter a Number: "))
while(start_number>=0):
    print(start_number)
    start_number-=1
print("Countdown finished!")

# Question_02: Number Guessing Game with a Constant Secret Number

# Description:

#  The program sets the secret_number to a constant value of 42.
#  It initializes the variable guess to None.
#  It prints an initial message explaining the game to the user.
# The while loop continues to execute as long as the user's guess (guess) is not equal to the secret number (secret_number).

# Inside the loop, the program:
#  Prompts the user to enter a guess (guess = int(input("Enter your guess: "))).
#  Check if the guess is less than the secret number. If so, it prints "Too low! Try again."
#  Check if the guess is greater than the secret number. If so, it prints "Too high! Try again."

# If the guess is correct, it prints "Congratulations! You guessed the secret number."
# Once the correct guess is made, the loop exits, and the program prints "Game over!".
print('Question_02')
secret_number = 42
guess=None
print("The while loop continues to execute as long as the user's guess is not equal to the secret number.")
while(True):
    guess = int(input("Enter your guess: "))
    if(guess < secret_number):
        print("Too low! Try again.")
    elif(guess > secret_number):
        print("Too high! Try again.")
    else:
        print("Congratulations! Game over!")
        break