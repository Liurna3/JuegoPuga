import pygame, time
from bibloteca.Player import Player
from bibloteca.Game import Game
from settings import *


from Title import Title

if __name__ == '__main__':
    game = Game(1280, 720, 60)
    game.setBackground("./res/fondo.jpg")
    game.setEatSound("./res/mixkit-video-game-retro-click-237.wav")
    game.setNameApp("Celulas")
    game.setFoodImage("./res/cancer.png")
    game.setBarColor((0, 255, 0))
    game.setGameOverMessage("GAME OVER  GAME OVER  GAME OVER", (255, 0, 0))
    game.setInitMessage("Preparado?", (0, 0, 255))
    game.setScoreMessage("Puntaje: ", (255, 255, 255))
    game.setFontDisplay("JetBrains Mono", 20)
    game.setFontTitle("JetBrains Mono", 10)
    game.setMaxVidas(10)

    p1 = Player(control_id=0,position=(CENTER_X - 300, CENTER_Y))
    p1.setControl(control_id=0,key_down=pygame.K_s,key_up=pygame.K_w, key_left=pygame.K_a,key_right=pygame.K_d,key_fire = pygame.K_z)
    p1.setImagen('./res/celula.png')

    p2 = Player(control_id=1, position=(CENTER_X + 300, CENTER_Y))
    p2.setControl(control_id=1,key_down=pygame.K_k,key_up=pygame.K_i,key_left=pygame.K_j,key_right=pygame.K_l,key_fire = pygame.K_b) 
    p2.setImagen('./res/celula2.png')
    game.addPlayer(p1)
    game.addPlayer(p2)
    title = Title()

    while True:
        title.run()
        game.set_max_vidas(title.getDificultad())
        while not game.isGameOver(): 
            game.run()    
        print(game.getScore())
        time.sleep(2)
        title.scene_active = True
        game.reset()

