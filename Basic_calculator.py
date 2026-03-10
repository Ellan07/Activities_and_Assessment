def myfunc():
    print("Select Operation:")
    print("[1] Add")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    
    user = int(input("Enter Choice: "))

    if user == 1:
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))
        result = a + b
        print("Result is:", result)

    elif user == 2:
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))
        result = a - b
        print("Result is:", result)

    elif user == 3:
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))
        result = a * b
        print("Result is:", result)

    elif user == 4:
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))
        if b != 0:
            result = a / b
            print("Result is:", result)
        else:
            print("Cannot divide by zero!")

    else:
        print("Invalid choice")

myfunc()
   
