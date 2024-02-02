class Bank:

    def open_account(self,amount):
        print("sucessfull open account in:",amount)
        self.bank=amount

    def deposit_money(self,amount):
        print("sucessfull money deposit into the account:",amount)

    def withdraw_money(self,amount):
        print("sucessfull money withdraw form the account:",amount)

a=Bank()
print(a)

a1=Bank()
a1.open_account('sbi')
print(a1.__dict__)

a.deposit_money(1000)
a.withdraw_money(500)

