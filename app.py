from tkinter import *
from pytube import YouTube


# Create display window
root = Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title("YouTube Downloader")


Label(root, text="YouTube Downloader By Alphonse Brandon").pack()


# Field to enter link
link = StringVar()

Label(root, text = "Paste the Link Here: ", font = "Helvetica 12 bold").place(x = 50, y = 50)

