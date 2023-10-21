import pygame #importa a biblioteca pygame
import random as rnd #importa a biblioteca random
import numpy as np
import gameover

from pygame.locals import *
from sys import exit
from LocomocaoW import locomocaoW
from LocomocaoB import locomocaoB
from gameover import game_over

pygame.init()
#largura e altura da tela
largura = 640
altura = 640
tela = pygame.display.set_mode((largura, altura)) #Cria tela

pygame.display.set_caption("War of Horus")
pygame.display.set_icon(pygame.image.load('imagens/tile.png'))

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

#seta o turno da peça
turno = 0

#Define quando vai ocorrer o sorteio
aleat = 0
#contador de turnos para a 
cont = 1
#variaveis que vão receber o valor srteado para definir a movimentação
numero = None
poder = None

#Vetores para a seleção das peças

Cordenadas_W = np.array([])
Cordenadas_B = np.array([])

pygame.mixer.music.load('Sounds/questforthegoldencatidol.ogg')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

##################################Main Game function#########################################
while True:
    

    for event in pygame.event.get():
            if event.type == QUIT: #sair do jogo
                pygame.quit()
                exit()
            if (bx4 == 84 or by4 == 84) or (wx14 == 84 or wy14 == 84):
                game_over(turno, pygame.font.Font("fontes/OpenSansPXBold.ttf", 36), cont)
                pygame.quit()
                exit()

            
    mx, my = pygame.mouse.get_pos()

################################# construção do mapa ##################################################
    #tela.fill((0,85,0)) #cria um plano de fundo base verde
    #for K in range(8):
    #    for j in range(8):
    #        pygame.draw.rect(tela, (238,238,213),((j)*(largura/8)*2,(K)*(altura/8)*2,(largura/8),(altura/8))) #Set dos quadrados brancos 
    #        pygame.draw.rect(tela, (238,238,213),((j+0.5)*(largura/8)*2,(K+0.5)*(altura/8)*2,(largura/8),(altura/8)))#pygame.draw.rect(tela, (cor RGB),(posição x, posição y, largura,altura))
    CasaBranco = pygame.image.load('imagens/template.png')
    CasaPreto = pygame.image.load('imagens/template2.png')
    for K in range(8):    
        for j in range(8):
                tela.blit(pygame.transform.scale(CasaPreto,(largura/8,altura/8)),((j)*(largura/8),(K)*(altura/8),(largura/8),(altura/8)))
                

    for K in range(8):    
        for j in range(8):
                tela.blit(pygame.transform.scale(CasaBranco,(largura/8,altura/8)),((j)*(largura/8)*2,(K)*(altura/8)*2,(largura/8),(altura/8)))
                tela.blit(pygame.transform.scale(CasaBranco,(largura/8,altura/8)),((j+0.5)*(largura/8)*2,(K+0.5)*(altura/8)*2,(largura/8),(altura/8)))



##################################Carrega img Pedras Pretas e Brancas###############################################################


    peaoPreto = pygame.image.load('imagens/pedras/Bmumia.png')
    reiPreto = pygame.image.load('imagens/pedras/Bisis.png')
    rainhaPreto = pygame.image.load('imagens/pedras/Bmumia.png')
    torrePreto = pygame.image.load('imagens/pedras/Bmumia.png')
    bispoPreto = pygame.image.load('imagens/pedras/Bmumia.png')
    cavaloPreto = pygame.image.load('imagens/pedras/Bmumia.png')
    
    peaoBranco = pygame.image.load('imagens/pedras/Wmumia.png')
    reiBranco = pygame.image.load('imagens/pedras/Whorus.png')
    rainhaBranco = pygame.image.load('imagens/pedras/Wmumia.png')
    torreBranco = pygame.image.load('imagens/pedras/Wmumia.png')
    bispoBranco = pygame.image.load('imagens/pedras/Wmumia.png')
    cavaloBranco = pygame.image.load('imagens/pedras/Wmumia.png')
    
    larguraImg = 60
    alturaImg = 60


##################################Set das Peças pretas separadamente###############################################################

    tela.blit(pygame.transform.scale(torrePreto, (larguraImg, alturaImg)), ((bx1+0.5)*(largura/8) - larguraImg/2, (by1+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(cavaloPreto, (larguraImg, alturaImg)), ((bx2+0.5)*(largura/8) - larguraImg/2, (by2+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(bispoPreto, (larguraImg, alturaImg)), ((bx3+0.5)*(largura/8) - larguraImg/2, (by3+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(reiPreto, (larguraImg, alturaImg)), ((bx4+0.5)*(largura/8) - larguraImg/2, (by4+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(rainhaPreto, (larguraImg, alturaImg)), ((bx5+0.5)*(largura/8) - larguraImg/2, (by5+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(bispoPreto, (larguraImg, alturaImg)), ((bx6+0.5)*(largura/8) - larguraImg/2, (by6+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(cavaloPreto, (larguraImg, alturaImg)), ((bx7+0.5)*(largura/8) - larguraImg/2, (by7+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(torrePreto, (larguraImg, alturaImg)), ((bx8+0.5)*(largura/8) - larguraImg/2, (by8+0.5)*(altura/8) - alturaImg/2))

    tela.blit(pygame.transform.scale(peaoPreto, (larguraImg, alturaImg)), ((bx11+0.5)*(largura/8) - larguraImg/2, (by11+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(peaoPreto, (larguraImg, alturaImg)), ((bx12+0.5)*(largura/8) - larguraImg/2, (by12+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(peaoPreto, (larguraImg, alturaImg)), ((bx13+0.5)*(largura/8) - larguraImg/2, (by13+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(peaoPreto, (larguraImg, alturaImg)), ((bx14+0.5)*(largura/8) - larguraImg/2, (by14+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(peaoPreto, (larguraImg, alturaImg)), ((bx15+0.5)*(largura/8) - larguraImg/2, (by15+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(peaoPreto, (larguraImg, alturaImg)), ((bx16+0.5)*(largura/8) - larguraImg/2, (by16+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(peaoPreto, (larguraImg, alturaImg)), ((bx17+0.5)*(largura/8) - larguraImg/2, (by17+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(peaoPreto, (larguraImg, alturaImg)), ((bx18+0.5)*(largura/8) - larguraImg/2, (by18+0.5)*(altura/8) - alturaImg/2))

    Cordenadas_B = np.array([[bx1,by1],[bx2,by2],[bx3,by3],[bx4,by4],[bx5,by5],[bx6,by6],[bx7,by7],[bx8,by8],[bx11,by11],[bx12,by12],[bx13,by13],[bx14,by14],[bx15,by15],[bx16,by16],[bx17,by17],[bx18,by18]])

##################################Set das Peças Brancas separadamente###############################################################
    
     # Desenhar as peças brancas do tabuleiro
    tela.blit(pygame.transform.scale(torreBranco, (larguraImg, alturaImg)), ((wx1+0.5)*(largura/8) - larguraImg/2, (wy1+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(cavaloBranco, (larguraImg, alturaImg)), ((wx2+0.5)*(largura/8) - larguraImg/2, (wy2+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(bispoBranco, (larguraImg, alturaImg)), ((wx3+0.5)*(largura/8) - larguraImg/2, (wy3+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(peaoBranco, (larguraImg, alturaImg)), ((wx4+0.5)*(largura/8) - larguraImg/2, (wy4+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(rainhaBranco, (larguraImg, alturaImg)), ((wx5+0.5)*(largura/8) - larguraImg/2, (wy5+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(bispoBranco, (larguraImg, alturaImg)), ((wx6+0.5)*(largura/8) - larguraImg/2, (wy6+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(cavaloBranco, (larguraImg, alturaImg)), ((wx7+0.5)*(largura/8) - larguraImg/2, (wy7+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(torreBranco, (larguraImg, alturaImg)), ((wx8+0.5)*(largura/8) - larguraImg/2, (wy8+0.5)*(altura/8) - alturaImg/2))

    tela.blit(pygame.transform.scale(peaoBranco, (larguraImg, alturaImg)), ((wx11+0.5)*(largura/8) - larguraImg/2, (wy11+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(peaoBranco, (larguraImg, alturaImg)), ((wx12+0.5)*(largura/8) - larguraImg/2, (wy12+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(peaoBranco, (larguraImg, alturaImg)), ((wx13+0.5)*(largura/8) - larguraImg/2, (wy13+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(reiBranco, (larguraImg, alturaImg)), ((wx14+0.5)*(largura/8) - larguraImg/2, (wy14+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(peaoBranco, (larguraImg, alturaImg)), ((wx15+0.5)*(largura/8) - larguraImg/2, (wy15+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(peaoBranco, (larguraImg, alturaImg)), ((wx16+0.5)*(largura/8) - larguraImg/2, (wy16+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(peaoBranco, (larguraImg, alturaImg)), ((wx17+0.5)*(largura/8) - larguraImg/2, (wy17+0.5)*(altura/8) - alturaImg/2))
    tela.blit(pygame.transform.scale(peaoBranco, (larguraImg, alturaImg)), ((wx18+0.5)*(largura/8) - larguraImg/2, (wy18+0.5)*(altura/8) - alturaImg/2))


    Cordenadas_W = np.array([[wx1, wy1], [wx2, wy2], [wx3, wy3], [wx4, wy4], [wx5, wy5], [wx6, wy6], [wx7, wy7], [wx8, wy8], [wx11, wy11], [wx12, wy12], [wx13, wy13], [wx14, wy14], [wx15, wy15], [wx16, wy16], [wx17, wy17], [wx18, wy18]])

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

    if turno%2 == 0:                                        #Se o turno for par: as peças brancas jogam
        if aleat == 0:                                      #se a variavel aleat = 0
            if cont%3 == 0:                                    #ver se o o contador das rodadas é multiplo de 3
                poder = rnd.randint(0,4)                        #se sim, sorteia um poder
                aleat = 1
            else:                                               #caso contrario, sorteia um movimento normal
                numero = rnd.randint(0,5)
                aleat = 1
                print(numero)

    ################################Funções de locomoção das peças brancas#######################################################################################
        wx1, wy1, Statew1, turno,  Cordenadas_B = locomocaoW(wx1,wy1,Statew1,mx,my,largura,altura,event,tela, turno,numero,poder,cont,Cordenadas_B)
        wx2, wy2, Statew2, turno,  Cordenadas_B = locomocaoW(wx2,wy2,Statew2,mx,my,largura,altura,event,tela, turno,numero,poder,cont,Cordenadas_B)
        wx3, wy3, Statew3, turno,  Cordenadas_B = locomocaoW(wx3,wy3,Statew3,mx,my,largura,altura,event,tela, turno,numero,poder,cont,Cordenadas_B)
        wx4, wy4, Statew4, turno,  Cordenadas_B = locomocaoW(wx4,wy4,Statew4,mx,my,largura,altura,event,tela, turno,numero,poder,cont,Cordenadas_B)
        wx5, wy5, Statew5, turno,  Cordenadas_B = locomocaoW(wx5,wy5,Statew5,mx,my,largura,altura,event,tela, turno,numero,poder,cont,Cordenadas_B)
        wx6, wy6, Statew6, turno,  Cordenadas_B = locomocaoW(wx6,wy6,Statew6,mx,my,largura,altura,event,tela, turno,numero,poder,cont,Cordenadas_B)
        wx7, wy7, Statew7, turno,  Cordenadas_B = locomocaoW(wx7,wy7,Statew7,mx,my,largura,altura,event,tela, turno,numero,poder,cont,Cordenadas_B)
        wx8, wy8, Statew8, turno,  Cordenadas_B = locomocaoW(wx8,wy8,Statew8,mx,my,largura,altura,event,tela, turno,numero,poder,cont,Cordenadas_B)
        wx11, wy11, Statew11, turno, Cordenadas_B = locomocaoW(wx11, wy11, Statew11, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_B)
        wx12, wy12, Statew12, turno,  Cordenadas_B = locomocaoW(wx12, wy12, Statew12, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_B)
        wx13, wy13, Statew13, turno,  Cordenadas_B = locomocaoW(wx13, wy13, Statew13, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_B)
        wx14, wy14, Statew14, turno,  Cordenadas_B = locomocaoW(wx14, wy14, Statew14, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_B)
        wx15, wy15, Statew15, turno,  Cordenadas_B = locomocaoW(wx15, wy15, Statew15, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_B)
        wx16, wy16, Statew16, turno,  Cordenadas_B = locomocaoW(wx16, wy16, Statew16, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_B)
        wx17, wy17, Statew17, turno,  Cordenadas_B = locomocaoW(wx17, wy17, Statew17, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_B)
        wx18, wy18, Statew18, turno,  Cordenadas_B = locomocaoW(wx18, wy18, Statew18, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_B)
        
        bx1, bx2, bx3, bx4, bx5, bx6, bx7, bx8, bx11, bx12, bx13, bx14, bx15, bx16, bx17, bx18 = Cordenadas_B[:,0]
        by1, by2, by3, by4, by5, by6, by7, by8, by11, by12, by13, by14, by15, by16, by17, by18 = Cordenadas_B[:,1]

        Cordenadas_W = np.array([[wx1, wy1], [wx2, wy2], [wx3, wy3], [wx4, wy4], [wx5, wy5], [wx6, wy6], [wx7, wy7], [wx8, wy8], [wx11, wy11], [wx12, wy12], [wx13, wy13], [wx14, wy14], [wx15, wy15], [wx16, wy16], [wx17, wy17], [wx18, wy18]])

    


    if turno%2 == 1:                                #Se o turno for impar: as peças pretas jogam
        if aleat == 1:                                  #se leat for 1
            if cont%3 == 0:                             #se cont for multiplo de 3, sorteia um poder
                poder = rnd.randint(0,5)
                aleat = 0
            else:                                       #caso contrario, sorteia um movimento normal
                numero = rnd.randint(0,5)
                aleat = 0
    
    ################################Funções de locomoção das peças pretas#######################################################################################

        bx1, by1, Stateb1, turno, cont, Cordenadas_W = locomocaoB(bx1, by1, Stateb1, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx2, by2, Stateb2, turno, cont, Cordenadas_W = locomocaoB(bx2, by2, Stateb2, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx3, by3, Stateb3, turno, cont, Cordenadas_W = locomocaoB(bx3, by3, Stateb3, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx4, by4, Stateb4, turno, cont, Cordenadas_W = locomocaoB(bx4, by4, Stateb4, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx5, by5, Stateb5, turno, cont, Cordenadas_W = locomocaoB(bx5, by5, Stateb5, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx6, by6, Stateb6, turno, cont, Cordenadas_W = locomocaoB(bx6, by6, Stateb6, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx7, by7, Stateb7, turno, cont, Cordenadas_W = locomocaoB(bx7, by7, Stateb7, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx8, by8, Stateb8, turno, cont, Cordenadas_W = locomocaoB(bx8, by8, Stateb8, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx11, by11, Stateb11, turno, cont, Cordenadas_W = locomocaoB(bx11, by11, Stateb11, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx12, by12, Stateb12, turno, cont, Cordenadas_W = locomocaoB(bx12, by12, Stateb12, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx13, by13, Stateb13, turno, cont, Cordenadas_W = locomocaoB(bx13, by13, Stateb13, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx14, by14, Stateb14, turno, cont, Cordenadas_W = locomocaoB(bx14, by14, Stateb14, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx15, by15, Stateb15, turno, cont, Cordenadas_W = locomocaoB(bx15, by15, Stateb15, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx16, by16, Stateb16, turno, cont, Cordenadas_W = locomocaoB(bx16, by16, Stateb16, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx17, by17, Stateb17, turno, cont, Cordenadas_W = locomocaoB(bx17, by17, Stateb17, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)
        bx18, by18, Stateb18, turno, cont, Cordenadas_W = locomocaoB(bx18, by18, Stateb18, mx, my, largura, altura, event, tela, turno,numero,poder,cont,Cordenadas_W)

        wx1, wx2, wx3, wx4, wx5, wx6, wx7, wx8, wx11, wx12, wx13, wx14, wx15, wx16, wx17, wx18 = Cordenadas_W[:,0]
        wy1, wy2, wy3, wy4, wy5, wy6, wy7, wy8, wy11, wy12, wy13, wy14, wy15, wy16, wy17, wy18 = Cordenadas_W[:,1]

        Cordenadas_B = np.array([[bx1,by1],[bx2,by2],[bx3,by3],[bx4,by4],[bx5,by5],[bx6,by6],[bx7,by7],[bx8,by8],[bx11,by11],[bx12,by12],[bx13,by13],[bx14,by14],[bx15,by15],[bx16,by16],[bx17,by17],[bx18,by18]])

        

        

    #selection color(199, 198, 149)
    pygame.display.update() # faz o loop/atualização do game
