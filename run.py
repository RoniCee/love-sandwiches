# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

"""sales = SHEET.worksheet('sales')
data = sales.get_all_values()
print(data)"""

def get_sales_data():
    while True:
        """Get sales figures input from the user"""
        print("Please enter the six data from the last market")
        print("Data should be six numbers, seperated by commas")
        print("Example 12,13,14,115,16,17")
        data_str = input("Enter your data here: ")
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid")
            break
    return sales_data
#print(f"The data provided is {data_str}")

def validate_data(values):
    """inside the try, coverts all string values into integers. Raises value error if strings cannot be converted into int or ig there isn't 6 exact values"""
    
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provide {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data {e}, please try again\n")
        return False
    return True

def update_sales_worksheet(data):
    """Update sales worksheet, add new row with the list data provided"""
    print("Updating sales worksheet\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully\n")


def calculate_surplus_data(sales_row):
    """Compare sales with stock and calculate surplus for each item type.
    Surplus is salses figures subtracted from stock"""

    print("Calculating surplus data.......\n")
    stock = SHEET.worksheet("stock").get_all_values()
    print(stock)

#[int(value) for value in values}]



def main():
    data = get_sales_data()
    sales_data = [int(num)for num in data]
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)



print("Welcome to Love Sandwiches")
main()

