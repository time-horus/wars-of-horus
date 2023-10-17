import pygame
from pygame.locals import *


def SorteiaW(mx,largura,my,px,py,numero):
    match numero:
        case 0:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py
            #print("1")
        case 1:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py-1
            #print("2")
        case 2:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py-2
            #print("3")
        case 3:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py-3
            #print("4")
        case 4:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py-4
            #print("5")
        case 5:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py-5
        
    return(loc)

def SorteiaB(mx,largura,my,px,py,numero):
    match numero:
        case 0:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py

        case 1:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py+1

        case 2:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py+2

        case 3:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py+3

        case 4:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py+4

        case 5:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py+5
    
    return(loc)
