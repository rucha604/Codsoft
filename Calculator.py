# Initialize the loop control variable
i = 1

# Start an indefinite loop
while i == 1:
    # Request user input for the first number
    x = int(input("Enter the first number: "))
    
    # Ask the user to select an operation
    choice = input("1) +, 2) -, 3) *, 4) / (do not enter 0 as the second number)\nEnter the operator(Enter In arithmetic Symbol): ")
    
    # Request user input for the second number
    y = int(input("Enter the second number: "))

    # Check the operation chosen by the user and perform the corresponding calculation
    if choice == '+':
        sum_val = x + y
        print(x, "+", y, "=", sum_val)
    elif choice == '-':
        diff = x - y
        print(x, "-", y, "=", diff)
    elif choice == '*':
        mul = x * y
        print(x, "*", y, "=", mul)
    elif choice == '/':
        # Ensure the user doesn't input 0 as the second number for division
        if y != 0:
            div = x / y
            print(x, "/", y, "=", div)
        else:
            print("Cannot divide by zero! Please enter a non-zero value.")
    else:
        # Notify the user if an invalid choice was made
        print("Enter a valid choice")

    # Ask the user whether to continue or exit
    cont = input("Do you want to continue [C] or exit [E]? ")
    cont_1 = cont.capitalize()

    # Check user's choice to continue or exit the calculator
    if cont_1 == 'C':
        # If 'C' is entered, continue the loop
        i = 1
    else:
        # If any other input is entered, exit the loop
        i = i + 1
        # The following line is commented out as it's not required.
        print("Exiting calculator !")
