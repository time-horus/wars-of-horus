import pygame
import start
from start import tocar_som
from pygame.locals import *
import numpy as np

def W_Come_B(Cordenadas_B,px,py,plague,fx,fy):
    if plague == 0:
        for index, V in enumerate(Cordenadas_B):
            if tuple(V) == (px,py):
                Cordenadas_B[index] = [fx,fy]
                tocar_som('Sounds/teleporte.ogg', volume=1)
                plague = None
                break
    elif plague == 2:
        for index, V in enumerate(Cordenadas_B):
            if tuple(V) == (px,py):
                [px,py]= [fx,fy]
                tocar_som('Sounds/pan.ogg', volume=1)

                plague = None
                break
    else:     
        for index, V in enumerate(Cordenadas_B):
            if tuple(V) == (px,py):
                Cordenadas_B[index] = [84,84]
                tocar_som('Sounds/sand-spell.flac', volume=0.5)
                break
    return (Cordenadas_B,px,py)
                           
                        
                   
def B_Come_W(Cordenadas_W,px,py,plague,fx,fy):
    if plague == 0:
        for index, V in enumerate(Cordenadas_W):
            if tuple(V) == (px,py):
                Cordenadas_W[index] = [fx,fy]
                tocar_som('Sounds/teleporte.ogg', volume=1)
                plague=None
                break
    elif plague == 2:
        for index, V in enumerate(Cordenadas_W):
            if tuple(V) == (px,py):
                [px,py] = [fx,fy]
                tocar_som('Sounds/pan.ogg', volume=0.7)
                plague=None
                break
    else:
        for index, V in enumerate(Cordenadas_W):
            if tuple(V) == (px,py):
                Cordenadas_W[index] = [84,84]
                tocar_som('Sounds/sand-spell.flac', volume=0.5)
                break
        
                               
    return (Cordenadas_W,px,py)
