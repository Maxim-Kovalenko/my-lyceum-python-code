while True:
    print("Hi!")
    print("It's calculator")
    a = float(input("write 1st number: "))
    b = float(input("write 2nd number: "))
    add = a + b
    sub = a - b
    mul = a * b
    if b == 0:
        print("addition is:", a,)
        print("subtraction is: ", a,)
        print("multiplication is: 0")
        print("Error!Can't divide because 2nd number is 0")
    else:
        print("addition is: ", add,)
        print("subtraction is: ", sub,)
        print("multiplication is: ", mul,)
        print("division is: ", a / b,)