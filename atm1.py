class ATM:
    def __init__(self):
        with open("number1.csv", "r") as f:
            self.number = list(map(int, f.read().strip().split(",")))

        with open("atm_balance.txt", "r") as f:
            self.balance = list(map(int, f.read().strip().split(",")))

        with open("atm_pin.txt", "r") as f:
            self.pin = list(map(int, f.read().strip().split(",")))

        self.index = None   

    def check_number(self, entered_number):
        if entered_number in self.number:
            self.index = self.number.index(entered_number)
            return True
        return False

    def check_pin(self, entered_pin):
        return entered_pin == self.pin[self.index]

    def check_balance(self):
        print(f"Your Balance is: ₹{self.balance[self.index]}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > self.balance[self.index]:
            print("Insufficient balance.")
        else:   
            self.balance[self.index] -= amount
            print("Withdrawal Successful!")
            print(f"Remaining Balance: ₹{self.balance[self.index]}")
            self.save_balance()

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
        else:
            self.balance[self.index] += amount
            print(f"Deposited Successfully! Updated Balance: ₹{self.balance[self.index]}")
            self.save_balance()

    def change_pin(self, old_pin, new_pin):
        if self.pin[self.index] == old_pin:
            self.pin[self.index] = new_pin
            with open("atm_pin.txt", "w") as f:
                f.write(",".join(map(str, self.pin)))
            print("PIN Changed Successfully!")
        else:
            print("Incorrect Old PIN!")

    def save_balance(self):
        with open("atm_balance.txt", "w") as f:
            f.write(",".join(map(str, self.balance)))


def main():
    atm = ATM()
    print("Welcome to the ATM System")

    
    while True:
        try:
            entered_number = int(input("Enter your account number: "))
            if atm.check_number(entered_number):
                break
            else:
                print("Invalid account number.")
        except ValueError:
            print("Account number must be numeric.")

    
    while True:
        try:
            entered_pin = int(input("Enter your PIN: "))
            if atm.check_pin(entered_pin):
                break
            else:
                print("Wrong PIN.")
        except ValueError:
            print("PIN must be numeric.")

    
    while True:
        print("\n=== ATM Menu ===")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Change PIN")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                atm.check_balance()
            elif choice == 2:
                atm.withdraw(int(input("Enter amount to withdraw: ")))
            elif choice == 3:
                atm.deposit(int(input("Enter amount to deposit: ")))
            elif choice == 4:
                old_pin = int(input("Enter old PIN: "))
                new_pin = int(input("Enter new PIN: "))
                atm.change_pin(old_pin, new_pin)
            elif choice == 5:
                print("Thank you for using our ATM!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter numbers only.")


if __name__ == "__main__":
    main()
