import random

# Define a function to get the complexity level from the user
def complexity():
    difficulty = int(input("1. Easy (only small alphabets)\n2. Medium (small alphabets with capital alphabets)\n3. Hard (small and capital alphabets with special characters)\nEnter The Complexity (1-3): "))
    return difficulty

# Define a function for generating an easy password (only small alphabets)
def easy(length):
    password = ""
    small = "abcdefghijklmnopqrstuvwxyz"
    for i in range(length):
        password = password + random.choice(small)
    return password

# Define a function for generating a medium password (small and capital alphabets)
def medium(length):
    password = ""
    small = "abcdefghijklmnopqrstuvwxyz"
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(length):
        password = password + random.choice(small + big)
    return password

# Define a function for generating a hard password (small and capital alphabets with special characters)
def hard(length):
    password = ""
    small = "abcdefghijklmnopqrstuvwxyz"
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!@#$%^&*()<>?"
    for i in range(length):
        password = password + random.choice(small + big + symbols)
    return password

# Ask the user for the length of the password
length = int(input("Enter the length of the password: "))

# Initialize comp to an invalid value
comp = 4

# Continue asking for complexity until a valid choice is made (1, 2, or 3)
while comp >= 4:
    if comp != 4:
        print("Enter a valid choice!")
    comp = complexity()

# Generate the password based on the chosen complexity level
if comp == 1:
    code = easy(length)
elif comp == 2:
    code = medium(length)
elif comp == 3:
    code = hard(length)

# Display the generated password
print("Password generated ---->", code)
