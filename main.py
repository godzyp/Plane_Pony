import pygame
import time
import sys
import os
from random import randint
from plane_class import plane
from plane_class import twilight_Sparkle
from enemy_class import enemy
from enemy_class import changeling_hitter


class Enemy_Node:

    def __init__(self,Enemy_Type,Time_To_Show):
         self.Enemy = Enemy_Type
         self.Time_Stamp = Time_To_Show
         #self.Top_Left = Position


class Bullet(pygame.sprite.Sprite):
    def __init__(self,bullet_surface,bullet_init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=bullet_surface
        self.rect=self.image.get_rect()
        self.rect.midtop=bullet_init_pos
        self.speed=8

    def update(self):
        self.rect.top-=self.speed
        if self.rect.top<-self.rect.height:
            self.kill()


##############################################################################################################################################
##############################################################################################################################################

def window_init():
    global screen
    global ticks
    global frame_rate
    global clock
    global screen_width
    global screen_height
    global Game_Interface
    global button_count
    global main_screen_buttons
    global main_screen_background
    global n
    pygame.init()                                                                                           #pygame初始化
    pygame.mixer.init()
    n=0
    ticks=30
    frame_rate=60               #固定帧率(FPS)
    clock=pygame.time.Clock()   #构建并返回时间对象P
    screen_height=800                                                                                       #游戏窗口像素高度
    screen_width=1080                                                                                       #游戏窗口像素宽度
    os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d"%(350,30)                                                     #调整屏幕相对位置(LEFT,TOP)
    #pygame.display.set_icon()                                                                              #更改窗口图标
    pygame.display.set_caption("Plane_Pony")                                                                #更改窗口标题
    screen=pygame.display.set_mode([screen_width,screen_height])                                            #显示屏幕
    main_screen_background=pygame.image.load(os.path.join('./image\Image1.png'))                            #加载主界面背景图片
    screen.blit(main_screen_background,(0,0))                                                               #绘制主界面背景(image,[LEFT,TOP])

    main_screen_buttons=[]                                                                                  #按钮图片容器
    for i in range(0,5):                                                                                    #i==width
        for j in range(0,2):                                                                                #j==height
            #TODO
            main_screen_buttons.append(pygame.image.load(os.path.join('./image\Image1.png')).convert_alpha().subsurface(pygame.Rect(j*230,i*60,230,60)))
            #加载按钮图片(pw460*ph480)
            #子表面裁剪(subsurface)图片(Rect(left, top, width, height))
    screen.blit(main_screen_buttons[0],(800,300))                                                           #(start)
    screen.blit(main_screen_buttons[2],(800,390))                                                           #(guide)
    screen.blit(main_screen_buttons[4],(800,480))                                                           #(optionls)
    screen.blit(main_screen_buttons[6],(800,570))                                                           #(manual)
    screen.blit(main_screen_buttons[8],(800,670))                                                           #(quit)

    Game_Interface=1            #当前所处界面计数器(global)
    button_count=[0,0,0,0,0]
    '''
    按钮点击标记,[0](主界面:main_screen)=1(start),2(guide),3(optionls),4(manual),5(quit)
    '''
    #pygame.mouse.set_cursor     #设置初始鼠标图标                                                   
    #pygame.mouse.set_pos(500,500)#设置初始鼠标坐标(LEFT,TOP)
    
def plane_game_init():
    global offset
    global enemy_group
    global enemy_down_group
    global plane_image
    global Player
    global plane_game_screen_background

    global bullet_image
    global plane_surface
    global bullet1_surface

    offset={pygame.K_LEFT:0,pygame.K_RIGHT:0,pygame.K_UP:0,pygame.K_DOWN:0,pygame.K_z:0,pygame.K_x:0}                    #操作字典集
    
    plane_game_screen_background=pygame.image.load(os.path.join('./image\\background.png')).convert_alpha()

    enemy_group=pygame.sprite.Group()
    enemy_down_group=pygame.sprite.Group()

    Player=twilight_Sparkle.Twilight_Sparkle(screen,[500,300])                        #创建实例对象

    bullet_image=pygame.image.load(os.path.join('./image\Bullet1.png')).convert_alpha()
    bullet1_surface=bullet_image.subsurface(pygame.Rect(0,0,13,16))
    

def game_main():
    enemy_list = []

    enemy_list.append(Enemy_Node(changeling_hitter.Changeling_Hitter(screen,[200 + 40,10]),100))
    enemy_list.append(Enemy_Node(changeling_hitter.Changeling_Hitter(screen,[-200 + 1080 -40,10]),100))

    enemy_list.append(Enemy_Node(changeling_hitter.Changeling_Hitter(screen,[300 + 40,10]),120))
    enemy_list.append(Enemy_Node(changeling_hitter.Changeling_Hitter(screen,[-300 + 1080 -40,10]),120))

    enemy_list.append(Enemy_Node(changeling_hitter.Changeling_Hitter(screen,[400 + 40,10]),140))
    enemy_list.append(Enemy_Node(changeling_hitter.Changeling_Hitter(screen,[-400 + 1080 -40,10]),140))

    Which_Enemy = 0
    while True:
        global ticks
        global n
        ticks+=1
        clock.tick(frame_rate)                                              #固定程序循环运行次数并返回一次时间(毫秒)
        screen.blit(main_screen_background,(0,0))                           #绘制屏幕
        screen.blit(Player.image,Player.rect)                               #绘制Player
        screen.blit(plane_game_screen_background,(0,-3400+n+screen_height)) #滚动地图

        if ticks%50<20:                                                     #玩家动画
            Player.image=Player.plane_surface[0]
        else:
            Player.image=Player.plane_surface[1]
        screen.blit(Player.image,Player.rect)

        if offset[pygame.K_z]==1:                                           #发射子弹
            if Player.bullet_spacing==1 or Player.bullet_spacing%10==0:
                Player.single_shoot(bullet1_surface)
                pygame.mixer.music.load(os.path.join('./image\Ts.laser.ogg'))
                pygame.mixer.music.play(loops=1)
                pygame.mixer.music.set_volume(0.05)
            Player.bullet_spacing+=1

        #if ticks%30==0:                                                     #随机敌人刷新
            #enemy=Enemy(enemy_down_surface[0],[randint(0,screen_width-enemy_down_surface[0].get_width()),randint(0,enemy_down_surface[0].get_height())])
        
        print(Which_Enemy)
        while Which_Enemy < len(enemy_list) :
            if ticks == enemy_list[Which_Enemy].Time_Stamp :
                enemy_group.add(enemy_list[Which_Enemy].Enemy)
                Which_Enemy += 1
            else:
                break
        
        #enemy_group.add(enemy_list[Which_Enemy].Enemy)

        enemy_group.update()
        enemy_group.draw(screen)

        Player.bullets.update()
        Player.bullets.draw(screen)

        enemy_down_group.add(pygame.sprite.groupcollide(enemy_group,Player.bullets,True,True,pygame.sprite.collide_mask))   #敌人击杀
        Player_down=pygame.sprite.spritecollide(Player,enemy_group,True,pygame.sprite.collide_mask)                         #玩家死亡
        
        for enemy_down in enemy_down_group:
            screen.blit(enemy_down.surface[enemy_down.down_index],enemy_down.rect)

            if ticks%15==0:                         #敌人死亡动画
                if enemy_down.down_index<3:
                    enemy_down.down_index+=1
                else:
                    enemy_down_group.remove(enemy_down)

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_z:         #触发动作事件
                    offset[event.key]=1
                elif event.key == pygame.K_x:       #触发技能动作事件
                    offset[event.key]=2
                elif event.key in offset:           #触发移动事件
                    offset[event.key]=Player.speed                                           #移动像素距离
            elif event.type==pygame.KEYUP:          #松键事件
                if event.key == pygame.K_z:         #触发动作事件
                    offset[event.key]=0
                elif event.key == pygame.K_x:       #触发技能动作事件
                    offset[event.key]=1
                elif event.key in offset:           #触发移动事件
                    offset[event.key]=0
            if event.type == pygame.QUIT:                                                     #触发退出事件程序关闭
                pygame.quit()
                exit()
                
        n+=5
        if (-3400+n+screen_height)>0:
            n=0
            
        if len(Player_down)>0:
            break

        Player.update(offset)                                                                 #Player状态更新
        pygame.display.update()                                                               #屏幕刷新

def main_screen_button_clicked(mouse_pos,Interface,mouse_event):
    '''
    模拟鼠标点击按钮效果
    形参(鼠标指针坐标，当前所处界面，鼠标状态(1:MOUSEBUTTONDOWN; 2:MOUSEBUTTONUP))
    1:主界面; 2:游戏界面 3:
    '''
    global Game_Interface
    global button_count
    if Interface==1:                                                                                    #当前所处界面为 主界面:main_screen
        if mouse_event==2:                                                                              #MOUSEBUTTONUP触发事件
            if button_count[0]==1:
                screen.blit(main_screen_buttons[0],(800,300))
            if button_count[0]==2:
                screen.blit(main_screen_buttons[2],(800,390))
            if button_count[0]==3:
                screen.blit(main_screen_buttons[4],(800,480))
            if button_count[0]==4:
                screen.blit(main_screen_buttons[6],(800,570))
            if button_count[0]==5:
                screen.blit(main_screen_buttons[8],(800,670))
        if mouse_pos[0]>800 and mouse_pos[0]<1030 and mouse_pos[1]>300 and mouse_pos[1]<360:
            if mouse_event==1:                                                                         #MOUSEBUTTONDOWN触发事件
                button_count[0]=1
                screen.blit(main_screen_buttons[1],(800,300))
            if mouse_event==2:                                                                         #跳转界面至游戏界面
                Game_Interface=2    
        if mouse_pos[0]>800 and mouse_pos[0]<1030 and mouse_pos[1]>390 and mouse_pos[1]<450:
            if mouse_event==1:
                button_count[0]=2
                screen.blit(main_screen_buttons[3],(800,390))
        if mouse_pos[0]>800 and mouse_pos[0]<1030 and mouse_pos[1]>480 and mouse_pos[1]<540:
            if mouse_event==1:
                button_count[0]=3
                screen.blit(main_screen_buttons[5],(800,480)) 
        if mouse_pos[0]>800 and mouse_pos[0]<1030 and mouse_pos[1]>570 and mouse_pos[1]<630:
            if mouse_event==1:
                button_count[0]=4
                screen.blit(main_screen_buttons[7],(800,570)) 
        if mouse_pos[0]>800 and mouse_pos[0]<1030 and mouse_pos[1]>660 and mouse_pos[1]<720:
            if mouse_event==1:
                button_count[0]=5
                screen.blit(main_screen_buttons[9],(800,670))


##############################################################################################################################################
##############################################################################################################################################


window_init()
while True:                                                                                             #游戏进程主函数
    if Game_Interface==1:                   #主界面
        while True:
            if Game_Interface != 1:                                                                     #页面切换
                break
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:                                                #MOUSEBUTTONUP==6||MOUSEBUTTONDOWN==5
                    main_screen_button_clicked(pygame.mouse.get_pos(),Game_Interface,1)                 #鼠标点击按钮触发按钮DOWN动画效果
                if event.type == pygame.MOUSEBUTTONUP:
                    main_screen_button_clicked(pygame.mouse.get_pos(),Game_Interface,2)                 #鼠标点击按钮触发按钮UP动画效果
                if event.type == pygame.QUIT:                                                           #触发退出事件程序关闭
                    pygame.quit()
                    exit()
            pygame.display.update()                                                                     #屏幕刷新
    if Game_Interface==2:                   #游戏界面
        plane_game_init()                   #游戏初始化
        game_main()
        
        

