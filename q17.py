def calculator(x, y, operator):
    if operator == 1:
        return x+y
    elif operator == 2:
        return x-y
    elif operator== 3:
        return x*y
    elif operator==4:
        try:
            out = x/y
            return out
        except ZeroDivisionError as error:
            print(error)
    else:
        return "Invalid operator"


print("Calculator")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
operator = int(input("Enter the operation you want to do: "))

result = calculator(num1, num2, operator)
if result is not None:
    print("Result = ", result)



    
            
