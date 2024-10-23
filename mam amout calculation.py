item = int(input('enter the items purchased'))
cost = float(input('Enter the cost per price'))
total_cost = item * cost
dis = float(input('Enter the discoutn in percentage'))
dis_amt = (dis * total_cost) / 100
dis_cost = total_cost - dis_amt
tax = float(input('Enter tax in percetage'))
tax_amt = (tax * dis_cost) / 100
price = dis_cost + tax_amt
print(price)
