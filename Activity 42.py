def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P ,Q):
    return P * Q 
def divied(*P, Q): 
    return P / Q

print ("Please select the operation.")
print ("a. Add")
print ("b. Subtract")
print ("c. Multiply")
print ("d. Divied")

choice = input("Please enter choice (a/ b/ c/ d):")
num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'a':
    print (num_1, "+", num_2, "=", add(num_1, num_2))

elif choice == 'a':
    print (num_1, "+", num_2, "=", subtract(num_1, num_2))

elif choice == 'a':
    print (num_1, "+", num_2, "=", multiply(num_1, num_2))

elif choice == 'a':
    print (num_1, "+", num_2, "=", divied(num_1, num_2))

else:
    print ("This is an invalid input")