import random
def choose_word():
    words = ["banana","apple","orange","cherry","grape","melon"]
    return random.choice(words)

def play_hangman():
    print("yahoooo welcome to hangman !!!!!")

    word = choose_word()
    word_length = len(word)
    guessed_letter = set()
    incorrect_guesses = 0
    max_attempt = 6

    while incorrect_guesses < max_attempt:
        display_word = ""
        for letter in word:
            if letter in guessed_letter:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("\nWord :", display_word)
        guess = input("Guess a letter : ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("!! invalid input . please enter a single letter. ")
            continue

        if guess in guessed_letter:
            print("you have already guess that letter. ")
            continue
        guessed_letter.add(guess)

        if guess not in word:
            incorrect_guesses += 1
            print(f"so sorry {guess} is not in the word ")

        if all(letter in guessed_letter for letter in word):
            print("\n Congratulations! you guessed it correct the word : ", word)
            break

    if incorrect_guesses == max_attempt:

        print("\nSorry, you've run out of attempts. The word was: ", word)

if __name__ == "__main__":
    play_hangman()        
        


