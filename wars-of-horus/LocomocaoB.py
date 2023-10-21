import pygame
import Sorteio
import Poderes
import ComePecas
import Moves
import numpy as np

from Poderes import PoderB
from Sorteio import SorteiaB
from ComePecas import B_Come_W
from Moves import MoveB
from Moves import MovePB
from pygame.locals import *

def locomocaoB(px,py,state,mx,my,largura,altura,event,tela,turno,numero,poder,cont,Cordenadas_W):
    plague = None
    fx = None
    fy = None
    if round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py and event.type == MOUSEBUTTONDOWN: #faz a comparação da posição no click do mouse com a posição da peça, se for igual:
        
        state = 1                                                                                #muda o estado da peça para 1(selecionado)
    if state == 1:
        
        if cont%3 == 0:
            MovePB(tela,px,py,poder)
            loc = PoderB(mx,largura,my,px,py,poder)
            plague = poder
            fx = px
            fy = py
        else:
            MoveB(tela,px,py,numero)
            loc = SorteiaB(mx,largura,my,px,py,numero)

    if event.type == MOUSEBUTTONUP and state == 1 and loc:  
        state = 0                                                                                #muda State para 0
        mx, my = pygame.mouse.get_pos()                                                     #pega a posição do mouse no momento do click
        px = round((mx/(largura/8))-0.5)                                                    #tratamento da posição do mouse e atribuição na posição da peça
        py = round((my/(altura/8))-0.5)
        Cordenadas_W,px,py = B_Come_W(Cordenadas_W,px,py,plague,fx,fy)                                         #Checagem se a uma peça comeu a outra
        turno = turno+1                                                                     #Adiciona mais um no valor de turno
        cont = cont+1                                                                       #Adiciona mais um no contador de rodadas(Só no turno das pretas)
        
    return (px,py,state,turno,cont,Cordenadas_W) #retorna as variaveis e o array modificado