import pygame
gameover=pygame.image.load('photo/text/gameover.png')
rocket_conter_speed=0
score=0
af1=True
af2=False
rocket_y_limit=True
gameplay=True
rocket_spawn=[]
clock=pygame.time.Clock()
rocket=pygame.image.load('photo/rocket.png')
rocket_x=1050
player_dam=0
speed_player=10
run_player=150
rocket_y=500
rocket_conter_y=0
time_spawn_rocket=0
speed_rocket=15
pygame.init()
screen = pygame.display.set_mode((1000,563))
fon_mus=pygame.mixer.Sound('sound/fon_mus.mp3')
fon_mus.play()
time1=4000
a=True
runn = False
icon = pygame.image.load('photo/icon.png')
walk_left=[pygame.image.load('photo/left/1.png').convert_alpha(),
           pygame.image.load('photo/left/2.png').convert_alpha(),
           pygame.image.load('photo/left/1.png').convert_alpha(),
           pygame.image.load('photo/left/2.png').convert_alpha()
           ]
walk_right=[pygame.image.load('photo/right/1.png').convert_alpha(),
            pygame.image.load('photo/right/2.png').convert_alpha(),
            pygame.image.load('photo/right/1.png').convert_alpha(),
            pygame.image.load('photo/right/2.png').convert_alpha()
            ]
player_walk=0
player_jump=500
player_max_jump=7
player_jum=False
pygame.display.set_icon(icon)
fon = pygame.image.load('photo/afon.png').convert_alpha()
pygame.display.update()
survive_score=0
rocket_timer=pygame.USEREVENT+1
pygame.time.set_timer(rocket_timer ,time1)
while runn==False:

    player_rect = walk_left[0].get_rect(topleft=(run_player, player_jump))
    keys = pygame.key.get_pressed()

    if gameplay==True:
        screen.blit(fon,(0,0))

        if rocket_spawn:
            for (i,es) in enumerate(rocket_spawn):
                screen.blit(rocket,es)
                es.x-=speed_rocket
                if es.x < -150:
                    rocket_spawn.pop(i)


            if player_rect.colliderect(es):
                player_dam+=1

        if keys[pygame.K_LEFT]:
            af1=True
            af2=False
            screen.blit(walk_left[player_walk],(run_player,player_jump))
        elif keys[pygame.K_RIGHT]:
            af1 = False
            af2 = True
            screen.blit(walk_right[player_walk],(run_player,player_jump))
        else:
            if af1==True and af2==False:
                screen.blit(walk_left[0], (run_player, player_jump ))
            if af1==False and af2==True:
                screen.blit(walk_right[0], (run_player, player_jump))
        if not player_jum:
            if keys[pygame.K_UP]:
                player_jum=True
        else:
            if player_max_jump >= -7:
                if player_max_jump>0:
                    player_jump-=(player_max_jump**2)/2
                else:
                    player_jump+=(player_max_jump**2)/2
                player_max_jump-=1
            else:
                player_jum=False
                player_max_jump=7
        if player_dam==3:
            gameplay=False

    pygame.display.update()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and run_player >10:
        run_player-=speed_player
    elif keys[pygame.K_RIGHT] and run_player <970:
        run_player+=speed_player


    if player_walk==3:
        player_walk=0
    else:
        player_walk+=1

    if rocket_conter_speed==3:
        speed_rocket+=5
        rocket_conter_speed=0
    if rocket_y>480:
        if rocket_conter_y == 10:
            rocket_y -= 5
            rocket_conter_y = 0
    if time1>500:
        if time_spawn_rocket==5:
            time1-=500
            time_spawn_rocket=0


    pygame.display.update()
    if gameplay:
        for event1 in pygame.event.get():
            if event1.type==rocket_timer:
                score+=50
                survive_score+=50
                rocket_conter_y+=1
                rocket_conter_speed+=1
                time_spawn_rocket+=1
                print('ваша статисика : ', score)
                print('скорость' ,speed_rocket)
                print('урон от 1 до 3 ',player_dam)
                player_dam=0
                rocket_spawn.append(rocket.get_rect(topleft=(rocket_x,rocket_y)))
    else:
        if a:
            print('ваша статисика : ' ,score)
            a=False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=True
            pygame.quit()

    clock.tick(15)