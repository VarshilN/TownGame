import pygame
import sys
import math
import MenuButtons.buttons
import Mission_1.utils
# Initialize Pygame
def run(screen,START,M1,coins,costs):
    WIDTH, HEIGHT =1920,1080
    db_height,db_width=800,200
    buttons=MenuButtons.buttons
    utils=Mission_1.utils
    if START == 0:
        screen.blit(utils.background_3, (0, 0))
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0,150)) 
        screen.blit(overlay, (0, 0))
        intro_lines = utils.split_text(utils.intro_text, 800)
        # draw_text(utils.intro_text, utils.font, (255, 255, 255), 10, 80)
        db_width=800
        db_height=300
        utils.draw_dialog_box(screen,200,200, db_width, db_height, intro_lines,utils.start_time)
        utils.start_btn.draw(screen)
    elif START == 1:
      screen.blit(utils.background_1, (0, 0))
      overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
      overlay.fill((0, 0, 0, 80))
      screen.blit(overlay, (0, 0))
        # utils.draw_dialog_box(utils.prev_text_1, utils.font, WHITE, 10, 10, WIDTH - 50)
      # utils.top_row(screen,coins)
      utils.draw_text(screen,"Air Quality (AQ): ", utils.font, utils.GREEN, 50, 280)
      for i in range(5):
          pygame.draw.circle(screen, utils.GREY, (300 + i * 40, 300), 10)
          pygame.draw.circle(screen, utils.BLACK, (300 + i * 40, 300), 10, 2)
      utils.draw_text(screen,"Water Quality (WQ): ", utils.font, utils.GREEN, 50, 330)
      for i in range(5):
          pygame.draw.circle(screen, utils.GREY, (350 + i * 40, 350), 10)
          pygame.draw.circle(screen, utils.BLACK, (350 + i * 40, 350), 10, 2)
      utils.draw_text(screen,"Waste Management (WM): ", utils.font, utils.GREEN, 50, 380)
      for i in range(5):
          pygame.draw.circle(screen, utils.GREY, (435 + i * 40, 400), 10)
          pygame.draw.circle(screen, utils.BLACK, (435 + i * 40, 400), 10, 2)
      utils.draw_text(screen,f"Coins: {coins}Cr", utils.font, utils.GOLDEN, 50, 450)
      db_width = 800
      db_height = 200
      screen.blit(utils.assistent, (0,0))
      utils.draw_dialog_box(screen,125,75,db_width,db_height,utils.split_text(utils.intro_dialog,800),utils.start_time)
      utils.back_btn.draw(screen)
      utils.enter_btn.draw(screen)
    elif START == 2:
        screen.blit(utils.background_2, (0, 0))
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0, 150))
        screen.blit(overlay, (0, 0))
        ##intro to assistant       
        utils.draw_text(screen,"Mission-1:Street Sweeping Programm",utils.font,utils.WHITE,400,200)
        utils.draw_text(screen,"Mission-2:River Cleaning Programm",utils.font,utils.WHITE,400,250)
        utils.draw_text(screen,"Mission-3:Visit Plastic And Goods Industry",utils.font,utils.WHITE,400,300)
        utils.top_row(screen,coins)
        utils.mission_btn.draw(screen)
        utils.quit_btn.draw(screen)
    elif START == 3:
        
        if M1 == 1:
          db_width=800
          db_height=250
          if utils.c1==0:
            screen.blit(utils.m1i1, (0, 0))
            screen.blit(utils.assistent,(0,0))
            utils.draw_dialog_box(screen,125,75, db_width, db_height,utils.split_text(utils.prev_text_1,800),utils.start_time,20)
            utils.skip_btn.draw(screen)
          else:
              screen.blit(utils.m1i2, (0, 0))
              screen.blit(utils.assistent,(0,0))
              utils.top_row(screen,coins)
              db_height=500
              utils.draw_dialog_box(screen,125,75, db_width, db_height,utils.split_text(utils.prev_text_2,800),utils.start_time,10)
              utils.next_btn1.draw(screen)
        elif M1 == 2:
              screen.blit(utils.m1i3, (0, 0))
              screen.blit(utils.assistent,(0,0))
              utils.draw_dialog_box(screen,125,75,500,200,utils.split_text(utils.visit_pub,500),utils.start_time)
              utils.next_btn1.draw(screen)
        elif M1 == 3:
            if utils.c2==0:
              screen.blit(utils.m1p1, (0, 0))               
              screen.blit(utils.pub_assistent,(30,20))
              utils.draw_dialog_box(screen,125,75,500,200,utils.split_text(utils.welcome_pub,500),utils.start_time,10)
              utils.skip_btn.draw(screen)       
            elif utils.c2==1:
              screen.blit(utils.m1p1, (0, 0))               
              screen.blit(utils.assistent,(0,0))
              utils.draw_dialog_box(screen,125,75,500,200,utils.split_text(utils.ask_about_pub,500),utils.start_time,10)
              utils.skip_btn.draw(screen)
            elif utils.c2==2:
              screen.blit(utils.m1p1, (0,0))               
              screen.blit(utils.pub_assistent,(30,20))
              utils.draw_dialog_box(screen,125,75,900,500,utils.split_text(utils.reply_about_pub,900),utils.start_time,10)
              utils.skip_btn.draw(screen)
            else: 
              screen.blit(utils.m1p1, (0, 0))
              screen.blit(utils.assistent,(0,0))               
              utils.draw_dialog_box(screen,125,75,500,200,utils.split_text(utils.ask_pub,500),utils.start_time,10)
              utils.next_btn1.draw(screen)
        elif M1 == 4:
            screen.blit(utils.m1p2, (0, 0))
            screen.blit(utils.pub_assistent,(30,20))
            utils.draw_dialog_box(screen,125,75,500,200,utils.split_text(utils.reply_pub,500),utils.start_time,10)   
            utils.next_btn1.draw(screen)       
        elif M1 == 5:
            screen.blit(utils.m1p2, (0, 0))
            if utils.c3==0:
              screen.blit(utils.assistent,(0,0))           
              utils.draw_dialog_box(screen,125,75,500,300,utils.split_text(utils.allot_budget,500),utils.start_time,10)  
              utils.skip_btn.draw(screen) 
            elif utils.c3==1:
              screen.blit(utils.assistent,(0,0))
              utils.draw_dialog_box(screen,125,75,400,100,[f"Current Budget: {coins}Cr"],utils.start_time)
              utils.top_row(screen,coins)
              utils.o1_btn.draw(screen)
              utils.o2_btn.draw(screen)
              utils.o3_btn.draw(screen)
              utils.visit_env_btn.draw(screen)
            elif utils.c3==2:
              screen.blit(utils.pub_assistent,(30,20))
              utils.draw_dialog_box(screen,125,75,500,300,utils.split_text(utils.reply3_con,500),utils.start_time,20) 
              utils.skip_btn.draw(screen)
        elif M1 == 6:
            screen.blit(utils.m1p1, (0, 0))
            screen.blit(utils.assistent,(0,0))
            utils.draw_dialog_box(screen,125,75,400,200,utils.split_text(utils.ask_20,400),utils.start_time,20)
            utils.next_btn1.draw(screen)
        elif M1 == 7:
            if utils.c4==0:
              screen.blit(utils.m1p2, (0, 0))
              screen.blit(utils.pub_assistent,(30,20))
              utils.draw_dialog_box(screen,125,75,500,200,utils.split_text(utils.reply1_20,500),utils.start_time,20)
              utils.skip_btn.draw(screen)
            else:
                screen.blit(utils.m1p1, (0, 0))
                screen.blit(utils.pub_assistent,(30,20))
                utils.draw_dialog_box(screen,125,75,500,200,utils.split_text(utils.reply2_20,500),utils.start_time,20)
                utils.con_sev_btn.draw(screen)
        elif M1 == 8:  # contra service
                if utils.c5==0:
                  screen.blit(utils.m1c1, (0, 0))
                  screen.blit(utils.con_assistent,(30,20))
                  utils.draw_dialog_box(screen,125,75,400,200,utils.split_text(utils.welcome_con,400),utils.start_time,20)
                  utils.skip_btn.draw(screen)
                elif utils.c5==1:
                  screen.blit(utils.m1c1, (0, 0))
                  screen.blit(utils.assistent,(0,0))
                  utils.draw_dialog_box(screen,125,75,400,200,utils.split_text(utils.ask_about_con,400),utils.start_time,10)
                  utils.skip_btn.draw(screen)
                elif utils.c5==2:
                  screen.blit(utils.m1c1, (0, 0))
                  screen.blit(utils.con_assistent,(30,20))
                  utils.draw_dialog_box(screen,125,75,800,400,utils.split_text(utils.reply_about_con,800),utils.start_time,10)
                  utils.skip_btn.draw(screen)
                elif utils.c5==3:
                  screen.blit(utils.m1c2, (0, 0))
                  screen.blit(utils.assistent,(0,0))
                  utils.draw_dialog_box(screen,125,75,500,200,utils.split_text(utils.ask_con,500),utils.start_time,10)
                  utils.skip_btn.draw(screen)
                elif utils.c5==4:
                  screen.blit(utils.m1c2, (0, 0))
                  screen.blit(utils.con_assistent,(30,20))
                  utils.draw_dialog_box(screen,125,75,500,300,utils.split_text(utils.reply_con,500),utils.start_time,10)     
                  utils.skip_btn.draw(screen)          
                else:
                    screen.blit(utils.m1c2, (0, 0))       
                    screen.blit(utils.assistent,(0,0))
                    utils.draw_dialog_box(screen,125,75,500,300,utils.split_text(utils.negotiate_con,500),utils.start_time)                
                    utils.c1_btn.draw(screen)
                    utils.c2_btn.draw(screen)
                    utils.c3_btn.draw(screen)   
                    utils.c4_btn.draw(screen)   
                    utils.back_btn1.draw(screen)              
        elif M1 == 9: 
            screen.blit(utils.m1c1, (0, 0))
            screen.blit(utils.con_assistent,(30,20))
            utils.draw_dialog_box(screen,125,75,400,200,utils.split_text(utils.reply1_con,400),utils.start_time,20)            
            utils.back_btn1.draw(screen)
        elif M1 == 10:
            screen.blit(utils.m1c2, (0, 0))
            screen.blit(utils.con_assistent,(30,20))
            utils.draw_dialog_box(screen,125,75,500,300,utils.split_text(utils.reply2_con+"\n"+utils.reply3_con,500),utils.start_time,20)          
            utils.next_btn1.draw(screen)
        elif M1 == 11:
            screen.blit(utils.m1c2, (0, 0))
            screen.blit(utils.con_assistent,(30,20))
            utils.draw_dialog_box(screen,125,75,400,100,utils.split_text(utils.reply3_con,400),utils.start_time,20)
            utils.next_btn1.draw(screen)
        elif M1 == 12:
            # add some animation for mission completion
            screen.blit(utils.background_2, (0, 0))
            screen.blit(utils.assistent,(0,0))
            utils.draw_dialog_box(screen,125,75,300,200,utils.split_text(utils.completion_mssge1,300),utils.start_time,10)
            utils.draw_text(screen,"Waste Management (WM): ", utils.font, utils.GREEN, 50, 380)
            if costs==0:
              for i in range(5):
                  pygame.draw.circle(screen, utils.GREY, (435 + i * 40, 380), 10)
                  pygame.draw.circle(screen, utils.BLACK, (435 + i * 40, 380), 10, 2)
            elif costs==10:
              for i in range(2):
                  pygame.draw.circle(screen,utils.YELLOW , (435 + i * 40, 380), 10)
                  pygame.draw.circle(screen, utils.BLACK, (435 + i * 40, 380), 10, 2)
              for i in range(2,5):
                  pygame.draw.circle(screen,utils. GREY, (435 + i * 40, 380), 10)
                  pygame.draw.circle(screen, utils.BLACK, (435 + i * 40,380), 10, 2)
            elif costs==15:
              for i in range(3):
                  pygame.draw.circle(screen,utils.YELLOW , (435 + i * 40, 380), 10)
                  pygame.draw.circle(screen,utils. BLACK, (435 + i * 40, 380), 10, 2)
              for i in range(3,5):
                  pygame.draw.circle(screen, utils.GREY, (435 + i * 40, 380), 10)
                  pygame.draw.circle(screen, utils.BLACK, (435 + i * 40, 380), 10, 2)
            elif costs==20:
              for i in range(4):
                  pygame.draw.circle(screen,utils.YELLOW, (435 + i * 40, 380), 10)
                  pygame.draw.circle(screen, utils.BLACK, (435 + i * 40, 380), 10, 2)
              for i in range(4,5):
                  pygame.draw.circle(screen, utils.GREY, (435 + i * 40, 380), 10)
                  pygame.draw.circle(screen, utils.BLACK, (435 + i * 40, 380), 10, 2)
            elif costs==25:
              for i in range(5):
                  pygame.draw.circle(screen,utils.YELLOW , (435 + i * 40, 380), 10)
                  pygame.draw.circle(screen, utils.BLACK, (435 + i * 40, 380), 10, 2)
            elif costs==30:
              for i in range(5):
                  pygame.draw.circle(screen,utils.YELLOW , (435 + i * 40, 380), 10)
                  pygame.draw.circle(screen, utils.BLACK, (435 + i * 40, 380), 10, 2)
            utils.next_btn1.draw(screen)
        elif M1 == 13:
            screen.blit(utils.background_2, (0, 0))
            utils.draw_dialog_box(screen,125,75,300,100,utils.split_text(utils.completion_mssge2,500),utils.start_time,10)
            utils.draw_dialog_box(screen,125,200,150,70,[f'coins :{coins}'],utils.start_time)
            utils.draw_dialog_box(screen,125,260,150,70,[f'costs :{costs}'],utils.start_time)
            utils.next_btn1.draw(screen)
        elif M1 == 14:
            if utils.c6==0:
              screen.blit(utils.m1p2, (0, 0))
              screen.blit(utils.pub_assistent,(30,20))
              utils.draw_dialog_box(screen,125,75,300,200,utils.split_text(utils.reply1_20,300),utils.start_time,10)
              utils.skip_btn.draw(screen)
            else:
              screen.blit(utils.m1p1, (0, 0))  
              screen.blit(utils.pub_assistent,(30,20))         
              utils.draw_dialog_box(screen,125,75,400,200,utils.split_text(utils.reply2_50,400),utils.start_time,10)
              utils.visit_env_btn.draw(screen)
        elif M1 == 15:  # env department 
            if utils.c7==0:
              screen.blit(utils.m1e1, (0, 0))
              utils.draw_dialog_box(screen,125,75,400,200,utils.split_text(utils.visit_env1,400),utils.start_time,20)  
              utils.skip_btn.draw(screen)   
            elif utils.c7==1: 
              screen.blit(utils.m1e1, (0, 0))
              screen.blit(utils.env_assistent,(30,20))
              utils.draw_dialog_box(screen,125,75,400,200,utils.split_text(utils.welcome_env,400),utils.start_time,10)  
              utils.skip_btn.draw(screen)   
            elif utils.c7==2:
              screen.blit(utils.m1e1, (0, 0))
              screen.blit(utils.assistent,(0,0))
              utils.draw_dialog_box(screen,125,75,400,200,utils.split_text(utils.ask_about_env,400),utils.start_time,20)  
              utils.skip_btn.draw(screen)  
            elif utils.c7==3:
              screen.blit(utils.m1e1, (0, 0))
              screen.blit(utils.env_assistent,(30,20))
              utils.draw_dialog_box(screen,125,75,800,400,utils.split_text(utils.reply_about_env,800),utils.start_time,10)  
              utils.skip_btn.draw(screen)  
            else:
              screen.blit(utils.m1e2, (0, 0))
              screen.blit(utils.assistent,(0,0))
              utils.draw_dialog_box(screen,125,75,300,100,utils.split_text(utils.ask_env,300),utils.start_time,10)            
              utils.env_next_0.draw(screen)
        elif M1 == 16:
          screen.blit(utils.m1e1, (0, 0))
          screen.blit(utils.env_assistent,(30,20))
          utils.draw_dialog_box(screen,125,75,400,200,utils.split_text(utils.reply_env,400),utils.start_time,20)
          utils.next_btn1.draw(screen)
        elif M1 == 17:
            screen.blit(utils.m1e1, (0, 0))
            screen.blit(utils.assistent,(0,0))
            if utils.c8==0:
              utils.draw_dialog_box(screen,125,75,500,300,utils.split_text(utils.allot_budget1,400),utils.start_time,20) 
              utils.skip_btn.draw(screen)
            elif utils.c8==2:
                utils.draw_dialog_box(screen,125,75,500,300,utils.split_text(utils.reply3_con,500),utils.start_time,20) 
                utils.next_btn1.draw(screen)
            elif utils.c8==1:
                utils.draw_dialog_box(screen,125,75,300,100,[f"Current Budget: {coins}Cr"],utils.start_time,20)
                utils.e1_btn.draw(screen)
                utils.e2_btn.draw(screen)
                utils.e3_btn.draw(screen)
                utils.back_btn1.draw(screen)
            # utils.start_time = pygame.time.get_ticks()
    utils.menu_btn.draw(screen)
    pygame.display.flip()
def is_completed(M1):
  return M1==-1

