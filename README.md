🎥 YouTube Downloader Interativo (yt-dlp)

Script em Python para baixar vídeos do YouTube de forma interativa, um por vez.
Mesmo quando a URL tem v=...&list=..., o programa força vídeo único (usa noplaylist=True e URL limpa por id) e, se o vídeo pertencer a uma playlist, permite navegar para o próximo título perguntando se você quer baixar.

✨ Principais recursos

Mostra o título do vídeo antes de baixar.

Pergunta: baixar este vídeo? (s/n)

Se o vídeo fizer parte de uma playlist:

Após cada decisão, mostra o próximo vídeo e pergunta novamente.

Navegação vídeo a vídeo (sem “baixar todos”).

Evita baixar playlist inteira quando a URL contém &list=....

Compatível com Windows, macOS e Linux.

🧠 Como funciona (fluxo)

Solicita uma URL do YouTube (vídeo ou playlist).

Exibe o título do vídeo atual.

Pergunta se deseja baixar este vídeo.

Se o vídeo pertencer a uma playlist:

Mostra o próximo título e pergunta novamente se deseja baixar.

Você pode seguir para o próximo ou encerrar a qualquer momento.

Ao final, pode inserir outra URL ou sair.

O download é sempre individual. Não há opção de “baixar todos”.

⚙️ Instalação
1) Python

Instale o Python 3.8+:

Windows/macOS/Linux: python.org/downloads

2) Dependências

No terminal/prompt:

pip install -r requirements.txt


Conteúdo do requirements.txt:

yt-dlp

3) (Opcional, mas recomendado) FFmpeg

Para melhor qualidade e para juntar vídeo+áudio corretamente:

Windows (Winget):

winget install --id Gyan.FFmpeg


Windows (Chocolatey):

choco install ffmpeg


macOS (Homebrew):

brew install ffmpeg


Linux (Debian/Ubuntu):

sudo apt-get update && sudo apt-get install -y ffmpeg

▶️ Uso

Salve o script como DownloadVideo.py e execute:

python DownloadVideo.py


Exemplo (vídeo único):

Cole a URL do YouTube (vídeo ou playlist) ou tecle Enter para sair:
https://www.youtube.com/watch?v=dQw4w9WgXcQ

Vídeo detectado: Rick Astley - Never Gonna Give You Up
Deseja fazer o download deste vídeo? [s/n]: s
Baixando...
Download concluído!

Deseja inserir outra URL? [s/n]: n
Encerrando o programa...


Exemplo (playlist: navegação vídeo a vídeo):

Cole a URL do YouTube (vídeo ou playlist):
https://www.youtube.com/playlist?list=PL123...

[1/10] Nome do primeiro vídeo
Deseja fazer o download deste vídeo? [s/n]: s
Baixando...
Download concluído!

Deseja verificar o próximo vídeo da lista? [s/n]: s
[2/10] Nome do segundo vídeo
...

🧩 Personalização rápida

No código, você pode ajustar as opções do yt-dlp em ydl_opts_download:

ydl_opts_download = {
    "noplaylist": True,              # mantém sempre vídeo único
    "format": "mp4/bestvideo+bestaudio/best",
    "outtmpl": "%(title)s.%(ext)s",  # nome do arquivo de saída
}


Outros templates úteis:

%(playlist_title|Desconhecida)s/%(playlist_index|0)03d - %(title)s.%(ext)s

downloads/%(uploader)s - %(title)s.%(ext)s

❗ Solução de problemas

“ffmpeg not found” / áudio fora de sincronia / avisos de container
→ Instale o FFmpeg (seção acima) e garanta que ffmpeg esteja no PATH.

Windows abre a Microsoft Store ao digitar python
→ Desative App Execution Aliases:
Configurações → Aplicativos → Configurações avançadas de alias de execução de aplicativos
Desative os toggles de python.exe/python3.exe.

Várias versões do Python
→ Apontar o interpretador explicitamente (ex.: C:\Users\SeuUser\AppData\Local\Programs\Python\Python3xx\python.exe)
ou configurar o Python correto no VS Code (⌘/Ctrl+Shift+P → Python: Select Interpreter).

📁 Estrutura sugerida
youtube-downloader/
├─ DownloadVideo.py
├─ requirements.txt
└─ README.md

🔐 Aviso legal

Este projeto destina-se a fins pessoais/educacionais.
Respeite os termos de serviço do YouTube e os direitos autorais aplicáveis.

🧾 Licença

Distribuído sob a MIT License.
Sinta-se à vontade para usar, modificar e compartilhar, mantendo os créditos.

✍️ Autor

Kenede Lima
Projeto pessoal de automação e aprendizado em Python.
