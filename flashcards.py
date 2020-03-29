import tkinter as tk
import random
from tkinter import *


#I want to study for the GRE.

#I go to a website that has a word list and I copy and paste it into a csv file:
# https://www.graduateshotline.com/gre-word-list.html#x2

#First I'll parse my file and put the words and their definitions into a dictionary


file = open("gre_vocab.csv", "r", encoding='utf-8-sig')
gre_words = {}
global current_word
global flip
flip = 0 #means it is the word showing
for line in file:
    line = line.rstrip('\n') #get rid of end of line marker, '\n'
    line = line.split(",") #csv is comma separated, so we will get words and definitions in a string list
    gre_words[line[0]] = line[1]

    
#I'm going to want my flashcard words to appear randomly so let's create a function that randomly selects a word
def random_word(rlist):
    word = random.choice(list(rlist.keys()))
    return word


def next_card():
    global current_word
    current_word = random_word(gre_words)
    card.configure(text = current_word, background = "black")


def flip_card(status):
    global flip
    if status == 0:
        card.configure(text= gre_words[current_word], background = "red")
        flip = 1
    else:
        card.configure(text = current_word, background = "black")
        flip = 0


#Setting up the window
window = tk.Tk()
window.title("Flashcard Application")
window.configure(width = 500, height = 500, background = 'lightblue')
window.update()
windowHeight = window.winfo_height()
windowWidth = window.winfo_width()


#Initial card value
current_word = random_word(gre_words)
card = tk.Label(
    text= current_word,
    fg="white",
    bg="black",
    width=50,
    height=10
)

card.place(relx = .5, rely = .3, anchor = tk.CENTER)

button = tk.Button(window, text = "Flip Card", command= lambda : flip_card(flip))
button.place(relx = .2, rely = .5, anchor = tk.CENTER)


button2 = tk.Button(window, text = "Next", command= lambda : next_card())
button2.place(relx = .8, rely = .5, anchor = tk.CENTER)

window.mainloop()



