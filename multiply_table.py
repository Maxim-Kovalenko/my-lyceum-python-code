# Составьте программу для вывода таблицы умножения от 1 до 10 для любого введенного числа.
print("Hi!")
print("It's table output")
while True:
    a = float(input("Enter number: "))
    for i in range(1, 11):
        print(a, "*", i, "=", a * i)