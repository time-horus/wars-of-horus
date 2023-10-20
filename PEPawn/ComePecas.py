import pygame
from pygame.locals import *


def Come(Cordenadas_X_B,Cordenadas_Y_B,Cordenadas_X_W,Cordenadas_Y_W,turno):
    a = 0
    if (turno-1)%2 == 0:
        for Z in Cordenadas_X_B:
            for V in Cordenadas_X_W:
                for J in Cordenadas_Y_B:
                    a = 0
                    for K in Cordenadas_Y_W:
                        if Z == V and J == K:
                            Cordenadas_X_B[a] = 22
                            Cordenadas_Y_B[a] = 22
                            a=0
                            break
                        a = a+1
                    

    if (turno-1)%2 == 1:
        for Z in Cordenadas_X_B:
            for V in Cordenadas_X_W:
                for J in Cordenadas_Y_B:
                    a=0
                    for K in Cordenadas_Y_W:
                        if Z == V and J == K:
                            Cordenadas_X_W[a] = 22
                            Cordenadas_Y_W[a] = 22
                            a=0
                            break
                        a = a+1

    return (Cordenadas_X_B,Cordenadas_Y_B,Cordenadas_X_W,Cordenadas_Y_W)
                        
                    