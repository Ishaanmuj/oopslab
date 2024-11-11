def pattern1():
    for i in range(1, 6):
        for j in range(i):
            print(i, end=" ")
        print()

def pattern2():
    for i in range(5, 0, -1):
        print(" " * (5 - i), end="")
        for j in range(i):
            print(i, end=" ")
        print()

def pattern3():
    for i in range(1, 6):
        print(" " * (5 - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def pattern4():
    for i in range(5, 0, -1):
        print(" " * (5 - i), end="")
        for j in range(i):
            print(i, end=" ")
        print()

def pattern5():
    for i in range(5, 0, -1):
        print(" " * (5 - i), end="")
        for j in range(i):
            print(5, end=" ")
        print()

def pattern6():
    for i in range(1, 6):
        print(" " * (5 - i), end="")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

def pattern7():
    for i in range(6, 0, -1):
        for j in range(i):
            print(j, end=" ")
        print()

def pattern8():
    n = 1
    for i in range(1, 6):
        for j in range(n, n + i):
            print(j, end=" ")
        print()
        n += i

def pattern9():
    n = 1
    for i in range(1, 5):
        for j in range(n, n + i):
            print(j, end=" ")
        print()
        n += i

def pattern10():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()

def pattern11():
    for i in range(5, 0, -1):
        for j in range(5, i - 1, -1):
            print(j, end=" ")
        for j in range(i, 6):
            print(j, end=" ")
        print()

def pattern12():
    n = 10
    for i in range(1, 6):
        for j in range(i):
            print(n - 2 * j, end=" ")
        print()
        n -= 2

def pattern13():
    for i in range(7):
        for j in range(i + 1):
            print(i * j, end=" ")
        print()

def pattern14():
    for i in range(1, 10, 2):
        for j in range(i):
            print(i, end=" ")
        print()

def pattern15():
    for i in range(1, 6):
        print(" " * (5 - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def pattern16():
    for i in range(1, 8):
        print(" " * (7 - i), end="")
        for j in range(i):
            print("*", end=" ")
        print()

def pattern17():
    for i in range(6, 0, -1):
        print(" " * (6 - i), end="")
        for j in range(i):
            print("*", end=" ")
        print()

def pattern18():
    for i in range(1, 6):
        for j in range(i):
            print("*", end=" ")
        print()


pattern1()
print()
pattern2()
print()
pattern3()
print()
pattern4()
print()
pattern5()
print()
pattern6()
print()
pattern7()
print()
pattern8()
print()
pattern9()
print()
pattern10()
print()
pattern11()
print()
pattern12()
print()
pattern13()
print()
pattern14()
print()
pattern15()
print()
pattern16()
print()
pattern17()
print()
pattern18()
