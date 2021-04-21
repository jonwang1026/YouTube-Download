from pytube import YouTube, Stream


def audioOnly(fileName, path, url):
    try:
        yt = YouTube(url)
        print(yt.streams.get_audio_only().download(path, fileName) + " downloaded")
    except:
        print("double check the video URL")


def mp4(fileName, path, url):
    try:
        yt = YouTube(url)
        for item in yt.streams:
            print(item)
    except:
        print("double check the video URL")


url = 'https://www.youtube.com/watch?v=nI23M0n8SE0'
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
#path = str(input("Enter path to download file: "))

mp4(fileName, path, url)


