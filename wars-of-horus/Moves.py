import pygame


def MoveW(tela,px,py,numero):
    match numero:
        case 0:#Mumia
            tela.blit(pygame.image.load("imagens/moves/mumiaW.png"),((px-7)*(1200/15),(py-7)*(1200/15)))

        case 1: #Camelo   
            tela.blit(pygame.image.load("imagens/moves/camelo.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
        case 2:#Sacerdote
            tela.blit(pygame.image.load("imagens/moves/sacerdote.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
        case 3:#Piramide
            tela.blit(pygame.image.load("imagens/moves/piramide.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
        case 4:#Isis
            tela.blit(pygame.image.load("imagens/moves/isis.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
        case 5:#Hórus
            tela.blit(pygame.image.load("imagens/moves/horus.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
    return()

def MoveB(tela,px,py,numero):
    match numero:
        case 0:#Mumia
            tela.blit(pygame.image.load("imagens/moves/mumiaB.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
        case 1: #Camelo   
            tela.blit(pygame.image.load("imagens/moves/camelo.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
        case 2:#Sacerdote
            tela.blit(pygame.image.load("imagens/moves/sacerdote.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
        case 3:#Piramide
            tela.blit(pygame.image.load("imagens/moves/piramide.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
        case 4:#Isis
            tela.blit(pygame.image.load("imagens/moves/isis.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
        case 5:#Hórus
            tela.blit(pygame.image.load("imagens/moves/horus.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
            
    return()

def MovePW(tela,px,py,poder):
    match poder:
        case 1: #Camelo com esteroides   
            tela.blit(pygame.image.load("imagens/moves/cameloFODA.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
        case 3:#Moon walk
            tela.blit(pygame.image.load("imagens/moves/backW.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
        case 4:#De volta para o futuro
            tela.blit(pygame.image.load("imagens/moves/Delorean.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
        
    return()

def MovePB(tela,px,py,poder):
    match poder:
        case 1: #Camelo com esteroides   
            tela.blit(pygame.image.load("imagens/moves/cameloFODA.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
        case 3:#Moon walk
            tela.blit(pygame.image.load("imagens/moves/backB.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
        case 4:#De volta para o futuro
            tela.blit(pygame.image.load("imagens/moves/Delorean.png"),((px-7)*(1200/15),(py-7)*(1200/15)))
    return()
