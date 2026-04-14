try:
    with open("el.txt", "x") as file:
        print("File created!")
except FileExistsError:
    print("File already exists!")

while True:
    print("\nWelcome to messaging app")
    print("1. Send message")
    print("2. View message")
    print("3. Exit program")

    choice = input("Enter your choice: ")

    if choice == "1":
        message = input("Enter your message: ")
        try:
            with open("el.txt", "a") as file:
                file.write(message + "\n")
            print("Message saved!")
        except:
            print("Error writing to file.")

    elif choice == "2":
        try:
            with open("el.txt", "r") as file:
                message = file.read()
                print("\nMessages:")
                print(message)
        except FileNotFoundError:
            print("File not found!")

    elif choice == "3":
        print("thank you for using my program<3 ")
        break

    else:
        print("Invalid choice. Try again.")