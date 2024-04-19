import pygame
import sys
import math
import Mission_2.utils1
import MenuButtons.buttons
# Initialize Pygame
pygame.init()
def run(screen,M2,coins,costs0,costs):
    buttons=MenuButtons.buttons
    utils1=Mission_2.utils1
    if M2==0:
        screen.blit(utils1.background_1, (0, 0))
        overlay = pygame.Surface((1920, 1080), pygame.SRCALPHA)
        overlay.fill((0,0,0, 150))
        screen.blit(overlay, (0, 0))
        ##intro to assistant       
        screen.blit(utils1.assistent,(175,125))
        utils1.draw_dialog_box(screen,300,200,800,250,utils1.split_text(utils1.intro_dialog,800),10)
        utils1.top_row(screen,coins,costs0)
        utils1.mission_btn.draw(screen)
        utils1.quit_btn.draw(screen)
    elif M2==1: #show prev text 1 and 2
            WIDTH=800
            db_height=400  
            if utils1.c1==0:  
              screen.blit(utils1.m2i1, (0, 0))
              screen.blit(utils1.assistent,(0,0))
              utils1.draw_dialog_box(screen,125,75, WIDTH, db_height,utils1.split_text(utils1.prev_text1,800),10) 
              utils1.skip_btn.draw(screen)
            elif utils1.c1==1:
              screen.blit(utils1.m2i2, (0, 0))
              screen.blit(utils1.assistent,(0,0))
              utils1.top_row(screen,coins,costs0)
              utils1.draw_dialog_box(screen,125,75, WIDTH, db_height,utils1.split_text(utils1.prev_text2,800),10)
              utils1.skip_btn.draw(screen)
            elif utils1.c1==2:
              screen.blit(utils1.m2i2,(0,0))
              screen.blit(utils1.assistent,(0,0))
              utils1.draw_dialog_box(screen,125,75, 400, 200,utils1.split_text(utils1.visit_text,400),10)
              utils1.skip_btn.draw(screen)
            elif utils1.c1==3:
              screen.blit(utils1.m2d2,(0,0))
              screen.blit(utils1.tp1,(20,0))
              utils1.draw_dialog_box(screen,125,75, 400, 200,utils1.split_text(utils1.welcome_tp,400),10)
              utils1.skip_btn.draw(screen)
            elif utils1.c1==4:
              screen.blit(utils1.m2d2,(0,0))
              screen.blit(utils1.assistent,(0,0))
              utils1.draw_dialog_box(screen,125,75, 700, 200,utils1.split_text(utils1.assistent_tp,700),10)
              utils1.ask_box(screen,200,620,900,50,utils1.ask_op1,2)
              utils1.ask_box(screen,200,690,500,50,utils1.ask_op2,3)
            elif utils1.c1==5:
                screen.blit(utils1.m2d1,(0,0))
                screen.blit(utils1.tp1,(0,0))
                utils1.draw_dialog_box(screen,125,75, 700, 300,utils1.split_text(utils1.reply_tp1,700),10)
                utils1.m2_btn.draw(screen)
                utils1.back_btn1.draw(screen)
            elif utils1.c1==6:
                screen.blit(utils1.m2d1,(0,0))
                screen.blit(utils1.tp1,(0,0))
                utils1.draw_dialog_box(screen,125,75, 400, db_height,utils1.split_text(utils1.reply_tp2,400),10)
                utils1.back_btn1.draw(screen)
    elif M2==2:
        if utils1.PUB1==15 or utils1.PUB1==55:
            if  utils1.c2==0:
                    screen.blit(utils1.m2i2,(0,0))
                    screen.blit(utils1.assistent,(0,0))
                    utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.pub_visit,500),10)
                    utils1.skip_btn.draw(screen)
            elif utils1.c2==1:
                  screen.blit(utils1.m2p1, (0, 0))
                  screen.blit(utils1.pub_assistent,(30,20))              
                  utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.welcome_pub,500),10)
                  utils1.skip_btn.draw(screen)
            else: 
                screen.blit(utils1.m2p2, (0, 0))
                screen.blit(utils1.assistent,(0,0))             
                utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.ask_pub,500),10)
                utils1.next_btn1.draw(screen)
        elif utils1.PUB1==40:
            #chose to visit pub or env
            screen.blit(utils1.m2p1, (0, 0))
            screen.blit(utils1.assistent,(0,0))
            if pygame.time.get_ticks() - utils1.start_time < 5000:
              screen.blit(utils1.m2p1, (0, 0))         
              utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.prev_text3,500),10)
            else: 
              utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.prev_text3,500))
              utils1.visit_env1.draw(screen)
              utils1.visit_pub.draw(screen)
        elif utils1.PUB1==0:
            if utils1.c2==0:
              if pygame.time.get_ticks()-utils1.start_time<5000:
                  screen.blit(utils1.m2i2,(0,0))
                  screen.blit(utils1.assistent,(0,0))
                  utils1.draw_dialog_box(screen,125,75,400,200,utils1.split_text(utils1.env_visit,400),20)
              else:
                screen.blit(utils1.e1, (0, 0))
                screen.blit(utils1.env_assistent,(30,20))
                utils1.draw_dialog_box(screen,125,75,400,200,utils1.split_text(utils1.welcome_env,400),20)
                utils1.skip_btn.draw(screen)
            elif utils1.c2==1:
                screen.blit(utils1.e2, (0, 0))
                screen.blit(utils1.env_assistent,(30,20))
                utils1.draw_dialog_box(screen,125,75,700,300,utils1.split_text(utils1.reply_env01,700),20)
                utils1.skip_btn.draw(screen)
            elif utils1.c2==2:
              screen.blit(utils1.e2, (0, 0))
              screen.blit(utils1.assistent,(0,0))
              utils1.draw_dialog_box(screen,125,120,500,200,utils1.split_text(utils1.ask_env0,500),10)      
              utils1.next_btn1.draw(screen)            
    elif M2==3:### for PUB=15
            screen.blit(utils1.m2p2, (0, 0))
            screen.blit(utils1.pub_assistent,(30,20))
            if pygame.time.get_ticks() - utils1.start_time < 5000:
              utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.reply_pub01,500),10)
            else:
                  utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.reply_pub0,500))
                  utils1.con_sev.draw(screen)
                  utils1.visit_env.draw(screen)           
    elif M2==4:## for pub =55
            
            if utils1.c3==0:
              screen.blit(utils1.m2p2, (0, 0))
              screen.blit(utils1.pub_assistent,(0,0))
              utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.reply_env6,500),10)
              utils1.skip_btn.draw(screen)
            elif  utils1.c3==1:
              screen.blit(utils1.m2p2, (0, 0))
              screen.blit(utils1.pub_assistent,(0,0))
              utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.reply_pub3,500),10)
              utils1.ask_box(screen,200,690,700,50,utils1.ask_pub_op1,3) 
              utils1.visit_env.draw(screen)
              utils1.con_sev.draw(screen)
              utils1.continue_btn.draw(screen)
            elif utils1.c3==2:
                screen.blit(utils1.m2p1, (0, 0))
                screen.blit(utils1.pub_assistent,(0,0))
                utils1.draw_dialog_box(screen,125,75,700,400,utils1.split_text(utils1.reply_pub_op1,700),10)
                utils1.back_btn.draw(screen)
    elif M2==5:
          
          screen.blit(utils1.env_assistent,(30,20))
          if utils1.c4==0:
              screen.blit(utils1.e2,(0,0))
              if pygame.time.get_ticks()-utils1.start_time<5000:
                  utils1.draw_dialog_box(screen,125,120,500,200,utils1.split_text(utils1.reply_env6,500),10)
              else:
                screen.blit(utils1.e1,(0,0))
                utils1.draw_dialog_box(screen,125,120,500,200,utils1.split_text(utils1.reply_env9,500),10)
                utils1.skip_btn.draw(screen)
          elif utils1.c4==1:            
                utils1.draw_dialog_box(screen,125,120,700,400,utils1.split_text(utils1.reply_env_op2,700),10)
                utils1.back_btn1.draw(screen)
          else:
              screen.blit(utils1.e2,(0,0))
              utils1.draw_dialog_box(screen,125,120,500,200,utils1.split_text(utils1.reply_env7,500))
              utils1.ask_box(screen,200,690,500,50,utils1.ask_env_op2,3)
              utils1.visit_pub.draw(screen)
              utils1.con_sev.draw(screen)  
    elif M2==6:
            if utils1.c5==0:
              screen.blit(utils1.m2i2,(0,0))
              screen.blit(utils1.assistent,(0,0))
              utils1.draw_dialog_box(screen,125,120,400,200,utils1.split_text(utils1.env_visit,400),20)
              utils1.skip_btn.draw(screen)
            elif utils1.c5==1:
              screen.blit(utils1.e1, (0, 0))
              screen.blit(utils1.env_assistent,(30,20))
              utils1.draw_dialog_box(screen,125,120,400,200,utils1.split_text(utils1.welcome_env,400),20)
              utils1.skip_btn.draw(screen)
            elif utils1.c5==2:
                screen.blit(utils1.e1,(0,0))
                screen.blit(utils1.assistent,(0,0))
                utils1.draw_dialog_box(screen,125,120,700,400,utils1.split_text(utils1.ask_env0,700),10)
                utils1.ask_box(screen,200,620,700,50,utils1.ask_env_op1,2)
                utils1.ask_box(screen,200,690,500,50,utils1.ask_env_op2,3)
                utils1.back_btn.draw(screen)
            elif utils1.c5==3:
                screen.blit(utils1.e2,(0,0))
                screen.blit(utils1.env_assistent,(30,20))
                utils1.draw_dialog_box(screen,125,120,700,400,utils1.split_text(utils1.reply_env_op2,700),10)
                utils1.back_btn1.draw(screen)
    elif M2==7:
                if utils1.c6==0:
                  screen.blit(utils1.m2i1,(0,0))
                  screen.blit(utils1.assistent,(0,0))
                  utils1.draw_dialog_box(screen,125,75,400,200,utils1.split_text(utils1.con_visit,400),40)
                  utils1.skip_btn.draw(screen)
                elif utils1.c6==1:
                  screen.blit(utils1.cn1, (0, 0))
                  screen.blit(utils1.con_assistent,(30,20))
                  utils1.draw_dialog_box(screen,125,75,400,200,utils1.split_text(utils1.welcome_con,400),20)
                  utils1.skip_btn.draw(screen)
                elif utils1.c6==2:
                  screen.blit(utils1.cn2, (0, 0))
                  screen.blit(utils1.assistent,(0,0))
                  utils1.draw_dialog_box(screen,125,75,700,400,utils1.split_text(utils1.ask_con,700),10)
                  utils1.ask_box(screen,200,620,900,50,utils1.ask_con_op1,2)
                  utils1.skip_btn.draw(screen)
                elif  utils1.c6==3:
                  screen.blit(utils1.cn2, (0, 0))
                  screen.blit(utils1.con_assistent,(30,20))
                  utils1.draw_dialog_box(screen,125,75,700,400,utils1.split_text(utils1.reply_con_op1,700),10)   
                  utils1.back_btn.draw(screen)                       
                else:
                    screen.blit(utils1.cn2, (0, 0))  
                    screen.blit(utils1.con_assistent,(30,20))     
                    utils1.draw_dialog_box(screen,125,75,500,300,utils1.split_text(utils1.reply_con,500))                
                    utils1.next_btn2.draw(screen)
                    utils1.back_btn1.draw(screen)
    elif M2==8:
            if utils1.c7==0:
                screen.blit(utils1.m2p1, (0, 0))               
                utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.pub_visit,500),10)
                utils1.skip_btn.draw(screen)
            elif utils1.c7==1:
                screen.blit(utils1.m2p1, (0, 0))   
                screen.blit(utils1.pub_assistent,(30,20))             
                utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.welcome_pub,500),10)
                utils1.skip_btn.draw(screen)
            elif utils1.c7==2:               
                screen.blit(utils1.m2p1, (0, 0)) 
                screen.blit(utils1.pub_assistent,(30,20))                 
                utils1.draw_dialog_box(screen,125,75,700,400,utils1.split_text(utils1.reply_pub02,700),10)
                utils1.skip_btn.draw(screen)
            elif utils1.c7==3:
                screen.blit(utils1.m2p1, (0, 0))
                screen.blit(utils1.pub_assistent,(0,0))
                utils1.draw_dialog_box(screen,125,75,700,400,utils1.split_text(utils1.reply_pub_op1,700),10)
                utils1.back_btn.draw(screen)   
            else:
                screen.blit(utils1.m2p1, (0, 0))
                screen.blit(utils1.assistent,(0,0))               
                utils1.draw_dialog_box(screen,125,75,700,400,utils1.split_text(utils1.ask_con,700),10)
                utils1.ask_box(screen,200,690,700,50,utils1.ask_pub_op1,3) 
                utils1.next_btn1.draw(screen)
    elif M2==9:#reply env with pub=40
          screen.blit(utils1.e2,(0,0))
          screen.blit(utils1.env_assistent,(0,0))
          if  utils1.c8==0:
              utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.reply_env01,500),10)
              utils1.skip_btn.draw(screen)
          elif utils1.c8==1:
              if pygame.time.get_ticks()-utils1.start_time<5000:
                  utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.reply_env6,500),10)
              else:
                utils1.draw_dialog_box(screen,125,75,700,300,utils1.split_text(utils1.reply_env8,700),10)
                utils1.skip_btn.draw(screen)
          else:
                 utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.reply_env8,500))
                 utils1.visit_pub.draw(screen) 
                 utils1.back_btn2.draw(screen)
    elif M2==10: 
          screen.blit(utils1.e1, (0, 0))
          utils1.top_row(screen,coins,costs0)
          if pygame.time.get_ticks()-utils1.start_time<5000:
            utils1.draw_dialog_box(screen,125,75,700,400,utils1.split_text(utils1.reply_env0,700),10)
          else:
              utils1.draw_dialog_box(screen,125,75,700,400,utils1.split_text(utils1.reply_env0,700))
              utils1.next_btn1.draw(screen)
    elif M2==11: ## reply con for negotiate in case of pub=15
              utils1.top_row(screen,coins,costs0)
              screen.blit(utils1.cn2, (0, 0))       
              utils1.draw_dialog_box(screen,125,75,500,300,utils1.split_text(utils1.negotiate_con,500))
              screen.blit(utils1.assistent,(0,0))
              utils1.m2c4.draw(screen)
              utils1.m2c5.draw(screen)
              utils1.m2c6.draw(screen)
              utils1.back_btn2.draw(screen)
    elif M2==12:#reply con with pub 55
            screen.blit(utils1.cn2, (0, 0))       
            utils1.top_row(screen,coins,costs0)
            utils1.draw_dialog_box(screen,125,75,500,300,utils1.split_text(utils1.negotiate_con,500))
            screen.blit(utils1.assistent,(0,0))
            utils1.m2e1.draw(screen)
            utils1.m2e2.draw(screen)
            utils1.m2e3.draw(screen) ###select different btns
            utils1.back_btn2.draw(screen)
    elif M2==13: #reply con with only pub=0
          screen.blit(utils1.cn2, (0, 0))    
          utils1.top_row(screen,coins,costs0)
          utils1.draw_dialog_box(screen,125,75,500,300,utils1.split_text(utils1.negotiate_con,500))
          screen.blit(utils1.assistent,(0,0))
          utils1.m2c4.draw(screen)
          utils1.m2c5.draw(screen)
          utils1.m2c6.draw(screen)
          utils1.back_btn2.draw(screen)    
    elif M2==14: ##inside of public dept budget allotment request
        screen.blit(utils1.m2p2, (0, 0))
        if pygame.time.get_ticks()-utils1.start_time<5000 :
          utils1.draw_dialog_box(screen,125,75,700,300,utils1.split_text(utils1.reply_env0,700),10)
        else:
            utils1.draw_dialog_box(screen,125,75,700,300,utils1.split_text(utils1.reply_env0,700))
            utils1.next_btn2.draw(screen)
    elif M2==15: ##inside of  public dept for pub = 40
        screen.blit(utils1.m2p1,(0,0))
        screen.blit(utils1.pub_assistent,(30,20))  
        if pygame.time.get_ticks()-utils1.start_time<5000 :
          utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.reply_pub3,500),10)
        else:
            utils1.top_row(screen,coins,costs0)
            utils1.draw_dialog_box(screen,125,75,500,200,utils1.split_text(utils1.reply_pub3,500))
            utils1.con_sev.draw(screen)
            utils1.env_pub.draw(screen)
            utils1.continue_btn.draw(screen)  
            utils1.back_btn.draw(screen)       
    elif M2==16: ## env budget allotment for PUB=15
          screen.blit(utils1.e1, (0, 0))
          screen.blit(utils1.assistent,(0,0))
          if pygame.time.get_ticks() - utils1.start_time < 5000:
            utils1.draw_dialog_box(screen,125,75,700,400,utils1.split_text(utils1.allot_budget1,700),20)
          else:
                utils1.top_row(screen,coins,costs0)
                utils1.draw_dialog_box(screen,125,75,300,100,[f"Current Budget: {coins}Cr"])
                utils1.m2e4.draw(screen)
                utils1.m2e5.draw(screen)
                utils1.m2e6.draw(screen)
                utils1.back_btn2.draw(screen)
    elif M2==17: ##env budget allotment for PUB==55
          screen.blit(utils1.e1, (0, 0))
          screen.blit(utils1.assistent,(0,0))
          if pygame.time.get_ticks() - utils1.start_time < 5000:
            utils1.draw_dialog_box(screen,125,75,700,400,utils1.split_text(utils1.allot_budget1,700),10)
          else:
                utils1.top_row(screen,coins,costs0)
                utils1.draw_dialog_box(screen,125,75,300,100,[f"Current Budget: {coins}Cr"])
                utils1.m2e1.draw(screen)
                utils1.m2e2.draw(screen)
                utils1.m2e3.draw(screen) ## select different buttons
                utils1.back_btn2.draw(screen)
    elif M2==18:
            screen.blit(utils1.m2p2, (0, 0))
            screen.blit(utils1.assistent,(0,0))
            if pygame.time.get_ticks() - utils1.start_time < 12000:
              utils1.draw_dialog_box(screen,125,75,500,300,utils1.split_text(utils1.allot_budget1,500),10)
            else:              
                utils1.draw_dialog_box(screen,125,75,400,100,[f"Current Budget: {coins}Cr"])
                utils1.top_row(screen,coins,costs0)
                utils1.p1.draw(screen)
                utils1.p2.draw(screen)
                utils1.p3.draw(screen)
                utils1.back_btn2.draw(screen)    
    elif M2==19:#con service for pub=40
                screen.blit(utils1.cn2, (0, 0))       
                utils1.draw_dialog_box(screen,125,75,500,300,utils1.split_text(utils1.negotiate_con,500))
                screen.blit(utils1.assistent,(0,0))
                utils1.top_row(screen,coins,costs0)
                utils1.m2c1.draw(screen)
                utils1.m2c2.draw(screen)
                if coins>=15:
                  utils1.m2c3.draw(screen)
                utils1.back_btn2.draw(screen)
    elif M2==20:## budget and costs mission-competed
            screen.blit(utils1.background_1, (0, 0))
            utils1.draw_dialog_box(screen,125,75,300,100,utils1.split_text(utils1.completion_mssge2,500))
            utils1.draw_dialog_box(screen,125,200,150,70,[f'coins :{coins}'])
            utils1.draw_dialog_box(screen,125,260,150,70,[f'costs :{costs}'])
            utils1.draw_text(screen,"Water Quality (WQ): ", utils1.font, utils1.GREEN, 50, 380)
            if costs<=20:
                for  i in range(1):
                  pygame.draw.circle(screen, utils1.YELLOW, (435 + i * 30, 380), 10)
                  pygame.draw.circle(screen, utils1.BLACK, (435 + i * 30, 380), 10, 2)
                for i in range(1,5):
                  pygame.draw.circle(screen, utils1.GREY, (435 + i * 30, 380), 10)
                  pygame.draw.circle(screen, utils1.BLACK, (435 + i * 30, 380), 10, 2)
            elif costs<=30 and costs>20:
              for  i in range(2):
                pygame.draw.circle(screen, utils1.YELLOW, (435 + i * 30, 380), 10)
                pygame.draw.circle(screen, utils1.BLACK, (435 + i * 30, 380), 10, 2)
              for i in range(2,5):
                pygame.draw.circle(screen, utils1.GREY, (435 + i * 30, 380), 10)
                pygame.draw.circle(screen, utils1.BLACK, (435 + i * 30, 380), 10, 2)
            elif costs<=35 and costs>30:
              for  i in range(3):
                pygame.draw.circle(screen, utils1.YELLOW, (435 + i * 30, 380), 10)
                pygame.draw.circle(screen, utils1.BLACK, (435 + i * 30, 380), 10, 2)
              for i in range(3,5):
                pygame.draw.circle(screen, utils1.GREY, (435 + i * 30, 380), 10)
                pygame.draw.circle(screen, utils1.BLACK, (435 + i * 30, 380), 10, 2)
            elif costs<=40 and costs>35:
              for  i in range(4):
                pygame.draw.circle(screen, utils1.YELLOW, (435 + i * 30, 380), 10)
                pygame.draw.circle(screen, utils1.BLACK, (435 + i * 30, 380), 10, 2)
              for i in range(4,5):
                pygame.draw.circle(screen, utils1.GREY, (435 + i * 30, 380), 10)
                pygame.draw.circle(screen, utils1.BLACK, (435 + i * 30, 380), 10, 2)
            elif costs>=45:
              for  i in range(5):
                pygame.draw.circle(screen, utils1.YELLOW, (435 + i * 30, 380), 10)
                pygame.draw.circle(screen, utils1.BLACK, (435 + i * 30, 380), 10, 2)
            utils1.next_btn1.draw(screen)
    elif M2==-1:
          screen.blit(utils1.m2p1,(0,0))
          utils1.next_btn.draw(screen)
            # utils1.start_time=pygame.time.get_ticks()
    utils1.menu_btn.draw(screen)
    pygame.display.flip()
# pygame.quit()
def is_completed(M2):
    return M2==-1 