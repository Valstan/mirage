from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *


# часы, минуты, секунды
start = (0, 0, 6)
end = (0, 13, 19)

start_time = 3600 * start[0] + 60 * start[1] + start[2]
end_time = 3600 * end[0] + 60 * end[1] + end[2]

ffmpeg_extract_subclip("111.mp4", start_time, end_time, targetname="rutub_vk.mp4")

img = ['1.png']

clips = [ImageClip(m).set_duration(2)
         for m in img]

concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile("000.mp4", fps=24)

clip1 = VideoFileClip("000.mp4")
clip3 = VideoFileClip("rutub_vk.mp4")
final_clip = concatenate_videoclips([clip1, clip3])
final_clip.write_videofile("telega.mp4")
