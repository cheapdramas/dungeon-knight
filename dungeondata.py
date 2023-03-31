import pygame
pygame.init()
import os

TILE_SIZE = 32
SCREEN_SIZE = pygame.Rect((0, 0, 1000, 640))



                 
MAPS = {         
    'MAP1' : [



'                                                                                                    ',
'                                                                                                    ',
'                                                                                                    ',
'                                                                                                    ',
'                                                                                                    ',
'                                                                                                    ',
'                                                                                                    ',
'                                                                                                    ',
'                                                                                                    ',
'                                                                                                    ',
'                                                                                                    ',
'                                                                                                    ',
'           1111111111111111111111111111111111111111111111111111111111111111111111111                ',
'           1                                                                       1                ',
'           1   m                                                                   1                ',
'           1                                                         M             1                ',            
'           1                                                                       1                ',
'           1                                                                       1                ',
'           1                                                                       1                ',
'           1                                                                       1                ',
'           1                                                                       1                ',
'           1                                                                       1                ',
'           1                                                                       1                ',
'           1                                                                       1                ',
'           1                                                                       1                ',
'           1                                                                       1                ',
'           1                                                                       1                ',
'           1111111111111111111111111111                11111111111111111111111111111                ',
'                                      1                1                                            ',
'                                      1                1                                            ',
'                                      1                1                                            ',
'                                      1                1                                            ',
'                                      1                1                                            ',
'                              111111111                111111111                                    ',
'                              1                                1                                    ',
'                              1                                1                                    ',
'                              1                                1                                    ',
'                              1                                1                                    ',
'                              1                                1                                    ',
'                              1                                1                                    ',
'                              1                                1                                    ',
'                              1               p                1                                    ',
'                              1                                1                                    ',
'                              1                                1                                    ',
'                              1111111111111111111111111111111111                                    ',






]
}
settings = {
    'mobs_speed' : 0,
    
    

    
}


win_width = 1000
win_height = 654
window = pygame.display.set_mode(SCREEN_SIZE.size)  
print(win_height)   







abs_images = os.path.abspath(__file__+"/..") + "\\IMAGES\\"
abs_font = os.path.abspath(__file__+"/..") + "\\FONTT\\"
abs_music = os.path.abspath(__file__+"/..") + "\\MUSIC\\"
font = pygame.font.Font('PKMN RBYGSC.ttf',30)
print(abs_font)

simp_im_list = []
player_back_anim = []
player_back_anim.append(pygame.image.load(abs_images + 'player_back_anim1.png')) 
player_back_anim.append(pygame.image.load(abs_images + 'player_back.png'))
player_back_anim.append(pygame.image.load(abs_images + 'player_back_anim2.png'))

just_stand_list = []

just_stand_list.append(pygame.image.load(abs_images +'player_back.png'))
just_stand_list.append(pygame.image.load(abs_images +'player_straight.png'))
just_stand_list.append(pygame.image.load(abs_images +'player_left.png'))
just_stand_list.append(pygame.image.load(abs_images +'player_right.png'))


 
player_str_anim = []
player_str_anim.append(pygame.image.load(abs_images +'player_str_anim1.png')) 
player_str_anim.append(pygame.image.load(abs_images +'player_straight.png'))
player_str_anim.append(pygame.image.load(abs_images +'player_str_anim2.png'))



player_left_anim = []
player_left_anim.append(pygame.image.load(abs_images + 'player_left_anim1.png')) 
player_left_anim.append(pygame.image.load(abs_images + 'player_left.png'))
player_left_anim.append(pygame.image.load(abs_images + 'player_left_anim2.png'))


player_right_anim = []
player_right_anim.append(pygame.image.load(abs_images + 'player_right_anim1.png'))
player_right_anim.append(pygame.image.load(abs_images + 'player_right.png')) 
player_right_anim.append(pygame.image.load(abs_images + 'player_right_anim2.png'))

gun1_right = []
gun1_right.append(pygame.image.load(abs_images + 'player_right_anim1_gun1.png'))
gun1_right.append(pygame.image.load(abs_images + 'player_right_gun1.png'))
gun1_right.append(pygame.image.load(abs_images + 'player_right_anim2_gun1.png'))

idk_mob = pygame.image.load(abs_images + 'pers.png')
idk_mobanim = pygame.image.load(abs_images +'persanim.png')

pulya = pygame.image.load(abs_images + 'pulyamoya.png')
idk_mob_up = pygame.image.load(abs_images + 'idk_up.png')

expa_im = pygame.image.load(abs_images + 'expa.png')


























simp_im_list.append(pygame.image.load(abs_images + 'player_left.png'))
simp_im_list.append(pygame.image.load(abs_images + 'player_back.png'))
simp_im_list.append(pygame.image.load(abs_images + 'player_right.png'))
simp_im_list.append(pygame.image.load(abs_images + 'player_straight.png'))
simp_im_list.append(pygame.image.load(abs_images + 'player_back_anim1.png'))
simp_im_list.append(pygame.image.load(abs_images + 'player_back_anim2.png'))
simp_im_list.append(pygame.image.load(abs_images + 'player_left_anim1.png'))
simp_im_list.append(pygame.image.load(abs_images + 'player_left_anim2.png'))
simp_im_list.append(pygame.image.load(abs_images + 'player_right_anim1.png'))
simp_im_list.append(pygame.image.load(abs_images + 'player_right_anim2.png'))
simp_im_list.append(pygame.image.load(abs_images + 'player_str_anim1.png'))
simp_im_list.append(pygame.image.load(abs_images + 'player_str_anim2.png'))

heart_fullhp_im = pygame.image.load(abs_images +'heart_hp_player_v2.png')
heart_halfhp_im = pygame.image.load(abs_images +'heart_halfhp_player_v2.png')
heart_expa_im = pygame.image.load(abs_images + 'heart_hp_player_v2.png')


#heart hp rects
heart_full_im_rect1 = heart_fullhp_im.get_rect(topleft = (800,30))
heart_full_im_rect2 = heart_fullhp_im.get_rect(topleft = (850,30))
heart_full_im_rect3 = heart_fullhp_im.get_rect(topleft = (900,30))
heart_emptyhp_im = pygame.image.load(abs_images + 'heart_emptyhp_player_v2.png')

heart_halfhp_im_rect1 = heart_halfhp_im.get_rect(topleft = (800,30))
heart_halfhp_im_rect2 = heart_halfhp_im.get_rect(topleft = (850,30))
heart_halfhp_im_rect3 = heart_halfhp_im.get_rect(topleft = (900,30))

heart_emptyhp_im_rect1 = heart_emptyhp_im.get_rect(topleft = (800,30))
heart_emptyhp_im_rect2 = heart_emptyhp_im.get_rect(topleft = (850,30))
heart_emptyhp_im_rect3 = heart_emptyhp_im.get_rect(topleft = (900,30))
heart_expa_anim_vertx = pygame.image.load(abs_images + 'heart_expa_vertx_anim.png')
heart_expa_anim_side = pygame.image.load(abs_images + 'heart_anim_side.png')



heart_expa_anim = []
heart_expa_anim.append(heart_expa_im)
heart_expa_anim.append(heart_expa_anim_vertx)
heart_expa_anim.append(heart_expa_anim_side)


