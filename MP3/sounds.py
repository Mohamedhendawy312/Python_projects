# Libraries definitions
from glob import glob
from tkinter import *
import tkinter as tk
from tkinter import font
from turtle import clear
from numpy import pad
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
from pyparsing import col

# Defining the window intial vales 
window = tk.Tk()
window.title("MP3")
window.iconbitmap('images/music.ico')
window.geometry("680x480")
# This can be used if we want the window not being resizble
window.resizable(0, 0)                             

# Initializing pygame mixer
pygame.mixer.init()

# song length
def play_time():
    # fixing the doubling step bug that occure because of overlooping
    if stopped:
        return

    # Get Current song elapsed time
    current_time = pygame.mixer.music.get_pos() / 1000

    # Convert to time formate
    converted_current_time = time.strftime('%H:%M:%S',time.gmtime(current_time))

    # grab song title from playlist
    song = playlist_area.get(ACTIVE)

    # play song structure
    song = f'audio/{song}.mp3'

    # Get song with mutagen with MP3 formate
    song_mut = MP3(song)

    # Get song length playtime
    global song_length
    song_length = song_mut.info.length

    # Convert time formate
    converted_song_length = time.strftime('%H:%M:%S',time.gmtime(song_length))

    # Increase current time by 1 sec
    current_time += 1
    if int(slider.get()) == int(song_length):
        status_bar.config(text=f'Time Elapsed: {converted_song_length}  ')

    elif paused:
        pass

    elif int(slider.get()) == int(current_time):
        # Slider hasn't been moved
        # Update slider to position
        slider_position = int(song_length)
        slider.config(to=slider_position, value=int(current_time))
    else:
        # Slider has moved
        slider_position = int(song_length)
        slider.config(to=slider_position, value=int(slider.get()))

        # Convert to time formate
        converted_current_time = time.strftime('%H:%M:%S',time.gmtime(int(slider.get())))

        # Output time status bar
        status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}   ')

        # Move this thing along by one second
        next_time = int(slider.get()) + 1
        slider.config(value=next_time)

    # Update Time
    status_bar.after(1000, play_time)
    

# Add song function
def add_song():
    # file type specified
    song = filedialog.askopenfilename(initialdir='audio/', title="Chose A song", filetypes=(("mp3 Files", "*.mp3"), ))
    
    # strip the unwanted char in the name
    song = song.replace("C:/Users/ELZAHBIA/Desktop/MP3/audio/", "")
    song = song.replace(".mp3", "").capitalize()
    
    # Add song to list box
    playlist_area.insert(END, song)

# Add many song function
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Chose A song", filetypes=(("mp3 Files", "*.mp3"), ))

    # strip the unwanted char in the name
    for song in songs:
        song = song.replace("C:/Users/ELZAHBIA/Desktop/MP3/audio/", "")
        song = song.replace(".mp3", "").capitalize()

        # Add song to list box
        playlist_area.insert(END, song)

# Add play function
def play():
    # Setting the stopped variable into False when playing globally
    global stopped
    stopped = False

    # The local directory location
    song = playlist_area.get(ACTIVE)
    song = f'audio/{song}.mp3'

    # Loading and playing the song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Calling the play_time function
    play_time()

# Create globale variable stopped
global stopped
stopped = False

# Add stop function
def stop():
    # Reset slider and and status bar
    status_bar.config(text='')
    slider.config(value=0)

    # Stop song
    pygame.mixer.music.stop()
    playlist_area.selection_clear(ACTIVE)

    # Clear the status bar
    status_bar.config(text="")

    # Set stop variable is true
    global stopped
    stopped = True

# Create globale variable pasuse
global paused
paused = False

# Add pause and unpause function
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # pause
        pygame.mixer.music.pause()
        paused = True

# add next song function
def next():
    # Reset slider and and status bar
    status_bar.config(text='')
    slider.config(value=0)

    # Get the current song tuple number value
    next_song = playlist_area.curselection()

    # add one to the tuple number value
    next_song = next_song[0] + 1

    # grab song title from playlist
    song = playlist_area.get(next_song)

    # play song structure
    song = f'audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Update selection selector bar
    playlist_area.selection_clear(0, END)
    playlist_area.activate(next_song)
    playlist_area.selection_set(next_song, last=None)

# add next song function
def previous():
    # Reset slider and and status bar
    status_bar.config(text='')
    slider.config(value=0)

    # Get the current song tuple number value
    previous_song = playlist_area.curselection()

    # add one to the tuple number value
    previous_song = previous_song[0] + -1

    # grab song title from playlist
    song = playlist_area.get(previous_song)

    # play song structure
    song = f'audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Update selection selector bar
    playlist_area.selection_clear(0, END)
    playlist_area.activate(previous_song)
    playlist_area.selection_set(previous_song, last=None)

def delete_song():
    # we call the stop function to use the benifits of reseting and stopping after deleting so it dont continue altough we deleted it
    stop()
    playlist_area.delete(ANCHOR)
    pygame.mixer.music.stop()

def delete_all_songs():
    # we call the stop function to use the benifits of reseting and stopping after deleting so it dont continue altough we deleted it
    stop()
    playlist_area.delete(0, END)
    pygame.mixer.music.stop()

def slide(x):
    ## slider_label.config(text=f'{int(slider.get())} of {int(song_length)}')
    song = playlist_area.get(ACTIVE)
    song = f'audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(slider.get()))

def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())

# Create Master frame
master_frame = Frame(window)
master_frame.pack(pady=20)

# Create Playlist Area
playlist_area = Listbox(master_frame, bg="black", fg="blue", font=15, width=60, height=13, selectbackground="white", selectforeground="black")
playlist_area.grid(row=0, column=0, padx=20)

# Create control buttons images
back_button_img = PhotoImage(file="images/backward.png")
pause_button_img = PhotoImage(file="images/pause.png")
play_button_img = PhotoImage(file="images/play.png")
stop_button_img = PhotoImage(file="images/stop.png")
forward_button_img = PhotoImage(file="images/forward.png")


# Create control frame
controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)

# Create volume label frame
volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=0)

# Create control buttons
back_button = Button(controls_frame, image=back_button_img, borderwidth=0, command=previous)
pause_button = Button(controls_frame, image=pause_button_img, borderwidth=0, command=lambda: pause(paused))
play_button = Button(controls_frame, image=play_button_img, borderwidth=0, command=play)
stop_button = Button(controls_frame, image=stop_button_img, borderwidth=0, command=stop)
forward_button = Button(controls_frame, image=forward_button_img, borderwidth=0, command=next)

# choosing where each button will be in the window using the grid function
back_button.grid(row=0, column=0, padx=10)
pause_button.grid(row=0, column=3, padx=10)
play_button.grid(row=0, column=2, padx=10)
stop_button.grid(row=0, column=4, padx=10)
forward_button.grid(row=0, column=1, padx=10)

# Create Menu
my_menu = Menu(window)
window.config(menu=my_menu)

# Create add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add a Single Song To The Playlist", command=add_song)

# Create add many songs to playlist
add_song_menu.add_command(label="Add Multiple Songs To The Playlist", command=add_many_songs)

# Create delete song menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a Song From The Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From The Playlist", command=delete_all_songs)

# Create status bar
status_bar = Label(window, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Creating slider
slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=500)
slider.grid(row=2, column=0, pady=10)

# Create Volume slider
volume_slider= ttk.Scale(volume_frame, from_=1, to=0, orient=VERTICAL, value=1, command=volume, length=230)
volume_slider.pack(pady=0)

# Running the application
if __name__ == "__main__":
    mainloop()