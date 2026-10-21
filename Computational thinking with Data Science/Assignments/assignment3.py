import random

secretnumber = random.randint(1,1000)
secretname = 'Dante'

def guessNum():
    win = False
    count = 0
    
    while win == False and count < 10:
        guess = int(input("Guess a number between 1 and 1000"))
        if guess < secretnumber:
            print("Guess Higher")
            count+=1
        
        elif guess > secretnumber:
            print("Guess Lower")
            count+=1
        
        elif guess == secretnumber:
            print ("You Win!!!")
            win = True 
            break
        
    if win == False:
        mes = "You Lose"
    elif win == True:
            mes = 'You win'
    return mes

def guessName():
    secretname = secretname.lower()
    win = False
    lenName = len(secretname)
    aster = ''
    
    print(lenName)
    for x in range(lenName):
        aster += '*'
    print (aster)
    
    while win == False:
        match = False
        
        guess = input('Guess the word by entering a letter')
        
        for i in range(lenName):
            if guess == secretname[i]:
                aster.replace(aster[i],guess)
                print(aster)
                break
            else:
                print('no match found at index',i)
        
        
