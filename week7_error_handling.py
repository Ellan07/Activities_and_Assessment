def show_menu():
    print("\n=== MENU ===")
    print("1. Withdraw Money")
    print("2. Check Balance")
    print("3. Exit")


def check_balance(balance):
    print(f"Current Balance: {balance}")


def withdraw(balance):
    while True:
        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Invalid amount. Please enter a positive number.")

            elif amount > balance:
                print("Insufficient funds.")

                print("\nWhat would you like to do?")
                print("1. Check Balance")
                print("2. Try Again")
                print("3. Exit")

                error_choice = input("Choose option: ")

                if error_choice == "1":
                    print(f"Current Balance: {balance}")

                elif error_choice == "2":
                    continue

                elif error_choice == "3":
                    print("Exiting program...")
                    exit()

                else:
                    print("Invalid option.")

            else:
                balance -= amount
                print("Withdrawal successful!")
                print(f"Remaining balance: {balance}")
                return balance

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    balance = 1000

    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            balance = withdraw(balance)

        elif choice == "2":
            check_balance(balance)

        elif choice == "3":
            print("Thank you. Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")


main()