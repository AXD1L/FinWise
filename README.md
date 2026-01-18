# 💰 FinWise – Personal Budget Tracker (CLI)

FinWise is a **command-line based personal budget tracker** built using Python.  
It helps users efficiently manage their **income and expenses**, track transactions, and view financial summaries — all through a simple and interactive terminal interface.

---

## 🚀 Features

- ➕ Add multiple income and expense transactions
- 📋 View all recorded transactions in a clean tabular format
- ✏️ Edit existing transactions using Transaction ID
- ❌ Delete transactions with confirmation
- 📊 View financial summary (Total Income, Expenses, Remaining Balance)
- 💾 Save transactions to a JSON file
- 🖥️ User-friendly CLI menu system

---

## 🛠️ Technologies Used

- **Python 3**
- `datetime` module – for date handling
- `json` module – for data storage

---

## 📂 Project Structure

## 📂 Project Structure


FinWise/
│
├── app_logic.py      # Main application logic
├── data.json         # Stored transaction data (auto-generated)
├── rough.py          # Practice / experimental file
├── test.py           # Testing file
└── README.md         # Project documentation
▶️ How to Run the Application
Clone the repository

bash
Copy code
git clone https://github.com/AXD1L/FinWise.git
Navigate to the project directory

bash
Copy code
cd FinWise
Run the application

bash
Copy code
python app_logic.py
📌 Application Menu
text
Copy code
1. Add Transaction
2. View Transactions
3. Edit Transactions
4. Delete Transaction
5. Show Summary
6. Save & Exit
🧾 Transaction Details
Each transaction contains:

Transaction ID

Type (Income / Expense)

Category (Food, Rent, Salary, etc.)

Amount (₹)

Description

Date

💡 Future Enhancements
Monthly & category-wise analysis

Data visualization (charts & graphs)

GUI or Web version (Flask / Streamlit)

Export reports to CSV or PDF

User authentication system

🤝 Contributing
Contributions are welcome!
Feel free to fork this repository and submit a pull request.

📜 License
This project is open-source and free to use for learning and personal development.

👨‍💻 Author
Mohammad Aadil Siddiqui
Aspiring AI/ML & Data Science Engineer
Built with ❤️ using Python
