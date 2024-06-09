import csv
import os
from functions import verify_user, calculate_tax, save_to_csv, read_from_csv

def main():
    filename = 'tax_records.csv'

    print("\n---Welcome to Malaysian Tax Input Program---\n")


    # Registration
    def register():
        ic_number = input("\nEnter your IC number (12 digits): ")
        password = input("Enter your password (last 4 digits of your IC): ")
        
        # Verify user during registration
        if not verify_user(ic_number, password):
            print("\nInvalid registration details. IC number must be 12 digits and password must be the last 4 digits of the IC number.\n")
            return
        
        with open('users.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([ic_number, password])

        print("\nRegistration successful. Please log in.\n")

    # Login
    def login():
        ic_number = input("\nEnter your IC number: ")
        password = input("Enter your password (last 4 digits of your IC): ")

        # Make sure IC number is 12 digit and password is last 4 digit of IC
        if verify_user(ic_number, password):
            # User logged in successfully or not
            with open('users.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == ic_number and row[1] == password:
                        print("\nLogged in successfully!\n")
                        break
                else:
                    print("\nInvalid username or password!\n")
                    return
                        
        
            # Input annual income and tax relief
            try:
                income = float(input("Enter your annual income: "))
                tax_relief = float(input("Enter your tax relief amount: "))
            except ValueError:
                print("\nInvalid input. Please enter numeric values for income and tax relief.\n")
                return

            # Calculate tax payable
            tax_payable = calculate_tax(income, tax_relief)
            print(f"Your tax payable is: {tax_payable}")

            # Store user data in CSV
            data = [ic_number, income, tax_relief, tax_payable]
            save_to_csv(data, filename)
        
            # Read and display tax records
            df = read_from_csv(filename)
            if df is not None:
                print("\nTax Records:")
                print(df)
        else:
            print("\nInvalid login credentials.\n")

    
    # Show the tax records
    def show_record():
        df = read_from_csv(filename)
        if df is not None:
            print("\nTax Records:")
            print(df)

    # Main starting place
    while True:
        print("\nHow can i help you?\n1. Register a new account\n2. Login and calculate tax payable\n3. Show Tax record\n4. Exit")
        selection = int(input("Please enter a number for your selection: "))
        if selection == 1:
            register()
        elif selection == 2:
            login()
        elif selection == 3:
            show_record()
        elif selection == 4:
            print("\nThank you for using the program!\n")
            break
        else:
            print("\nInvalid number! Please try again.\n")

if __name__ == "__main__":
    main()