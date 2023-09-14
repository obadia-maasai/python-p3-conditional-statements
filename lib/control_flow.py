#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username == 'admin' and password == 'password123':
        return True
    else:
        return False
print("admin_login")

def hows_the_weather(temperature):
    # your code here
    if temperature < 32:
        return "It's freezing!"
    elif temperature >= 32 and temperature < 70:
        return "It's cool."
    else:
        return "It's warm."
print("how_the_weather")

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
print("fizzbuzz")

def calculator(operation, num1, num2):
    # your code here
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Invalid operation."
print("calculator")