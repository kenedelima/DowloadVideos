import subprocess


def baixar_video():
    while True:
        # Solicita ao usuário a URL do vídeo
        video_url = input(
            "Digite a URL do vídeo do YouTube que você deseja baixar: ")

        # Checa se a URL fornecida é válida
        if not video_url:
            print("URL inválida. Por favor, tente novamente.")
            continue

        try:
            # Executa o comando do yt-dlp para baixar o vídeo
            subprocess.run(['yt-dlp', video_url])
            print("Download concluído!")
        except Exception as e:
            print(f"Ocorreu um erro ao tentar baixar o vídeo: {e}")

        # Pergunta ao usuário se deseja baixar outro vídeo
        opcao = input("Deseja baixar outro vídeo? (s/n): ").strip().lower()
        if opcao != 's':
            print("Encerrando o programa...")
            break


# Executa o programa
baixar_video()
