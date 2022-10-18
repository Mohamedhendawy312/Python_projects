# Libraries definitions
from multiprocessing.sharedctypes import Value
from tkinter import *
from random import randint
from tkinter import messagebox
import random

from matplotlib.pyplot import text

# Window specifications
window = Tk()
window.title("Rock-Paper_Scissor")
window.geometry("900x700")
window.config(bg="White")

# Images definitions
rock = PhotoImage(file='images/rock.png')
paper = PhotoImage(file='images/paper.png')
scissor = PhotoImage(file='images/scissor.png')

# Creating a list of thoose images
image_list = [rock, paper, scissor]

# PC choosing random number from the image_list from 0 and 2
pc_number = random.randint(0,2)

def game(player_choice):
    # Converting choice to a number
    global pc_number
    pc_number = randint(0,2)
    image_label.config(image=image_list[pc_number])

    # Game conditions
    if player_choice == 0:
        if pc_number == 0:
            messagebox.showinfo("Rock Paper Scissor","It's a draw")
        elif pc_number == 1:
            messagebox.showinfo("Rock Paper Scissor","You loose :(")
        elif pc_number == 2:
            messagebox.showinfo("Rock Paper Scissor","You Win :)")

    elif player_choice == 1:
        if pc_number == 0:
            messagebox.showinfo("Rock Paper Scissor","You Win :)")
        elif pc_number == 1:
            messagebox.showinfo("Rock Paper Scissor","It's a draw")
        elif pc_number == 2:
            messagebox.showinfo("Rock Paper Scissor","You loose :(")

    elif player_choice == 2:
        if pc_number == 0:
            messagebox.showinfo("Rock Paper Scissor","You loose :(")
        elif pc_number == 1:
            messagebox.showinfo("Rock Paper Scissor","You Win :)")
        elif pc_number == 2:
            messagebox.showinfo("Rock Paper Scissor","It's a draw")


# Create choice buttons frame
pc_frame = LabelFrame(window, text="                     PC Choice",font=70, bg="White", bd=0)
pc_frame.grid()

# Throw the PC choice 
image_label = Label(pc_frame, image=image_list[pc_number], bg="White", bd=0)
image_label.grid(row=0, column=0)

# Create choice buttons frame
choice_frame = LabelFrame(window,text="                  Player Choice: Rock ?"
+
"                                     Player Choice: Paper ?"
+
"                                Player Choice: Scissor ?",
font=60, bg="White", bd=0)
choice_frame.grid(pady=20)

# Create player choice buttons
rock_button = Button(choice_frame, image=rock, borderwidth=0, command=lambda: game(0))
paper_button = Button(choice_frame, image=paper, borderwidth=0, command=lambda: game(1))
scissor_button = Button(choice_frame, image=scissor, borderwidth=0, command=lambda: game(2))

# choosing where each button will be in the window using the grid function
rock_button.grid(row=1, column=0, pady=20, padx=20)
paper_button.grid(row=1, column=1, pady=20, padx=20)
scissor_button.grid(row=1, column=2, pady=20, padx=20)

# Running the application
if __name__ == "__main__":
    mainloop()