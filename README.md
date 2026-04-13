# 💳 ATM System (Python)

## 📌 Overview

A simple **ATM Simulation System** built using Python.
This project allows users to perform basic banking operations like checking balance, withdrawing money, depositing funds, and changing PIN using a CSV-based database.

---

## 🚀 Features

✔️ Secure Login (Account Number + PIN)

✔️ Check Account Balance

✔️ Withdraw Money

✔️ Deposit Money

✔️ Change PIN

✔️ Data stored in CSV file

✔️ Auto-save after every transaction


---

## 🖼️ Screenshots

### 🔐 Login Screen
<img width="498" height="267" alt="image" src="https://github.com/user-attachments/assets/4607da37-2c06-4e0c-a97e-4d4fc4536789" />


### 💰 Transaction Menu

<img width="544" height="269" alt="image" src="https://github.com/user-attachments/assets/5dd5849d-55f2-47ba-9726-b814c9148f59" />

---

## 📂 Project Structure

```
📁ATM_Project/ │ ├── main.py # Entry point
├── atm.py # Main ATM logic
└── README.md # Documentation
```

---

## ⚙️ Requirements

* Python 3.x

---

## ▶️ How to Run

```bash
git clone https://github.com/your-username/atm-system.git
cd atm-system
python atm2.py
```

---

## 📊 CSV File Format

The system uses a CSV file (`atmdata.csv`) to store user data:

```
account,pin,balance
123456,8888,5000
987654,2222,10000
456789,3333,7500
```

---

## 🔐 Sample Credentials

| Account No | PIN  |
| ---------- | ---- |
| 123456     | 8888 |
| 987654     | 2222 |

---

## ⚠️ Important Notes

* CSV file must be in the same directory
* Account number & PIN should be numeric
* Data is automatically updated after transactions

---

## 🛠️ Future Improvements

* 🔒 Hidden PIN input (password type)
* 🧾 Transaction history
* 🖥️ GUI using Tkinter
* 🌐 Database integration (MySQL)

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 👨‍💻 Author

**Sumit Nandeda**

---

⭐ If you like this project, don't forget to star the repo!
