# Import the random module to generate computer's choice
import random

# Choices for computer
n = ["rock", "paper", "scissors"]

# Initialize point counters for the computer and the user
c_points = 0
u_points = 0

# Loop for playing again
choice = 1
while choice != 2:
    # Generate a random choice for the computer from the list n
    comp = random.choice(n)

    # Ask the user for their choice
    user = input("Enter rock, paper, or scissors: ")
    print("You: ", user)
    print("Computer: ", comp)

    # Check the outcomes and update the points accordingly
    if comp == user:
        print("Tie")
    elif comp == "scissors" and user == "rock" or user == "paper" and comp == "rock" or comp == "paper" and user == "scissors":
        print("You get a point!")
        u_points = u_points + 1
    elif user == "scissors" and comp == "rock" or comp == "paper" and user == "rock" or comp == "scissors" and user == "paper":
        print("Computer gets a point!")
        c_points = c_points + 1
    elif user != "rock" or user != "paper" or user != "scissors":
        print("Enter a valid choice.")

    # Ask the user if they want to play again
    choice = int(input("\nDo you want to play again?\nIf yes, press 1; otherwise, press 2: "))

# Display the final scores
print("\nComputer points --->", c_points)
print("Your points --->", u_points)

# Determine the winner or if it's a tie
if c_points > u_points:
    print("COMPUTER WINS!")
elif u_points > c_points:
    print("YOU WIN!")
else:
    print("IT'S A TIE!")

