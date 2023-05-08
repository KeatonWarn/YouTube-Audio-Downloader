import whisper
from pytube import YouTube
import os

def create_and_open_txt(text, filename):
    with open(filename, "w") as file:
        file.write(text)
    os.startfile(filename)

url = input("Enter the YouTube video URL: ")
yt = YouTube(url)
audio_stream = yt.streams.filter(only_audio=True).first()

output_path = "Youtubeaudios"
filename = "audio.mp3"
audio_stream.download(output_path=output_path, filename=filename)

print(f"Audio downloaded to {output_path}/{filename}")
