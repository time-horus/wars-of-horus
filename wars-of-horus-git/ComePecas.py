import pygame
from pygame.locals import *
import numpy as np

def W_Come_B(Cordenadas_B,px,py):
    for index, V in enumerate(Cordenadas_B):
        if tuple(V) == (px,py):
            Cordenadas_B[index] = [84,84]
            break
                 
    return (Cordenadas_B)
                           
                        
                   
def B_Come_W(Cordenadas_W,px,py):    
    for index, V in enumerate(Cordenadas_W):
        if tuple(V) == (px,py):
            Cordenadas_W[index] = [84,84]
            break
                               
    return (Cordenadas_W)