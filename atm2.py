class ATM:
    def __init__(self):
        self.accounts = []
        self.pins = []
        self.balances = []
        self.index = None

        with open("atmdata.csv", "r") as f:
            lines = f.readlines()[1:]  # we can use next(f) for header line  remove 

            for line in lines:
                account, pin, balance = line.strip().split(",")
                self.accounts.append(int(account))
                self.pins.append(int(pin))
                self.balances.append(int(balance))

    def save_data(self):
        with open("atmdata.csv", "w") as f:
            f.write("account,pin,balance\n")

            for i in range(len(self.accounts)):
                f.write(f"{self.accounts[i]},{self.pins[i]},{self.balances[i]}\n")

    def check_number(self, entered_number):
        if entered_number in self.accounts:
            self.index = self.accounts.index(entered_number)
            return True
        return False

    def check_pin(self, entered_pin):
        return entered_pin == self.pins[self.index]

    def check_balance(self):
        print(f"Your Balance is: ₹{self.balances[self.index]}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > self.balances[self.index]:
            print("Insufficient balance.")
        else:
            self.balances[self.index] -= amount
            self.save_data()
            print(f"Withdrawal Successful! Remaining Balance: ₹{self.balances[self.index]}")

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
        else:
            self.balances[self.index] += amount
            self.save_data()
            print(f"Deposited Successfully! Updated Balance: ₹{self.balances[self.index]}")

    def change_pin(self, old_pin, new_pin):
        if self.pins[self.index] == old_pin:
            self.pins[self.index] = new_pin
            self.save_data()
            print("PIN Changed Successfully!")
        else:
            print("Incorrect Old PIN!")


def main():
    atm = ATM()
    print("Welcome to the ATM System")

    while True:
        try:
            acc = int(input("Enter your account number: "))
            if atm.check_number(acc):
                break
            print("Invalid account number.")
        except ValueError:
            print("Account number must be numeric.")

    while True:
        try:
            pin = int(input("Enter your PIN: "))
            if atm.check_pin(pin):
                break
            print("Wrong PIN.")
        except ValueError:
            print("PIN must be numeric.")

    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change PIN")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                atm.check_balance()
            elif choice == 2:
                atm.withdraw(int(input("Enter amount: ")))
            elif choice == 3:
                atm.deposit(int(input("Enter amount: ")))
            elif choice == 4:
                atm.change_pin(
                    int(input("Enter old PIN: ")),
                    int(input("Enter new PIN: "))
                )
            elif choice == 5:
                print("Thank you for using ATM")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Numbers only allowed")


if __name__ == "__main__":
    main()
