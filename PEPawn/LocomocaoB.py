import pygame
import Sorteio
import Poderes

from Poderes import PoderB
from Sorteio import SorteiaB

from pygame.locals import *


def locomocaoB(px,py,state,mx,my,largura,altura,event,tela,turno,numero,poder,cont):


    if round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py and event.type == MOUSEBUTTONDOWN: #faz a comparação da posição no click do mouse com a posição da peça, se for igual:
        pygame.draw.circle(tela, (125,148,93),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),32) #troca a cor da peça para mostrar seleção
        pygame.draw.circle(tela, (199, 198, 149),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),30)
        state = 1                                                                                #muda o estado da peça para 1(selecionado)
    if state == 1:
        pygame.draw.circle(tela, (125,148,93),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),32) #troca a cor da peça para mostrar seleção
        pygame.draw.circle(tela, (199, 198, 149),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),30)
        if cont%3 == 0:
            loc = PoderB(mx,largura,my,px,py,poder)
        else:
            loc = SorteiaB(mx,largura,my,px,py,numero)

    if event.type == MOUSEBUTTONUP and state == 1 and loc:  
        pygame.draw.circle(tela, (125,148,93),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),32) #troca a cor da peça para mostrar seleção
        pygame.draw.circle(tela, (199, 198, 149),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),30)                                           #se click do mouse e State == 1
        state = 0                                                                                #muda State para 0
        mx, my = pygame.mouse.get_pos()                                                      #pega a posição do mouse no momento do click
        px = round((mx/(largura/8))-0.5)                                                    #tratamento da posição do mouse e atribuição na posição da peça
        py = round((my/(altura/8))-0.5)
        turno = turno+1
        cont = cont+1
        print(cont)
        
    return (px,py,state,turno,cont)
