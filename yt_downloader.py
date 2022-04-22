from pytube import YouTube

def ytdl(url):
    yt = YouTube(url=url)
    print(yt.title)

    yt_dl = yt.streams.get_lowest_resolution()
    print(f'{round(yt_dl.filesize / 1024000), 3} MB')
    yt_dl.download()
    return True

if __name__ == '__main__':
    ytdl("https://www.youtube.com/watch?v=zmqtfYqy2-U")