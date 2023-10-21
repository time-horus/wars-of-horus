import pygame
from pygame.locals import *

def PoderW(mx,largura,my,px,py,poder):
    match poder:
        case 0:
            loc = round((mx/(largura/8))-0.5) or round((my/(largura/8))-0.5)
            print("Plot Twist")

        case 1:
            loc = ( (round((mx/(largura/8))-0.5) == px+1 or round((mx/(largura/8))-0.5) == px-1) and ((round((my/(largura/8))-0.5) == py-3)) or ((((round((mx/largura/8))-0.5) == px-3 or round((mx/largura/8))-0.5) == px+3)  and ((round((my/largura/8))-0.5) == py-1)))
            print("Camelo nos Esteroides de Cobre")

        case 2:
            loc = round((mx/(largura/8))-0.5) or round((my/(largura/8))-0.5)
            print("Bonk")
        case 3:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) >= py
            print("Moon Walk")
        case 4:
            loc = (round((mx/(largura/8))-0.5) == px+1 and round((my/(largura/8))-0.5) <= py+1) or (round((mx/(largura/8))-0.5) == px-1 and round((my/(largura/8))-0.5) <= py-1) or (round((mx/(largura/8))-0.5) == px-1 and round((my/(largura/8))-0.5) <= py+1) or (round((mx/(largura/8))-0.5) == px+1 and round((my/(largura/8))-0.5) <= py-1)
            print("De volta para o futuro")
        
        
    return(loc)

def PoderB(mx,largura,my,px,py,poder):

    match poder:
        case 0:
            loc = round((mx/(largura/8))-0.5) or round((my/(largura/8))-0.5)
            print("Plot Twist")
        case 1:
            loc = ( (round((mx/(largura/8))-0.5) == px+1 or round((mx/(largura/8))-0.5) == px-1) and ((round((my/(largura/8))-0.5) == py+3)) or ((((round((mx/largura/8))-0.5) == px-3 or round((mx/largura/8))-0.5) == px+3)  and ((round((my/largura/8))-0.5) == py+1)))
            print("Camelo nos Esteroides de Cobre")
        case 2:
            loc = round((mx/(largura/8))-0.5) or round((my/(largura/8))-0.5)
            print("Bonk")
        case 3:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) <= py
            print("Moon Walk")
        case 4:
            loc = (round((mx/(largura/8))-0.5) == px+1 and round((my/(largura/8))-0.5) <= py+1) or (round((mx/(largura/8))-0.5) == px-1 and round((my/(largura/8))-0.5) <= py-1) or (round((mx/(largura/8))-0.5) == px-1 and round((my/(largura/8))-0.5) <= py+1) or (round((mx/(largura/8))-0.5) == px+1 and round((my/(largura/8))-0.5) <= py-1)
            print("De Volta para o futuro")

    return(loc)
