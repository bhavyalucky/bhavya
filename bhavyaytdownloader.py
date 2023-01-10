from tkinter import *

from tkinter import filedialog 
from pytube import YouTube


root = Tk()

root.geometry("800x500")
root.title("YT video downloader")
root.configure(bg="black")

def browse():
    download_directory = filedialog.askdirectory(initialdir="C://Users/SAMYAKLAB_116/Downloads",title="save video")
    label3['text'] = download_directory

def download():
    download_link = entry1.get
    download_path = label3["text"]
    getvideo = YouTube(download_link)
    stream= getvideo.streams.get_highest_resolution()
    stream.download(download_path)
    




	
label1 = Label(root, bg="white", text="YouTube Video Downloader", font=("aerial",24, "italic"), )
label1.place(x=10, y=20)


label2 = Label(root, bg="green", text="Video Link -:", font=("aerial",20))
label2.place(x=10, y=120)

entry1 = Entry(root, width = 50, bg="white", font=("aerial",23))
entry1.place(x=200, y=120)


button2 = Button(root, text="download video",font="algeria",bg="light blue",command=download)
button2.place(x=10,y=160)


label2 = Label(root, bg="green", text="Video Destination -:", font=("aerial",20))
label2.place(x=10, y=320)


label3 = Label(root, width =50, bg="red", font=("aerial",20))
label3.place(x=285, y=320)

button1 = Button(root, text="browse",font="algeria",bg="light blue",command=browse)
button1.place(x=10,y=360)

    


root.mainloop()