import csv
import os
import pandas as pd

def verify_user(ic_number, password):
    # Check if IC number is 12 digits long and password matches the last 4 digits of IC number
    return len(ic_number) == 12 and password == ic_number[-4:]

def calculate_tax(income, tax_relief):
    # Tax calculation based on Malaysian tax rates for the current year
    taxable_income = income - tax_relief
    
    # Tax brackets and rates assessment year 2023
    tax_brackets = [
        (5000, 0.00),
        (20000, 0.01),
        (35000, 0.03),
        (50000, 0.06),
        (70000, 0.11),
        (100000, 0.19),
        (400000, 0.25),
        (600000, 0.26),
        (2000000, 0.28),
        (float('inf'), 0.30)
    ]
    
    # Tax payable calculation
    tax_payable = 0
    previous_bracket = 0
    taxable_income_remain = 0
    for bracket in tax_brackets:
        if taxable_income > bracket[0]:
            tax_payable += (bracket[0] - previous_bracket) * bracket[1]
            taxable_income_remain = taxable_income - bracket[0]
            previous_bracket = bracket[0]
        else:
            tax_payable += taxable_income_remain * bracket[1]
            break

    return tax_payable

# Save tax record to csv file
def save_to_csv(data, filename):
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['IC Number', 'Income', 'Tax Relief', 'Tax Payable'])
        writer.writerow(data)

# Read tax record from csv file
def read_from_csv(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return None
