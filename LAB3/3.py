def armstrong_numbers():
    for num in range(1, 1001):
        num_str = str(num)
        sum_of_digits = sum(int(digit) ** len(num_str) for digit in num_str)
        if sum_of_digits == num:
            print(num)

armstrong_numbers()
