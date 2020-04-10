choice = ""
while choice != 0:
    print("Hi!")
    print("It's seconds calculator")
    choice = input("Will we start (y - yes, n - no )? ")
    s = int(input("Write number of seconds (0 to exit): "))
    if s != 0:
        m = s // 60
        s = s % 60
        h = m // 60
        m = m % 60
        d = h // 24
        h = h % 24
        print("It's", s, "seconds")
        print(m, "minutes")
        print(h, "hours")
        print(d, "days")
    else:
        print("Please write seconds number")

