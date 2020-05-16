import random
import string
print ("Python")
print ("Assignment 2")
print ('Task 3\n')
print ("Name Place Animal Things Game\n")

print ('Welcome To The Game\n')

print("\nPlease Face Device In Opposite Direction When Playing\n")

lst = []

for i in range(1, 3):
    print("Player", i , "Name:")
    ele = input()
    lst.append(ele) # adding the element

print("The players list is:", lst)

def randomString(stringLength=1):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

print("Play game with letter -> ", randomString())

player = lst
for i in player:
    print("\n\nPlayer ->", i)
    name = input("Enter name:\n")
    place = input("Enter place:\n")
    animal = input("Enter animal:\n")
    thing = input("Enter thing:\n")
    print("Player", i, "Entered", name,place,animal,thing)

print("\n\nNow Check Your This And Decide Who Is Winner.")
for i in player:
    print("\nPlayer", i, "Entered: \n", name, place, animal, thing)
print("\nThank You For Playing The Game")