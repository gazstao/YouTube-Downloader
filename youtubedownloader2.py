from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path

print("\nGazsTao\nYouTube Vídeo Downloader")

url = input("Digite a URL: ")
destino = Path("pasta_video")
destino.mkdir(exist_ok=True)

yt = YouTube(url, on_progress_callback=on_progress)

print(f"Título: {yt.title}")
print(f"Duração: {yt.length // 60} min {yt.length % 60} s")

print("\nStreams disponíveis:")
for s in yt.streams:
    tipo = "vídeo+áudio" if s.is_progressive else "somente vídeo/áudio separado"
    # usa getattr para evitar erro quando atributo não existe
    resolucao = getattr(s, "resolution", None) or getattr(s, "abr", "")
    fps = getattr(s, "fps", "")
    print(
        f"itag={s.itag:>3} | {s.mime_type:<12} | "
        f"{resolucao:<8} | {fps or ''}fps | {tipo}"
    )

itag_escolhido = input("\nDigite o itag do stream que deseja baixar (ou Enter para maior resolução): ")

if itag_escolhido.strip():
    stream = yt.streams.get_by_itag(int(itag_escolhido))
else:
    stream = yt.streams.get_highest_resolution()

if stream:
    print(f"\nBaixando: {stream.default_filename} ...")
    stream.download(output_path=destino)
    print(f"Download concluído! Arquivo salvo em: {destino}")
else:
    print("itag inválido ou stream não encontrado.")
