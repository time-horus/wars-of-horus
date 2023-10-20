import pygame
from pygame.locals import *

def PoderW(mx,largura,my,px,py,poder):
    match poder:
        case 0:
            loc = (round((mx/(largura/8))-0.5) == px-1 or round((mx/(largura/8))-0.5) == px+1) and round((my/(largura/8))-0.5) == py-2
            print("Camelo de Cobre")
        case 1:
            loc = ( (round((mx/(largura/8))-0.5) == px+1 or round((mx/(largura/8))-0.5) == px-1) and ((round((my/(largura/8))-0.5) == py-3)) or ((((round((mx/largura/8))-0.5) == px-3 or round((mx/largura/8))-0.5) == px+3)  and ((round((my/largura/8))-0.5) == py-1)))
            print("Camelo nos Esteroides de Cobre")

        case 2:
            loc = (round((mx/(largura/8))-0.5) == px-1 or round((mx/(largura/8))-0.5) == px+1) and round((my/(largura/8))-0.5) == py-2
            #print("3")
        case 3:
            loc = (round((mx/(largura/8))-0.5) == px-1 or round((mx/(largura/8))-0.5) == px+1) and round((my/(largura/8))-0.5) == py-2
            #print("4")
        case 4:
            loc = (round((mx/(largura/8))-0.5) == px-1 or round((mx/(largura/8))-0.5) == px+1) and round((my/(largura/8))-0.5) == py-2
            #print("5")
        case 5:
            loc = (round((mx/(largura/8))-0.5) == px-1 or round((mx/(largura/8))-0.5) == px+1) and round((my/(largura/8))-0.5) == py-2
        
    return(loc)

def PoderB(mx,largura,my,px,py,poder):
    match poder:
        case 0:
            loc = (round((mx/(largura/8))-0.5) == px-1 or round((mx/(largura/8))-0.5) == px+1) and round((my/(largura/8))-0.5) == py+2
            print("Camelo Oxidado")
        case 1:
            loc = ( (round((mx/(largura/8))-0.5) == px+1 or round((mx/(largura/8))-0.5) == px-1) and ((round((my/(largura/8))-0.5) == py+3)) or ((((round((mx/largura/8))-0.5) == px-3 or round((mx/largura/8))-0.5) == px+3)  and ((round((my/largura/8))-0.5) == py+1)))
            print("Camelo nos Esteroides de Cobre")
        case 2:
            loc = (round((mx/(largura/8))-0.5) == px-1 or round((mx/(largura/8))-0.5) == px+1) and round((my/(largura/8))-0.5) == py+2
            #print("3")
        case 3:
            loc = (round((mx/(largura/8))-0.5) == px-1 or round((mx/(largura/8))-0.5) == px+1) and round((my/(largura/8))-0.5) == py+2
            #print("4")
        case 4:
            loc = (round((mx/(largura/8))-0.5) == px-1 or round((mx/(largura/8))-0.5) == px+1) and round((my/(largura/8))-0.5) == py+2
            #print("5")
        case 5:
            loc = (round((mx/(largura/8))-0.5) == px-1 or round((mx/(largura/8))-0.5) == px+1) and round((my/(largura/8))-0.5) == py+2
        
    return(loc)
