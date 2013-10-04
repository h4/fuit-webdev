# -*- encoding: utf-8 -*-
"""
Определение функции
"""

def square(x):
    'Calculates the square of the number x.'
    return x*x

print square(100)

def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result

print factorial(10)

         
def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n.""" 
     a, b = 0, 1
     while b < n:
         print b,
         a, b = b, a+b

# Now call the function we just defined:
fib(2000)