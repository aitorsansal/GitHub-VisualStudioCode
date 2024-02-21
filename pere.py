import random
def AitorFunc():
    def get_user_guess():
        return int(input("Enter your guess: "))

    def play_game():
        number_to_guess = random.randint(1, 10)
        attempts = 3

        while attempts > 0:
            user_guess = get_user_guess()
            if user_guess == number_to_guess:
                print("Congratulations! You've guessed the number.")
                return
            else:
                attempts -= 1
                print("Wrong guess. You have", attempts, "attempts left.")

        print("Sorry, you didn't guess the number. The number was", number_to_guess)

    play_game()


def AngelFunc():
    word = input("THIS IS A MAGIC TRICK, THINK A WORD AND WRITE IT, I WON'T SEE IT -----------> ")
    print("Your word was: "+ word)

    print("I'm a genius")


def VictorFunc():
    print("Victor")


def ManuFunc():
    print("Manu")


AitorFunc()
AngelFunc()
VictorFunc()
ManuFunc()