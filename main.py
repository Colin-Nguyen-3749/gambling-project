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

deposit()

