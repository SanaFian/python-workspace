# ============================================
# Project 05: Bank Account Management System
# ============================================

class BankAccount:
    """Represents a bank account with encapsulated balance."""
    
    def __init__(self, owner_name, initial_balance=0.0):
        self.owner_name = owner_name
        # Private attribute: directly modifying this outside the class is forbidden!
        self.__balance = float(initial_balance)
        self.transaction_history = []
        self._record_transaction("Account Created", initial_balance)

    def _record_transaction(self, action, amount):
        """Helper method to log internal transactions."""
        self.transaction_history.append(f"{action}: ${amount:.2f} | Remaining: ${self.__balance:.2f}")

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__balance += amount
            self._record_transaction("Deposit", amount)
            print(f"[+] Successfully deposited ${amount:.2f}.")
        else:
            print("[!] Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct money from the account if sufficient funds exist."""
        if amount <= 0:
            print("[!] Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print(f"[!] Insufficient funds! Current balance: ${self.__balance:.2f}")
        else:
            self.__balance -= amount
            self._record_transaction("Withdrawal", amount)
            print(f"[-] Successfully withdrew ${amount:.2f}.")

    def get_balance(self):
        """Getter method to view the balance securely."""
        return self.__balance

    def show_statement(self):
        """Print full transaction history."""
        print(f"\n--- Statement for {self.owner_name} ---")
        for record in self.transaction_history:
            print(record)
        print(f"Current Balance: ${self.__balance:.2f}")
        print("---------------------------------------")


def main():
    print("Welcome to Python Bank System!")
    name = input("Enter account holder's name: ").strip() or "Sana"
    account = BankAccount(owner_name=name, initial_balance=100.0)

    while True:
        print("\n=== Bank Menu ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Statement")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            print(f"\n[Balance] Available: ${account.get_balance():.2f}")
        elif choice == "2":
            try:
                amt = float(input("Enter deposit amount: "))
                account.deposit(amt)
            except ValueError:
                print("[!] Invalid number format.")
        elif choice == "3":
            try:
                amt = float(input("Enter withdrawal amount: "))
                account.withdraw(amt)
            except ValueError:
                print("[!] Invalid number format.")
        elif choice == "4":
            account.show_statement()
        elif choice == "5":
            print("\nThank you for banking with us. Have a productive day, Sana!")
            break
        else:
            print("[!] Invalid choice. Try again.")


if __name__ == "__main__":
    main()
