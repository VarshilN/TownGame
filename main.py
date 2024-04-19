import pygame
import Mission_1.mission_1
import sys
import Mission_1.utils
import Mission_2.mission_2
import Mission_2.utils1
import Mission_3.utils2
import Mission_3.mission_3
import MenuButtons.menu
# import mission_2
def main():
    pygame.init()
    WIDTH, HEIGHT = 1920,1080
    screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Greenerie Rescue: The Mayor's Mission")
    current_mission = 1# Start with mission 1
    game_paused=False
    M1=0
    START=0
    M2=-1
    M3=-1
    costs=0
    coins1=0
    costs2=0
    costs1=0
    running = True
    utils=Mission_1.utils
    utils1=Mission_2.utils1
    utils2=Mission_3.utils2
    mission_1=Mission_1.mission_1
    mission_2=Mission_2.mission_2
    mission_3=Mission_3.mission_3
    menu = MenuButtons.menu
    # start_time=pygame.time.get_ticks()
    coins=100
    #time programm started 
    PUB1=0
    ENV1=0
    while running:
        if game_paused:
            m=menu.menu(screen)
            if(m==1):
                game_paused=False
            elif(m==-1):
                game_paused=False
                M1=0
                current_mission=1
                START=0
                utils.c1=0
                utils.c2=0
                utils.c3=0
                utils.c4=0
                utils.c5=0
                utils.c7=0
                utils.c8=0
                utils.c6=0
                utils1.c1=0
                utils1.c2=0
                utils1.c3=0
                utils1.c4=0
                utils1.c5=0
                utils1.c7=0
                utils1.c8=0
                utils1.c6=0
                utils2.c1=0
                utils2.c2=0
                utils2.c3=0
                utils2.c4=0
                utils2.c5=0
                utils2.c7=0
                utils2.c8=0
                utils2.c6=0
                coins=100
                costs=0
                costs1=0
                costs2=0
                utils1.PUB1=0
                utils1.ENV1=0
                utils2.PUB1=0
                utils2.ENV1=0
                utils1.PUB=0
                utils1.CON=0
                utils1.ENV=0
                
                M2=-1
                M3=-1
        elif current_mission == 1:    
            mission_1.run(screen,START,M1,coins,costs)
            # utils.menu_btn.draw(screen)
            # Check completion utils1.ditions for mission 1
            if mission_1.is_completed(M1):
                current_mission = 2  # Move to mission 2 
                M2=0
                M1=-1
        elif current_mission==2:
            mission_2.run(screen,M2,coins,costs,costs1)
            if mission_2.is_completed(M2):
                current_mission=3
                M3=0
                M2=-1
        elif current_mission==3:
            mission_3.run(screen,M3,coins,costs,costs1)
            if mission_3.is_completed(M3):
                current_mission=4
                M3=-1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if utils.menu_btn.draw(screen) or utils1.menu_btn.draw(screen) or utils2.menu_btn.draw(screen):
                    game_paused=True
                elif START==0:
                    if(utils.start_btn.draw(screen)):
                        START=1
                elif START==1:
                    if(utils.enter_btn.draw(screen)):
                        START=2
                    elif(utils.back_btn.draw(screen)):
                        START=0
                elif START==2:
                    if(utils.mission_btn.draw(screen)):
                        START=3
                        M1=1
                    elif(utils.quit_btn.draw(screen)):
                        START=1
                elif M1==1:
                    if utils.skip_btn.draw(screen):
                        utils.c1+=1
                    elif utils.next_btn1.draw(screen):
                        M1=2             
                elif M1==2:
                    if utils.next_btn1.draw(screen):
                        M1=3
                elif M1==3:
                    if utils.skip_btn.draw(screen):
                        utils.c2+=1
                    elif utils.next_btn1.draw(screen):
                        M1=4
                elif M1==4:
                    if(utils.next_btn1.draw(screen)):
                        M1=5
                elif M1==5:           
                    if utils.o1_btn.draw(screen):
                        M1=6     
                        coins1=20  
                        utils1.PUB1=15 
                        costs2=5           
                    elif utils.o2_btn.draw(screen):
                        M1=14
                        coins1=50
                        utils1.PUB1=40
                        costs2=10
                    elif utils.visit_env_btn.draw(screen):
                        M1=15
                    elif utils.skip_btn.draw(screen):
                        if utils.c3==0:
                            utils.c3+=1
                        elif utils.c3==2:
                            M1=12
                    elif utils.o3_btn.draw(screen):
                        coins-=70
                        utils1.PUB1=55
                        costs+=15
                        costs=15
                        utils.c3+=1
                elif M1==6:
                    if utils.next_btn1.draw(screen):
                        M1=7
                elif M1==7:
                    if utils.con_sev_btn.draw(screen):
                        M1=8
                    elif utils.skip_btn.draw(screen):
                        utils.c4+=1
                elif M1==8:
                    if utils.skip_btn.draw(screen):
                        utils.c5+=1
                    elif utils.c1_btn.draw(screen):
                        M1=9
                    elif utils.c2_btn.draw(screen):
                        M1=10
                        coins= coins-5-coins1
                        costs=5+costs2
                    elif utils.c3_btn.draw(screen):
                        M1=11
                        coins= coins-10-coins1
                        costs = 10+costs2
                    elif utils.c4_btn.draw(screen):
                        M1=11
                        coins= coins-20-coins1
                        costs = 20+costs2
                    elif utils.back_btn1.draw(screen):
                        M1=5
                elif M1==9:
                    if utils.back_btn1.draw(screen):
                        M1=8
                elif M1==10:
                    if utils.next_btn1.draw(screen):
                        M1=12
                elif M1==11:
                    if utils.next_btn1.draw(screen):
                        M1=12
                elif M1==12:
                    if utils.next_btn1.draw(screen):
                        M1=13
                elif M1==13:
                    if utils.next_btn1.draw(screen):
                        M1=-1
                elif M1==14:
                    if utils.skip_btn.draw(screen):
                        utils.c6+=1
                    elif utils.visit_env_btn.draw(screen):
                        M1=15
                elif M1==15:
                    if utils.skip_btn.draw(screen):
                        utils.c7+=1
                    elif utils.env_next_0.draw(screen):
                        M1=16
                elif M1==16:
                    if utils.next_btn1.draw(screen):
                        M1=17
                elif M1==17:
                    if utils.skip_btn.draw(screen):
                        utils.c8+=1
                    elif utils.e1_btn.draw(screen):
                        utils.c8=2
                        utils1.ENV1=10
                        costs=10+costs2
                        coins=coins-20-coins1
                    elif utils.e2_btn.draw(screen):
                        utils.c8+=1
                        utils1.ENV1=15                      
                        costs=15+costs2
                        coins=coins-30-coins1
                    elif utils.e3_btn.draw(screen):
                        utils.c8=2              
                        costs= 20+costs2
                        utils1.ENV1=20
                        coins= coins-40-coins1
                    elif utils.back_btn1.draw(screen):
                        M1=5
                    elif utils.next_btn1.draw(screen):
                        M1=12
                if M2==0:
                        if utils1.mission_btn.draw(screen):
                            M2=1
                        elif utils1.quit_btn.draw(screen):
                            pygame.quit()
                            sys.exit()
                elif M2==1:
                        if(utils1.m2_btn.draw(screen)):
                            M2=2
                        elif utils1.skip_btn.draw(screen):
                            utils1.c1+=1
                        elif utils1.ask_btn3.draw(screen) and utils1.c1==4:
                            utils1.c1=5
                        elif utils1.ask_btn4.draw(screen) and utils1.c1==4:
                            utils1.c1=6
                        elif utils1.back_btn1.draw(screen) and (utils1.c1==5 or utils1.c1==6):
                            utils1.c1=4
                elif M2==2:
                        if utils1.next_btn1.draw(screen):
                            if utils1.PUB1==15:
                                M2=3
                            elif utils1.PUB1==55:
                                M2=4                      
                            elif utils1.PUB1==0:
                                M2=5
                        elif utils1.visit_env1.draw(screen):
                            if utils1.PUB1==40:
                                utils1.ENV=1
                                M2=6
                        elif utils1.visit_pub.draw(screen):
                            if utils1.PUB1==40:
                                utils1.PUB=1
                                M2=8
                        elif utils1.skip_btn.draw(screen):
                            utils1.c2+=1
                elif M2==3:
                        if utils1.visit_env.draw(screen):
                            M2=6
                            utils1.ENV=2
                        elif utils1.con_sev.draw(screen):
                            M2=7
                            utils1.CON=1
                elif M2==4:
                        if utils1.skip_btn.draw(screen):
                            utils1.c3+=1
                        if utils1.visit_env.draw(screen):
                            M2=6
                            utils1.ENV=3
                        elif utils1.con_sev.draw(screen):
                            M2=7
                            utils1.CON=2
                        elif utils1.continue_btn.draw(screen):
                            costs1=30
                            utils2.PUB1=25
                            utils2.ENV1=0
                            M2=20
                        elif utils1.ask_btn4.draw(screen):
                            utils1.c3=2
                        elif utils1.back_btn.draw(screen):
                            utils1.c3=1
                elif M2==5:#budget 0 
                        if(utils1.skip_btn.draw(screen)):
                            if utils1.c4==0:
                                utils1.c4+=2
                        if utils1.visit_pub.draw(screen):
                            M2=8
                            utils1.PUB=2
                        elif utils1.con_sev.draw(screen):
                            M2=7
                            utils1.CON=3
                        elif utils1.ask_btn4.draw(screen):
                            utils1.c4=1
                        elif utils1.back_btn1.draw(screen):
                            utils1.c4=2   
                elif M2==6:
                        if utils1.skip_btn.draw(screen):
                            utils1.c5+=1
                        elif utils1.ask_btn4.draw(screen):
                            utils1.c5=3
                        elif utils1.ask_btn3.draw(screen) and utils1.c5==2:
                            if utils1.ENV==1:
                                M2=9
                            elif utils1.ENV==2:
                                M2=10
                            elif utils1.ENV==3:
                                M2=10
                        elif utils1.back_btn.draw(screen):
                            if utils1.ENV==1:
                                M2=2
                            elif utils1.ENV==2:
                                M2=3
                            elif utils1.ENV==3:
                                M2=4
                        elif utils1.back_btn1.draw(screen) and utils1.c5==3:
                            utils1.c5=2
                elif M2==7:
                        if utils1.next_btn2.draw(screen):
                            if  utils1.CON==1:
                                M2=11
                            elif utils1.CON==2:
                                M2=12
                            elif utils1.CON==3:
                                M2=13      
                            elif utils1.CON==4:
                                M2=19                         
                        elif utils1.back_btn1.draw(screen):
                            if utils1.CON==1:
                                M2=3
                            elif utils1.CON==2:
                                M2=4
                            elif utils1.CON==3:
                                M2=5
                            elif utils1.CON==4:
                                M2=15
                        elif utils1.skip_btn.draw(screen):
                            if utils1.c6==2:
                                utils1.c6+=2
                            else:
                                utils1.c6+=1
                        elif utils1.ask_btn3.draw(screen):
                            utils1.c6=3
                        elif utils1.back_btn.draw(screen):
                            utils1.c6=2
                elif M2==8:
                        if utils1.next_btn1.draw(screen):
                            if utils1.PUB==1:
                                M2=15
                            elif utils1.PUB==2:
                                M2=14   
                            elif utils1.PUB==3:
                                M2=15
                        elif utils1.skip_btn.draw(screen):
                            if utils1.c7==2:
                                utils1.c7+=2
                            else:
                                utils1.c7+=1   
                        elif utils1.back_btn.draw(screen):
                            utils1.c7=2
                        elif utils1.ask_btn4.draw(screen):
                            utils1.c7=3
                elif M2==9:
                        if utils1.visit_pub.draw(screen):
                            M2=8
                            utils1.PUB=3
                        elif utils1.back_btn2.draw(screen):
                            M2=2
                        elif utils1.skip_btn.draw(screen):
                            utils1.c8+=1
                elif M2==10:
                        if utils1.next_btn1.draw(screen):
                            if utils1.ENV==2:
                                M2=16
                            elif utils1.ENV==3:
                                M2=17
                elif M2==11: 
                        if utils1.m2c4.draw(screen):
                            utils2.PUB1=15
                            M2=20
                            costs1=20
                            coins-=20
                        elif utils1.m2c5.draw(screen):
                            utils2.PUB1=15
                            M2=20
                            costs1=30
                            coins-=30
                        elif utils1.m2c6.draw(screen):
                            utils2.PUB1=15
                            M2=20
                            costs1=40
                            coins-=40
                        elif utils1.back_btn2.draw(screen):
                            M2=3                       
                elif M2==12:
                        if utils1.m2e1.draw(screen):
                            M2=20
                            costs1=40
                            utils2.PUB1=25 
                            utils2.ENV1=0      
                            coins-=10
                        elif utils1.m2e2.draw(screen):
                            costs1=50
                            utils2.PUB1=25
                            utils2.ENV1=0
                            M2=20
                            coins-=20
                        elif utils1.m2e3.draw(screen):
                            M2=20
                            costs1=60
                            utils2.PUB1=25
                            utils2.ENV1=0
                            coins-=30
                        elif utils1.back_btn2.draw(screen):
                            M2=4
                elif M2==13:#contr service for 0
                        if utils1.m2c4.draw(screen):
                            if utils1.ENV1==10:
                                M2=20
                                utils2.ENV1=10
                                costs1+=0
                            elif utils1.ENV1==15:
                                M2=20
                                utils2.ENV1=10
                                costs1+=5
                            elif utils1.ENV1==20:
                                costs1+=10
                                M2==20
                                utils2.ENV1=10
                            costs1+=20
                            utils2.PUB1=0
                            coins-=20
                        elif utils1.m2c5.draw(screen):
                            if utils1.ENV1==10:
                                M2=20
                                utils2.ENV1=10
                                costs1+=0
                            elif utils1.ENV1==15:
                                M2=20
                                utils2.ENV1=10
                                costs1+=5
                            elif utils1.ENV1==20:
                                costs1+=10
                                M2==20
                                utils2.ENV1=10
                            costs1+=30
                            coins-=30
                            utils2.PUB1=0
                        elif utils1.m2c6.draw(screen):
                            if utils1.ENV1==10:
                                M2=20
                                utils2.ENV1=10
                                costs1+=0
                            elif utils1.ENV1==15:
                                M2=20
                                utils2.ENV1=10
                                costs1+=5
                            elif utils1.ENV1==20:
                                costs1+=10
                                M2==20
                                utils2.ENV1=10
                            utils2.PUB1=0
                            costs1+=40
                        elif utils1.back_btn2.draw(screen):
                            M2=5
                elif M2==14:
                        if utils1.next_btn2.draw(screen):
                            M2=18
                elif M2==15:
                        if utils1.con_sev.draw(screen):   
                            M2=7
                            utils1.CON=4
                        elif utils1.env_pub.draw(screen):
                            costs1=20
                            utils2.PUB1=20
                            if utils1.ENV1==10:
                                costs1+=utils1.ENV1
                                utils2.ENV1=0
                            elif utils1.ENV1==15:
                                costs1+=5
                                utils2.ENV1=10
                            elif utils1.ENV1==20:
                                costs1+=10
                                utils2.ENV1=10
                            M2=20
                        elif utils1.continue_btn.draw(screen):
                            costs1=20
                            utils2.PUB1=20
                            M2=20
                        elif utils1.back_btn.draw(screen):
                            M2=2
                elif M2==16:## env budget for pub=15
                        if utils1.m2e4.draw(screen):
                            utils2.PUB1=0
                            costs1=35
                            M2=20                   
                            utils2.ENV1=20
                            coins-=40
                        elif utils1.m2e5.draw(screen):
                            utils2.PUB1=0
                            costs1=40
                            M2=20              
                            utils2.ENV1=25
                            coins-=50
                        elif utils1.m2e6.draw(screen):
                            utils2.PUB1=0
                            costs1=45
                            M2=20
                            utils2.ENV1=30
                            coins-=60
                        elif utils1.back_btn2.draw(screen):
                            M2=3
                elif M2==17: #env budget for pub1=55               
                        if utils1.m2e1.draw(screen):
                            M2=20
                            costs1=40
                            coins-=10
                            utils2.PUB1=25
                            utils2.ENV1=0
                        elif utils1.m2e2.draw(screen):
                            M2=20
                            costs1=40
                            utils2.ENV1=10             
                            utils2.PUB1=25
                            coins-=20                    
                        elif utils1.m2e3.draw(screen):
                            M2=20
                            costs1=45
                            utils2.ENV1=15
                            utils2.PUB1=25
                            coins-=30       
                        elif utils1.back_btn2.draw(screen):
                            M2=4
                elif M2==18:#pub budget for 0
                        if utils1.p1.draw(screen):
                            if utils1.ENV1==10:
                                M2=20
                                utils2.ENV1=0
                                costs1+=utils1.ENV1
                            elif utils1.ENV1==15:
                                M2=20
                                utils2.ENV1=10
                                costs1+=5
                            elif utils1.ENV1==20:
                                costs1+=10
                                M2==20
                                utils2.ENV1=10
                            costs1+=20
                            utils2.PUB1=20
                            coins-=40
                        elif utils1.p2.draw(screen):
                            if utils1.ENV1==10:
                                M2=20
                                utils2.ENV1=0
                                costs1+=utils1.ENV1
                            elif utils1.ENV1==15:
                                M2=20
                                utils2.ENV1=10
                                costs1+=5
                            elif utils1.ENV1==20:
                                costs1+=10
                                M2==20
                                utils2.ENV1=10
                            costs1+=25   
                            coins-=50
                            utils2.PUB1=25
                        elif utils1.p3.draw(screen):
                            if utils1.ENV1==10:
                                M2=20
                                utils2.ENV1=0
                                costs1+=utils1.ENV1
                            elif utils1.ENV1==15:
                                M2=20
                                utils2.ENV1=10
                                costs1+=5
                            elif utils1.ENV1==20:
                                costs1+=10
                                M2==20
                                utils2.ENV1=10
                            costs1+=30
                            utils2.PUB1=30
                            coins-=60
                        elif utils1.back_btn2.draw(screen):
                            M2=2
                elif M2==19:
                        if utils1.m2c1.draw(screen):
                            costs1=20
                            utils2.PUB1=20
                            M2=20
                            utils2.ENV1=0
                            costs1+=5
                            coins-=5
                        elif utils1.m2c2.draw(screen):
                            costs1=20
                            utils2.PUB1=20
                            M2=20
                            utils2.ENV1=0
                            costs1+=10
                            coins-=10
                        elif utils1.m2c3.draw(screen):
                            costs1=20
                            utils2.PUB1=20
                            M2=20
                            utils2.ENV1=0
                            costs1+=15
                            coins-=15
                        elif utils1.back_btn2.draw(screen):
                            M2=2
                elif M2==20:
                    if utils1.next_btn1.draw(screen):
                        M2=-1
                elif M3==0:
                    if utils2.enter_btn.draw(screen):
                        M3=1
                    elif utils2.quit_btn.draw(screen):
                        pygame.quit()
                elif M3==1:
                    if utils2.enter_btn.draw(screen):
                        M3=2
                    elif utils2.skip_btn.draw(screen):
                        utils2.c1+=1
                elif M3==2:
                    if utils2.skip_btn.draw(screen):
                        utils2.c2+=1
                    elif utils2.ask_btn1.draw(screen):
                        M3=3
                    elif utils2.ask_btn2.draw(screen):
                        M3=4
                elif M3==3:
                    if utils2.skip_btn.draw(screen):
                        utils2.c3+=1
                    elif utils2.p1.draw(screen):
                        M3=5
                    elif utils2.back_btn.draw(screen):
                        M3=2
                elif M3==4:
                    if utils2.ask_btn3.draw(screen):
                        utils2.c4=1
                    elif utils2.ask_btn4.draw(screen):
                        utils2.c4=2
                    elif utils2.back_btn.draw(screen):
                        if utils2.c4==0:
                            M3=2
                        elif utils2.c4==1 or utils2.c4==2:
                            utils2.c4=0
                elif M3==5:
                    if utils2.skip_btn.draw(screen):
                        utils2.c5+=1
                    elif utils2.m3e1.draw(screen):
                        M3=6
                elif M3==6:
                    if utils2.skip_btn.draw(screen):
                        utils2.c6+=1
                    elif utils2.next_btn1.draw(screen):
                        utils2.c6+=1
                    elif utils2.visit_btn.draw(screen):
                        M3=7
                elif M3==7:
                    if utils2.skip_btn.draw(screen):
                        utils2.c7+=1
                    elif utils2.ask_btn1.draw(screen):
                        if utils2.c7==6:
                            utils2.c7+=1
                        elif utils2.c7==7:
                            M3=8
                elif M3==8:
                    if utils2.skip_btn.draw(screen):                  
                        utils2.c8+=1
                    elif utils2.continue_btn.draw(screen):
                        M3=9
                elif M3==9:
                    if utils2.res_btn.draw(screen):
                        M1=0
                        current_mission=1
                        START=0
                        utils.c1=0
                        utils.c2=0
                        utils.c3=0
                        utils.c4=0
                        utils.c5=0
                        utils.c7=0
                        utils.c8=0
                        utils.c6=0
                        utils1.c1=0
                        utils1.c2=0
                        utils1.c3=0
                        utils1.c4=0
                        utils1.c5=0
                        utils1.c7=0
                        utils1.c8=0
                        utils1.c6=0
                        utils2.c1=0
                        utils2.c2=0
                        utils2.c3=0
                        utils2.c4=0
                        utils2.c5=0
                        utils2.c7=0
                        utils2.c8=0
                        utils2.c6=0
                        coins=100
                        costs=0
                        costs1=0
                        costs2=0
                        utils1.PUB1=0
                        utils1.ENV1=0
                        utils2.PUB1=0
                        utils2.ENV1=0
                        utils1.PUB=0
                        utils1.CON=0
                        utils1.ENV=0            
                        M2=-1
                        M3=-1
                elif M2==-1:
                    M2=-2
                if M1!=-1:
                    utils.start_time=pygame.time.get_ticks()
                elif M2!=-1:
                    utils1.start_time=pygame.time.get_ticks()
                elif M3!=-1:
                    utils2.start_time=pygame.time.get_ticks()                  
            # pygame.display.update()
if __name__ == "__main__":
    main()
