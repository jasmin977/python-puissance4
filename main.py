import pygame
from game import *



def show(d, p): #show the player piece if the game is still playing or the winner
    s = pygame.Surface((1100, 700), pygame.SRCALPHA)  # per-pixel alpha
    s.fill((0, 0, 0, 128))  # notice the alpha value in the color

    if (p == 1):
        screen.blit(s, (0, 0))
        win_rect = p1.get_rect(center=(window_width / 2, window_height / 2))
        screen.blit(p1, win_rect)
    elif (p == 2):
        screen.blit(s, (0, 0))
        win_rect = p2.get_rect(center=(window_width / 2, window_height / 2))
        screen.blit(p2, win_rect)

    else:

        for i in range(6):
            for j in range(7):
                if (d[i][j] == 1):
                    screen.blit(W, (290 + (j * 76), 140 + (i * 75)))
                if (d[i][j] == 2):
                    screen.blit(R, (290 + (j * 76), 140 + (i * 75)))


# initialize game engine
pygame.init()

window_width = 1100
window_height = 700

size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Jeux puissance 4")

close = False

W = pygame.image.load("img/W.png")

R = pygame.image.load("img/R.png")


j_playing = pygame.image.load("img/p1.png")
r_playing = pygame.image.load("img/p2.png")

p1 = pygame.image.load("img/p1win.png")
p2 = pygame.image.load("img/p2win.png")
reset = pygame.image.load("img/pressedRestart.png")
quit = pygame.image.load("img/QUIT.png")

clockIMG = pygame.image.load("img/clock.png")
# Scale the image to your needed size
imgCLOCK = pygame.transform.scale(clockIMG, (40,40))
#--------------------------------------------------------------

curfolllow = pygame.image.load("img/cur.png")

# velocity / speed of movement
vel = 5

# Indicates pygame is running
run = True


#--------------------------------------------------------------
font = pygame.font.SysFont(None, 32)

clock = pygame.time.Clock()

start_time = pygame.time.get_ticks()

#------------------------------------------
buttonSound = pygame.mixer.Sound("img/btnsound.mp3")

bgsound=pygame.mixer.music.load('img/bgsound.mp3')
pygame.mixer.music.play(-1) # -1 will ensure the song keeps looping

g = the_game()
player = 1


background_image = pygame.image.load("img/bg.png").convert()

while (close == False):

    counting_time = pygame.time.get_ticks()-start_time

    # change milliseconds into minutes, seconds,
    counting_minutes = (counting_time / 60000)
    counting_seconds = (counting_time % 60000) / 1000

    counting_string = "{}:{}" .format (int(counting_minutes), int(counting_seconds))
    font = pygame.font.SysFont("Segoe UI", 50)

    counting_text = font.render(str(counting_string), 1, (39, 97, 230))


    #we gonna check for the event coming from user
    for event in pygame.event.get(): # get a list of all the events that can happen
        if event.type == pygame.QUIT: #if he hit the red butoom on the corner
            close = True

        if event.type == pygame.MOUSEMOTION: #gonna change the cursor when its on the right colums
            x, y = event.pos
            if ((x in range(287, 354)) or (x in range(366, 431)) or (x in range(442, 505)) or (x in range(519, 580)) or(x in range(596, 658))\
                    or (x in range(671, 732)) or (x in range(749, 809)) and (y in range(120, 595))) or ((x in range(871, 971)) or (x in range(980, 1082)) and (y in range(36, 136))):
                cursor = pygame.image.load('img/curHAND.png')
                pygame.mouse.set_visible(False)  # hide the cursor

                # write this in the loop
                coord = pygame.mouse.get_pos()



            else:
                cursor = pygame.image.load('img/cursor.png')
                pygame.mouse.set_visible(False)  # hide the cursor

                # write this in the loop
                coord = pygame.mouse.get_pos()






        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos() # get cursor position
                #print('pos', pos)
                p = position(pos)
                if (p != None): #if its in range (0,6)

                    if (g.get_game_end() == 0):
                        av = available(g.get_d(), p)

                        if (av == -2): # the reset button is clicked
                            g.reset()
                            start_time=pygame.time.get_ticks() #reset time

                        if (av == -3): # the quit button is clicked
                            close = True


                        elif (av != -1): #its availbe
                            buttonSound.play()
                            g.play(player, p)
                            player = change(player)




    screen.blit(background_image, [0, 0])
    screen.blit(reset, [870, 35])
    screen.blit(quit, [980, 35])


    screen.blit(counting_text, [507, 615])
    clock.tick(25)
    screen.blit(imgCLOCK, [455, 630])


    if (player==1):
        screen.blit(j_playing, [911, 508])
    else:
        screen.blit(r_playing,[911, 508])


    # moving the lil triangle with the cursor
    if (x<321):
        screen.blit(curfolllow, [286, 45])
    elif (x>779):
        screen.blit(curfolllow, [746, 45])
    else:
        screen.blit(curfolllow, [x - 40, 45])



    show(g.get_d(), g.check_win())
    screen.blit(cursor, coord)
    pygame.display.flip()