# Question 1
# Write a program to check whether a number is divisible by 7 or not.
print("************************* Question 1 *************************")

number = int(input("Enter a number to check whether a number is divisible by 7 or not: "))
print("You have entered: ", number)
if(number%7 == 0):
    print(number, "is divisible by 7.")
else:
    print(number, "is not divisible by 7.")
    
# Question 2
# Find the length of the text python and convert the value to float and convert it to string.
print("************************* Question 2 *************************")

text_input = input("Enter a text to find the length of the text: ")
print("The length of text included spaces is:", len(text_input))

# Convert the length of the text to float
float_value = float(len(text_input))
print("Converted length to float:", float_value)

# Convert the float back to string
string_value = str(float_value)
print("Converted float to string:", string_value)

# # Question 3
# Write a program to check whether a year is a leap year or not.
print("************************* Question 3 *************************")

year = int(input("Enter a year: "))

is_leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

if is_leap_year:
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")

# # Question 4
# # Write a program to check whether a number is prime or not.
print("************************* Question 4 *************************")

checkNumber = int(input("Enter a number to check if its prime or not: "))
is_prime = True

for i in range(2, checkNumber):
    if checkNumber%i == 0:
        is_prime = False
        break
    
if is_prime and checkNumber > 1:
    print(f'{checkNumber} is a prime number')
else:
    print(f'{checkNumber} is not a prime number')

# Question 5
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
print("************************* Question 5 *************************")
triangle_var = '#'
for i in range(8):
    print(triangle_var * i)

# Question 6
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("************************* Question 6 *************************")
in_python = "on" in "python"
in_dragon = "on" in "dragon"

both_having_on = in_python and in_dragon
print(both_having_on)