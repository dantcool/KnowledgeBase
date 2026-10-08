
num = int(input("num "))

for x in range(2,num,1):
    isPrime = True
    for y in range(2,x,1):
        if x%y == 0:
            isPrime = False
            break
print(isPrime)


