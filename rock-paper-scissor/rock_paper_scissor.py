# Libraries definitions
from multiprocessing.sharedctypes import Value
from tkinter import *
from random import randint
from tkinter import ttk
from tkinter import messagebox
import random
from numpy import pad

# Window specifications
window = Tk()
window.title("Rock-Paper_Scissor")
window.geometry("700x500")
window.config(bg="White")

# Images definitions
rock = PhotoImage(file='images/rock.png')
paper = PhotoImage(file='images/paper.png')
scissor = PhotoImage(file='images/scissor.png')

# Creating a list of thoose images
image_list = [rock, paper, scissor]

# PC choosing random number from the image_list from 0 and 2
choose_number = random.randint(0,2)

# Throw the PC choice 
image_label = Label(window, image=image_list[choose_number], bg="White", bd=0)
image_label.pack(pady=20)

# Play function
def play():
    # PC choice
    choose_number = randint(0,2)
    image_label.config(image=image_list[choose_number])

    # 0 : Rock
    # 1 : Paper
    # 2 : Scissor

    # Converting choice to a number
    if player_choice.get() == "Rock":
        player_choice_value = 0
    elif player_choice.get() == "Paper":
        player_choice_value = 1
    elif player_choice.get() == "Scissor":
        player_choice_value = 2

    # Game conditions
    if player_choice_value == 0:
        if choose_number == 0:
            messagebox.showinfo("Rock Paper Scissor","It's a draw")
        elif choose_number == 1:
            messagebox.showinfo("Rock Paper Scissor","You loose :(")
        elif choose_number == 2:
            messagebox.showinfo("Rock Paper Scissor","You Win :)")

    elif player_choice_value == 1:
        if choose_number == 0:
            messagebox.showinfo("Rock Paper Scissor","You Win :)")
        elif choose_number == 1:
            messagebox.showinfo("Rock Paper Scissor","It's a draw")
        elif choose_number == 2:
            messagebox.showinfo("Rock Paper Scissor","You loose :(")

    elif player_choice_value == 2:
        if choose_number == 0:
            messagebox.showinfo("Rock Paper Scissor","You loose :(")
        elif choose_number == 1:
            messagebox.showinfo("Rock Paper Scissor","You Win :)")
        elif choose_number == 2:
            messagebox.showinfo("Rock Paper Scissor","It's a draw")

# Player choice
player_choice = ttk.Combobox(window, value=("Rock", "Paper", "Scissor"), width=30)
player_choice.current(0)
player_choice.pack(pady=20)

# Create play button
play_button =  Button(window, text="Play", font=20, bg="Green", fg="White", width=15, height=3, command=play)
play_button.pack(pady=10)

# Running the application
if __name__ == "__main__":
    mainloop()