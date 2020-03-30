from_num = 1
to_num = 2
while to_num > from_num:
    print("Hi!")
    print("It's number guesser")
    print("Enter from: ")
    from_num = int(input("From: "))
    print("Enter to: ")
    to_num = int(input("To: "))
    print("It's a number from:", from_num,"to:", to_num,)
    if from_num > to_num:
        print("Invalid input")
    else:
        answer = ""
        while answer != "y":
            trialNumber = 0
            trial = (from_num + to_num) // 2
            print("Guess is", trial, "?(y - yes, g - greater, l -lower) :")
            answer =input( )
            if answer == "y" or answer == "g" or answer == "l":
                trialNumber = 0
                if answer == "y":
                    print("You guessed", trial, "!Good bye!")
                elif answer == "g":
                    from_num = trial + 1
                elif answer == "l":
                    to_num = trial - 1


