a = int(input("Enter percentage to check grade : "))
if a>=90 and a<=100:
    print("A Grade")
elif a>=70 and a<90:
    print("B Grade")
elif a>=50 and a<70:
    print("C Grade")
elif a>=30 and a<50:
    print("D Grade")
elif a>=0 and a<30:
    print("E Grade")
else:
    print("PLEASE PROVIDE CORECT PERCENTAGE")
