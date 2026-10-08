string1 = 'my pussy'
string2 = 'my bootyhole'
myint = 5

print(string1[myint]) 
print(string2[myint])

#starts at index 0 ends at myint 
print(string1[:myint])
print(string2[:myint])

#starts at index of my int and stops at end of string
print(string1[myint:])

print(string1[myint]+string1[:myint]+string1[myint+1:])