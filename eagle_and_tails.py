import random
while True:
    print("Hi!")
    print("It's eagle and tails game")
    choicePlayer = input("Write eagle or tails to play: ")
    choiceAI = ["eagle", "tails"]
    choice_random = random.choice(choiceAI)
    if choicePlayer == choice_random:
        print("Yay!You won!")
        print("Your choice was:", choicePlayer,)
    elif choicePlayer != choice_random:
        print("Oh No!")
        print("You lost!")
        print("Game Over!")
    else:
        print("Oops!")
        print("Invalid input!")
