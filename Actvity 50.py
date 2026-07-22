#useing a try and except
try: 
    number = int(input("Enter a number: "))
    print("the number entered is", number)
#useing value error
except ValueError as ex:
    print("Exception:",ex)