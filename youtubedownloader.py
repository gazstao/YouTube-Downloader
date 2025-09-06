from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path

print("\nGazsTao\nYouTube Vídeo Downloader")
url = input("Digite a URL: ")
destino = Path("pasta_video")
destino.mkdir(exist_ok = True)

yt = YouTube(url, on_progress_callback=on_progress)
print(f"Título: {yt.title}\nDuração: {yt.length}s")

# for stream in yt.streams:
#    print(stream)
# print("\n\n\n")
# print(yt.streams.get_highest_resolution())

# streams que tem áudio e vídeo juntos
progressive = yt.streams.filter(progressive=True, file_extension='mp4')
for s in progressive:
    print(s.resolution, s.mime_type, s.filesize_mb, s.itag)

input("Pressione enter para continuar")
# baixar o de maior resolução com áudio
progressive.get_highest_resolution().download(output_path=destino)

# yt.streams.get_highest_resolution().download(output_path=destino)
print(f"Download concluído! Vídeo salvo em :{destino}")
