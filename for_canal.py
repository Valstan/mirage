from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *

regim = 1  # 1 - просто вырезать кусочек
path_in_file = "d:/"  # "d:/2222222/"
name_in_file = "S2380001.MP4"  # "S2360033.MP4"
path_out_file = "d:/"
name_out_file = "out_video.mp4"

if regim == 1:
    # часы, минуты, секунды
    start = (0, 9, 24)
    end = (0, 12, 50)

    start_time = 3600 * start[0] + 60 * start[1] + start[2]
    end_time = 3600 * end[0] + 60 * end[1] + end[2]

    ffmpeg_extract_subclip(path_in_file + name_in_file, start_time, end_time, targetname=path_out_file + name_out_file)
else:
    img = ['1.png']

    clips = [ImageClip(m).set_duration(2)
             for m in img]

    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile("000.mp4", fps=24)

    clip1 = VideoFileClip("000.mp4")
    clip3 = VideoFileClip("rutub_vk.mp4")
    final_clip = concatenate_videoclips([clip1, clip3])
    final_clip.write_videofile("telega.mp4")
