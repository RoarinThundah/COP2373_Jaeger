# Import the reduce function from the functools module
from functools import reduce


def get_expenses():

# Collects list of expenses from user, each expense is a dictionary for type and ammount
    expenses = []
    while True:
        print("\nEnter an expense (or press Enter on type to finish):")

        # Get the type of expense from the user
        expense_type = input("Type of expense: ")
        if not expense_type:
            break  # Exit the loop if the user enters an empty string

        # Get the amount of the expense and handle potential errors
        while True:
            try:
                amount_str = input(f"Amount for {expense_type}: $")
                amount = float(amount_str)
                if amount < 0:
                    print("Please enter a positive number for the amount.")
                    continue
                break  # Exit the inner loop if input is a valid positive number
            except ValueError:
                print("Invalid input. Please enter a valid number for the amount.")

        # Add the expense as a dictionary to the list
        expenses.append({'type': expense_type, 'amount': amount})

    return expenses


def analyze_expenses(expenses):
    # Sorts expences from high to low using reduce
    if not expenses:
        print("\nNo expenses were entered.")
        return

    # Calculate total expense using reduce
    total_expense = reduce(lambda total, expense: total + expense['amount'], expenses, 0)

    # Find highest expense using reduce
    highest_expense = reduce(lambda exp1, exp2: exp1 if exp1['amount'] > exp2['amount'] else exp2, expenses)

    # Find the lowest expense using reduce
    lowest_expense = reduce(lambda exp1, exp2: exp1 if exp1['amount'] < exp2['amount'] else exp2, expenses)

    # Display the results
    print("\nMonthly Expense Analysis")
    print(f"Total Expense: ${total_expense:,.2f}")
    print(f"Highest Expense: {highest_expense['type']} - ${highest_expense['amount']:,.2f}")
    print(f"Lowest Expense:  {lowest_expense['type']} - ${lowest_expense['amount']:,.2f}")



def main():
    # Main function to run the expense analyzer program
    print("Welcome to the Monthly Expense Analyzer!")
    user_expenses = get_expenses()
    analyze_expenses(user_expenses)


# Run the main function when the script is executed
if __name__ == "__main__":
    main()