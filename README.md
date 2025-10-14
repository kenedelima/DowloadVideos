🎥 YouTube Downloader Interativo (com yt-dlp)

Um script em Python para baixar vídeos do YouTube de forma interativa, utilizando a biblioteca yt-dlp
.
O diferencial deste projeto é a interface de perguntas dinâmicas:
o programa exibe o título de cada vídeo, pergunta se o usuário deseja baixar, e permite navegar manualmente por playlists, decidindo vídeo a vídeo o que baixar.

🚀 Funcionalidades

Baixa vídeos únicos ou playlists completas do YouTube

Mostra o título do vídeo antes de baixar

Permite decidir:

Baixar ou não o vídeo atual

Ver o próximo vídeo da playlist

Encerrar o programa a qualquer momento

Detecta automaticamente se a URL é de vídeo ou playlist

Permite continuar o download a partir do próximo vídeo da lista

🧠 Fluxo do Programa

O programa solicita a URL do vídeo ou playlist

Mostra o título do vídeo atual

Pergunta:

Deseja baixar este vídeo?

✅ Sim → baixa o vídeo

❌ Não → pergunta se deseja inserir outra URL

Se o vídeo pertencer a uma playlist:

Após o download, mostra o próximo título

Pergunta:

Deseja baixar este vídeo?

✅ Sim → baixa e mostra o próximo

❌ Não → pergunta se quer ver o próximo ou encerrar

💻 Exemplo de Execução
Cole a URL do YouTube (vídeo ou playlist) ou tecle Enter para sair:
https://www.youtube.com/watch?v=dQw4w9WgXcQ

Vídeo detectado: Rick Astley - Never Gonna Give You Up
Deseja fazer o download deste vídeo? [s/n]: s
Baixando...
Download concluído!

Deseja inserir outra URL? [s/n]: n
Encerrando o programa...


Ou, no caso de playlist:

Cole a URL do YouTube (vídeo ou playlist):
https://www.youtube.com/playlist?list=PL123abcXYZ

[1/10] Nome do primeiro vídeo
Deseja fazer o download deste vídeo? [s/n]: s
Baixando...
Download concluído!

Deseja verificar o próximo vídeo da lista ou encerrar? [p/e]: p
[2/10] Nome do segundo vídeo
...

⚙️ Instalação

Instale o Python 3.8+

Download do Python

Instale o yt-dlp

pip install yt-dlp


Baixe o script
Salve o código em um arquivo chamado youtube_downloader.py.

Execute o script

python youtube_downloader.py

📁 Estrutura sugerida do projeto
youtube_downloader/
├── youtube_downloader.py
├── README.md
└── requirements.txt

Exemplo de requirements.txt
yt-dlp

🧩 Personalização

Você pode editar as opções de download (formato, nome do arquivo, pasta de saída) dentro da função baixar_video():

ydl_opts_download = {
    "format": "bestvideo+bestaudio/best",
    "outtmpl": "%(playlist_title|Desconhecida)s/%(playlist_index|0)03d - %(title)s.%(ext)s",
}

🛠️ Tecnologias

Python 3.8+

yt-dlp – fork moderno do youtube-dl, com suporte a novos sites e formatos

🧾 Licença

Este projeto é distribuído sob a licença MIT.
Você pode usá-lo, modificá-lo e distribuí-lo livremente, desde que mantenha os créditos.

💡 Dica

Para evitar problemas com o Windows bloqueando o Python da Microsoft Store,
instale o Python direto do site oficial e desative os App Execution Aliases em:

Configurações → Aplicativos → Configurações avançadas de alias de execução de aplicativos

✨ Autor

Kenede Lima
