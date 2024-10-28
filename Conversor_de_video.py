from tkinter import *
from tkinter import filedialog
from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable, RegexMatchError
import os

# Função que pega o link digitado e faz o download do vídeo
def Baixar_Video():
    url = link.get()    # Captura o texto 
    textodownload.set("Baixando vídeo...")  # Mensagem de status

    # Abre o diálogo para escolher o local e o nome do arquivo
    arquivo_path = filedialog.asksaveasfilename(defaultextension=".mp4", 
                                                filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")])
    
    if arquivo_path:  # Verifica se o usuário escolheu um caminho
        try:
            yt = YouTube(url)  # Cria uma instância do YouTube com o link
            stream = yt.streams.get_highest_resolution()  # Seleciona a melhor resolução disponível
            stream.download(output_path=arquivo_path.rsplit('/', 1)[0], filename=arquivo_path.split('/')[-1])  # Baixa o vídeo no diretório escolhido
            textodownload.set("Download completo!")  # Atualiza para mensagem de sucesso
        except VideoUnavailable:  # Captura a exceção quando o vídeo não está disponível
            textodownload.set("Erro: O vídeo não está disponível.")
        except RegexMatchError:  # Captura a exceção quando a URL não é válida
            textodownload.set("Erro: URL não encontrada.")
        except Exception as e:  # Captura qualquer outra exceção
            textodownload.set(f"Erro: {str(e)}")
    else:
        textodownload.set("Caminho não encontrado")

# Função que pega o link digitado e faz o download do áudio
def Baixar_Audio():
    url = link.get()  # Captura o texto 
    textodownload.set("Baixando áudio...")  # Mensagem de status

    # Abre o diálogo para escolher o local e o nome do arquivo
    arquivo_path = filedialog.asksaveasfilename(defaultextension=".mp3", 
                                                filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")])
    
    if arquivo_path:  # Verifica se o usuário escolheu um caminho
        try:
            yt = YouTube(url)  # Cria uma instância do YouTube com o link
            audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()    # Seleciona o melhor áudio
            audio_stream.download(output_path=arquivo_path.rsplit('/', 1)[0], filename=arquivo_path.split('/')[-1])     # Baixa o áudio no diretório escolhido
            textodownload.set("Download completo!")  # Atualiza para mensagem de sucesso
        except VideoUnavailable:  # Captura a exceção quando o vídeo não está disponível
            textodownload.set("Erro: O vídeo não está disponível.")
        except RegexMatchError:  # Captura a exceção quando a URL não é válida
            textodownload.set("Erro: URL não encontrada.")
        except Exception as e:  # Captura qualquer outra exceção
            textodownload.set(f"Erro: {str(e)}")
    else:
        textodownload.set("Caminho não encontrado")

# Função do tema escuro
def Tema_Escuro():
    if Tela_inicial.cget("bg") == "#1E1E1E":  # Verifica se já está em tema escuro
        Tela_inicial.configure(bg="#ffffff")
        Botao_tema_escuro.configure(image=icone_claro, bd=0, bg="#ffffff")
        Texto.configure(bg="#ffffff", fg="#000000")
        link.configure(bg="#e7ebee", fg="#000000")
        Baixar_mp4.configure(bg="#e52a3f", fg="#FFFFFF")
        Baixar_mp3.configure(bg="#e52a3f", fg="#FFFFFF")
        onde_fica_o_texto.configure(bg="#ffffff", fg="#000000")
        
    else:
        Tela_inicial.configure(bg="#1E1E1E")
        Botao_tema_escuro.configure(image=icone_escuro, bd=0, bg="#1E1E1E")
        Texto.configure(bg="#1E1E1E", fg="#ffffff")
        link.configure(bg="#2c2c2c", fg="#ffffff")
        Baixar_mp4.configure(bg="#e52a3f", fg="#FFFFFF")
        Baixar_mp3.configure(bg="#e52a3f", fg="#FFFFFF")
        onde_fica_o_texto.configure(bg="#1E1E1E", fg="#ffffff")

# Funções para mudar a cor dos botões (hover) ao passar o mouse
def on_enter_mp4(e):
    Baixar_mp4.config(bg="#8a1421")  # Cor quando o mouse está sobre o botão MP4

def on_leave_mp4(e):
    Baixar_mp4.config(bg="#e52a3f")  # Cor original do botão MP4

def on_enter_mp3(e):
    Baixar_mp3.config(bg="#8a1421")  # Cor quando o mouse está sobre o botão MP3

def on_leave_mp3(e):
    Baixar_mp3.config(bg="#e52a3f")  # Cor original do botão MP3

# Onde começa o layout da tela
Tela_inicial = Tk()
Tela_inicial.title("Conversor de vídeos do YouTube")        # Título da Janela
Tela_inicial.configure(bg="#ffffff")                        # deixa o fundo branco
Tela_inicial.resizable(False, False)
base_dir_icone = os.path.dirname(os.path.abspath(__file__))                       # Não deixa o usuario mexer na proporção da tela
icone_path = os.path.join(base_dir_icone, "imagens", "icone.ico")
Tela_inicial.iconbitmap(icone_path) 
# Carregar ícones
base_dir_moon = os.path.dirname(os.path.abspath(__file__))
icone_claro_path = os.path.join(base_dir_moon, "imagens", "Moon.png")
icone_claro = PhotoImage(file=icone_claro_path)
# Sol
base_dir_sun = os.path.dirname(os.path.abspath(__file__))
icone_escuro_path = os.path.join(base_dir_sun, "imagens", "Sun.png")
icone_escuro = PhotoImage(file=icone_escuro_path)

# Widgets
Texto = Label(Tela_inicial, text="Insira o URL do vídeo", font="Arial 10", bg="#ffffff")
link = Entry(Tela_inicial, bg="#e7ebee")                                                                     # Caixa de texto que pega o link
Baixar_mp4 = Button(Tela_inicial, text="Baixar como mp4", command=Baixar_Video, bg="#e52a3f", fg="#FFFFFF")  # Botão que executa a função de baixar video
Baixar_mp3 = Button(Tela_inicial, text="Baixar como mp3", command=Baixar_Audio, bg="#e52a3f", fg="#FFFFFF")  # Botão que executa a função de baixar audio
Botao_tema_escuro = Button(Tela_inicial, text="Tema escuro", command=Tema_Escuro, image=icone_claro, bd=0, bg="#ffffff")
textodownload = StringVar() 
textodownload.set("") 

onde_fica_o_texto = Label(Tela_inicial, font="Arial 10", textvariable=textodownload, width=20, bg="#ffffff")

# Posição dos elementos na tela
Texto.grid(row=0, column=2, pady=2)  
link.grid(row=1, column=2, pady=2)  
Baixar_mp4.grid(row=2, column=2, pady=2)  
Baixar_mp3.grid(row=3, column=2, pady=2)  
onde_fica_o_texto.grid(row=4, column=2)
Botao_tema_escuro.grid(row=0, column=5, sticky="e", padx=(100, 0))

# Adiciona eventos para hover
Baixar_mp4.bind("<Enter>", on_enter_mp4)
Baixar_mp4.bind("<Leave>", on_leave_mp4)
Baixar_mp3.bind("<Enter>", on_enter_mp3)
Baixar_mp3.bind("<Leave>", on_leave_mp3)

# Comando que deixa a tela ativa
Tela_inicial.mainloop()