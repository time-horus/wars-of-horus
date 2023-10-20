import pygame
from pygame.locals import *


def SorteiaW(mx,largura,my,px,py,numero):
    numero = 0
    match numero:
        case 0:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py-1 #Peão
            #print("1")
        case 1:
            loc = ( (round((mx/(largura/8))-0.5) == px+1 or round((mx/(largura/8))-0.5) == px-1) and ((round((my/(largura/8))-0.5) == py-2)) or ((((round((mx/largura/8))-0.5) == px-2 or round((mx/largura/8))-0.5) == px+2)  and ((round((my/largura/8))-0.5) == py-1))) #Cavalo
            #print("2")
        case 2:
            loc = ((round((mx/(largura/8))-0.5) == px+1 and round((mx/(largura/8))-0.5) == py-1) or (round((mx/(largura/8))-0.5) == px+2 and round((mx/(largura/8))-0.5) == py-2) or (round((mx/(largura/8))-0.5) == px+3 and round((mx/(largura/8))-0.5) == py-3)or (round((mx/(largura/8))-0.5) == px+4 and round((mx/(largura/8))-0.5) == py-4)or (round((mx/(largura/8))-0.5) == px+5 and round((mx/(largura/8))-0.5) == py-5)or (round((mx/(largura/8))-0.5) == px+6 and round((mx/(largura/8))-0.5) == py-6)or (round((mx/(largura/8))-0.5) == px+7 and round((mx/(largura/8))-0.5) == py-7)) or (round((mx/(largura/8))-0.5) == px-1 and round((mx/(largura/8))-0.5) == py+1) or (round((mx/(largura/8))-0.5) == px-2 and round((mx/(largura/8))-0.5) == py+2) or (round((mx/(largura/8))-0.5) == px+1 and round((mx/(largura/8))-0.5) == py-1) or (round((mx/(largura/8))-0.5) == px+1 and round((mx/(largura/8))-0.5) == py-1) or (round((mx/(largura/8))-0.5) == px+1 and round((mx/(largura/8))-0.5) == py-1) or (round((mx/(largura/8))-0.5) == px+1 and round((mx/(largura/8))-0.5) == py-1) or (round((mx/(largura/8))-0.5) == px+1 and round((mx/(largura/8))-0.5) == py-1)
            #print("3")
        case 3:
            loc =  (round((mx/(largura/8))-0.5) == px and (8 >= round((my/(largura/8))-0.5) >= 0)) or (round((my/(largura/8))-0.5) == py and (8 >= round((mx/(largura/8))-0.5) >=0)) #Torre
            #print("4")
        case 4:
            loc = round((mx/(largura/8))-0.5) == px and round((my/(largura/8))-0.5) == py-4 #Rainha
            #print("5")
        case 5:
             loc = ((round((mx/(largura/8))-0.5) == px-1 or (round((mx/(largura/8))-0.5) == px +1)) and (round((my/(largura/8))-0.5) == py) or (round((mx/(largura/8))-0.5) == px) or ((round((my/(largura/8))-0.5) == py-1 or round((my/(largura/8))-0.5) == py+1) and  (round((mx/(largura/8))-0.5) == px or round((mx/(largura/8))-0.5) == px)) or (round((mx/(largura/8))-0.5) == px-1 or (round((mx/(largura/8))-0.5) == px+1) and ((round((my/(largura/8))-0.5) == py-1 or round((my/(largura/8))-0.5) == py+1))))#rei
        
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