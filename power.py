# Составьте программу для возведения любого числа в любую натуральную степень используя цикл FOR.
print("Hi!")
print("It's power printer")
while True:
    a = float(input("Write base number: "))
    power = int(input("Write max power number: "))
    for i in range(2, power + 1):
        print(a ** i)
