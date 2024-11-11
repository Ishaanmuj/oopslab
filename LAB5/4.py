numbers = [1, 2, 3, 4]
result = list(map(lambda x, y: x ** y, numbers, range(len(numbers))))
print(result)
