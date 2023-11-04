from pytube import YouTube
import argparse


def youtube2mp3 (url="https://www.youtube.com/watch?v=Cp9pk-FkE6E", ext = 'M'):
    yt = YouTube(url)
    title = yt.title
    print('Loading...')
    if ext == 'music'or ext == 'm' or ext == 'M' or ext == 'Music' or ext == 'musique' or ext == 'Musique':
        son = yt.streams.filter(only_audio=True)
        yt.streams.get_by_itag(son[-1].itag).download()
        print('Success !')
    elif ext == 'video' or ext == 'v' or ext == 'V' or ext == 'Video' :
        video = yt.streams.filter(file_extension='mp4')
        yt.streams.get_by_itag(video[1].itag).download()
        print('Success !')
    else:
        print('Erreur, format non reconnu')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.set_defaults(url="https://www.youtube.com/watch?v=Cp9pk-FkE6E")

    parser.add_argument("--url", type=str, help="URL de la vidéo Youtube à télécharger")
    parser.add_argument("--f", type=str, help="Format à télécharger : M pour musique, V pour vidéo")
    
    parser.set_defaults(url="https://www.youtube.com/watch?v=Cp9pk-FkE6E", f="M")

    args = parser.parse_args()
    print(args.url)
    print(args.f)
    
    youtube2mp3(args.url,args.f)
