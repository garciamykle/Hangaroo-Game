import random
import time
wordList = ['ant','baboon','badger', 'bat', 'bear','beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']
secretWord = random.choice(wordList)
length_word = len(secretWord)
lettersGuessed =[]
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guessWord =[]


def start():
    print ("Hello Player!\n")
    name = input("Enter your Nickname: ")
    print ("Hello, " + name, "Let's Play Hangaroo Game!\n")
    time.sleep(2)


start()

def secret():
    for character in secretWord:
        guessWord.append("_")
        
    print ("The word you have to guess has", length_word, "characters")
    print (' '.join(guessWord))
    time.sleep(2)
    
    print ("You can only have 3 mistakes!")
    time.sleep(2)
    print ("Please only type 1 letter per guess so that it won't crash!") 
    time.sleep(2)
    print ("Hint: Name of an animal")
    time.sleep(2)
    
def guessing():
    turns = 0

    while turns < 3:
        print ("\n", ' '.join(alphabet))
        guess = input("Please Choose a letter: \n").lower()
        
        if guess not in alphabet:
            print ("Kangaroo: Do you not know what a letter is? Please pick a LETTER...")
            turns +=1
            print("Mistakes: ", turns)
        elif guess in lettersGuessed:
            print("Kangaroo: You have already guessed that letter!")
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print ("Kangaroo: WOW! You're good! You guess it correctly!")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guessWord[x] = guess
                        print(' '.join(guessWord))
                alphabet.remove(guess)
            else:
                print("Kangaroo: That letter is not part of the Secret Word. TRY AGAIN!")
                alphabet.remove(guess)
                turns += 1
                print("Mistakes: ", turns)
                if turns == 3:
                    print("Sorry you have used all your turns and the kangaroo died.")
                    print("The secret word was", secretWord)
                    break
        if '_' not in guessWord:
                        print("YOU WON! CONGRATULATIONS!\n")
                        print("Kangaroo: You saved me Thank You :*\n")
                        break              
secret()
guessing()

print("GAME OVER!!!")
                    
                
    