requirement = True
available = 100

for x in range(20,0,-1):
    if x % 2 == 0:
        requirement = True
        available -=1
        print(x,end=' ')
        print (available)
    elif x % 2 == 1:
        requirement = False
        print(x,"")    

# set a list
BB = ["Walter","Jesse","Gus","Hank"]
# loop thru the list
for i in range(0,4,1): # Change the numbers, what happens?
    print(BB[i])