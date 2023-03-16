import moviepy.editor as mp
clip = mp.VideoFileClip("bunny.mp4")
clip_resized = clip.resize(height=1080)
clip_resized.write_videofile("movie_resized.mp4")