import tkinter as tk
import customtkinter as ctk
from pytube import YouTube

def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        title.configure(text=yt_object.title, text_color="white")
        finish_label.configure(text="Downloaded!")
        video.download()
    except:
        finish_label.configure(text="Download Error, please Try again!")


def on_progress(streams, chunk, bytes_remaining):
    total_size = streams.filesize
    bytes_download = total_size - bytes_remaining
    percent_complete = (bytes_download / total_size) * 100
    cast_per = str(int(percent_complete))
    p_percent.configure(text=cast_per+'%') 
    p_percent.update()

    p_bar.set(float(percent_complete)/ 100)


# System Setting
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# App frame
app = ctk.CTk()
app.geometry("800x500")
app.title("Youtube Downloader")

# Adding UI elements
title = ctk.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=20, pady=20)

# link input
url_var = tk.StringVar()
link = ctk.CTkEntry(app, width=400, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finish_label = ctk.CTkLabel(app, text="")
finish_label.pack()

# Progress percentage
p_percent = ctk.CTkLabel(app, text="0%")
p_percent.pack()

# progress bar
p_bar = ctk.CTkProgressBar(app, width=400)
p_bar.set(0)
p_bar.pack(padx=20, pady=20)

# Download Button
download = ctk.CTkButton(app, text="Download", command=start_download)
download.pack(padx=20, pady=20)

if __name__ == '__main__':
    app.mainloop()