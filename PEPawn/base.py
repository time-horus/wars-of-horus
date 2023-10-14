
import pygame #importa a biblioteca pygame

from pygame.locals import *
from sys import exit
#from Locomocao import locomocao

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
Stateb1 = 0; Stateb11 = 0; Statew1 = 0; Statew11 = 0
Stateb2 = 0; Stateb12 = 0; Statew2 = 0; Statew12 = 0
Stateb3 = 0; Stateb13 = 0; Statew3 = 0; Statew13 = 0
Stateb4 = 0; Stateb14 = 0; Statew4 = 0; Statew14 = 0
Stateb5 = 0; Stateb15 = 0; Statew5 = 0; Statew15 = 0
Stateb6 = 0; Stateb16 = 0; Statew6 = 0; Statew16 = 0
Stateb7 = 0; Stateb17 = 0; Statew7 = 0; Statew17 = 0
Stateb8 = 0; Stateb18 = 0; Statew8 = 0; Statew18 = 0

def locomocao(px,py,state,mx,my,largura,altura,event,tela):
    
    if round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py and event.type == MOUSEBUTTONDOWN: #faz a comparação da posição no click do mouse com a posição da peça, se for igual:
        pygame.draw.circle(tela, (125,148,93),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),32) #troca a cor da peça para mostrar seleção
        pygame.draw.circle(tela, (199, 198, 149),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),30)
        state = 1
        print("1")                                                                              #muda o estado da peça para 1(selecionado)
    if state == 1:
        print("2")
        pygame.draw.circle(tela, (125,148,93),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),32) #troca a cor da peça para mostrar seleção
        pygame.draw.circle(tela, (199, 198, 149),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),30)
    if event.type == MOUSEBUTTONUP and state == 1: 
        print("3") 
        pygame.draw.circle(tela, (125,148,93),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),32) #troca a cor da peça para mostrar seleção
        pygame.draw.circle(tela, (199, 198, 149),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),30)                                           #se click do mouse e State == 1
        state = 0                                                                                #muda State para 0
        mx, my = pygame.mouse.get_pos()                                                      #pega a posição do mouse no momento do click
        px = round((mx/(largura/8))-0.5)                                                    #tratamento da posição do mouse e atribuição na posição da peça
        py = round((my/(altura/8))-0.5)
    return (px,py,state)
##################################Main Game function#########################################
while True:

    for event in pygame.event.get():
            if event.type == QUIT: #sair do jogo
                pygame.quit()
                exit()
    
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
    #Backup se tudo explodir
    # #W1
    # if round((mx/(largura/8))-0.5) == wx1 and round((my/(largura/8))-0.5) == wy1 and event.type == MOUSEBUTTONDOWN: #faz a comparação da posição no click do mouse com a posição da peça, se for igual:
    #     pygame.draw.circle(tela, (125,148,93),((wx1+0.5)*(largura/8),(wy1+0.5)*(altura/8)),32) #troca a cor da peça para mostrar seleção
    #     pygame.draw.circle(tela, (199, 198, 149),((wx1+0.5)*(largura/8),(wy1+0.5)*(altura/8)),30)
    #     Statew1 = 1                                                                                #muda o estado da peça para 1(selecionado)
    # if Statew1 == 1:
    #     pygame.draw.circle(tela, (125,148,93),((wx1+0.5)*(largura/8),(wy1+0.5)*(altura/8)),32) #troca a cor da peça para mostrar seleção
    #     pygame.draw.circle(tela, (199, 198, 149),((wx1+0.5)*(largura/8),(wy1+0.5)*(altura/8)),30)
    # if event.type == MOUSEBUTTONUP and Statew1 == 1:  
    #     pygame.draw.circle(tela, (125,148,93),((wx1+0.5)*(largura/8),(wy1+0.5)*(altura/8)),32) #troca a cor da peça para mostrar seleção
    #     pygame.draw.circle(tela, (199, 198, 149),((wx1+0.5)*(largura/8),(wy1+0.5)*(altura/8)),30)                                           #se click do mouse e State == 1
    #     Statew1 = 0                                                                                #muda State para 0
    #     mx, my = pygame.mouse.get_pos()                                                      #pega a posição do mouse no momento do click
    #     wx1 = round((mx/(largura/8))-0.5)                                                    #tratamento da posição do mouse e atribuição na posição da peça
    #     wy1 = round((my/(altura/8))-0.5)
    
    wx1, wy1, Statew1 = locomocao(wx1,wy1,Statew1,mx,my,largura,altura,event,tela)
    wx2, wy2, Statew2 = locomocao(wx2,wy2,Statew2,mx,my,largura,altura,event,tela)
    wx3, wy3, Statew3 = locomocao(wx3,wy3,Statew3,mx,my,largura,altura,event,tela)
    wx4, wy4, Statew4 = locomocao(wx4,wy4,Statew4,mx,my,largura,altura,event,tela)
    wx5, wy5, Statew5 = locomocao(wx5,wy5,Statew5,mx,my,largura,altura,event,tela)
    wx6, wy6, Statew6 = locomocao(wx6,wy6,Statew6,mx,my,largura,altura,event,tela)
    wx7, wy7, Statew7 = locomocao(wx7,wy7,Statew7,mx,my,largura,altura,event,tela)
    wx8, wy8, Statew8 = locomocao(wx8,wy8,Statew8,mx,my,largura,altura,event,tela)
    wx11, wy11, Statew11 = locomocao(wx11, wy11, Statew11, mx, my, largura, altura, event, tela)
    wx12, wy12, Statew12 = locomocao(wx12, wy12, Statew12, mx, my, largura, altura, event, tela)
    wx13, wy13, Statew13 = locomocao(wx13, wy13, Statew13, mx, my, largura, altura, event, tela)
    wx14, wy14, Statew14 = locomocao(wx14, wy14, Statew14, mx, my, largura, altura, event, tela)
    wx15, wy15, Statew15 = locomocao(wx15, wy15, Statew15, mx, my, largura, altura, event, tela)
    wx16, wy16, Statew16 = locomocao(wx16, wy16, Statew16, mx, my, largura, altura, event, tela)
    wx17, wy17, Statew17 = locomocao(wx17, wy17, Statew17, mx, my, largura, altura, event, tela)
    wx18, wy18, Statew18 = locomocao(wx18, wy18, Statew18, mx, my, largura, altura, event, tela)

    bx1, by1, Stateb1 = locomocao(bx1, by1, Stateb1, mx, my, largura, altura, event, tela)
    bx2, by2, Stateb2 = locomocao(bx2, by2, Stateb2, mx, my, largura, altura, event, tela)
    bx3, by3, Stateb3 = locomocao(bx3, by3, Stateb3, mx, my, largura, altura, event, tela)
    bx4, by4, Stateb4 = locomocao(bx4, by4, Stateb4, mx, my, largura, altura, event, tela)
    bx5, by5, Stateb5 = locomocao(bx5, by5, Stateb5, mx, my, largura, altura, event, tela)
    bx6, by6, Stateb6 = locomocao(bx6, by6, Stateb6, mx, my, largura, altura, event, tela)
    bx7, by7, Stateb7 = locomocao(bx7, by7, Stateb7, mx, my, largura, altura, event, tela)
    bx8, by8, Stateb8 = locomocao(bx8, by8, Stateb8, mx, my, largura, altura, event, tela)
    bx11, by11, Stateb11 = locomocao(bx11, by11, Stateb11, mx, my, largura, altura, event, tela)
    bx12, by12, Stateb12 = locomocao(bx12, by12, Stateb12, mx, my, largura, altura, event, tela)
    bx13, by13, Stateb13 = locomocao(bx13, by13, Stateb13, mx, my, largura, altura, event, tela)
    bx14, by14, Stateb14 = locomocao(bx14, by14, Stateb14, mx, my, largura, altura, event, tela)
    bx15, by15, Stateb15 = locomocao(bx15, by15, Stateb15, mx, my, largura, altura, event, tela)
    bx16, by16, Stateb16 = locomocao(bx16, by16, Stateb16, mx, my, largura, altura, event, tela)
    bx17, by17, Stateb17 = locomocao(bx17, by17, Stateb17, mx, my, largura, altura, event, tela)
    bx18, by18, Stateb18 = locomocao(bx18, by18, Stateb18, mx, my, largura, altura, event, tela)
    #print(wx2,wy2)

    #selection color(199, 198, 149)
    pygame.display.update() # faz o loop/atualização do game
