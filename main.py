import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4, 
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4, 
    "C": 3,
    "D": 2
}

# calculate how much the user should win based on how much they bet 
# and how many lines they got correct (three in a row)
# This is not meant to be a fair or realistic slot machine in 
# any way btw
def check_winnings(columns, lines, bet, values):
    
    winnings = 0
    winning_lines = []
    
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]

            if symbol != symbol_to_check:
                break

        # yes, this else statement is for the for loop, 
        # not the if statement
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # define column list
    # and generate a column for every single column we have 
    columns = []

    # picks random values for each row in our column
    for _ in range(cols):

        column = []

        # : is the slice operator so that we can create a copy
        # instead of a reference to all_symbols
        current_symbols = all_symbols[:]

        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

# Prints and properly displays slot machine
def print_slot_machine(columns):

    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            
            # prevents from printing an extra and unneeded | 
            # at the end of our slot machine display
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="")
        print()

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


# define one single round of a game
def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount! Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    print(f"You won: ${winnings}!")
    # The asterisk here is called the splat operator!
    print(f"You won on line(s):", *winning_lines)

    return winnings - total_bet


def main():
    
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play! (q to quit) ")

        if answer == "q":
            break
            
        balance += spin(balance)

    print(f"You left with ${balance}")
    
main()