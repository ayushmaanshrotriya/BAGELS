import random
NUM_DIGITS = 4
MAX_GUESSES = 12

def main():
    print(f"I WILL THINK OF ANY {NUM_DIGITS} DIGIT NUMBER. YOU HAVE TO GUESS.")
    while(True):
        secretNum = getSecretNumber()
        print(f"I have thought of a number")
        print(f"Guess it. You have max {MAX_GUESSES} guess")

        numOfGuesses = 1
        while numOfGuesses<=MAX_GUESSES:
            guess = ''
            while len(guess)!=NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numOfGuesses}")
                guess = input('> ')
            clues = getClues(guess, secretNum)
            print(clues)
            numOfGuesses+=1

            if guess == secretNum:
                break
            if numOfGuesses>MAX_GUESSES:
                print("You ran out of guesses")
                print(f"The answer was {secretNum}")
        print("Do you want to play again? (YES or NO)")
        if not input("> ").lower().startswith('y'):
            break
    print("Thanks for playing")


def getSecretNumber():
    numbers  = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        print("You Got It")
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
if __name__ == '__main__':
    main()




