secretWord = str(input("Please Enter the word to guess: "))
turn = len(secretWord)
print ("This word contains", turn, "letters.")
lettersGuessed = input("Type a list of letters: ")

def isWordGuessed(secretWord, lettersGuessed):
    for k in secretWord:
        x = k in lettersGuessed
        if x == "False":
            break
            

    return x   

print(isWordGuessed(secretWord, lettersGuessed))