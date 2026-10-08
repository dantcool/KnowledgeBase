def isWholeNum(x):
   wholeNum = False
   num = x
   numString = str(x)
   if numString[-1] == '0':
       wholeNum = True

   return numString,wholeNum
   


def averageNum(x,y,z):
    average = (x+y+z)/3
    return average

x = 4
y = 34
z = 6
average = averageNum(x,y,z)
iswholenum = isWholeNum(average)

print(average,iswholenum)