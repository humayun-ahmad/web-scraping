# Tutorial Link : https://data-flair.training/blogs/python-youtube-downloader-with-pytube/
#
#
#

from tkinter import *
from pytube import YouTube


#  Create Display Window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("youtube video downloader")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

