numbers_list = [1, 2, 3]
numbers_tuple = (4, 5, 6)
result = list(map(str, numbers_list + list(numbers_tuple)))
print(result)
