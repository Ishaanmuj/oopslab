input_string = input()
vowels = "aeiouAEIOU"
count = sum(1 for char in input_string if char in vowels)
print(count)
