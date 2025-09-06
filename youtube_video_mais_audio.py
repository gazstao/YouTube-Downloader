from pytubefix import YouTube
from pathlib import Path

url = input("URL: ")
destino = Path("video_audio")
destino.mkdir(exist_ok=True)

yt = YouTube(url)
print(f"Título: {yt.title}")
# maior resolução só-vídeo (sem áudio)
video_stream = yt.streams.filter(only_video=True, file_extension='mp4').order_by('resolution').desc().first()
# melhor áudio
audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

video_name = yt.title+"_video.mp4"
audio_name = yt.title+"_audio.mp4"
video_path = video_stream.download(output_path=destino, filename=video_name)
audio_path = audio_stream.download(output_path=destino, filename=audio_name)

print(f"Baixado:\n  vídeo -> {video_path}\n  áudio -> {audio_path}")
