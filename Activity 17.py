actual_cost = float(input("Please Enter the Actual Product Price: "))

sale_amount = float(input("Please enter the sales amount: "))

if (sale_amount > actual_cost):

 amount = sale_amount - actual_cost
 print("total profit = {0}". format(amount))
else:
 print("no profit!!!")

