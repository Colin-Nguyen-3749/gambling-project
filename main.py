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
def get_bet():

    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                break

            else:
                # Add f to the front of the string so that you can 
                # include variables into your string
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")

        else: 
            print("Please enter a number")

    return amount

        

def main():
    
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount! Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    

main()