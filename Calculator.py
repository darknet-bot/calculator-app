num1 =float(input("Enter first  number:  "))
op = input("Enter operator:")
num2 =float(input("Enter second number:  "))
# num3 =float(input("Enter third number"))
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="/":
    print(num1/num2)
elif op=="*":
    print(num1*num2)
elif op=="%":
    print(num1 % num2)
else:
    print("Invalid")