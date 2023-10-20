import pygame
from pygame.locals import *


def SorteiaW(mx,largura,my,px,py,numero):
    numero = 3
    match numero:
        case 0:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py-1 #Peão
            #print("1")
        case 1:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py-1 #Cavalo
            #print("2")
        case 2:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py-2 #Bispo
            #print("3")
        case 3:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py-3 #Torre
            #print("4")
        case 4:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py-4 #Rainha
            #print("5")
        case 5:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py-5 #rei
        
    return(loc)

def SorteiaB(mx,largura,my,px,py,numero):
    numero = 3

    match numero:
        case 0:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py-1 #Peão

        case 1:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py+1#cavalo

        case 2:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py+2#Bispo

        case 3:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py+3#Torre

        case 4:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py+4#Rainha

        case 5:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py+6#Rei
    
    return(loc)
