from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=jsSd5oR_n8I")
yt = yt.get('mp4', '720p')
yt.download()
