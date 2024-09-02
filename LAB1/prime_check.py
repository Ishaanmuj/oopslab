a = int(input("Enter number to check prime : "))
flag = 1
for i in range(2,a):
    if a%i==0:
        flag =0
        break
if flag==1:
    print("Number is prime")
else:
    print("Number is not prime")