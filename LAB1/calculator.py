print("************** CALCULATOR **************")

flag = 1
while flag==1:
    a = int(input("Enter NUMBER1 : "))
    b = int(input("Enter NUMBER2 : "))
    c = input("Select operation : +, -, /, *, exit : ")
    if c=="+":
        print("Result : " + str(a+b))
    elif c=="-":
        print("Result : " + str(a-b))
    elif c=="/":
        print("Result : " + str(a/b))
    elif c=="*":
        print("Result : " + str(a*b))
    elif c=="exit":
        flag = 0
        print("Thank you for using calculator")


