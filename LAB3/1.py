def is_disarium(num):
    num_str = str(num)
    total = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    return total == num

num = int(input())
if is_disarium(num):
    print(f"{num} is a Disarium number.")
else:
    print(f"{num} is not a Disarium number.")
