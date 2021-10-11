from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

start = (0, 3, 32)
end = (1, 7, 23)

start_time = 3600 * start[0] + 60 * start[1] + start[2]
end_time = 3600 * end[0] + 60 * end[1] + end[2]

ffmpeg_extract_subclip("111.mp4", start_time, end_time, targetname="222.mp4")

