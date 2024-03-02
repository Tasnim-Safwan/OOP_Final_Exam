class Bank:
  def __init__(self):
    self.users = {}
    self.email={}
    self.total_balance = 0
    self.total_loan = 0
    self.loan_enabled = True

  def create_account(self, name, email, password, balance):
    if name in self.email:
      print("Account already exists for", email)
      return
    self.users[name] = User(name, email, password,balance)
    self.users[email]= User(name, email, password,balance)
    print("Account created successfully for", name)

  def get_user(self, name):
    return self.users.get(name)

  def is_loan_enabled(self):
    return self.loan_enabled

  def toggle_loan(self):
    self.loan_enabled = not self.loan_enabled
    print("Loan feature", "enabled" if self.loan_enabled else "disabled")

class User:
  def __init__(self, name, email, password, balance):
    self.name = name
    self.email= email
    self.password= password
    self.balance = balance
    bank.total_balance+= balance
    self.transactions = []

  def deposit(self, amount):
    self.balance += amount
    bank.total_balance+= amount
    self.transactions.append(f"Deposit: +{amount}")
    print(f"{amount} deposited successfully. Current balance: {self.balance}")

  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient funds")
      return
    self.balance -= amount
    bank.total_balance-= amount
    self.transactions.append(f"Withdrawal: -{amount}")
    print(f"{amount} withdrawn successfully. Current balance: {self.balance}")


  def check_balance(self):
    print(f"Current balance: {self.balance}")

  def transfer(self, bank, recipient, amount):
    if amount > self.balance:
      print("Insufficient funds")
      return
    recipient_user = bank.get_user(recipient)
    if not recipient_user:
      print("Invalid")
      return
    self.balance -= amount
    recipient_user.deposit(amount)
    bank.total_balance -= amount
    self.transactions.append(f"Transfer to {recipient}: -{amount}")
    recipient_user.transactions.append(f"Transfer from {self.name}: +{amount}")

  def get_transactions(self):
    if not self.transactions:
      print("No transactions found")
      return
    print("Transactions:")
    for transaction in self.transactions:
      print(transaction)

  def request_loan(self, bank, amount):
    if not bank.is_loan_enabled():
      print("Loans are currently disabled")
      return
    if amount > 2 * self.balance:
      print("Loan amount exceeds twice your balance")
      return
    bank.total_loan += amount
    bank.total_balance-= amount
    self.balance += amount
    
    self.transactions.append(f"Loan: +{amount}")
    print(f"Loan of {amount} approved. Current balance: {self.balance}")
    

    # Check for bank bankruptcy 
    if bank.total_balance - bank.total_loan < 0:
      print("Warning: Bank is low on funds!")


# Example usage
bank = Bank()

# Admin actions
bank.create_account("Jhankar Mahbub","jm@gmail.com", 123, 1000)
bank.create_account("Tasnim Safwan","ts@gmail.com", 345, 500)

print("Total bank balance:", bank.total_balance)  # 0 (initial)
# User actions
Jhankar = bank.get_user("Jhankar Mahbub")
Jhankar.deposit(500)
Jhankar.withdraw(200)
Jhankar.check_balance()  
print("Total bank balance:", bank.total_balance)  
Jhankar.transfer(bank, "Tasnim Safwan", 100)
print("Total bank balance:", bank.total_balance)  
Jhankar.get_transactions()
Jhankar.request_loan(bank, 1000)  
print("Total bank balance:", bank.total_balance)  

Tasnim = bank.get_user("Tasnim Safwan")
Tasnim.check_balance()  
Tasnim.get_transactions()
print("Total bank balance:", bank.total_balance)  
bank.toggle_loan 
