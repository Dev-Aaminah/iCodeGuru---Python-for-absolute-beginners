# Write a Python program that simulates flipping a coin 10 times. The program should:
# 1. Use a for loop to simulate 10 coin flips.
# 2. Generate a random outcome for each flip (either "Heads" or "Tails").
# 3. Count the number of "Heads" and "Tails" outcomes.
# 4. Print the result of each flip.
# 5. Print the total counts of "Heads" and "Tails" at the end.

import random
head = 0
tail = 0
for i in range(10):
    flip = random.choice(["Head", "Tail"])
    print("Flip", i, ":", flip)
    if(flip == 'Head'):
        head +=1
    else:
        tail+=1
print("Head count :", head)
print("Tail count :", tail)