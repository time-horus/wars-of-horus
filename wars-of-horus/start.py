import pygame
import sys
import subprocess

def fechar():
    pygame.quit()
    sys.exit()

def tocar_som(som_arquivo, volume=0.2):
    som = pygame.mixer.Sound(som_arquivo)
    som.set_volume(volume)
    som.play()

def iniciar_jogo():
    tocar_som('Sounds/sand-spell.flac', volume=0.2)
    subprocess.Popen(["python", "code_1.py"])
    fechar()

def sobre():
    tela_sobre = pygame.display.set_mode((640, 640))
    fundo_sobre = pygame.image.load("imagens/background.png")
    botao_voltar_normal = pygame.transform.scale(pygame.image.load("imagens/botoes/EXIT.png"), (190, 52))
    botao_voltar_hover = pygame.transform.scale(pygame.image.load("imagens/botoes/EXIT2.png"), (190, 52))
    botao_voltar_rect = botao_voltar_normal.get_rect()
    botao_voltar_rect.center = (320, 530)  # ajuste da posição inicial
    botao_voltar_hovered = False  # variável para rastrear o hover

    sobre_executando = True

    # texto do sobre
    resumo_fonte = pygame.font.Font("fontes/OpenSansPXBold.ttf", 36)
    resumo_texto = "Welcome! Here you will face challenges and full of surprises PLAGES. This free software game began due to the 2023 IEEE Robotics and Automation Society (RAS) selection process of Bauru-SP, And it was developed by Team Horus. Have fun and good luck, you'll need it! Repository: https://github.com/time-horus/ wars-of-horus"

    # quebrar o texto em várias linhas
    linhas = []
    linha_atual = ""
    palavras = resumo_texto.split()
    for palavra in palavras:
        if resumo_fonte.size(linha_atual + palavra)[0] <= 580:  # ajustar para que o texto caiba na tela (considerando margens)
            linha_atual += palavra + " "
        else:
            linhas.append(linha_atual)
            linha_atual = palavra + " "
    linhas.append(linha_atual)

    while sobre_executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sobre_executando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar_rect.collidepoint(evento.pos):
                    tocar_som('Sounds/sand-spell.flac', volume=0.2)
                    sobre_executando = False
            if evento.type == pygame.MOUSEMOTION:
                if botao_voltar_rect.collidepoint(evento.pos):
                    botao_voltar_hovered = True
                else:
                    botao_voltar_hovered = False

        tela_sobre.fill((0, 0, 0))
        tela_sobre.blit(fundo_sobre, (0, 0))
        if botao_voltar_hovered:
            tela_sobre.blit(botao_voltar_hover, botao_voltar_rect)
        else:
            tela_sobre.blit(botao_voltar_normal, botao_voltar_rect)

        # renderizar o texto quebrado
        y_pos = 50  # posição vertical inicial
        for linha in linhas:
            resumo_renderizado = resumo_fonte.render(linha, True, (255, 255, 255))
            tela_sobre.blit(resumo_renderizado, (30, y_pos))  # Ajuste da posição do texto
            y_pos += resumo_fonte.get_height()

        pygame.display.flip()

def main():
    pygame.init()

    pygame.mixer.music.load('Sounds/cugzilia.ogg')
    volume_musica = 0.5
    pygame.mixer.music.set_volume(volume_musica)
    pygame.mixer.music.play(-1)

    tela = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("Menu Inicial")

    tela.fill((0, 0, 0))

    fundo = pygame.image.load("imagens/background.png")
    botao_jogar_normal = pygame.transform.scale(pygame.image.load("imagens/botoes/Start.png"), (190, 50))
    botao_sobre_normal = pygame.transform.scale(pygame.image.load("imagens/botoes/About.png"), (190, 50))
    botao_musica_normal = pygame.transform.scale(pygame.image.load("imagens/botoes/Music.png"), (190, 50))
    botao_sair_normal = pygame.transform.scale(pygame.image.load("imagens/botoes/EXIT.png"), (190, 52))
    logo = pygame.transform.scale(pygame.image.load("imagens/logo.png"), (775, 325))

    botao_jogar_hover = pygame.transform.scale(pygame.image.load("imagens/botoes/Start2.png"), (190, 50))
    botao_sobre_hover = pygame.transform.scale(pygame.image.load("imagens/botoes/About2.png"), (190, 50))
    botao_sair_hover = pygame.transform.scale(pygame.image.load("imagens/botoes/EXIT2.png"), (190, 52))

    botao_musica_hover = pygame.transform.scale(pygame.image.load("imagens/botoes/Music2.png"), (190, 50))

    botao_musica_mudo = pygame.transform.scale(pygame.image.load("imagens/botoes/Music2.png"), (190, 50))

    botao_jogar = botao_jogar_normal
    botao_sobre = botao_sobre_normal
    botao_musica = botao_musica_normal
    botao_sair = botao_sair_normal

    fundo_rect = fundo.get_rect()
    botao_jogar_rect = botao_jogar.get_rect()
    botao_sobre_rect = botao_sobre.get_rect()
    botao_musica_rect = botao_musica.get_rect()
    botao_sair_rect = botao_sair.get_rect()
    logo_rect = logo.get_rect()

    fundo_rect.center = tela.get_rect().center
    botao_jogar_rect.center = (320, 320)
    botao_sobre_rect.center = (320, 390)
    botao_musica_rect.center = (320, 460)
    botao_sair_rect.center = (320, 530)
    logo_rect.center = (320, 165)

    tela_atual = "menu"
    musica_mudo = False  # Variável para rastrear se a música está em mudo ou não

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fechar()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if tela_atual == "menu":
                    if botao_jogar_rect.collidepoint(evento.pos):
                        tocar_som('Sounds/sand-spell.flac', volume=0.2)
                        iniciar_jogo()
                    elif botao_sobre_rect.collidepoint(evento.pos):
                        tocar_som('Sounds/sand-spell.flac', volume=0.2)
                        sobre()
                    elif botao_musica_rect.collidepoint(evento.pos):
                        tocar_som('Sounds/sand-spell.flac', volume=0.2)
                        if volume_musica == 0.5:
                            volume_musica = 0
                            pygame.mixer.music.set_volume(volume_musica)
                            botao_musica = botao_musica_mudo  # Usar a imagem de música em mudo
                            musica_mudo = True  # Marcar que a música está em mudo
                        else:
                            volume_musica = 0.5
                            pygame.mixer.music.set_volume(volume_musica)
                            botao_musica = botao_musica_normal
                            musica_mudo = False  # Marcar que a música não está em mudo
                    elif botao_sair_rect.collidepoint(evento.pos):
                        tocar_som('Sounds/sand-spell.flac', volume=0.2)
                        fechar()

            if evento.type == pygame.MOUSEMOTION:
                if tela_atual == "menu":
                    if botao_jogar_rect.collidepoint(evento.pos):
                        botao_jogar = botao_jogar_hover
                    else:
                        botao_jogar = botao_jogar_normal
                    if botao_sobre_rect.collidepoint(evento.pos):
                        botao_sobre = botao_sobre_hover
                    else:
                        botao_sobre = botao_sobre_normal
                    if botao_musica_rect.collidepoint(evento.pos):
                        botao_musica = botao_musica_hover
                    else:
                        botao_musica = botao_musica_normal
                    if botao_sair_rect.collidepoint(evento.pos):
                        botao_sair = botao_sair_hover
                    else:
                        botao_sair = botao_sair_normal

        tela.fill((0, 0, 0))
        tela.blit(fundo, (0, 0))
        tela.blit(logo, logo_rect)

        # Se a música estiver em mudo, usar a imagem correspondente
        if musica_mudo:
            tela.blit(botao_musica_mudo, botao_musica_rect)
        else:
            tela.blit(botao_musica, botao_musica_rect)

        tela.blit(botao_jogar, botao_jogar_rect)
        tela.blit(botao_sobre, botao_sobre_rect)
        tela.blit(botao_sair, botao_sair_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main()