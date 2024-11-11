def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input())
sum_of_factorials = sum(factorial(int(digit)) for digit in str(n))

if sum_of_factorials == n:
    print("Strong")
else:
    print("Not Strong")
