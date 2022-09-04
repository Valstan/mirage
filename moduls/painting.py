from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.painting import painting
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.tools.drawing import circle

clip = VideoFileClip("222.mp4")

final = painting(clip, saturation=6, black=0.006)

final.write_videofile('333.mp4')

clip = (
    VideoFileClip('333.mp4', audio=False).subclip(25, 30).add_mask()
)

w, h = clip.size

# The mask is a circle with vanishing radius r(t) = 800-200*t
clip.mask.get_frame = lambda t: circle(
    screensize=(clip.w, clip.h),
    center=(clip.w / 2, clip.h / 4),
    radius=max(0, int(800 - 200 * t)),
    col1=1,
    col2=0,
    blur=4,
)

the_end = TextClip(
    "The End", font="Arial", color="white", fontsize=40
).duration(clip.duration)

final2 = CompositeVideoClip([the_end.set_pos("center"), clip], size=clip.size)

final2.write_videofile("theEnd.mp4")
