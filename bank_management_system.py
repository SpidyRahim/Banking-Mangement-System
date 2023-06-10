import random


class Bank:
    def __init__(self):
        self.users = []
        self.admins = []
        self.is_loan_enabled = True
        self.total_balance = 0
        self.total_loan_amount = 0

    def create_user_account(self):
        name = input("Enter your name: ")
        initial_deposit = float(input("Enter initial deposit amount: "))
        user_id = random.randint(1000, 9999)
        password = input("Set a password for your account: ")
        account = Account(user_id, name, password, initial_deposit)
        self.users.append(account)
        self.total_balance += initial_deposit
        print(f"Account created successfully. Your user ID is: {user_id}")

    def create_admin_account(self):
        admin_id = input("Enter admin ID: ")
        password = input("Set a password for your account: ")
        admin = Admin(admin_id, password)
        self.admins.append(admin)
        print("Admin account created successfully.")

    def user_login(self):
        user_id = int(input("Enter your user ID: "))
        password = input("Enter your password: ")
        for user in self.users:
            if user.authenticate(user_id, password):
                return user
        print("Invalid user ID or password.")
        return None

    def admin_login(self):
        admin_id = input("Enter admin ID: ")
        password = input("Enter admin password: ")
        for admin in self.admins:
            if admin.authenticate(admin_id, password):
                return admin
        print("Invalid admin ID or password.")
        return None

    def check_balance(self, user):
        print(f"Your available balance is: {user.balance}")

    def deposit(self, user):
        amount = float(input("Enter the amount to deposit: "))
        user.balance += amount
        self.total_balance += amount
        print(
            f"Amount {amount} deposited successfully. Your current balance is: {user.balance}")
        transaction = f"Deposit: +{amount}"
        user.add_transaction(transaction)

    def withdraw(self, user):
        amount = float(input("Enter the amount to withdraw: "))
        if user.balance < amount:
            print("Insufficient balance.")
        elif self.total_balance < amount:
            print("The bank is bankrupt")
        else:
            user.balance -= amount
            self.total_balance -= amount
            print(
                f"Amount {amount} withdrawn successfully. Your current balance is: {user.balance}")
            transaction = f"Withdrawal: -{amount}"
            user.add_transaction(transaction)

    def transfer(self, sender):
        receiver_id = int(input("Enter the recipient's user ID: "))
        amount = float(input("Enter the amount to transfer: "))

        if sender.balance >= amount:
            sender.balance -= amount
            for user in self.users:
                if user.user_id == receiver_id:
                    user.balance += amount
                    print(
                        f"Amount {amount} transferred successfully to user ID: {receiver_id}.")
                    sender_transaction = f"Transfer: -{amount} to User ID: {receiver_id}"
                    receiver_transaction = f"Transfer: +{amount} from User ID: {sender.user_id}"
                    sender.add_transaction(sender_transaction)
                    user.add_transaction(receiver_transaction)
                    break
            else:
                print(f"User ID: {receiver_id} not found.")
        else:
            print("Insufficient balance.")

    def display_transaction_history(self, user):
        if len(user.transactions) > 0:
            print("Transaction History:")
            for transaction in user.transactions:
                print(transaction)
        else:
            print("No transaction history.")

    def take_loan(self, user):
        if self.is_loan_enabled:
            max_loan_limit = user.balance * 2

            loan_amount = float(input(f"Enter the loan amount (You can take only double of your main balance): "))
            if loan_amount > max_loan_limit:
                print(f"You can take maximum {max_loan_limit} as a loan")
            elif loan_amount > self.total_balance:
                print("Sorry, we can't provide the amount")
            else:
                user.balance += loan_amount
                self.total_balance -= loan_amount
                self.total_loan_amount += loan_amount
                print(
                    f"Loan of {loan_amount} granted. Your current balance is: {user.balance}")
                transaction = f"Loan: +{loan_amount}"
                user.add_transaction(transaction)
        else:
            print("The loan feature is currently disabled.")

    def check_bank_balance(self, admin):
        print(f"The total bank balance is: {self.total_balance}")

    def check_bank_loan_amount(self, admin):
        print(f"The total loan amount in the bank: {self.total_loan_amount}")

    def toggle_loan_feature(self, admin):
        self.is_loan_enabled = not self.is_loan_enabled
        status = "enabled" if self.is_loan_enabled else "disabled"
        print(f"Loan feature is now {status}.")


class Account:
    def __init__(self, user_id, name, password, initial_deposit):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.balance = initial_deposit
        self.transactions = []

    def authenticate(self, user_id, password):
        return self.user_id == user_id and self.password == password

    def add_transaction(self, transaction):
        self.transactions.append(transaction)


class Admin:
    def __init__(self, admin_id, password):
        self.admin_id = admin_id
        self.password = password

    def authenticate(self, admin_id, password):
        return self.admin_id == admin_id and self.password == password


def main():
    bank = Bank()

    while True:
        print("\n===== Welcome to the Banking Management System =====")
        print("1. Create User Account")
        print("2. Create Admin Account")
        print("3. User Login")
        print("4. Admin Login")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            bank.create_user_account()
        elif choice == "2":
            bank.create_admin_account()
        elif choice == "3":
            user = bank.user_login()
            if user:
                while True:
                    print("\n===== User Menu =====")
                    print("1. Check Balance")
                    print("2. Deposit Amount")
                    print("3. Withdraw Amount")
                    print("4. Transfer Amount")
                    print("5. Transaction History")
                    print("6. Take Loan")
                    print("7. Logout")

                    option = input("Enter your option (1-7): ")

                    if option == "1":
                        bank.check_balance(user)
                    elif option == "2":
                        bank.deposit(user)
                    elif option == "3":
                        bank.withdraw(user)
                    elif option == "4":
                        bank.transfer(user)
                    elif option == "5":
                        bank.display_transaction_history(user)
                    elif option == "6":
                        bank.take_loan(user)
                    elif option == "7":
                        break
                    else:
                        print("Invalid option. Please try again.")

        elif choice == "4":
            admin = bank.admin_login()
            if admin:
                while True:
                    print("\n===== Admin Menu =====")
                    print("1. Check Bank Balance")
                    print("2. Check Bank Loan Amount")
                    print("3. Toggle Loan Feature")
                    print("4. Logout")

                    option = input("Enter your option (1-4): ")

                    if option == "1":
                        bank.check_bank_balance(admin)
                    elif option == "2":
                        bank.check_bank_loan_amount(admin)
                    elif option == "3":
                        bank.toggle_loan_feature(admin)
                    elif option == "4":
                        break
                    else:
                        print("Invalid option. Please try again.")

        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
