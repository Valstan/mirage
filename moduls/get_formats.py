import youtube_dl as youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    meta = ydl.extract_info(
        'https://youtu.be/jsSd5oR_n8I', download=False)
    formats = meta.get('formats', [meta])
for f in formats:
    print(f['ext'])
