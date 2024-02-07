class Account:
    def __init__(self,name,amount,place):
        self.acc_name=name
        self.deposit_amount=amount
        self.acc_place=place

class Saving_account:
    min_bal=500
    def saving(self):
        print(f'show the min_bal in Saving_account:{Saving_account.min_bal}')
        

class Current_acount(Account,Saving_account):
    min_bal=10000
    def current(self):
        print(f'show the min_bal in Current_acount:{Current_acount.min_bal}')

obj=Current_acount('Ahmad',2000,'Bangalore')
print(obj.__dict__)
obj.saving()
obj.current()