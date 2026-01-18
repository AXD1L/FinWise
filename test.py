while True:
    try:
        a = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input.")