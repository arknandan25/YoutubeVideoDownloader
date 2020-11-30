import ipdb
import pytube
import tkinter as tk
from tkinter.ttk import *
from tkinter import * 
import time 

DEFAULT_SAVE_PATH = '/Users/arkchauhan/Documents/videos'

def progress_function(stream, chunk, bytes_remaining):
    # ipdb.set_trace()
    # print(round((1-bytes_remaining/stream.filesize)*100, 3), '% done...')
    percent = round((1-bytes_remaining/stream.filesize)*100, 3)
    # percent = (100*(stream.filesize-bytes_remaining))/stream.filesize
    print("{:00.0f}% downloaded".format(percent))
    # percent =  "{:00.0f}% ".format(percent)
    # # print(percent)
    progress_label.config(text="{:00.0f}% downloaded".format(percent), fg="blue")
    progress['value'] = int(percent)
    master.update_idletasks() 


def video_downloader(link, save_path = None):
    try:
        youtube  = pytube.YouTube(link, on_progress_callback=progress_function)
        video_id = youtube.streams.filter(progressive=True).order_by('resolution').desc()[0].itag
        video = youtube.streams.get_by_itag(video_id)

        # ipdb.set_trace()
        if save_path is None:
            video.download(DEFAULT_SAVE_PATH)
        else:
            video.download(save_path)
        print('Downloaded...')
        print('Statistics:')

        # ipdb.set_trace()
        op_label.config(text="Video name:    '{n}'      Video resolution: {r}".format(n=video.title, r=video.resolution), fg="green")
    except Exception as k:
        print(k)
        op_label.config(text="Download failed man!!!!", fg="red")

master = tk.Tk()
master.title("Video Downloader by Ark")
tk.Label(master, text="Youtube Video Url").grid(row=0)
e1 = tk.Entry(master)
e1.grid(row=0, column=1)
op_label = tk.Label(master,  text="Welcome Ark, the great!", fg="red")
op_label.grid(row=8, column=0)
progress_label = tk.Label(master,  text="", fg="red")
progress_label.grid(row=0,column=4)
progress = Progressbar(master, orient = "horizontal", length = 100, mode = 'determinate') 
progress.grid(row=3,column=1)
tk.Button(master, text='Submit', command=lambda: video_downloader(e1.get(), DEFAULT_SAVE_PATH)).grid(row=5, column=1, sticky=tk.W, pady=4)
tk.Button(master, text='Quit task', command=master.quit).grid(row=5, column=3, sticky=tk.W, pady=4)

master.mainloop()
