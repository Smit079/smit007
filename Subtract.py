Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def subtract_numbers(a, b):
    return a - b


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


result = subtract_numbers(num1, num2)


print(f"The result of {num1} - {num2} is: {result}")
