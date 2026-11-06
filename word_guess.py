import random
words = ["hello", "castle", "Garden", "Window", "Shadow", "Telescope", "Volcano", "Skeleton", "Hurricane", 
         "Aquarium", "Paradox", "Hypothesis", "Renaissance", "Perseverance", "Mischievous", "Hippopotamus",
         "Pickle", "Nonsense", "Quarantine", "Suspicious", "Bureaucracy", "Government", "Constellation", "Theory"]
secret_word = random.choice(words).lower()
length = len(secret_word)
print("Current word:", "_ "*length)
attempt = 10
guessed_letters = []
while attempt > 0:
    try:
        guess = input("Guess a letter: ").lower()
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
    print(current_word)
    if guess not in secret_word:
        attempt -= 1
        print("Wrong guess! Attempts left:", attempt)
    else:
        print("Great guess!")
    if "_" not in current_word:
        print(f"Congratulations!! You guessed the word: {secret_word}")
        break
    if attempt == 0 :
        print(f"Sorry you failed :( The word was {secret_word}")
        break
