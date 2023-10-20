import pygame
import Sorteio
import Poderes
import ComePecas
import numpy as np

from Poderes import PoderW
from Sorteio import SorteiaW
from ComePecas import W_Come_B

from pygame.locals import *


def locomocaoW(px,py,state,mx,my,largura,altura,event,tela,turno,numero,poder,cont,Cordenadas_B):
    
    if round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py and event.type == MOUSEBUTTONDOWN: #faz a comparação da posição no click do mouse com a posição da peça, se for igual:
        pygame.draw.circle(tela, (125,148,93),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),32) #troca a cor da peça para mostrar seleção
        pygame.draw.circle(tela, (199, 198, 149),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),30)
        state = 1

    if state == 1:
        pygame.draw.circle(tela, (125,148,93),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),32) #A peça continua selecionada
        pygame.draw.circle(tela, (199, 198, 149),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),30)
        if cont%3 == 0:                 #checa se o contador de rodadas é igual a 3
            loc = PoderW(mx,largura,my,px,py,poder) #Sorteia um poder
        else:
            loc = SorteiaW(mx,largura,my,px,py,numero) # sorteia ma locomoção normal

                                                                                          
    if event.type == MOUSEBUTTONUP and state == 1 and loc:
        pygame.draw.circle(tela, (125,148,93),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),32) #troca a cor da peça para mostrar seleção
        pygame.draw.circle(tela, (199, 198, 149),((px+0.5)*(largura/8),(py+0.5)*(altura/8)),30)                                           #se click do mouse e State == 1
        state = 0                                                                                #muda State para 0
        mx, my = pygame.mouse.get_pos()                                                      #pega a posição do mouse no momento do click
        px = round((mx/(largura/8))-0.5)                                                    #tratamento da posição do mouse e atribuição na posição da peça
        py = round((my/(altura/8))-0.5)
        Cordenadas_B = W_Come_B(Cordenadas_B,px,py)
        turno = turno+1
    return (px,py,state,turno,Cordenadas_B)