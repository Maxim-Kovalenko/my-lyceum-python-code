print("Hi!")
print("This program reverse the text")
# Бесконечный цикл while
while True:
    # Вводим текст
    text = str(input("Input text: "))
    # Считаем длину строки
    length = len(text)
    # Вводим переменную для текста наоборот
    reversed_text = text[length::-1]
    # Выводим текст и текст наоборот
    print("The reversed text of " + text, "is:",reversed_text)
    # Перевод: Код символа",symbol,"— это: ",code
