from pytube import YouTube
import os
from pathlib import Path


def youtube2mp3 (url,path,ext):
    yt = YouTube(url)
    title = yt.title
    if ext == '.mp3':
        son = yt.streams.filter(only_audio=True)
        print(son)
        yt.streams.get_by_itag(son[-1].itag).download()
    else:
        video = yt.streams.filter(file_extension='mp4')
        print(video)
        yt.streams.get_by_itag(video[1].itag).download()

if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=Cp9pk-FkE6E'
    path = '.'
    ext = '.mp3'
    youtube2mp3(url,path,ext)
