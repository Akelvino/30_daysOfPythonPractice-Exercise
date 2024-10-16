class PersonalAccount:
    def __init__(self, firstname, lastname, income, expenses):
        self.fname = firstname
        self.lname= lastname
        self.income = income
        self.expenses = expenses
    
    def total_income(self):
        return(self.income.values())