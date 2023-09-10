from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

current_volume = float(0.5)

def play():
    filename = filedialog.askopenfilename(initialdir="C:/",title="Select mp3 file to play")
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]
    
    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="black",text="Current song:" + str(song_title))
        volume_label.config(fg="black",text="Volume: " + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Error opening the mp3 file")

def vol_up():
    try:
        global current_volume
        if current_volume >= 1:
            volume_label.config(fg="blue", text="Volume : Maximum")
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume : "+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text = "No song selected ")

def vol_down():
    try:
        global current_volume
        if current_volume <= 0:
            volume_label.config(fg="orange", text="Volume : Muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume : "+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text = "No song selected")



def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="No song selected ")

def res():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="No song selected")


master = Tk()
master.title("Music Player")
Label(master,text="Music Player",font=("Calibri",15),fg="black").grid(sticky="N",row=0,padx=120)
Label(master,text="Select your song",font=("Calibri",12),fg="black").grid(sticky="N",row=1)
Label(master,text="Volume",font=("Calibri",12),fg="red").grid(sticky="N",row=4)
song_title_label = Label(master,font=("Calibri",12))
song_title_label.grid(sticky="N",row=3)
volume_label = Label(master,font=("Calibri",12))
volume_label.grid(sticky="N",row=5)

Button(master, text="Select Song", font=("Calibri",12),command = play).grid(row=2,sticky="N")
Button(master, text="Pause", font=("Calibri",12),command = pause).grid(row=3,sticky="E")
Button(master, text="Resume", font=("Calibri",12),command = res).grid(row=3,sticky="W")
Button(master, text="-", font=("Calibri",12),width=5,command = vol_down).grid(row=5,sticky="W")
Button(master, text="+", font=("Calibri",12),width=5, command = vol_up).grid(row=5,sticky="E")
 
master.mainloop()
