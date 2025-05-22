from tkinter import *
from PIL import ImageTk,Image
import random
import tkinter.messagebox as tmsg
import random
secretNUm =  random.randint(1,20)
print("i am thinking a number 1 to 20 ")

#ask from user
for guess in range (1 ,7):
    print("take a guess: ")
    guessesTaken = int(input())

    if guess < secretNUm:
        print("the number is tow low")

    elif guess > secretNUm:
        print("the number is big")
    else:
        break
if(secretNUm == guessesTaken):
    ('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')

else:
    print("no its not correct")