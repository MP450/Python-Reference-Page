# Sources: GeeksForGeeks.org, docs.python,org

import random

# Print random floating number between 0 and 1
print(random.random())

##########

# Print integer between 0 and 9
print(random.randrange(0, 9))

# Print even integer between 0 and 100
print(random.randrange(0, 101, 2))

##########

# Create two variables with random numbers between 1 and 6
RandNum1 = random.uniform(1, 6.999999)
RandNum2 = random.uniform(1, 6.999999)
print(RandNum1, RandNum2)

# Print results as integers
print(int(RandNum1), ",", int(RandNum2))

##########

# Create a list with 10 random numbers
list = []

for i in range(10):
    list.append(random.random())

# Print random list
print(list)

# Print 2 values from list
print(random.sample(list, 2))

##########

# Assign a random number to a seed.
seed1 = random.seed(7)
print(random.randint(1, 100))

##########





