# 사칙연산 협업
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

import sys
num1, num2 = map(int, sys.stdin.readline().split())
print(add(num1, num2))
print(sub(num1, num2))
print(multiply(num1, num2))
print(divide(num1, num2))