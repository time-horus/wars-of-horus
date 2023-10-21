import pygame
from start import tocar_som

def game_over(turns,fonte=None, cont=0):
    tela_game_over = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("Game Over")
    pygame.display.set_icon(pygame.image.load('imagens/tile.png'))
    fundo_game_over = pygame.image.load("imagens/background.png")
    botao_voltar_normal = pygame.transform.scale(pygame.image.load("imagens/botoes/EXIT.png"), (190, 52))
    botao_voltar_hover = pygame.transform.scale(pygame.image.load("imagens/botoes/EXIT2.png"), (190, 52))
    botao_voltar_rect = botao_voltar_normal.get_rect()
    botao_voltar_rect.center = (320, 530)
    botao_voltar_hovered = False

    game_over_executando = True

    # Texto para a tela de Game Over
    if turns%2 == 0:
        texto_game_over = "Isis is the true pharaoh. Destiny is on your side."
    else:
        texto_game_over = "Horus is the true pharaoh. Destiny is on your side."

    # Função para dividir o texto em várias linhas
    def dividir_texto(texto, largura_max):
        linhas = []
        linha_atual = ""
        palavras = texto.split()
        for palavra in palavras:
            if (fonte or pygame.font.Font("fontes/OpenSansPXBold.ttf", 36)).size(linha_atual + palavra)[0] <= largura_max:
                linha_atual += palavra + " "
            else:
                linhas.append(linha_atual)
                linha_atual = palavra + " "
        linhas.append(linha_atual)
        return linhas

    linhas_game_over = dividir_texto(texto_game_over, 580)

    while game_over_executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over_executando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar_rect.collidepoint(evento.pos):
                    tocar_som('Sounds/sand-spell.flac', volume=0.2)
                    game_over_executando = False
            if evento.type == pygame.MOUSEMOTION:
                if botao_voltar_rect.collidepoint(evento.pos):
                    botao_voltar_hovered = True
                else:
                    botao_voltar_hovered = False

        tela_game_over.fill((0, 0, 0))
        tela_game_over.blit(fundo_game_over, (0, 0))

        # Mostrar "GAME OVER" no topo da tela
        texto_game_over_grande = pygame.font.Font("fontes/ARCADECLASSIC.TTF", 72).render("GAME OVER", True, (255, 255, 255))
        tela_game_over.blit(texto_game_over_grande, (160, 100))

        y_pos = 220
        for linha in linhas_game_over:
            texto_renderizado = fonte.render(linha, True, (255, 255, 255))
            tela_game_over.blit(texto_renderizado, (30, y_pos))
            y_pos += fonte.get_height()

        # Mostrar o número de turnos
        if cont == 1:
            texto_turnos = f"This game lasted {turns} turn."
        else:
            texto_turnos = f"This game lasted {turns} turns."
        texto_renderizado_turnos = fonte.render(texto_turnos, True, (255, 255, 255))
        tela_game_over.blit(texto_renderizado_turnos, (30, y_pos))

        if botao_voltar_hovered:
            tela_game_over.blit(botao_voltar_hover, botao_voltar_rect)
        else:
            tela_game_over.blit(botao_voltar_normal, botao_voltar_rect)

        pygame.display.flip()