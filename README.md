# Banking Management System

This is a Python program that simulates a basic banking management system. It allows users to create user accounts, deposit and withdraw money, transfer funds to other users, check account balances, view transaction history, and take loans. Additionally, it provides administrative functionalities such as creating admin accounts, checking the bank's total balance and loan amount, and toggling the loan feature on or off.

## Features
### 1. User Account Creation:
   - Users can create a new account by providing their name, initial deposit amount, and setting a password.
   - A unique user ID is generated for each account.

### 2. Admin Account Creation:
   - Administrators can create admin accounts by providing an admin ID and password.

### 3. User Login:
   - Users can log in using their generated user ID and password.

### 4. Admin Login:
   - Administrators can log in using their admin ID and password.

### 5. Check Balance:
   - Users can check their account balance, which reflects the amount of money available in their account.

### 6. Deposit Amount:
   - Users can deposit money into their account by specifying the amount they want to deposit.

### 7. Withdraw Amount:
   - Users can withdraw money from their account by specifying the amount they want to withdraw, as long as they have sufficient funds.

### 8. Transfer Amount:
   - Users can transfer money from their account to another user's account (if exists) by providing the recipient's user ID and the amount to transfer.
   - The sender's balance is reduced by the transferred amount, and the recipient's balance is increased accordingly.
   - Make sure there are minimum 2 user accounts that transfer the amount between themselves. So, have to create 2 user accounts.

### 9. Transaction History:
   - Users can view their transaction history, which displays all the previous transactions made on their account.
   - In transfer feature, the transaction history displays both sides.

### 10. Take Loan:
    - Users can request a loan by specifying the loan amount.
    - The maximum loan limit is twice the user's current balance.
    - If the loan amount is within the limit and the bank has sufficient funds, the loan is granted and added to the user's account balance.
    - The bank's total balance is reduced by the loan amount, and the total loan amount is increased accordingly.

### 11. Check Bank Balance (Admin):
    - Administrators can check the total balance of the bank, which represents the cumulative amount of money in all user accounts.

### 12. Check Bank Loan Amount (Admin):
    - Administrators can check the total loan amount in the bank, which represents the cumulative amount of loans granted to users.

### 13. Toggle Loan Feature (Admin):
    - Administrators can enable or disable the loan feature of the bank.
    - When the loan feature is disabled, users cannot request loans.

### 14. Exit:
    - Users and administrators can exit the program.

## Usage

1. Run the program using a Python interpreter.
2. Choose the desired option from the menu by entering the corresponding number.
3. Follow the prompts and provide the necessary information to perform various banking operations.
4. Continue using the program until you choose to exit.

## Notes

- User IDs and admin IDs are automatically generated and should be used for subsequent logins.
- Passwords are case-sensitive.
- The loan feature can be toggled on or off by an admin.


## Author

This Banking Management System was developed by Md. Rahim.