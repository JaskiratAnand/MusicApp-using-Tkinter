'''
Python Trainig Project

made by:
    Jaskirat Singh Anand (2002463, BTech CSE 5B2)
    Janmeet Singh (2102463, BTech CSE 5B2)
    Jasnoor Singh (2102465, BTech CSE 5B2)

'''


from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer

color_white = "#ffffff" 
color_green = "#39ad79"
color_grey = "#2a2c2e"

window = Tk()
window.title("")
window.geometry('640x360')
window.configure(background= color_white)
window.resizable(width=FALSE, height=FALSE)

#events'
def play_music():
    playing = listbox.get(ACTIVE)
    playing_song["text"] = playing
    mixer.music.load(playing)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def continue_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def next_music():
    running = playing_song["text"]
    index = songs.index(running)
    new_index = index + 1
    running = songs[new_index]
    mixer.music.load(running)
    mixer.music.play()

    listbox.delete(0, END)

    show()

    listbox.select_set(new_index)
    playing_song["text"] = running

def prev_music():
    running = playing_song["text"]
    index = songs.index(running)
    new_index = index - 1
    running = songs[new_index]
    mixer.music.load(running)
    mixer.music.play()

    listbox.delete(0, END)

    show()

    listbox.select_set(new_index)
    playing_song["text"] = running



# frames
left_frame = Frame(window, width= 280, height=280, bg= color_white)
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = Frame(window, width= 360, height=280, bg= color_white)
right_frame.grid(row=0, column=1, padx=0)
 
down_frame = Frame(window, width= 700, height=80, bg= color_grey)
down_frame.grid(row=1, column=0, columnspan=3, padx=0, pady=1)


#down frame
playing_song = Label(down_frame, text ="Choose a Song", font=("Seoge 12"), width=50, height=1, fg=color_white, bg= color_grey)
playing_song.place(x=0, y=1)

#right frame
listbox= Listbox(right_frame, selectmode=SINGLE, font=("Seoge 12 bold"), width=32, bg= color_green, fg= color_grey)
listbox.grid(row=0, column=0)

w=Scrollbar(right_frame)
w.grid(row=0, column=1)

listbox.config(yscrollcommand=w.set)
w.config(command= listbox.yview)

#images
img_music = Image.open('icons/music.png')
img_music= ImageTk.PhotoImage(img_music)
app_image = Label(left_frame, height=100, image=img_music, padx=10, bg= color_white)
app_image.place(x=80, y=60)


down = 30   #adjusting & aligning buttons
side = 32
a= 120

img_prev = Image.open('icons/prev.png')
img_prev = img_prev.resize((side,side))
img_prev = ImageTk.PhotoImage(img_prev)
prev_button = Button(down_frame, width = side, height=side, image=img_prev, padx=10, bg= color_white, command = prev_music)
prev_button.place(x= a+30, y=down)

img_play = Image.open('icons/play.png')
img_play = img_play.resize((side,side))
img_play = ImageTk.PhotoImage(img_play)
play_button = Button(down_frame, width=side, height=side, image=img_play, padx=10, bg= color_white, command= play_music)
play_button.place(x= a+90, y=down)

img_next = Image.open('icons/next.png')
img_next = img_next.resize((side,side))
img_next = ImageTk.PhotoImage(img_next)
next_button = Button(down_frame, width=side, height=side, image=img_next, padx=10, bg= color_white, command = next_music)
next_button.place(x= a+150, y=down)

img_pause = Image.open('icons/pause.png')
img_pause = img_pause.resize((side,side))
img_pause = ImageTk.PhotoImage(img_pause)
pause_button = Button(down_frame, width=side, height=side, image=img_pause, padx=10, bg= color_white, command = pause_music)
pause_button.place(x= a+210, y=down)

img_continue = Image.open('icons/continue.png')
img_continue = img_continue.resize((side,side))
img_continue = ImageTk.PhotoImage(img_continue)
continue_button = Button(down_frame, width=side, height=side, image=img_continue, padx=10, bg= color_white, command = continue_music)
continue_button.place(x= a+270, y=down)

img_stop = Image.open('icons/stop.png')
img_stop = img_stop.resize((side,side))
img_stop = ImageTk.PhotoImage(img_stop)
stop_button = Button(down_frame, width=side, height=side, image=img_stop, padx=10, bg= color_white, command = stop_music)
stop_button.place(x= a+330, y=down)



os.chdir('music')
songs = os.listdir()

def show():
    for i in songs:
         listbox.insert(END, i)

show()

mixer.init()
mixer_state = StringVar()
mixer_state.set("Choose one!")

window.mainloop()