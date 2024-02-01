class Bank:
    def __init__(self):
        print("constructor method - special method/special jelibi")

    def open_account(self,bank):
        print('account opened successfully in',bank)

Bank()
Bank()
b1=Bank()
b1.open_account('sbi')