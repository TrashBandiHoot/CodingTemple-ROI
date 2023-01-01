"""
    Income:
    $2,000

    Expenses:
    Taxes, 150
    Insurance, 100
    Utilities, 0
        electric
        water
        sewer
        garbage
        gas
    HOA, 0
    Lawn/Snow, 0
    Vacancy, 100
    Repairs, 100
    CAPEX, 100
    Property Management, 200
    Mortgage, 860

    TOTAL EXPENSES: 1610

    Cash flow:

    income - expenses = 390

    TOTL MONTHLY CASHFLOW: 390
    YEARLY: 4,680

    Cash on cash ROI:

    Down payment: 40,000
    Closing costs: 3,000
    Rehab budget: 7,000
    Misc.: 0

    TOTAL INVESTMENT: 50,000

    Annual cashflow/total investment = 9.36%

    COCROI = 9.36%

"""

class Calc():
    def __init__(self):
        self.monthlyincome = 0
        self.monthlyexpenses = 0
        self.monthlycashflow = 0
        self.returnOnInvestment = 0

    def income(self):
        rent = int(input('What is your rental income?: '))
        laundry = int(input('What is your laundry income?: '))
        storage = int(input('What is your storage income?: '))
        misc = int(input('What is your miscellaneous income?: '))

        self.monthlyincome = rent + laundry + storage + misc
        
        print(f'Your total monthly income is: {self.monthlyincome}')

         

    def expenses(self):
        # Taxes
        expense1 = int(input('How much are the taxes on the property?: '))
        # Insurance
        expense2 = int(input('How much is the insurance?: '))
        # Utilities
        expense3 = int(input('How much are utilities?: '))
        # HOA
        expense4 = int(input('How much do you pay for HOA?: '))
        # Lawn/Snow
        expense5 = int(input('How much do you pay for lawn/snow care?: '))
        # Vacancy
        expense6 = int(input('How much do you set aside for vacancies?: '))
        # Repairs
        expense7 = int(input('How much do you set aside for repairs?: '))
        # CAPEX
        expense8 = int(input('How much do you set aside for capital expenditures?: '))
        # Property Management
        expense9 = int(input('How much do you spend on property management?: '))
        # Mortgage
        expense10 = int(input('How much is the mortgage on the home?: '))
        
        self.monthlyexpenses = expense1+expense2+expense3+expense4+expense5+expense6+expense7+expense8+expense9+expense10

        print(f'Your monthly expense is:{self.monthlyexpenses}')

    def cashFlow(self):
        self.monthlycashflow = self.monthlyincome - self.monthlyexpenses
        print(f'Your total monthly cashflow is: {self.monthlycashflow}')

    def roi(self):
        expense1 = int(input('What is your down payment?: '))
        expense2 = int(input('What are your closing costs?: '))
        expense3 = int(input('What is your rehab budget?: '))
        expense4 = int(input('Miscellaneous costs?: '))

        totalinvestment = expense1 + expense2 + expense3 + expense4
        yearlyCashFlow = self.monthlycashflow * 12
        self.returnOnInvestment = yearlyCashFlow / totalinvestment
        print(f'Your ROI is {self.returnOnInvestment}')

c = Calc()


while True:

    userInput = input('Would you like to run the calculator? "Y" or "N": ')

    if userInput.upper() == 'Y':
        c.income()
        c.expenses()
        c.cashFlow()
        c.roi()
    else:
        break

