from pygame import *
init()
import math
from dungeondata import * 

heal_list = []
def quit_menu():
        
    level_which = 1
    def quit_menu():
        menu_check = 0
        
        level_which = 1
class Entity(pygame.sprite.Sprite):
    def __init__(self, color, pos, *groups):
        super().__init__(*groups)
        self.image = Surface((TILE_SIZE, TILE_SIZE)).convert_alpha()
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
class Player(Entity):
    def __init__(self, platforms, pos, *groups):
        super().__init__(Color("#0000FF"), pos)
        self.im_list = simp_im_list
        self.current_sprite = 0
        self.right = False
        self.left = False
        self.back = False
        self.take_buff = False
        self.straight = True
        self.rect.x = 700
        if self.rect.x == 1856:
            self.rect.x = 112
        self.rect.y = 732
        self.hp = 3
        print(self.rect.x)    
        
        
        
        self.vel = pygame.Vector2((0, 0))
        
        self.platforms = platforms
        self.speed = 8
        self.jump_strength = 10


        
        
    def update(self):
        pressed = pygame.key.get_pressed()
        up = pressed[K_w]
        left = pressed[K_a]
        right = pressed[K_d]
        down = pressed[K_s]
        if self.right == True:
            self.image = player_right_anim[int(self.current_sprite)]
            #print(self.rect.x,self.rect.y)
            self.current_sprite += 0.1
            if self.current_sprite >= len(player_back_anim):
                self.current_sprite = 0
        if self.left == True:
            self.image = player_left_anim[int(self.current_sprite)]
            self.current_sprite += 0.1
            if self.current_sprite >= len(player_back_anim):
                self.current_sprite = 0
        if self.back == True:
            self.image = player_back_anim[int(self.current_sprite)]
            self.current_sprite += 0.1
            if self.current_sprite >= len(player_back_anim):
                self.current_sprite = 0
        if self.straight == True:
            self.image = player_str_anim[int(self.current_sprite)]
            self.current_sprite += 0.1
            if self.current_sprite >= len(player_back_anim):
                self.current_sprite = 0
        

        if up:
            self.back = True
            self.left = False
            self.right = False
            self.straight = False
            self.move(0,-5)
            

            
           
            
            
            

        if left:
            self.left = True
            self.back = False
            self.straight = False
            self.right = False
            self.move(-5,0)
           

        if right:
            self.right = True
            self.left = False
            self.straight = False
            self.back = False
            
            self.move(5,0)
            
        if down:
            
            self.straight = True
            self.left = False
            self.back = False
            self.right = False
            self.move(0,5)
            
        
       
        
        #print(self.vel.y)
        if not(left or right):
            self.right = False
            self.left = False
            
            self.move(0,0)
        if not(down or up):
            self.straight = False
            
            self.back = False
            self.move(0,0)
       
    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0,platforms)
        if dy != 0:
            self.move_single_axis(0,dy,platforms)

        
        
       
    def move_single_axis(self,dx,dy,platforms):
        self.rect.x += dx
        self.rect.y += dy

        for p in platforms:
            if self.rect.colliderect(p):
                if dx > 0:
                    self.rect.right = p.rect.left
                if dx < 0:
                    self.rect.left = p.rect.right
                if dy > 0:
                    self.rect.bottom = p.rect.top
                if dy < 0:
                    self.rect.top = p.rect.bottom
    def get_damage(self,amount):
        if self.hp > 0:
            self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
    




class Mob(Entity):
    def __init__(self,platforms,pos,player,world,*groups):
        super().__init__(Color("#0000FF"), pos)
        self.speed = 5
        self.mobalive = True
        self.expa = 'sadas'
        self.mob_list = []
        
        self.hit = False
        
        
        self.player = player
        self.platforms = platforms
       
       
        self.world = world
        self.image = idk_mob
        
        print(len(MAPS['MAP1'][0]))
        print(len(MAPS['MAP1'][1]))

        
    def update(self):
        self.speed = settings['mobs_speed']
        distance = ((self.player.rect.x - self.rect.x)**2 + (self.player.rect.y - self.rect.y)**2)**0.2
        notmdist = round(distance)
        
        
        

        if self.mobalive == True:
            dirvect = Vector2(self.player.rect.x - self.rect.x,self.player.rect.y - self.rect.y)    
            dirvect.normalize() 
            dirvect.scale_to_length(self.speed)
            self.rect.move_ip(dirvect)
            self.collide(self.player)
        if self.player.rect.x > self.rect.x:
            self.image = idk_mobanim
        else:
            self.image = idk_mob
        if self.player.rect.y < self.rect.y and self.player.rect.x > self.rect.x:
            self.image = idk_mob_up
    


        
        



        
        



        
        
        #to_move = distance - 1
        #speed = 5
        #self.rect.x -= to_move 
        #self.rect.y -= to_move
        #if distance == 2:
        #    distance = 0
    def do_hit(self):
        self.hit = True
        if self.rect.x > self.player.rect.x:
            self.rect.x += 100
        if self.rect.x < self.player.rect.x:
            self.rect.x -= 100
        if self.rect.y > self.player.rect.y:
            self.rect.y += 100
        if self.rect.y < self.player.rect.y:
            self.rect.y -= 100
            
        
    def collide(self,player):
        if self.mobalive == True:
            if self.rect.colliderect(player):
                self.do_hit()
                self.player.get_damage(0.5)
                
class Gun1(Entity):
    def __init__(self,player,pos,*groups):
        super().__init__(Color("#0000FF"),pos)
        self.player = player
        self.current_sprite = 0
        
        self.is_enabled = False
       
        
        

        
        #if self.trigger:
        #    self.shoot()
            
    def change_pic(self):
        if self.is_enabled == True:
        
            player_right_anim.clear()
            player_right_anim.append(pygame.image.load(abs_images + 'player_right_anim1_gun1.png'))
            player_right_anim.append(pygame.image.load(abs_images + 'player_right_gun1.png'))
            player_right_anim.append(pygame.image.load(abs_images + 'player_right_anim2_gun1.png'))

            player_left_anim.clear()
            player_left_anim.append(pygame.image.load(abs_images +'player_left_anim1_gun1.png'))
            player_left_anim.append(pygame.image.load(abs_images +'player_left_gun1.png'))
            player_left_anim.append(pygame.image.load(abs_images +'player_left_anim2_gun1.png'))

            player_str_anim.clear()
            player_str_anim.append(pygame.image.load(abs_images +'player_str_anim1_gun1.png'))
            player_str_anim.append(pygame.image.load(abs_images +'player_straight_gun1.png'))
            player_str_anim.append(pygame.image.load(abs_images +'player_str_anim2_gun1.png'))

            player_back_anim.clear()
            player_back_anim.append(pygame.image.load(abs_images + 'player_back_anim1_gun1.png'))
            player_back_anim.append(pygame.image.load(abs_images + 'player_back_gun1.png'))
            player_back_anim.append(pygame.image.load(abs_images + 'player_back_anim2_gun1.png'))


class Bullets(pygame.sprite.Sprite):
    def __init__(self,player,pos,mob,mob1,*groups):
        super().__init__()
        self.player = player
        self.mob = mob
        self.mob1 = mob1
        
        self.image = Surface((TILE_SIZE, TILE_SIZE)).convert_alpha()
        self.image.fill((0,0,255))
        self.p_x = self.player.rect.x
        self.p_y = self.player.rect.y
        self.rect = self.image.get_rect(topleft = pos)
        self.to_right = False
        self.to_left = False
        self.to_up = False
        self.to_down = False
        self.speed = 10
    
        

        
        
       
        
    def update(self):
        if self.to_right == True:
            self.rect.x += self.speed
        if self.to_left == True:
            self.rect.x -= self.speed
        if self.to_up == True:
            self.rect.y -= self.speed
        if self.to_down == True:
            self.rect.y += self.speed


        if self.rect.colliderect(self.mob1.rect):
            entities.remove(self.mob1)
            entities.remove(self)
            
            heal_list.append(Heart_expa((self.mob1.rect.x,self.mob1.rect.y),self.player))
            #self.mob1.mobalive = False

            
        if self.rect.colliderect(self.mob.rect):
            entities.remove(mob)
            entities.remove(self)
            heal_list.append(Heart_expa((self.mob.rect.x,self.mob.rect.y),self.player))
            
            #self.mob.mobalive = False
            


class Heart_expa(pygame.sprite.Sprite):
    def __init__(self,pos,player,*groups):
        super().__init__()
        self.player = player
        self.image = heart_expa_im
        self.rect = self.image.get_rect(topleft = pos)
        self.count = 0
        
        
        
        

    def update(self):
        
        self.count += 0.1
        if self.count >= len(heart_expa_anim):
            self.count = 0
        self.image = heart_expa_anim[int(self.count)]
       
        if self.player.rect.colliderect(self.rect):
            entities.remove(self)
            heal_list.remove(self)
            self.player.hp += 1
    

        


        

        
            
    
    

       

    
        
        

        

        
class CameraView(pygame.sprite.LayeredUpdates):
    def __init__(self,target,gun1,world_size):
        super().__init__()
        self.target = target
        
        
        
        self.cam = pygame.Vector2(0,0)
        self.world_size = world_size
        
        if self.target:
            self.add(target)

        
            
                
        
        


    def update(self,*args):
        super().update(*args)
        if self.target:
            x = -self.target.rect.center[0] + SCREEN_SIZE.width/ 2
            y = -self.target.rect.center[1] + SCREEN_SIZE.height/ 2
            self.cam += (pygame.Vector2((x,y)) - self.cam) * 0.05
            self.cam.x = max(-(self.world_size.width-SCREEN_SIZE.width), min(0, self.cam.x))
            self.cam.y = max(-(self.world_size.height-SCREEN_SIZE.height), min(0, self.cam.y))
        
   




    def draw(self, surface):
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        init_rect = self._init_rect
        
        for spr in self.sprites():
            rec = spritedict[spr]
            newrect = surface_blit(spr.image, spr.rect.move(self.cam))
            
            
            
            if rec is init_rect:
                
                dirty_append(newrect)
            else:
                if newrect.colliderect(rec):
                    dirty_append(newrect.union(rec))
                else:
                    dirty_append(newrect)
                    dirty_append(rec)
            spritedict[spr] = newrect
        return dirty            
class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0
        self.level_which = 0
        self.setting_is = 0
        self.easy = 0 
        self.hard = 0
        self.medium = 0
        
        
        self.switchsound = pygame.mixer.Sound(abs_music + 'switchsound.mp3')
        self.selectsound = pygame.mixer.Sound(abs_music + 'selectsound.mp3')
    def idk(self):
        self.level_which = 1
    def to_settings(self):
        self.setting_is = 1
    def to_easy(self):
        self.easy = 1
    def to_medium(self):
        self.medium = 1
    def to_hard(self):
        self.hard = 1
    
        
        

    def append_option(self,option,callback):
        
        self._option_surfaces.append(font.render(option,True,(255,255,255)))
        self._callbacks.append(callback)
      
    def switch(self,direction):
        self._current_option_index = max(0,min(self._current_option_index + direction,len(self._option_surfaces)- 1))
        self.switchsound.play()

    def select(self):
        self._callbacks[self._current_option_index]()
        self.selectsound.play()
    
    def draw(self,surf,x,y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x ,y + i * option_y_padding)
            if i == self._current_option_index:
                pygame.draw.rect(surf,(255,255,0),option_rect)
            surf.blit(option,option_rect)

  
platforms = pygame.sprite.Group()
player = Player(platforms, (TILE_SIZE, TILE_SIZE))


gun1 = Gun1(player,(player.rect.x,player.rect.y))
def add_to_screen(mobsome,group):
    group.add(mobsome)


player.update()
level_width  = len(MAPS['MAP1'][0])*TILE_SIZE
level_height = len(MAPS['MAP1'])*TILE_SIZE
entities = CameraView(player,gun1,pygame.Rect(0, 0, level_width, level_height))



class Platform(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#DDDDDD"), pos, *groups)



x = y = 0
for row in MAPS['MAP1']:
    for col in row:
        if col == "1":
            Platform((x,y), entities,platforms)
        if col == 'p':
            player.rect.x = x
            player.rect.y = y   
        if col == 'm':
            mob = Mob(platforms,(x,y),player,MAPS['MAP1'])
            
            
            #mobs.add(mob)
            entities.add(mob)
        if col == 'M':
            mob1 = Mob(platforms,(x,y),player,MAPS['MAP1'])
            #mobs.add(mob1)
            
            entities.add(mob1)
            
            
            
            
        
            
        
        x += TILE_SIZE  
    y += TILE_SIZE
    x = 0
