from datetime import datetime
import json


def intro():
    print("\t Welcome to The Budget Tracker".upper())
    print("")

intro()
print("")
# Variables (Temp memory for transactions)
transactions = []
transaction_id = 1

# Main Functions


def add_transaction():
    global transaction_id
    global num
    
    # Helper Function:
    def get_valid_amount(attempts=2):
        for i in range(attempts):
            try:
                return float(input("Enter amount (in Rs): "))
            except ValueError:
                print(f"Invalid amount! {attempts-i-1} attempts left.")
        print("Exceeded maximum attempts.")
        return None

    # Taking the input value from the User
    try:
        num = int(input("Enter the number of trasactions you wanna add?: \n"))

    except ValueError:
        print("Invalid input! Enter a number! Not a word")
        print("")
        return

    # Checking condition for 0 value
    if num < 0:
        print("Value can't be less than Zero! ")
        print(" ")

    if num > 0:
        print(f"You can add {num} transactions:-")
        print(" ")

        # Main loop to add
        for i in range(num):
            # Type
            trans_type = (
                str(input("Enter type (Income/Expense): ")).capitalize().strip()
            )
            while trans_type not in ["Income", "Expense"]:
                trans_type = (
                    str(input("Enter type (Income/Expense): ")).capitalize().strip()
                )

            # Amount
            try:
                amount = int(input("Enter amount (in Rs): "))
                amount = float(amount)
            except ValueError:
                print("Invalid input! enter a valid amount! (in numbers)")
                print("")
                i = 0
                while i < 2:
                    amount = int(input("Enter amount (in Rs): "))
                    i += 1
                    print("")
                    print(f"You have used {i} out 2 attempts")

            # Category
            try:
                category = (
                    str(input("Enter category (e.g, Food, Rent, Salary): "))
                    .capitalize()
                    .strip()
                )
            except ValueError:
                print("Enter a valid category! (Food, Salary, Rent )")
                o = 0
                while o < 2:
                    category = (
                        str(input("Enter category (e.g, Food, Rent, Salary): "))
                        .capitalize()
                        .strip()
                    )
                    o += 1
                    print(" ")
                    print(f"You have used {i} out 2 attempts")
                    

            # Description
            description = str(input("Enter description: "))

            # Current Date
            date = datetime.now().strftime("%d-%m-%Y")

            transaction = {
                "id": transaction_id,
                "type": trans_type,
                "category": category,
                "amount": amount,
                "description": description,
                "date": date,
            }

            # Adding ID

            transactions.append(transaction)
            transaction_id += 1
            print("")
            print("Transactions added successfully!\n")

        print("All transactions recorded")
        print("")

    else:
        print("Enter a valid number")


def view_transaction():
    if not transactions:
        print("No data availabe to be viewed")
    else:
        print("ID | Date | Type | Category | Amount | Description |")
        for t in transactions:
            print(
                f"{t['id']} | {t['date']} | {t['type']} | {t['category']} | ₹{t['amount']} | {t['description']} \n"
            )
            print("")


def edit_transaction():
    if not transactions:
        print("No transactions available to be Edited!")
        return  # stop execution if list is empty

    try:
        ask = int(
            input(
                "Enter the transaction ID (Note: You can view your transactions using option 2): "
            )
        )
    except ValueError:
        print("Enter A valid Numeric Transaction ID number! ")
        print(" ")
        return

    found = False
    for x in transactions:
        ""
        if x["id"] == ask:
            found = True
            print(f"Editing Transaction ID: {ask}")
            print("Current details:")
            print(
                f" Type: {x['type']}\n Category: {x['category']}\n Amount: {x['amount']}\n Description: {x['description']}\n Date: {x['date']}"
            )
            print("")

            print("Which field do you want to edit?")
            print("1. Type\n2. Amount\n3. Category\n4. Description")

            try:
                prompt = int(input("Enter your choice (1-4): "))
                match prompt:
                    case 1:
                        e_type = (
                            input("Enter new type (Income/Expense): ")
                            .capitalize()
                            .replace(" ", "")
                        )
                        x["type"] = e_type
                    case 2:
                        e_amount = float(input("Enter new amount: "))
                        x["amount"] = e_amount
                    case 3:
                        e_category = (
                            input("Enter new category: ").capitalize().replace(" ", "")
                        )
                        x["category"] = e_category
                    case 4:
                        e_desc = input("Enter the new description: ")
                        x["description"] = e_desc
                    case _:
                        print("Invalid Choice")

            except ValueError:
                print("Enter a valid numeric choice (1-4)! ")
                print(" ")
                return

            print("")
            print("Transaction Updated Successfully!")
            break

    if not found:
        print("Transaction not found! Please check the ID and try again.")


def delete_transaction():
    if not transactions:
        print("No transactions available to be Deleted!")
        return  # stop execution if list is empty

    try:
        prompt = int(
            input(
                "Enter the transaction ID (Note: You can view your transactions using option 2): "
            )
        )
        print("")

        exists = False
        for y in transactions:
            if y["id"] == prompt:
                exists = True
                print(f"Deleting Transaction ID: {prompt}")
                print("Current details:")
                print(
                    f" Type: {y['type']}\n Category: {y['category']}\n Amount: {y['amount']}\n Description: {y['description']}\n Date: {y['date']}"
                )
                print("")

                confirm = (
                    str(input("Do you want to Delete this transaction? (YES/NO): "))
                    .lower()
                    .replace(" ", "")
                )

                if confirm == "yes":
                    transactions.remove(y)
                    print(
                        f"Transaction with Transaction ID : {prompt} removed successfully!"
                    )
                    print("")
                    print("Transactions Updated Successfuly!")
                else:
                    print(
                        "No Changes Made, you can view your transactions using (opiton 2)"
                    )

                break
    except ValueError:
        print("Enter a valid Transacton ID! ")
        print(" ")
        return

    if not exists:
        print("Invalid Transaction ID! Try Again")


def show_summary():
    if not transactions:
        print("No Transactions Available")
    else:
        income = sum(t["amount"] for t in transactions if t["type"].lower() == "income")
        expenses = sum(
            t["amount"] for t in transactions if t["type"].lower() == "expense")
        balance = income - expenses

        print(f"Total Income: ₹{income}")
        print(f"Total Expenses: ₹{expenses}")
        print(f"Remaining Balance: ₹{balance}")
        print("")


def save_data():
    with open("data.json", "w") as f:
        json.dump(transactions, f, indent=4)
    print("Transactions saved successfully!")


while True:
    try:
        choice = int(
            input(
                "Select the option you wanna perform form 1,2,3,4,5  or enter 6 to Exit the function menu?\n"
                "1. Add Transaction\n"
                "2. View Transactions\n"
                "3. Edit Transactions\n"
                "4. Delete Transaction\n"
                "5. Show Summary\n"
                "6. Save & Exit\n: "
                ""
            )
        )

        print("")

        if choice == 1:
            add_transaction()

        elif choice == 2:
            view_transaction()

        elif choice == 3:
            edit_transaction()

        elif choice == 4:
            delete_transaction()
        elif choice == 5:
            show_summary()

        elif choice == 6:
            save_data()
            print("Saved & Exited Successfully!!")
            break

    except ValueError:
        print("Error: Enter a valid choice (1-6)!")
        print("")

    # else:
    #     print("Invalid Choice")
    #     break
