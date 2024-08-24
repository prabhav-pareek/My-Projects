import random

def print_hangman(lives):
    stages = [ # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                """,
                # stage 7: head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                """,
                # stage 6: head, torso, both arms, and no legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                """,
                # stage 5: head, torso, left arm, and no legs
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                """,
                # stage 4: head, torso, right arm, and no legs
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                """,
                # stage 3: head, torso, and no arms or legs
                """
                   --------
                   |      |
                   |      O
                   |    
                   |    
                """,
                # stage 2: head and torso, no arms or legs
                """
                   --------
                   |      |
                   |      O
                """,
                # stage 1: only head, no torso, arms, or legs
                """
                   --------
                   |      O
                """,
                # stage 0: no head, torso, arms, or legs
                """
                   --------
                """
    ]
    print(stages[lives])

def game_loop():
    words = ['python', 'hangman', 'prabhav', 'graphicera', 'bhimtal']
    word = random.choice(words)
    guessed = '_' * len(word)
    lives = 7

    while True:
        print("\nLives:", lives)
        print_hangman(lives)
        print("\nWord:", guessed)
        print("\nGuess a letter:")
        letter = input().lower()

        if letter in guessed:
            print("\nYou've already guessed that letter.")
            continue

        if letter in word:
            indexes = [i for i, letter_ in enumerate(word) if letter_ == letter]
            for index in indexes:
                guessed = guessed[:index] + letter + guessed[index + 1:]

            if '_' not in guessed:
                print("\nCongratulations! You've guessed the word.")
                break
        else:
            lives -= 1

        if lives == 0:
            print("\nYou've run out of lives. The word was '{}'.".format(word))
            break

def main():
    print("Welcome to Hangman! Let's get started...")
    game_loop()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()