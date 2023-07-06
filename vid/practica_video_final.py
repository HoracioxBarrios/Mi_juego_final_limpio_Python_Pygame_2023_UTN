import pygame, sys
# from pyvidplayer import *

pygame.init()


def pepe_video_pelea_final_2():
    pygame.mixer.music.load("vid/video final goku vs roshi- cortado -parte 2.wav")
    # vid_2 = Video("vid\goku vs roshi video con audio completo .mp4")#vid final con
    # vid_2.set_size((ancho, alto))
    pygame.mixer.music.play()
    screen = pygame.display.set_mode((ancho, alto))
    while True:
        screen.fill("White")
        
        # if vid_2.active == True: # si es true cirre ek video
        #         vid_2.draw(screen, (0, 0))
        # else:
        #     vid_2.close()
            
            # main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     vid.close()
                #llamada a main menu ()
                # main_menu()
        pygame.display.update()
ancho = 1000
alto = 700

# pygame.mixer.music.load("vid\intrio video epic.wav")
# pygame.mixer.music.play()

def pepe_video_pelea_final_1():
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Epic Vid")

    vid_1 = Video("vid/video final goku vs roshi-coratodo-parte-1.avi")#vid final con
    vid_1.set_size((ancho, alto))


    while True:
        
        pygame.display.update()
        if vid_1.active == True: # si es true cirre ek video
                vid_1.draw(screen, (0, 0))
        else:
            vid_1.close()
            video_pelea_final_2()
            # main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     vid.close()
                #llamada a main menu ()
                # main_menu()



# video_pelea_final_1()
    
