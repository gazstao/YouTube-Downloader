# YouTube-Downloader
YouTube Video Downloader

#### Descrição

Um programa em Python para baixar vídeos do YouTube de forma prática.  
Utiliza a biblioteca pytube para baixar vídeos em várias resoluções.  
Interface de linha de comando simples, onde o usuário insere a URL do vídeo e seleciona a qualidade desejada.
  
  
#### Funcionalidades

Baixa vídeos do YouTube em diferentes resoluções.  
Interface de linha de comando intuitiva.  
Suporte a playlists (opcional, com ajustes no código).  
Salva vídeos localmente para acesso offline.  

```
youtubedownloader.py -> obtém a melhor resolução com áudio incluso
youtubedownloader2.py -> lista as resoluções existentes e obtém a indicada pelo usuário
youtube_video_mais_audio.py -> obtém a melhor resolução de vídeo e a melhor de áudio
video_audio/junta_video_audio.bat "nome_arquivo" (sem _video.mp4 ou _audio.mp4 no final) -> junta os dois arquivos criando a versão full
```

#### Requisitos

Python 3.6+  
Biblioteca pytube (pip install pytube)  
ffmpeg para juntar vídeo e áudio caso deseje a melhor resolução possível  
  

#### Instalação

Clone o repositório: ```git clone https://github.com/gazstao/YouTube-Downloader```  
Instale a dependência: pip install pytube  
Execute o programa: python downloader.py  

#### Uso

Execute o script.  
Insira a URL do vídeo do YouTube quando solicitado.  
Escolha a resolução desejada entre as opções disponíveis.  
O vídeo será salvo na pasta local.  
  

#### Exemplo
```
python youtubedownloader.py
URL do vídeo: https://www.youtube.com/watch?v=example
Download concluído!
```

#### Notas
Verifique a legalidade do download de vídeos na sua região.  
Certifique-se de ter uma conexão estável com a internet.  

#### Licença
GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
