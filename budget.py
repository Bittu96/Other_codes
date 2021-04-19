class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.totalAmount = 0.00
        print(f'{self.name} account opened with balance 0.00')
    
    def deposit(self, amount="", description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({'amount': self.amount, 'description':self.description})
        self.totalAmount += self.amount
        print(f'Deposit of {self.amount} -> {self.name} balance: {self.totalAmount}')

    def withdraw(self, amount="", description=""):
        self.amount = amount
        self.description = description
        
        if self.amount <= self.totalAmount:
            self.ledger.append({'amount': -self.amount, 'description':self.description})
            self.totalAmount -= self.amount
            return True
        else: return False 

    def check_funds(self, fund):
        self.fund = fund
        if self.fund <= self.totalAmount: return True
        else: return False 

    def get_balance(self):
        return self.totalAmount

    def transfer(self, fund, cls):
        self.fund = fund
        if self.fund < self.totalAmount:
            cls.deposit(self.fund, 'Transfer from Food')
            self.ledger.append({'amount': -self.fund, 'description':'Transfer to Entertainment'})
            self.totalAmount -= self.fund
            return True
        else: return False
    
    def __str__(self):
        # sheet = f"*************{self.name}*************\n"
        l = (30-len(self.name))//2
        sheet = '*'*l +self.name+ '*'*(30-len(self.name)-l)+'\n'
        for each in self.ledger:
            sheet += each['description'].ljust(23)[:23]+('%.2f'%each['amount']).rjust(7)+'\n'
        sheet+= 'Total:'+('%.2f'%self.totalAmount).rjust(7)
        return sheet

def create_spend_chart(categories):
    l1 = ((categories[0].ledger[0]['amount'] - categories[0].get_balance())/categories[0].ledger[0]['amount'])
    l2 = ((categories[1].ledger[0]['amount'] - categories[1].get_balance())/categories[1].ledger[0]['amount'])
    l3 = ((categories[2].ledger[0]['amount'] - categories[2].get_balance())/categories[2].ledger[0]['amount'])

    chart = "Percentage spent by category\n"
    l1, l2, l3 = 0, 70, 20
    for i in range(100,-10,-10):
        perc = (str(i)+'|').rjust(4)
        a = 'o' if i<=l1 else ' '
        b = 'o' if i<=l2 else ' '
        c = 'o' if i<=l3 else ' '
        markers = f' {a}  {b}  {c}  \n'
        chart+=(perc+ markers)
    chart+=('    ----------\n')
    chart+=("     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
    return chart


food = Category('Food')
ent = Category('Entertainment')
food.deposit(100, 'cake')
food.deposit(300, 'chocolates')
food.withdraw(100)
ent.deposit(1000)
ent.withdraw(500, 'Movie')
busi = Category('Business')
print(food)
print(ent)
print(busi)


