secretWord = input("please type the desired guess word: \n")
length_word = len(secretWord)
lettersGuessed = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guessWord =[]


def getGuessedWord():
    
    for character in secretWord:
        guessWord.append("_")
        
    print ("The word you have to guess has", length_word, "characters")
    print (' '.join(guessWord))
    
    turns = 1
    
    while turns < 3:
        
        guess = input("Pick a letter: \n").lower()
        
        if guess not in alphabet:
            print ("not a letter...\n")
        elif guess in lettersGuessed:
            print("already been used...\n")
        elif guess not in secretWord:
            print("Wrong guess...\n")
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print ("nice")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guessWord[x] = guess
                        print(' '.join(guessWord))
                        
        if '_' not in guessWord:
                        print("yes... you won... congrats...")
                        break

getGuessedWord()