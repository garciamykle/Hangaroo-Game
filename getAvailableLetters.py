secretWord = str(input("Please Enter the word to guess: "))
lettersGuessed = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
   
def getAvailableLetters():
    me=0
    while me == 0:
        lettersGuessed = input("Please type a letter: \n").lower()

        if lettersGuessed in secretWord:
            alphabet.remove(lettersGuessed)
        else:
            alphabet.remove(lettersGuessed)
                
        print ("These are the available words:\n")
        print (''.join(alphabet))

    return me
getAvailableLetters()