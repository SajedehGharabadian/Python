from moviepy import editor

vidio = editor.VideoFileClip('yamohamad.mp4')
vidio.audio.write_audiofile('yamohamad.mp3')

