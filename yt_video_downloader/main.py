import tkinter
import customtkinter
import youtube_dl
from pytube import YouTube
import os

print("Youtube Video Downloader : ")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Defining Function to download the video from the link
def download():
    try:
        yt_link = link.get()
        ytObject = YouTube(yt_link, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finished_label.configure(text="")
        download_path = os.getcwd()
        video.download(output_path=download_path)
    except Exception as e:
        print(f"Error : {e}")
        print("Video Not Aviable from the link.")
        finished_label.configure(text=f"Error : {e}", text_color='red')
        exit()
    finished_label.configure(text="Video Downloaded Successfully!", text_color="green")
    reset.pack(pady=5)

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completetion = bytes_downloaded / total_size * 100
    per = str(int(percentage_completetion))
    pPercentage.configure(text=f"{per}%")
    pPercentage.update()
    # print(per)
    # Updating Percentage Bar
    progressBar.set(float(percentage_completetion)/100)

def reset():
    progressBar.set(0)
    finished_label.configure(text="")
    pPercentage.configure(text="0%")
    link.configure(textvariable="")

# setting up the frame
app = customtkinter.CTk()
app.geometry("720x500")
app.title("Youtube Video Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert Youtube Link : ")
title.pack(padx=10, pady=10)

# Adding Input to take the Youtube Link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=45, textvariable=url_var)
link.pack()

# Finished Downloading
finished_label = customtkinter.CTkLabel(app, text="")
finished_label.pack(padx=10, pady=10)

# Progress Percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, height=5, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


# Download Button
download = customtkinter.CTkButton(app, text="Download Video", command=download)
download.pack(pady=10)

# reset Button
reset = customtkinter.CTkButton(app, text="Reset", command=reset)

# Run App Loop
app.mainloop()
