try:
    num1, num2 = eval(input("enter two number,  separated by a comma :"))
    result = num1 / num2
    print("Result is", result)
#using multiple except blocks for different type of error


except ZeroDivisionError:
    print("Divission by zero is error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1, 2")

except:
    print("wrong input")

else:
    print("No exceptions")

finally:
    print("this will execute no matter what")