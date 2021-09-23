#!python


isDoorLocked = False
hasKey = True

if (isDoorLocked==True and hasKey==True) or (isDoorLocked == False):
    print("You can get into your house")
else:
    print("You cannot get into your house")



a = 3
b = 5
c = 4

highest = max(a,b,c)
lowest = min(a,b,c)
middle = a + b + c - highest - lowest


print(lowest)
print(highest)
print(middle)
exit()



if a > b:
    if a > c:
        print("a is the largest")

if a > b and a > c:
    print("a is the largest")

# friends: Evan, Ethan, Max

if person == "Max" or "Evan" or "Ethan":
    print("person is my friend")
