string = str(input("Input sentence: "))


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    n = 0
    for text in counts:
        n = n + 1
    return n


print("There are", (word_count(string)), "words in this string:", string)
