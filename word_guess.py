secret_word = "hello"
length = len(secret_word)
current_word = "_ " * length
print(f"Current word: {current_word}")
attempt = 10
start = 1
while start <= attempt:
    guess = input("Guess a letter: ").lower()
    start += 1
    count = 1
    if guess in secret_word:
        print("Great guess!")
        for letter in secret_word:
            if letter == guess:
                pos = 1
                while pos <= count:
                    for blank in current_word:
                            blank = pos
                            #come out of inner loop
                            if blank == count:
                                #store letter instead of _
                                blank = guess
                                result = "_ " * (count - 1) + guess + "_ " * ((length) - count)
                                #printing the current word
                                print(f"Current word: {result}")
                                pos += 1
                                break
                            else:
                                pos += 1
                count += 1
                #come out of middle loop
                if blank == guess:
                    break
            else:
                count += 1
    else:
        attempt -= 1
        print(f"Wrong guess! Attempt left: {attempt}")
    #come out of outer loop
    if attempt == 0:
        break

        