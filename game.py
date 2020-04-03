while True:
    import random
    number = random.randint(1, 50)
    print("Hi!")
    print("It's guesser game")
    print("I made up a number")
    print("You should guess it")
    guess = int(input("write a number from 1 to 50 "))
    while guess != number:
        if guess < number:
            print("Your guess is lower")
        else:
            print("Your guess is greater")
        guess = int(input("Please, try again "))
    print("You're right!")
    print("This number is", number,)