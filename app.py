# Title: Youtube Downloader

from tkinter import * 
from pytube import YouTube


#  Creating Window
root = Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title("YouTube Downloader")


Label(root, text="YouTube Downloader By Alphonse Brandon").pack()


# Field to enter link
link = StringVar()

Label(root, text = "Paste the Link Here: ", font = "Helvetica 12 bold").place(x = 50, y = 50)

link_enter = Entry(root, textvariable = link, width = 50).place(x = 50, y = 100)


# Button to download

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = "Video Downloaded", font = "Helvetica 12 bold").place(x = 50, y = 150)


# Youtube Downloader Button

Button(root, text = "DOWNLOAD", font = 'arial 15 bold', bg = 'pale violet red', padx = 2, width = 10, height = 2, command = Downloader).place(x = 50, y = 200)


# Run the main loop

root.mainloop()