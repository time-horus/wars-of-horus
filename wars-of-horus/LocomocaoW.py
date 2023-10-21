import pygame
import Sorteio
import Poderes
import ComePecas
import Moves
import numpy as np

from Poderes import PoderW
from Sorteio import SorteiaW
from ComePecas import W_Come_B
from Moves import MoveW
from Moves import MovePW
from pygame.locals import *

def locomocaoW(px,py,state,mx,my,largura,altura,event,tela,turno,numero,poder,cont,Cordenadas_B):
    plague = None
    fx = None
    fy = None
    if round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py and event.type == MOUSEBUTTONDOWN: #faz a comparação da posição no click do mouse com a posição da peça, se for igual:
        state = 1

    if state == 1:
       
        if cont%3 == 0:                 #checa se o contador de rodadas é igual a 3
            MovePW(tela,px,py,poder)
            loc = PoderW(mx,largura,my,px,py,poder) #Sorteia um poder
            plague = poder
            fx = px
            fy = py
        else:
            MoveW(tela,px,py,numero)
            loc = SorteiaW(mx,largura,my,px,py,numero) # sorteia ma locomoção normal

                                                                                          
    if event.type == MOUSEBUTTONUP and state == 1 and loc:
        state = 0                                                                                #muda State para 0
        mx, my = pygame.mouse.get_pos()                                                      #pega a posição do mouse no momento do click
        px = round((mx/(largura/8))-0.5)                                                    #tratamento da posição do mouse e atribuição na posição da peça
        py = round((my/(altura/8))-0.5)
        Cordenadas_B,px,py = W_Come_B(Cordenadas_B,px,py,plague,fx,fy)
        turno = turno+1
    return (px,py,state,turno,Cordenadas_B)
