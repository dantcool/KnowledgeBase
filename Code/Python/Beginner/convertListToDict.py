#just run this cell to generate your list of random integers
import numpy as np
lo=int(float(input("First 2 digits of your R number:")))
hi=int(float(input("Last 3 digits of your R number:")))
thelist=list(np.random.randint(lo,hi,100).tolist()) 
print("\n\n The list you have is: ",thelist)


def convListToDict(x):
    listlength = len(x)
    myDict = {}

    for i in range(listlength):
        if x[i] in myDict:
            print (f'Duplicate Key: ',thelist[i])
        else:
            myDict.update({thelist[i]:'Unique'})
    return myDict

print(convListToDict(thelist))


