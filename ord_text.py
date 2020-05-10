print("Hi!")
print("This program outputing the code of the symbol")
while True:
    text = str(input("Input text: "))
    for symbol in text:
        code = ord(symbol)
        print("Code of the ", symbol, "is: ", code)
