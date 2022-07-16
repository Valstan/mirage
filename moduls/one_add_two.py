from moviepy.editor import VideoFileClip, concatenate_videoclips

clip1 = VideoFileClip("../zastava.mp4")
# clip2 = VideoFileClip("myvideo2.mp4").subclip(50, 60)
clip3 = VideoFileClip("../222.mp4")
final_clip = concatenate_videoclips([clip1, clip3])
final_clip.write_videofile("itogovoe.mp4")
