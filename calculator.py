print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
option = int(input("choose and operation:"))
if(option in [1,2,3,4]):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

if(option == 1):
    result = num1 + num2
elif(option == 2):
    result = num1 - num2
elif(option == 3):
    result = num1 * num2
elif(option == 4):
    result = num1 / num2

else:
    print("Invalid Operation entered")

print("result of operation is {}".format(result))
