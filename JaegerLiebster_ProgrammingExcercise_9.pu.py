import sys


class BankAcct:

    # define stats
    def __init__(self, name, number, balance, interest=0.03):

        self.name = name
        self.number = number
        self.balance = float(balance)
        self.interest = float(interest)

    def __str__(self):

        return (f" --- Account Data ---\n"
                f"Account Name: {self.name}\n"
                f"Account Number: {self.number}\n"
                f"Account Balance: ${self.balance:,.2f}\n"
                f"Account interest rate: {self.interest * 100:.2f}%")

    def deposit(self, deposit_amount):

        if deposit_amount > 0:
            self.balance += deposit_amount
            print(f"You have deposited ${deposit_amount:,.2f}. Your new balance is ${self.balance:,.2f}.")
        else:
            print("Invalid input: Deposit amount must be positive.", file=sys.stderr)

    def withdraw(self, withdraw_amount):

        if withdraw_amount <= 0:
            print("Invalid input: Withdrawal amount must be positive.", file=sys.stderr)
        elif withdraw_amount > self.balance:
            print(f"Error: Insufficient funds. Cannot withdraw ${withdraw_amount:,.2f}.", file=sys.stderr)
            print(f"  Available balance: ${self.balance:,.2f}", file=sys.stderr)
        else:
            self.balance -= withdraw_amount
            print(f"You have successfully withdrawn ${withdraw_amount:,.2f}. Your new balance is ${self.balance:,.2f}.")

    def get_balance(self):

        return self.balance

    def adjust_interest_rate(self, new_rate):

        if new_rate >= 0:
            self.interest = float(new_rate)
            print(f"Interest rate adjusted to {self.interest * 100:.2f}%.")
        else:
            print("Error: Interest rate cannot be negative.", file=sys.stderr)


    def calculate_interest(self, num_days):

        if num_days < 0:
            print("Error: Number of days must be non-negative.", file=sys.stderr)
            return 0.0

        interest_earned = self.balance * self.interest * (num_days / 365)
        return interest_earned

def test_bank_acct():

    print("--- 1. Creating new account ---")

    acct1 = BankAcct("John Smith", "123-456-789", 1000.00, 0.03)

    # Test __str__ method
    print(acct1)

    print("\n--- 2. Testing Deposit ---")
    acct1.deposit(500.50)
    acct1.deposit(-50)

    print("\n--- 3. Testing Withdrawal ---")
    acct1.withdraw(300)
    acct1.withdraw(5000)
    acct1.withdraw(-100)

    print("\n--- 4. Testing Get Balance ---")

    current_bal = acct1.get_balance()
    print(f"Balance from get_balance(): ${current_bal:,.2f}")

    print("\n--- 5. Testing Adjust Interest Rate ---")
    acct1.adjust_interest_rate(0.05)
    acct1.adjust_interest_rate(-0.01)

    print("\n--- 6. Testing Calculate Interest ---")
    interest = acct1.calculate_interest(30)
    print(f"Interest earned over 30 days: ${interest:,.2f}")

    # Calculate interest for 1 year
    interest_year = acct1.calculate_interest(365)
    print(f"Interest earned over 365 days: ${interest_year:,.2f}")

    print("\n--- 7. Final Account State ---")
    # Print the final state using __str__
    print(acct1)

if __name__ == "__main__":
    test_bank_acct()