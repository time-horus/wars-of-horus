import pygame #importa a biblioteca pygame

from pygame.locals import *
from sys import exit

pygame.init()

#largura e altura da tela
largura = 640
altura = 640
tela = pygame.display.set_mode((largura, altura)) #Cria tela

#peças brancas posição inicial
wx1 = 0; wx11 = 0 #X
wx2 = 1; wx12 = 1
wx3 = 2; wx13 = 2
wx4 = 3; wx14 = 3
wx5 = 4; wx15 = 4
wx6 = 5; wx16 = 5
wx7 = 6; wx17 = 6
wx8 = 7; wx18 = 7

wy1 = 6; wy11 = 7 #Y
wy2 = 6; wy12 = 7
wy3 = 6; wy13 = 7
wy4 = 6; wy14 = 7
wy5 = 6; wy15 = 7
wy6 = 6; wy16 = 7
wy7 = 6; wy17 = 7
wy8 = 6; wy18 = 7

#peças pretas posição inicial
bx1 = 0; bx11 = 0 #X
bx2 = 1; bx12 = 1
bx3 = 2; bx13 = 2
bx4 = 3; bx14 = 3
bx5 = 4; bx15 = 4
bx6 = 5; bx16 = 5
bx7 = 6; bx17 = 6
bx8 = 7; bx18 = 7

by1 = 0; by11 = 1 #Y
by2 = 0; by12 = 1
by3 = 0; by13 = 1
by4 = 0; by14 = 1
by5 = 0; by15 = 1
by6 = 0; by16 = 1
by7 = 0; by17 = 1
by8 = 0; by18 = 1

#coordenadas mouse X e Y
mx = 0
my = 0

#Estado da peça
State = 0

##################################Main Game function#########################################
while True:

    for event in pygame.event.get():
            if event.type == QUIT: #sair do jogo
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:#pegar a posição do mouse quando click
                 if event.button == 1:
                      mx, my = pygame.mouse.get_pos()

#################################construção do mapa##################################################
    tela.fill((0,85,0)) #cria um plano de fundo base verde
    for K in range(8):
        for j in range(8):
            pygame.draw.rect(tela, (238,238,213),((j)*(largura/8)*2,(K)*(altura/8)*2,(largura/8),(altura/8))) #Set dos quadrados brancos 
            pygame.draw.rect(tela, (238,238,213),((j+0.5)*(largura/8)*2,(K+0.5)*(altura/8)*2,(largura/8),(altura/8)))#pygame.draw.rect(tela, (cor RGB),(posição x, posição y, largura,altura))
##################################Set das Peças pretas separadamente###############################################################

    pygame.draw.circle(tela, (0,0,0),((bx1+0.5)*(largura/8),(by1+0.5)*(altura/8)),30) #pygame.draw.circle(tela, (cor RGB),(posição x, posição y), raio)
    pygame.draw.circle(tela, (0,0,0),((bx2+0.5)*(largura/8),(by2+0.5)*(altura/8)),30)
    pygame.draw.circle(tela, (0,0,0),((bx3+0.5)*(largura/8),(by3+0.5)*(altura/8)),30)
    pygame.draw.circle(tela, (0,0,0),((bx4+0.5)*(largura/8),(by4+0.5)*(altura/8)),30)
    pygame.draw.circle(tela, (0,0,0),((bx5+0.5)*(largura/8),(by5+0.5)*(altura/8)),30)
    pygame.draw.circle(tela, (0,0,0),((bx6+0.5)*(largura/8),(by6+0.5)*(altura/8)),30)
    pygame.draw.circle(tela, (0,0,0),((bx7+0.5)*(largura/8),(by7+0.5)*(altura/8)),30)
    pygame.draw.circle(tela, (0,0,0),((bx8+0.5)*(largura/8),(by8+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (0,0,0),((bx11+0.5)*(largura/8),(by11+0.5)*(altura/8)),30)
    pygame.draw.circle(tela, (0,0,0),((bx12+0.5)*(largura/8),(by12+0.5)*(altura/8)),30)
    pygame.draw.circle(tela, (0,0,0),((bx13+0.5)*(largura/8),(by13+0.5)*(altura/8)),30)
    pygame.draw.circle(tela, (0,0,0),((bx14+0.5)*(largura/8),(by14+0.5)*(altura/8)),30)
    pygame.draw.circle(tela, (0,0,0),((bx15+0.5)*(largura/8),(by15+0.5)*(altura/8)),30)
    pygame.draw.circle(tela, (0,0,0),((bx16+0.5)*(largura/8),(by16+0.5)*(altura/8)),30)
    pygame.draw.circle(tela, (0,0,0),((bx17+0.5)*(largura/8),(by17+0.5)*(altura/8)),30)
    pygame.draw.circle(tela, (0,0,0),((bx18+0.5)*(largura/8),(by18+0.5)*(altura/8)),30)

##################################Set das Peças Brancas separadamente###############################################################
    
    pygame.draw.circle(tela, (125,148,93),((wx1+0.5)*(largura/8),(wy1+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx1+0.5)*(largura/8),(wy1+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx2+0.5)*(largura/8),(wy2+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx2+0.5)*(largura/8),(wy2+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx3+0.5)*(largura/8),(wy3+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx3+0.5)*(largura/8),(wy3+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx4+0.5)*(largura/8),(wy4+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx4+0.5)*(largura/8),(wy4+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx5+0.5)*(largura/8),(wy5+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx5+0.5)*(largura/8),(wy5+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx6+0.5)*(largura/8),(wy6+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx6+0.5)*(largura/8),(wy6+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx7+0.5)*(largura/8),(wy7+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx7+0.5)*(largura/8),(wy7+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx8+0.5)*(largura/8),(wy8+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx8+0.5)*(largura/8),(wy8+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx11+0.5)*(largura/8),(wy11+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx11+0.5)*(largura/8),(wy11+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx12+0.5)*(largura/8),(wy12+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx12+0.5)*(largura/8),(wy12+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx13+0.5)*(largura/8),(wy13+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx13+0.5)*(largura/8),(wy13+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx14+0.5)*(largura/8),(wy14+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx14+0.5)*(largura/8),(wy14+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx15+0.5)*(largura/8),(wy15+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx15+0.5)*(largura/8),(wy15+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx16+0.5)*(largura/8),(wy16+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx16+0.5)*(largura/8),(wy16+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx17+0.5)*(largura/8),(wy17+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx17+0.5)*(largura/8),(wy17+0.5)*(altura/8)),30)

    pygame.draw.circle(tela, (125,148,93),((wx18+0.5)*(largura/8),(wy18+0.5)*(altura/8)),32)
    pygame.draw.circle(tela, (220,218,214),((wx18+0.5)*(largura/8),(wy18+0.5)*(altura/8)),30)

#####################################Seleção das peças ############################################
    if round((mx/(largura/8))-0.5) == wx1 and round((my/(largura/8))-0.5) == wy1: #faz a comparação da posição no click do mouse com a posição da peça, se for igual:
        pygame.draw.circle(tela, (125,148,93),((wx1+0.5)*(largura/8),(wy1+0.5)*(altura/8)),32) #troca a cor da peça para mostrar seleção
        pygame.draw.circle(tela, (199, 198, 149),((wx1+0.5)*(largura/8),(wy1+0.5)*(altura/8)),30)
        State = 1                                                                                #muda o estado da peça para 1(selecionado)
    if event.type == MOUSEBUTTONDOWN and State == 1:                                             #se click do mouse e State == 1
        State = 0                                                                                #muda State para 0
        if event.button == 1:   #mudar a posição da peça
            mx, my = pygame.mouse.get_pos()                                                      #pega a posição do mouse no momento do click
            wx1 = round((mx/(largura/8))-0.5)                                                    #tratamento da posição do mouse e atribuição na posição da peça
            wy1 = round((my/(largura/8))-0.5)
            #pygame.draw.circle(tela, (125,148,93),((wx1+0.5)*(largura/8),(wy1+0.5)*(altura/8)),32)
            #pygame.draw.circle(tela, (220,218,214),((wx1+0.5)*(largura/8),(wy1+0.5)*(altura/8)),30)

    #selection color(199, 198, 149)
    pygame.display.update() # faz o loop/atualização do game
    #test
