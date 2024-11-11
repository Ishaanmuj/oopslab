def fibonacci(n):
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list

n = 5
fib_nums = fibonacci(n)
result = list(map(lambda x: x ** 2, fib_nums))
print(result)
