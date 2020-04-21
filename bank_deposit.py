# Составьте программу для решения следюущей задачи:
# Клиент кладёт в банк сумму Х, под процент P. Сколько у него будет через N лет, если каждый год он будет снимать со счета сумму K.
print("Hi")
print("It's bank deposit calculator")
while True:
    x = float(input("What sum of money will you put for deposit: "))
    p = float(input("Write deposit percent: "))
    n = int(input("Write deposit years number: "))
    k = float(input("Write money sum bank will give you every year: "))
    p = p / 100
    end_sum =  x *(1 + p * n) - n * k
    print("The end sum of money for this", n, "years will be:", end_sum,)
    print("--------------------------------------------------------")
    print()