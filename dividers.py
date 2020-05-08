print("Hi!")
print("It's prime number calculator")
numbers = []
proverka = []
while True:
    n = int(input("Enter number: "))
    j = False
    i = n - 1
    while i != 2:
        i = i - 1
        if n % i == 0:
            numbers.append(i)
            j = True
        if numbers != proverka and i == 2 and j == True:
            print("This number is not prime")
            print("It's divides by:", numbers)
            break
    if j == False:
        print("This number is prime and divides only by", n, "and", 1)
        break
