n = int(input())
num_str = str(n)
num_digits = len(num_str)
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
if sum_of_powers == n:
    print("Armstrong")
else:
    print("Not Armstrong")
