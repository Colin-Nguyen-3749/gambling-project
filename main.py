MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# collects user input that gets 
# the deposit from the user
def deposit():

    # continuously ask the user to enter
    # a deposit amount until they give a 
    # valid amount
    while True:

        amount = input("What would you like to deposit? $")
        
        # This tells us if the input is a real 
        # and valid number (not including negatives!)
        if amount.isdigit():
            
            # convert the amount that's default a string 
            # into an integer
            amount = int(amount)

            # if greater than zero, it's valid and we can break 
            # out of this while loop
            if amount > 0:
                break

            else:
                print("Amount must be greater than 0!")

        else:
            print("Please enter a number!")

    return amount

# Ask the user the number of lines that they want to bet on 
def get_number_of_lines():

    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")

        if lines.isdigit():
            lines = int(lines)
            
            if 1 <= lines <= MAX_LINES: 
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")

    return lines

# Get the amount that the user wants to bet on each line



def main():
    
    balance = deposit()
    lines = get_number_of_lines()
    
    print(balance, lines)


main()