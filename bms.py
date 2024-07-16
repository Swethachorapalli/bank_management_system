import mysql.connector
from datetime import datetime

# Connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="70957@Swetha",
            database="bms"
        )
        print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Create tables if they don't exist
def create_tables(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS CustomerInformation (
                Customer_ID INT AUTO_INCREMENT PRIMARY KEY,
                First_Name VARCHAR(255) NOT NULL,
                Last_Name VARCHAR(255) NOT NULL,
                Address VARCHAR(255),
                City VARCHAR(255),
                State VARCHAR(255),
                Zip_Code VARCHAR(20),
                Email VARCHAR(255),
                Phone_Number VARCHAR(20),
                Date_of_Birth DATE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Account (
                Account_ID INT AUTO_INCREMENT PRIMARY KEY,
                Customer_ID INT,
                Account_Type VARCHAR(50),
                Balance DECIMAL(18, 2),
                Status VARCHAR(20),
                Date_Opened DATE,
                FOREIGN KEY (Customer_ID) REFERENCES CustomerInformation(Customer_ID)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Transaction (
                Transaction_ID INT AUTO_INCREMENT PRIMARY KEY,
                Account_ID INT,
                Transaction_Type VARCHAR(50),
                Amount DECIMAL(18, 2),
                Transaction_Date DATE,
                Description TEXT,
                FOREIGN KEY (Account_ID) REFERENCES Account(Account_ID)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS LoginCredentials (
                User_ID INT AUTO_INCREMENT PRIMARY KEY,
                Customer_ID INT,
                Username VARCHAR(255),
                Password VARCHAR(255),
                Last_Login_Date DATETIME,
                FOREIGN KEY (Customer_ID) REFERENCES CustomerInformation(Customer_ID)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS InterestRates (
                Account_Type VARCHAR(50) PRIMARY KEY,
                Interest_Rate DECIMAL(5, 2),
                Min_Balance DECIMAL(18, 2),
                Max_Balance DECIMAL(18, 2)
            )
        """)
        connection.commit()
        print("Tables created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Add customer
def add_customer(connection, customer_data):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO CustomerInformation (First_Name, Last_Name, Address, City, State, Zip_Code, Email, Phone_Number, Date_of_Birth) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (customer_data["First_Name"], customer_data["Last_Name"], customer_data["Address"], customer_data["City"], customer_data["State"], customer_data["Zip_Code"], customer_data["Email"], customer_data["Phone_Number"], customer_data["Date_of_Birth"]))
        connection.commit()
        print("Customer added successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# View customers
def view_customers(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM CustomerInformation")
        customers = cursor.fetchall()
        for customer in customers:
            print(customer)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Edit customer
def edit_customer(connection, customer_id, new_data):
    try:
        cursor = connection.cursor()
        sql = "UPDATE CustomerInformation SET First_Name = %s, Last_Name = %s, Address = %s, City = %s, State = %s, Zip_Code = %s, Email = %s, Phone_Number = %s, Date_of_Birth = %s WHERE Customer_ID = %s"
        cursor.execute(sql, (new_data["First_Name"], new_data["Last_Name"], new_data["Address"], new_data["City"], new_data["State"], new_data["Zip_Code"], new_data["Email"], new_data["Phone_Number"], new_data["Date_of_Birth"], customer_id))
        connection.commit()
        print("Customer updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Delete customer
def delete_customer(connection, customer_id):
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM CustomerInformation WHERE Customer_ID = %s"
        cursor.execute(sql, (customer_id,))
        connection.commit()
        print("Customer deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Add account
def add_account(connection, account_data):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO Account (Customer_ID, Account_Type, Balance, Status, Date_Opened) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (account_data["Customer_ID"], account_data["Account_Type"], account_data["Balance"], account_data["Status"], account_data["Date_Opened"]))
        connection.commit()
        print("Account added successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# View accounts
def view_accounts(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Account")
        accounts = cursor.fetchall()
        for account in accounts:
            print(account)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Edit account
def edit_account(connection, account_id, new_data):
    try:
        cursor = connection.cursor()
        sql = "UPDATE Account SET Customer_ID = %s, Account_Type = %s, Balance = %s, Status = %s, Date_Opened = %s WHERE Account_ID = %s"
        cursor.execute(sql, (new_data["Customer_ID"], new_data["Account_Type"], new_data["Balance"], new_data["Status"], new_data["Date_Opened"], account_id))
        connection.commit()
        print("Account updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Delete account
def delete_account(connection, account_id):
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM Account WHERE Account_ID = %s"
        cursor.execute(sql, (account_id,))
        connection.commit()
        print("Account deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Add transaction
def add_transaction(connection, transaction_data):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO Transaction (Account_ID, Transaction_Type, Amount, Transaction_Date, Description) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (transaction_data["Account_ID"], transaction_data["Transaction_Type"], transaction_data["Amount"], transaction_data["Transaction_Date"], transaction_data["Description"]))
        connection.commit()
        print("Transaction added successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# View transactions
def view_transactions(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Transaction")
        transactions = cursor.fetchall()
        for transaction in transactions:
            print(transaction)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Edit transaction
def edit_transaction(connection, transaction_id, new_data):
    try:
        cursor = connection.cursor()
        sql = "UPDATE Transaction SET Account_ID = %s, Transaction_Type = %s, Amount = %s, Transaction_Date = %s, Description = %s WHERE Transaction_ID = %s"
        cursor.execute(sql, (new_data["Account_ID"], new_data["Transaction_Type"], new_data["Amount"], new_data["Transaction_Date"], new_data["Description"], transaction_id))
        connection.commit()
        print("Transaction updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Delete transaction
def delete_transaction(connection, transaction_id):
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM Transaction WHERE Transaction_ID = %s"
        cursor.execute(sql, (transaction_id,))
        connection.commit()
        print("Transaction deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Add login credentials
def add_login_credentials(connection, login_data):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO LoginCredentials (Customer_ID, Username, Password, Last_Login_Date) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (login_data["Customer_ID"], login_data["Username"], login_data["Password"], login_data["Last_Login_Date"]))
        connection.commit()
        print("Login credentials added successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# View login credentials
def view_login_credentials(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM LoginCredentials")
        credentials = cursor.fetchall()
        for credential in credentials:
            print(credential)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Edit login credentials
def edit_login_credentials(connection, user_id, new_data):
    try:
        cursor = connection.cursor()
        sql = "UPDATE LoginCredentials SET Customer_ID = %s, Username = %s, Password = %s, Last_Login_Date = %s WHERE User_ID = %s"
        cursor.execute(sql, (new_data["Customer_ID"], new_data["Username"], new_data["Password"], new_data["Last_Login_Date"], user_id))
        connection.commit()
        print("Login credentials updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Delete login credentials
def delete_login_credentials(connection, user_id):
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM LoginCredentials WHERE User_ID = %s"
        cursor.execute(sql, (user_id,))
        connection.commit()
        print("Login credentials deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Add interest rates
def add_interest_rates(connection, interest_data):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO InterestRates (Account_Type, Interest_Rate, Min_Balance, Max_Balance) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (interest_data["Account_Type"], interest_data["Interest_Rate"], interest_data["Min_Balance"], interest_data["Max_Balance"]))
        connection.commit()
        print("Interest rates added successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# View interest rates
def view_interest_rates(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM InterestRates")
        rates = cursor.fetchall()
        for rate in rates:
            print(rate)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Edit interest rates
def edit_interest_rates(connection, account_type, new_data):
    try:
        cursor = connection.cursor()
        sql = "UPDATE InterestRates SET Interest_Rate = %s, Min_Balance = %s, Max_Balance = %s WHERE Account_Type = %s"
        cursor.execute(sql, (new_data["Interest_Rate"], new_data["Min_Balance"], new_data["Max_Balance"], account_type))
        connection.commit()
        print("Interest rates updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Delete interest rates
def delete_interest_rates(connection, account_type):
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM InterestRates WHERE Account_Type = %s"
        cursor.execute(sql, (account_type,))
        connection.commit()
        print("Interest rates deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Menu function
def menu():
    print("Banking System")
    print("1. Customer Operations")
    print("2. Account Operations")
    print("3. Transaction Operations")
    print("4. Login Credentials Operations")
    print("5. Interest Rates Operations")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice

# Main function
def main():
    connection = connect_to_database()
    if not connection:
        return

    create_tables(connection)

    while True:
        choice = menu()
        if choice == "1":
            customer_operations(connection)
        elif choice == "2":
            account_operations(connection)
        elif choice == "3":
            transaction_operations(connection)
        elif choice == "4":
            login_credentials_operations(connection)
        elif choice == "5":
            interest_rates_operations(connection)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    connection.close()

# Customer operations menu
def customer_operations(connection):
    while True:
        print("Customer Operations")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Edit Customer")
        print("4. Delete Customer")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_data = {
                "First_Name": input("Enter First Name: "),
                "Last_Name": input("Enter Last Name: "),
                "Address": input("Enter Address: "),
                "City": input("Enter City: "),
                "State": input("Enter State: "),
                "Zip_Code": input("Enter Zip Code: "),
                "Email": input("Enter Email: "),
                "Phone_Number": input("Enter Phone Number: "),
                "Date_of_Birth": input("Enter Date of Birth (YYYY-MM-DD): ")
            }
            add_customer(connection, customer_data)
        elif choice == "2":
            view_customers(connection)
        elif choice == "3":
            customer_id = int(input("Enter Customer ID to edit: "))
            new_data = {
                "First_Name": input("Enter First Name: "),
                "Last_Name": input("Enter Last Name: "),
                "Address": input("Enter Address: "),
                "City": input("Enter City: "),
                "State": input("Enter State: "),
                "Zip_Code": input("Enter Zip Code: "),
                "Email": input("Enter Email: "),
                "Phone_Number": input("Enter Phone Number: "),
                "Date_of_Birth": input("Enter Date of Birth (YYYY-MM-DD): ")
            }
            edit_customer(connection, customer_id, new_data)
        elif choice == "4":
            customer_id = int(input("Enter Customer ID to delete: "))
            delete_customer(connection, customer_id)
        elif choice == "5":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")

# Account operations menu
def account_operations(connection):
    while True:
        print("Account Operations")
        print("1. Add Account")
        print("2. View Accounts")
        print("3. Edit Account")
        print("4. Delete Account")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_data = {
                "Customer_ID": int(input("Enter Customer ID: ")),
                "Account_Type": input("Enter Account Type: "),
                "Balance": float(input("Enter Balance: ")),
                "Status": input("Enter Status: "),
                "Date_Opened": input("Enter Date Opened (YYYY-MM-DD): ")
            }
            add_account(connection, account_data)
        elif choice == "2":
            view_accounts(connection)
        elif choice == "3":
            account_id = int(input("Enter Account ID to edit: "))
            new_data = {
                "Customer_ID": int(input("Enter Customer ID: ")),
                "Account_Type": input("Enter Account Type: "),
                "Balance": float(input("Enter Balance: ")),
                "Status": input("Enter Status: "),
                "Date_Opened": input("Enter Date Opened (YYYY-MM-DD): ")
            }
            edit_account(connection, account_id, new_data)
        elif choice == "4":
            account_id = int(input("Enter Account ID to delete: "))
            delete_account(connection, account_id)
        elif choice == "5":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")

# Transaction operations menu
def transaction_operations(connection):
    while True:
        print("Transaction Operations")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Edit Transaction")
        print("4. Delete Transaction")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            transaction_data = {
                "Account_ID": int(input("Enter Account ID: ")),
                "Transaction_Type": input("Enter Transaction Type: "),
                "Amount": float(input("Enter Amount: ")),
                "Transaction_Date": input("Enter Transaction Date (YYYY-MM-DD): "),
                "Description": input("Enter Description: ")
            }
            add_transaction(connection, transaction_data)
        elif choice == "2":
            view_transactions(connection)
        elif choice == "3":
            transaction_id = int(input("Enter Transaction ID to edit: "))
            new_data = {
                "Account_ID": int(input("Enter Account ID: ")),
                "Transaction_Type": input("Enter Transaction Type: "),
                "Amount": float(input("Enter Amount: ")),
                "Transaction_Date": input("Enter Transaction Date (YYYY-MM-DD): "),
                "Description": input("Enter Description: ")
            }
            edit_transaction(connection, transaction_id, new_data)
        elif choice == "4":
            transaction_id = int(input("Enter Transaction ID to delete: "))
            delete_transaction(connection, transaction_id)
        elif choice == "5":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")

# Login credentials operations menu
def login_credentials_operations(connection):
    while True:
        print("Login Credentials Operations")
        print("1. Add Login Credentials")
        print("2. View Login Credentials")
        print("3. Edit Login Credentials")
        print("4. Delete Login Credentials")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            login_data = {
                "Customer_ID": int(input("Enter Customer ID: ")),
                "Username": input("Enter Username: "),
                "Password": input("Enter Password: "),
                "Last_Login_Date": datetime.now()
            }
            add_login_credentials(connection, login_data)
        elif choice == "2":
            view_login_credentials(connection)
        elif choice == "3":
            user_id = int(input("Enter User ID to edit: "))
            new_data = {
                "Customer_ID": int(input("Enter Customer ID: ")),
                "Username": input("Enter Username: "),
                "Password": input("Enter Password: "),
                "Last_Login_Date": datetime.now()
            }
            edit_login_credentials(connection, user_id, new_data)
        elif choice == "4":
            user_id = int(input("Enter User ID to delete: "))
            delete_login_credentials(connection, user_id)
        elif choice == "5":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")

# Interest rates operations menu
def interest_rates_operations(connection):
    while True:
        print("Interest Rates Operations")
        print("1. Add Interest Rates")
        print("2. View Interest Rates")
        print("3. Edit Interest Rates")
        print("4. Delete Interest Rates")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            interest_data = {
                "Account_Type": input("Enter Account Type: "),
                "Interest_Rate": float(input("Enter Interest Rate: ")),
                "Min_Balance": float(input("Enter Minimum Balance: ")),
                "Max_Balance": float(input("Enter Maximum Balance: "))
            }
            add_interest_rates(connection, interest_data)
        elif choice == "2":
            view_interest_rates(connection)
        elif choice == "3":
            account_type = input("Enter Account Type to edit: ")
            new_data = {
                "Interest_Rate": float(input("Enter Interest Rate: ")),
                "Min_Balance": float(input("Enter Minimum Balance: ")),
                "Max_Balance": float(input("Enter Maximum Balance: "))
            }
            edit_interest_rates(connection, account_type, new_data)
        elif choice == "4":
            account_type = input("Enter Account Type to delete: ")
            delete_interest_rates(connection, account_type)
        elif choice == "5":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
