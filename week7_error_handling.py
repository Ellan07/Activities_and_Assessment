def show_menu():
    print("\n=== MENU ===")  # display menu title
    print("1. Withdraw Money")  # option 1
    print("2. Check Balance")  # option 2
    print("3. Exit")  # option 3


def check_balance(balance):
    print(f"Current Balance: {balance}")  # show current balance


def withdraw(balance):
    while True:  # loop until valid withdrawal or exit
        try:
            amount = float(input("Enter amount to withdraw: "))  
            # ask user for amount and convert to number

            if amount <= 0:  
                print("Invalid amount. Please enter a positive number.")  
                # reject zero or negative values

            elif amount > balance:  
                print("Insufficient funds.")  
                # not enough money

                print("\nWhat would you like to do?")
                print("1. Check Balance")
                print("2. Try Again")
                print("3. Exit")

                error_choice = input("Choose option: ")  
                # get user decision

                if error_choice == "1":
                    print(f"Current Balance: {balance}")  # show balance

                elif error_choice == "2":
                    continue  # go back and try again

                elif error_choice == "3":
                    print("Exiting program...")
                    exit()  # stop program

                else:
                    print("Invalid option.")  # handle wrong input

            else:
                balance -= amount  # subtract amount from balance
                print("Withdrawal successful!")  # success message
                print(f"Remaining balance: {balance}")  # show updated balance
                return balance  # return updated balance to main program

        except ValueError:
            print("Invalid input. Please enter a number.")  
            # catch non-number input


def main():
    balance = 1000  # starting balance

    while True:  # main loop
        show_menu()  # call function to display menu
        choice = input("Enter your choice (1-3): ")  # get user input

        if choice == "1":
            balance = withdraw(balance)  
            # call withdraw function and update balance

        elif choice == "2":
            check_balance(balance)  
            # call function to display balance

        elif choice == "3":
            print("Thank you. Goodbye.")  
            break  # exit loop and end program

        else:
            print("Invalid choice. Try again.")  
            # handle invalid input


# start the program
main()