from datetime import datetime
import json

# ---------------------------------------------
# 🟩 INTRO
# ---------------------------------------------
def intro():
    print("\t" + "WELCOME TO THE BUDGET TRACKER".center(50, " "))
    print("")
    print("Track your income 💰 and expenses 💸 with ease.\n")

intro()
print("")

# ---------------------------------------------
# 🟩 GLOBAL VARIABLES
# ---------------------------------------------
transactions = []
transaction_id = 1


# ---------------------------------------------
# 🟩 ADD TRANSACTION
# ---------------------------------------------
def add_transaction():
    global transaction_id

    try:
        num = int(input("Enter the number of transactions you want to add: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return

    if num <= 0:
        print("❌ Please enter a number greater than 0.")
        return

    print(f"\nYou can add {num} transaction(s):\n")

    for _ in range(num):
        trans_type = input("Enter type (Income/Expense): ").capitalize().strip()
        while trans_type not in ["Income", "Expense"]:
            trans_type = input("Invalid type! Enter 'Income' or 'Expense': ").capitalize().strip()

        try:
            amount = float(input("Enter amount (in Rs): "))
        except ValueError:
            print("❌ Invalid amount! Skipping this transaction.")
            continue

        category = input("Enter category (e.g., Food, Rent, Salary): ").capitalize().strip()
        description = input("Enter description: ").strip()
        date = datetime.now().strftime("%d-%m-%Y")

        transaction = {
            "id": transaction_id,
            "type": trans_type,
            "category": category,
            "amount": amount,
            "description": description,
            "date": date,
        }

        transactions.append(transaction)
        print(f"✅ Transaction ID {transaction_id} added successfully!\n")
        transaction_id += 1

    print("📁 All transactions recorded.\n")


# ---------------------------------------------
# 🟩 VIEW TRANSACTIONS
# ---------------------------------------------
def view_transaction():
    if not transactions:
        print("⚠️ No data available to view.\n")
        return

    print("ID | Date | Type | Category | Amount | Description")
    print("-" * 60)
    for t in transactions:
        print(f"{t['id']} | {t['date']} | {t['type']} | {t['category']} | ₹{t['amount']} | {t['description']}")
    print("")


# ---------------------------------------------
# 🟩 EDIT TRANSACTION
# ---------------------------------------------
def edit_transaction():
    if not transactions:
        print("⚠️ No transactions available to edit!\n")
        return

    try:
        ask = int(input("Enter the transaction ID to edit: "))
    except ValueError:
        print("❌ Invalid input! Enter a numeric ID.\n")
        return

    for x in transactions:
        if x["id"] == ask:
            print(f"\nEditing Transaction ID: {ask}")
            print("Current details:")
            print(f" Type: {x['type']}\n Category: {x['category']}\n Amount: {x['amount']}\n Description: {x['description']}\n Date: {x['date']}\n")

            print("Which field do you want to edit?")
            print("1. Type\n2. Amount\n3. Category\n4. Description")

            try:
                prompt = int(input("Enter your choice (1-4): "))
            except ValueError:
                print("❌ Invalid choice.")
                return

            if prompt == 1:
                x["type"] = input("Enter new type (Income/Expense): ").capitalize().strip()
            elif prompt == 2:
                x["amount"] = float(input("Enter new amount: "))
            elif prompt == 3:
                x["category"] = input("Enter new category: ").capitalize().strip()
            elif prompt == 4:
                x["description"] = input("Enter new description: ").strip()
            else:
                print("❌ Invalid choice.")
                return

            print("\n✅ Transaction updated successfully!\n")
            return

    print("❌ Transaction not found! Please check the ID.\n")


# ---------------------------------------------
# 🟩 DELETE TRANSACTION
# ---------------------------------------------
def delete_transaction():
    if not transactions:
        print("⚠️ No transactions available to delete!\n")
        return

    try:
        prompt = int(input("Enter the transaction ID to delete: "))
    except ValueError:
        print("❌ Invalid input! Please enter a valid ID.\n")
        return

    for y in transactions:
        if y["id"] == prompt:
            print(f"\nDeleting Transaction ID: {prompt}")
            print(f" Type: {y['type']}\n Category: {y['category']}\n Amount: {y['amount']}\n Description: {y['description']}\n Date: {y['date']}\n")

            confirm = input("Do you want to delete this transaction? (YES/NO): ").lower().strip()
            if confirm == "yes":
                transactions.remove(y)
                print(f"✅ Transaction ID {prompt} deleted successfully!\n")
            else:
                print("❌ No changes made.\n")
            return

    print("❌ Invalid Transaction ID! Try again.\n")


# ---------------------------------------------
# 🟩 SHOW SUMMARY
# ---------------------------------------------
def show_summary():
    if not transactions:
        print("⚠️ No transactions available!\n")
        return

    income = sum(t["amount"] for t in transactions if t["type"].lower() == "income")
    expenses = sum(t["amount"] for t in transactions if t["type"].lower() == "expense")
    balance = income - expenses

    print("📊 SUMMARY REPORT")
    print("-" * 30)
    print(f"Total Income: ₹{income}")
    print(f"Total Expenses: ₹{expenses}")
    print(f"Remaining Balance: ₹{balance}\n")


# ---------------------------------------------
# 🟩 MENU LOOP
# ---------------------------------------------
while True:
    try:
        choice = int(input(
            "Select an option:\n"
            "1. Add Transaction\n"
            "2. View Transactions\n"
            "3. Edit Transaction\n"
            "4. Delete Transaction\n"
            "5. Show Summary\n"
            "6. Exit\n"
            "👉 Enter your choice: "
        ))
    except ValueError:
        print("❌ Invalid input! Please enter a number between 1–6.\n")
        continue

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
        break
    else:
        print("❌ Invalid choice! Please select from 1–6.\n")

# ---------------------------------------------
# 🟩 SAVE TO JSON
# ---------------------------------------------
with open("transactions_data.json", "w") as f:
    json.dump(transactions, f, indent=4)
    print("💾 Transactions saved successfully!")
