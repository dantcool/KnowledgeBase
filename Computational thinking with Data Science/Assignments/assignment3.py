import random

secretnumber = random.randint(1,10)

def guessNum():
    win = False
    count = 0
    
    while win == False and count < 10:
        guess = int(input("Guess a number between 1 and 10"))
        if guess < secretnumber:
            print("Guess Higher")
            count+=1
        
        elif guess > secretnumber:
            print("Guess Lower")
            count+=1
        
        elif guess == secretnumber:
            win = True 
            break
        
    if win == False:
        mes = "You Lose"
    elif win == True:
            mes = 'You win'
    return mes

def guessName():
    secretname = 'Dante'
    guessNum = 1  
    Win1 = False
    length = len((secretname))


    #turn secret name into list first make it lower case 
    secretnamel = secretname.lower()

    #turn string into list full of asterisk
    asterl = []
    for i in range(length):
        asterl.append("*")

    #Convert asterisk list to string then compare to secret screen if match win = true
    lstring = "".join(asterl)
    print(lstring)

    #While loop to see if win or number of guesses is no more than 10  
    while Win1 == False and guessNum <=10:
        #print guess number 
        print('Guess number ',guessNum)

        #Get use to guess letter
        guess = input("Enter a letter: ")

        #loop through string
        for i in range(length):
            #Check if guess matches matches current index if so insert guess letter into
            #matching index of asertisk list
            if guess == secretnamel[i]:
                asterl[i] = guess
                break
        else:
            print(guess," is not in the name")
 

        #Convert asterisk list to string then compare to secret screen if match win = true
        lstring = "".join(asterl)
        print(lstring)
        if lstring == secretnamel:
            Win1=True

        guessNum +=1

    #Evaluate win at end number of tries 
    if Win1 == True:
        print('You win')
    elif Win1 == False:
        print("you lose")

    else:
        print("something has gon wrong")
    


     