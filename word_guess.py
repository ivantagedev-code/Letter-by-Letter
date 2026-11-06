import random

easy_words = ["hello", "castle", "garden", "window", "shadow", "pickle", "theory",
              "planet", "bridge", "candle", "jungle", "pencil", "rocket", "purple", "monkey"]

medium_words = ["volcano", "paradox", "nonsense", "skeleton", "aquarium", "telescope", "hurricane",
                "mountain", "elephant", "notebook", "universe", "keyboard", "umbrella",
                "adventure", "chocolate"]

hard_words = ["suspicious", "hypothesis", "government", "quarantine", "bureaucracy", "renaissance",
              "perseverance", "mischievous", "hippopotamus", "constellation",
              "refrigerator", "extraordinary", "responsibility", "communication",
              "pronunciation", "disappointment", "archaeology", "electricity"]

hint = []
hint_used = False

while True:
    difficulty = input("SELECT YOUR DIFFICULTY: EASY OR MEDIUM OR HARD: ").lower()
    if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
        break
    else:
        print("Select a valid difficulty!")

if difficulty == "easy":
    secret_word = random.choice(easy_words)
    attempt = 3
elif difficulty == "medium":
    secret_word = random.choice(medium_words)
    attempt = 7
else:
    secret_word = random.choice(hard_words)
    attempt = 10

length = len(secret_word)
print("\nCurrent word:", "_ "*length)
guessed_letters = []

while attempt > 0:
    try:
        guess = input("Guess a letter: ").lower()
        if guess == "?":
            hint_used = True
            if guess not in hint:
                hint.append(guess)
                hint_letters = []
                for char in secret_word:
                    if char not in guessed_letters:
                        hint_letters.append(char)
                hints = random.choice(hint_letters)
                guess = hints
                print("Hint was succesfully used!")
            else:
                print("Hint left: 0")
                continue
        else:
            hint_used = False
        if not guess.isalpha():
            raise ValueError("Only letters are allowed")
        if len(guess) != 1:
            raise ValueError("Enter a single letter")
    except ValueError:
        print("Invalid input. Please try again.")
        continue
    
    result = ""
    if guess not in guessed_letters:
        guessed_letters.append(guess)
    else:
        print("Letter already guessed!")
        continue
    for letter in secret_word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "
    current_word = result 
    if guess not in secret_word:
        attempt -= 1
        print("Wrong guess! Attempts left:", attempt)
    else:
        if not hint_used:
            print("Great guess!")
    if "_" not in current_word:
        print(f"\nCongratulations!! You guessed the word: {secret_word}")
        break
    print(f"\nCurrent word: {current_word}")
    if attempt == 0 :
        print(f"\nSorry you failed :( The word was {secret_word}")
        break
