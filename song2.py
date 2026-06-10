# from moviepy import *
# from PIL import Image

# audio = AudioFileClip(r"C:\Users\Lenovo\Downloads\舊時光重來.mp3")

# images = [
    # "photo108.jpg",
    # "photo109.jpg",
    # "photo110.jpg",
	# "photo111.jpg"
# ]

# duration = audio.duration / len(images)

# clips = []

# for img in images:
    # clip = (
        # ImageClip(img)
        # .with_duration(duration)
        # .resized(height=720)
    # )

    # clips.append(clip)

# video = concatenate_videoclips(clips)

# video = video.with_audio(audio)

# video.write_videofile(
    # "老同學.mp4",
    # fps=24
# )     


from moviepy import (
    AudioFileClip,
    ImageClip,
    concatenate_videoclips
)

# MP3
audio = AudioFileClip(
    r"C:\Users\Lenovo\Downloads\舊時光重來.mp3"
)

# 照片
images = [
    r"C:\Users\Lenovo\Pictures\108.jpg",
    r"C:\Users\Lenovo\Pictures\109.jpg",
    r"C:\Users\Lenovo\Pictures\110.jpg",
    r"C:\Users\Lenovo\Pictures\115.jpg",
    r"C:\Users\Lenovo\Pictures\115.jpg"
    
]
# 每張照片顯示時間
duration = audio.duration / len(images)

clips = []

for img in images:

    clip = (
        ImageClip(img)
        .with_duration(duration)
        .resized(height=720)
    )

    clips.append(clip)

# 合併照片
video = concatenate_videoclips(
    clips,
    method="compose"
)

# 加入音樂
video = video.with_audio(audio)

video.write_videofile(
    "老同學.mp4",
    codec="libx264",
    audio_codec="aac",
    fps=30
)
print("完成：老同學.mp4")