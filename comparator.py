numbers = [1, 4, 6, 7, 9, 8, 3, 5, 2, 3, 10, 67, 45, 78, 75]


def shakerSort(a):
    #lb, ub границы неотсортированной части массива
    k = ub = len(a)-1
    lb = 1
    while (lb < ub):
    # проход сверху вниз
        for j in range(ub, lb-1, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                k=j
                lb = k
                print(a)
        return a


shakerSort(numbers)



