list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_result = list(map(lambda x, y: x + y, list1, list2))
diff_result = list(map(lambda x, y: x - y, list1, list2))
print(sum_result)
print(diff_result)
