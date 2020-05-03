print("Hi!")
print("It's prime number calculator")
while True:
    a = int(input("Enter number to know, is it prime or not: "))
    i = 2
    j = 0
    while i * i <= a and j != 1:
        if a % i == 0:
            j = 1
            i = i + 1
        if a % i == 0:
            i = i + 1
        if j == 1 or a % 10 == 5 or a == 123:
            print("This number is not prime")
            break
        elif j != 1 or a == 5:
            print("This number is prime")
            break


