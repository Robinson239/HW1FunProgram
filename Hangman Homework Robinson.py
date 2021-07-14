#Robinson Davis
#Date: 7/7/2021
#Fun hangman Homework

#Creating the main function
def main():
    #getting the random module to use later for selecting random words
    import random
    #The list of words that will be used in the game
    WordList = ["banana","elephant","telephone","cinnamon","shark","building","lemur"]
    #This is being used to keep track of when the game should end, when the variable becomes anything other than Y it will end
    Playing_Game="Y"
    while Playing_Game =="Y":
        #setting up variables to keep track of incorrect guesses
        IncorrectLimit= 6
        IncorrectGuesses= 0
        print("Welcome to hangman, Correctly guess all the letters of a word before 6 incorrect tries")
        #Variable used to tell the game when it will end
        GameFinished ="NO"
        #The part below is setting up the list to hold their previous guesses, while also setting up the random word being chosen. 
        guesslist= []
        word= random.choice(WordList)
        word_list= list(word)
        #this is the part that will display the progress on the word with letters and dashes
        word_display = list("_"*len(word))

        #I am running a loop that will continue till the word is guessed or the player runs out of guesses. 
        while GameFinished == "NO":
            #this shows the number of incorrect guesses and also calls a method to display the picture and displayed word
            print ("You have "+ str(IncorrectLimit-IncorrectGuesses) + " incorrect guesses left") 
            show_hangman(IncorrectGuesses,word_display)
            #this gets the guess of the user and verifies they didn't choose something they guessed already or enter something other than letters
            guess = input("What letter or word do you guess: ").lower()
            while guess.isalpha()== False and guess != word  or guess in guesslist:
                guess= input ("Invalid choice! Please use a letter or word that you haven't already guessed: ").lower()
            guesslist.append(guess)
            #this part of the if statement sees if they guessed a single letter correctly
            if guess in word and len(guess)==1:
                index_counter= 0
                #This part replaces the underscores with the correctly guessed letter
                #indexes are properly tracked to make sure the right thing is replaced
                for letter in word:
                    if letter == guess:
                        word_display[index_counter]= letter
                        index_counter+=1
                    else:
                        index_counter+=1
                print()
                print("Good Job, "+guess+ " is in the word")
            #if they guess the whole word correctly this part sets the displayed word to the real word. 
            elif guess == word:
                word_display= word_list
                print()
                print("Good Job, "+guess+ " is the word")
            #This part catches incorrectly guessed words and increases the incorrect guess count.  
            elif len(guess)> 1:
                print()
                print(guess+" is not the word.") 
                IncorrectGuesses += 1
            #This part covers incorrect letter guesses and increases incorrect guess count. 
            else:
                print()
                print(guess+" is not in the word.")
                IncorrectGuesses += 1
                
            #This part checks to see if the game has ended by incorrect guesses or completing the word. Loop will end if game is finished
            if IncorrectGuesses== IncorrectLimit  or word_list == word_display:
                GameFinished = "YES"
            else:
                GameFinished = "NO"
        #This prints out the end if they guessed the word. It calls the method that displays the picture and word
        if word_list == word_display:
            show_hangman(IncorrectGuesses,word_display)
            print("Congratulations! You guessed the word.")
        #This prints out the end if they lost and tells them the word. Also calls the method that displays the hangman. 
        else:
            show_hangman(IncorrectGuesses,word_display)
            print("Sorry you lost :(")
            print("The word was " + word)
        #this asks if they want to play again and checks to make sure they put a valid response. The loop will end if they type N
        Playing_Game = input("Play Again? (Y/N)").upper()
        while Playing_Game != "Y" and Playing_Game != "N":
            Playing_Game = input ("Invalid choice! Please use type Y or N to indicate whether you would like to keep playing: ").upper()
            
            
        
#This method displays the picture and also prints the dashes and the correctly guessed letters
def show_hangman(Incorrect_amount, list_of_word):
    hangman_list= ["""
                      ______
                      |    |
                      |
                      |
                      |
                     ---""",
                   """
                      ______
                      |    |
                      |    0
                      |    
                      |    
                     ---""",
                   """
                      ______
                      |    |
                      |    0
                      |    |
                      |    |
                     ---""",
                   """
                      ______
                      |    |
                      |    0
                      |    |-
                      |    |
                     ---""",
                   """
                      ______
                      |    |
                      |    0
                      |   -|-
                      |    |
                     ---""",
                   """
                      ______
                      |    |
                      |    0
                      |   -|-
                      |    |_
                     ---""",
                   """
                      ______
                      |    |
                      |    0
                      |   -|-
                      |   _|_
                     ---"""]
    print(hangman_list[Incorrect_amount])
    print()
    print(*list_of_word)
    print()
#calling the main function
main()

            
        

            
        
            
        








