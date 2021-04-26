from pytube import YouTube, Stream
import ffmpeg
from pathlib import Path
import os

def audioOnly(fileName, path, url):
    try:
        yt = YouTube(url)
        print(yt.streams.get_audio_only().download(path, fileName) + " downloaded")
    except:
        print("double check the video URL")

def lowVidQuality(fileName, path, url):
    yt = YouTube(url)
    print(yt.streams.get_highest_resolution().download(path, fileName) + " downloaded")

def mp4(fileName, path, url):
    try:
        yt = YouTube(url)
        video_input = yt.streams.filter(adaptive = True, only_video= True, mime_type= "video/mp4")
        if video_input is None or not video_input:
            lowVidQuality(fileName, path, url)
        else:
            audio_input = yt.streams.get_audio_only()
            audio_file_name = yt.title+"_audio"
            video_file_name = yt.title+ "_video"
            video_input.first().download(path, video_file_name)
            audio_input.download(path, audio_file_name)
    except:
        print("double check the video URL")

    directory = os.fsencode(path)
    os.listdir(directory)[0]
        filename = os.fsdecode(file)
        if filename.endswith(".mp4"):
            audio_path = ffmpeg.input(os.path.abspath(filename))
        elif filename.endswith(".webm"):
            video_path = ffmpeg.input(os.path.abspath(filename))
    convertedPath = path +"/Converted"
    Path(convertedPath).mkdir(parents=True, exist_ok=True)
    ffmpeg.concat(video_path, audio_path, v=1, a=1).output(convertedPath + "/converted_video.mp4").run()

url = 'https://www.youtube.com/watch?v=uo9JD9aPO8E'
#url = str(input("YouTube URL: "))

fileName = ""
#fileName = str(input("Enter video name. Leave blank by pressing 'enter' if you want the default video title :"))
if fileName == "":
    fileName = None

video_or_audio = "video"
"""video_or_audio = str(input("Do you want video or audio only. "
                           "If audio only type 'audio'. "
                           "If video type 'video' : "))"""

video_or_audio = video_or_audio.lower()


path = '/Users/jonathan/Desktop'
Path(path + "/downloadedFile").mkdir(parents=True, exist_ok=True)
path = path + "/downloadedFile"

#path = str(input("Enter path to download file: "))

mp4(fileName, path, url)


