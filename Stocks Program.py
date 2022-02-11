'''
Name: Alexander DiDomenico
Date: 1/31/22
Program: Stocks Program
'''

#Recieve Inputs
commRate = float(input("What was the comission rate? "))
shares = int(input("How many shares did you purchase? "))
purchase = float(input("What was the purchase price? "))
selling = float(input("What was the selling price? "))
#Calculations
amount = purchase*shares
commPaidPre = amount*commRate
sold = selling*shares
commPaidPost = sold*commRate
totalComm = commPaidPre + commPaidPost
profit = sold-amount-totalComm
#Print Statements with Formatting
print(f"Amount paid for stock: ${amount:.1f}")
print(f"Commision paid on the purhcase: ${commPaidPre:.1f}")
print(f"Amount the stok sold for: ${sold:.1f}")
print(f"Commision paif on the sale: ${commPaidPost:.1f}")
print(f"Total commision paid: ${totalComm:.1}")
print(f"Profit (positive or negative): ${profit:.1f}")

      
