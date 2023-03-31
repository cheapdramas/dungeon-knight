import pygame
from dungeondata import *
from dungeonclass import *
from random import randint  
from sys import exit
pygame.init()


pygame.display.set_caption('Dungeon Knight')
clock = pygame.time.Clock()
name_game = font.render('DK',False,(255,255,255))
name_game_rect = name_game.get_rect().size
settings_text = font.render('Game difficulty',False,(255,255,255))
settings_text_rect = settings_text.get_rect(topleft= (350,100))

def run():
    def full_hp_draw():
        window.blit(heart_fullhp_im,heart_full_im_rect1)
        window.blit(heart_fullhp_im,heart_full_im_rect2)
        window.blit(heart_fullhp_im,heart_full_im_rect3)
    def minus_half_heart_hp_draw():
        window.blit(heart_halfhp_im,heart_halfhp_im_rect1)
        window.blit(heart_fullhp_im,heart_full_im_rect2)
        window.blit(heart_fullhp_im,heart_full_im_rect3)
    def minus_full_heart_hp_draw():
        window.blit(heart_emptyhp_im,heart_emptyhp_im_rect1)
        window.blit(heart_fullhp_im,heart_full_im_rect2)
        window.blit(heart_fullhp_im,heart_full_im_rect3)
    def minus_full_and_half_heart_hp_draw():
        window.blit(heart_emptyhp_im,heart_emptyhp_im_rect1)
        window.blit(heart_halfhp_im,heart_halfhp_im_rect2)
        window.blit(heart_fullhp_im,heart_full_im_rect3)
    def two_empty_heart():
        window.blit(heart_emptyhp_im,heart_emptyhp_im_rect1)
        window.blit(heart_emptyhp_im,heart_emptyhp_im_rect2)
        window.blit(heart_fullhp_im,heart_full_im_rect3)
    def last_half_heart():
        window.blit(heart_emptyhp_im,heart_emptyhp_im_rect1)
        window.blit(heart_emptyhp_im,heart_emptyhp_im_rect2)
        window.blit(heart_halfhp_im,heart_halfhp_im_rect3)
    #def five_hearts_draw():
    #    window.blit(heart_)
    
    



    
    
    menu_check = 1
    def fps_counter():
        fps = str(int(clock.get_fps()))
        fps_t = font.render(fps , 1, pygame.Color((255,255,255)))
        window.blit(fps_t,(0,0))
    
    game = True
    
    #for menu
    def move(x,y):
        window.blit(name_game,(x,y))
        
        
    
    x = randint(50, 1000-60)
    y = randint(50, 600 - 60)
    x_speed = 2.5
    y_speed = 2.5
    
    
    menu = Menu()
    
    
    
    
   

    
    

    
        
    #menu end


    while game:
        
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                exit()
            #menu control
            if menu_check == 1:
                if eve.type == pygame.KEYDOWN:
                    if eve.key == pygame.K_SPACE:
                        menu.select()
                if eve.type == pygame.KEYDOWN:
                    if eve.key == pygame.K_w:
                        menu.switch(-1)
                if eve.type == pygame.KEYDOWN:
                    if eve.key == pygame.K_s:
                        menu.switch(1)
                
            #settings control
            if menu.setting_is == 1:
                if eve.type == pygame.KEYDOWN:
                    if eve.key == pygame.K_SPACE:
                        menu.select()
                if eve.type == pygame.KEYDOWN:
                    if eve.key == pygame.K_w:
                        menu.switch(-1)
                if eve.type == pygame.KEYDOWN:
                    if eve.key == pygame.K_s:
                        menu.switch(1)
                if eve.type == pygame.KEYDOWN:
                    if eve.key == pygame.K_ESCAPE:
                        menu.setting_is = 0
                        menu_check = 1
                

            # spawn bullets            
            if menu.level_which == 1:
                
                if gun1.is_enabled:
                    if eve.type == pygame.MOUSEBUTTONDOWN and player.right:

                        entities.add(bullet)
                        bullet.to_right = True
                        
                    if eve.type == pygame.MOUSEBUTTONDOWN and player.left:
                        entities.add(bullet)
                        bullet.to_left = True
                    if eve.type == pygame.MOUSEBUTTONDOWN and player.back:
                        entities.add(bullet)
                        bullet.to_up = True
                    if eve.type == pygame.MOUSEBUTTONDOWN and player.straight:
                        entities.add(bullet)
                        bullet.to_down = True
                
                        
                        
                        
            
                        
                        

           

                
        #menu
        if menu_check == 1:
            menu._callbacks.clear()
            menu._option_surfaces.clear()
            menu.append_option('Play',menu.idk)
            menu.append_option('Quit',exit)
            menu.append_option('Settings',menu.to_settings)
    
            window.fill((0,0,0))

            menu.draw(window,470,250,75)
            if (x + name_game_rect[0] >= win_width) or (x <= 0):
                    x_speed = -x_speed
            if (y + name_game_rect[1] >= win_height) or (y <= 0):
                y_speed = -y_speed
            x += x_speed
            y += y_speed
            move(x, y)
        #settings screen
        if menu.setting_is == 1:
            heart_expa = Heart_expa((mob.rect.x,mob.rect.y),player)
            
            menu._option_surfaces.clear()
            menu._callbacks.clear()
            menu_check = 0
            window.fill((0,0,0))
            window.blit(settings_text,settings_text_rect)
            pygame.draw.line(window,((255,255,255)),(300,70),(725,70),5)
            pygame.draw.line(window,((255,255,255)),(723,70),(723,150),5)
            pygame.draw.line(window,((255,255,255)),(300,150),(722,150),5)
            pygame.draw.line(window,((255,255,255)),(300,70),(300,150),5)


            #choose frames
            pygame.draw.line(window,((255,255,255)),(100,300),(100,500),5)
            pygame.draw.line(window,((255,255,255)),(97,300),(300,300),5)
            pygame.draw.line(window,((255,255,255)),(100,500),(300,500),5)
            pygame.draw.line(window,((255,255,255)),(300,300),(300,500),5)
            menu.append_option('Easy',menu.to_easy)
            
            menu.append_option('Medium',menu.to_medium)
            menu.append_option('Hard',menu.to_hard)
            

            menu.draw(window,150,300,75)
        
        
        if menu.easy == 1:
            settings['mobs_speed'] = 2
        if menu.medium == 1:
            settings['mobs_speed'] = 8
        if menu.hard == 1:
           settings['mobs_speed'] = 20

            


        
        if menu.level_which == 1:
            #expa = Heart_expa((mob.rect.x,mob.rect.y),player,mob,mob1)

            menu_check = 0
            pressed = pygame.key.get_pressed()
            if pressed[K_1]:
                gun1.change_pic()
                gun1.is_enabled = True
            for i in heal_list:
                entities.add(i)
            #if mob.mobalive == False:
            #    entities.add(expa)
            
            
            
           #print(expa.one)
            #print(entities)
            #print(player.hp)
            #print(len(heal_list))

            
            
             
            

            
            

            
            bullet = Bullets(player,(player.rect.x,player.rect.y),mob,mob1)
            

            
            

            #window.blit(heart)
            
            
            
            entities.update()
            #if mob.mobalive == False:

                 
            
            window.fill((0,0,0))
            
            
            
            
            #print(entities)
            
            
            for enty in mob.mob_list:
                entities.add(enty)
            entities.draw(window)
            if player.hp == 3:
                full_hp_draw()
                
            if player.hp == 2.5:
                minus_half_heart_hp_draw()
            if player.hp == 2:
                minus_full_heart_hp_draw()
            if player.hp == 1.5:
                minus_full_and_half_heart_hp_draw()
            if player.hp == 1:
                two_empty_heart()
            if player.hp == 0.5:
                last_half_heart()
            print(player.hp)

            
            
            if player.hp > 0:
                mob.hit = False

            if player.hp == 0:
                menu_check = 1
                menu.level_which = 0
            
            
        
            
           
            fps_counter()
            
            
            
            
        


            
        

        


        clock.tick(60)
        pygame.display.flip()
run()
