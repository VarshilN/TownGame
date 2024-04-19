import MenuButtons.buttons
import pygame
import sys
import Mission_3.utils2
## coins + text replies ..
## 1. take a visit to plastic industry and (talk to them about their work  or ask them directly to lower their emission)
## 2. if talking about work they reveal their method's find potentiel fault in them .
##3. address the fault and ask them to correct it. 
## 4. reply: asking for resources -> visit public department 
## 5. explain the reply -> public department discusses and finds something fishy 
## 6. go to environment department to discuss situation.
## 7. find some more problems.
## 8. visit plastic industry 
## 9. plastic industry asking  for additional help with public department or environment department and additional expences 
##10. negotiate with them and find conclusion.
def run(screen,M3,coins,costs,costs1):
    WIDTH,HEIGHT =1920,1080
    db_width,db_height=800,200
    buttons=MenuButtons.buttons
    utils2=Mission_3.utils2
    if M3==0:
        screen.blit(utils2.background_2, (0, 0))
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))
            # utils2.draw_dialog_box(utils2.prev_text_1, utils2.font, WHITE, 10, 10, WIDTH - 50)
        # utils2.top_row(screen,coins,costs,costs1)
        utils2.top_row(screen,coins,costs,costs1)
        screen.blit(utils2.assistent, (0,0))
        utils2.draw_dialog_box(screen,125,75,db_width,db_height,utils2.split_text(utils2.intro_dialog,800),10)
        # utils2.back_btn.draw(screen)
        utils2.enter_btn.draw(screen)
        utils2.quit_btn.draw(screen)
    elif M3==1:  
        screen.blit(utils2.assistent,(0,0))
        if utils2.c1==0:   
            screen.blit(utils2.m3pi1,(0,0))
            utils2.draw_dialog_box(screen,125,75,db_width,db_height,utils2.split_text(utils2.prev_text1,800),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c1==1:
            screen.blit(utils2.m3ps1,(0,0))
            utils2.draw_dialog_box(screen,125,75,db_width,db_height,utils2.split_text(utils2.prev_text2,800),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c1==2:
            screen.blit(utils2.m3pr1,(0,0))
            utils2.draw_dialog_box(screen,125,75,db_width,db_height+300,utils2.split_text(utils2.prev_text3,800),10)
            utils2.enter_btn.draw(screen)
        screen.blit(utils2.assistent,(0,0))
    elif M3==2:
        if utils2.c2==0:
            screen.blit(utils2.m3pi1,(0,0))
            utils2.draw_dialog_box(screen,125,75,500,300,utils2.split_text(utils2.visit_ind,500),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c2==1:
            screen.blit(utils2.m3pi2,(0,0))
            screen.blit(utils2.ind_assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,500,300,utils2.split_text(utils2.welcome_ind,500),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c2==2:
            screen.blit(utils2.m3pi2,(0,0))
            screen.blit(utils2.assistent,(0,0))
            utils2.draw_dialog_box(screen,125,75,500,300,utils2.split_text(utils2.ask_ind,500),10)
            screen.blit(utils2.assistent,(0,0))
            utils2.skip_btn.draw(screen)
        elif utils2.c2==3:
            screen.blit(utils2.m3pi2,(0,0))
            screen.blit(utils2.ind_assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,500,300,utils2.split_text(utils2.reply_ind,500),10)
            utils2.ask_box(screen,200,450,450,40,utils2.ask_op1,0)
            utils2.ask_box(screen,200,520,400,40,utils2.ask_op2,1)
    elif M3==3:
        screen.blit(utils2.m3pi1,(0,0))
        if utils2.c3==0:
            screen.blit(utils2.ind_assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,500,300,utils2.split_text(utils2.reply_ind,500),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c3==1:
            screen.blit(utils2.ind_assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,500,300,utils2.split_text(utils2.reply_ind1,500),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c3==2:
            screen.blit(utils2.assistent,(0,0))
            utils2.draw_dialog_box(screen,125,75,500,300,utils2.split_text(utils2.ask_ind1,500),10)
            utils2.p1.draw(screen)
            utils2.back_btn1.draw(screen) 
    elif M3==4:
        screen.blit(utils2.m3pi2,(0,0))
        screen.blit(utils2.ind_assistent,(30,20))
        if utils2.c4==0:
            utils2.draw_dialog_box(screen,200,100,800,500,utils2.split_text(utils2.reply_ind2,800),10)
            utils2.ask_box(screen,200,620,450,40,utils2.ask_op3,2)
            utils2.ask_box(screen,200,690,400,40,utils2.ask_op4,3)
            utils2.back_btn.draw(screen)
        elif utils2.c4==1:           
            utils2.draw_dialog_box(screen,125,75,700,400,utils2.split_text(utils2.reply_ind3,700),10)
            screen.blit(utils2.assistent,(0,0))
            # utils2.ask_box(screen,200,450,450,40,utils2.ask_op1,0)
            # utils2.ask_box(screen,20  0,520,400,40,utils2.ask_op2,1)
            utils2.back_btn.draw(screen)
        elif utils2.c4==2:
            screen.blit(utils2.assistent,(0,0))
            utils2.draw_dialog_box(screen,125,75,700,400,utils2.split_text(utils2.reply_ind4,700),10)
            # utils2.ask_box(screen,200,450,450,40,utils2.ask_op1,0)
            # utils2.ask_box(screen,200,520,400,40,utils2.ask_op2,1)
            utils2.back_btn.draw(screen)    
    elif M3==5:
        if utils2.c5==0:
            screen.blit(utils2.m3ps1,(0,0))
            
            utils2.draw_dialog_box(screen,125,75,200,100,utils2.split_text(utils2.visit_pub,200),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c5==1:
            screen.blit(utils2.m2p1,(0,0))
            screen.blit(utils2.pub_assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,450,300,utils2.split_text(utils2.welcome_pub,400),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c5==2:
            screen.blit(utils2.m2p2,(0,0))
            utils2.draw_dialog_box(screen,125,75,400,200,utils2.split_text(utils2.ask_pub,400),10)
            screen.blit(utils2.assistent,(0,0))
            utils2.skip_btn.draw(screen)
        elif utils2.c5==3:
            screen.blit(utils2.m3pr2,(0,0))
            screen.blit(utils2.pub_assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,800,400,utils2.split_text(utils2.reply_pub0,800),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c5==4:
            screen.blit(utils2.m2p1,(0,0))
            
            utils2.draw_dialog_box(screen,125,75,200,200,utils2.split_text(utils2.visit_env0,200),10)
            screen.blit(utils2.assistent,(0,0))
            utils2.skip_btn.draw(screen)
        elif utils2.c5==5:
            screen.blit(utils2.m3ps1,(0,0))
            screen.blit(utils2.assistent,(0,0))
            utils2.draw_dialog_box(screen,125,75,400,200,utils2.split_text(utils2.visit_env1,400),10)
            utils2.m3e1.draw(screen)
    elif M3==6:
        if utils2.c6==0:
            screen.blit(utils2.m3ps2,(0,0))
            utils2.draw_dialog_box(screen,125,75,250,100,utils2.split_text(utils2.visit_env,250),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c6==1:
            screen.blit(utils2.e1,(0,0))
            screen.blit(utils2.env_assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,400,300,utils2.split_text(utils2.welcome_env,400),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c6==2:
            screen.blit(utils2.e2,(0,0))
            screen.blit(utils2.assistent,(0,0))
            utils2.draw_dialog_box(screen,125,75,300,100,utils2.split_text(utils2.ask_pub,300),10)
         
            utils2.skip_btn.draw(screen)
        elif utils2.c6==3:
            screen.blit(utils2.m3ps2,(0,0))
            screen.blit(utils2.env_assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,700,500,utils2.split_text(utils2.reply_env0,700),10)
            utils2.next_btn1.draw(screen)
        elif utils2.c6==4:
            screen.blit(utils2.e1,(0,0))
            screen.blit(utils2.assistent,(0,0))
            utils2.draw_dialog_box(screen,125,75,300,200,utils2.split_text(utils2.visit_ind2,300),10)
          
            utils2.skip_btn.draw(screen)
        elif utils2.c6==5:
            screen.blit(utils2.e1,(0,0))
            screen.blit(utils2.assistent,(0,0))
            utils2.draw_dialog_box(screen,125,75,300,200,utils2.split_text(utils2.visit_ind0,300),10)
           
            utils2.visit_btn.draw(screen)
    elif M3==7:
        if utils2.c7==0:
            screen.blit(utils2.m3ps1,(0,0))
            screen.blit(utils2.assistent,(0,0))
            utils2.draw_dialog_box(screen,125,75,300,200,utils2.split_text(utils2.visit_ind,300),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c7==1:
            screen.blit(utils2.m3pi1,(0,0))
            screen.blit(utils2.ind_assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,300,200,utils2.split_text(utils2.welcome_ind0,300),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c7==2:
            screen.blit(utils2.m3pi1,(0,0))
            screen.blit(utils2.assistent,(0,0))
            utils2.draw_dialog_box(screen,125,75,400,300,utils2.split_text(utils2.ask_ind2,400),10)
           
            utils2.skip_btn.draw(screen)
        elif utils2.c7==3:
            screen.blit(utils2.m3pi2,(0,0))
            screen.blit(utils2.ind_assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,700,400,utils2.split_text(utils2.reply_ind7,700),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c7==4:
            screen.blit(utils2.m3pi2,(0,0))
            screen.blit(utils2.assistent,(0,0))
            utils2.draw_dialog_box(screen,125,75,400,300,utils2.split_text(utils2.ask_ind3,400),10)
          
            utils2.skip_btn.draw(screen)
        elif utils2.c7==5:
            screen.blit(utils2.m3pi2,(0,0))
            screen.blit(utils2.ind_assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,500,300,utils2.split_text(utils2.reply_ind8,500),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c7==6:
            screen.blit(utils2.m3pi2,(0,0))
            screen.blit(utils2.assistent,(0,0))
            utils2.draw_dialog_box(screen,125,75,400,300,utils2.split_text(utils2.ask_ind4,400),10)
       
            utils2.ask_box(screen,200,450,600,40,utils2.ask_op6,0)
        elif utils2.c7==7:
            screen.blit(utils2.m3pi1,(0,0))
            screen.blit(utils2.ind_assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,600,300,utils2.split_text(utils2.reply_ind9,600),10)
            utils2.ask_box(screen,200,450,600,40,utils2.visit_pub,0)
    elif M3==8:
        if utils2.c8==0:
            screen.blit(utils2.m3ps1,(0,0))
            utils2.draw_dialog_box(screen,125,75,300,200,utils2.split_text(utils2.visit_pub,300),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c8==1:
            screen.blit(utils2.m2p1,(0,0))
            screen.blit(utils2.assistent,(0,0))
            utils2.draw_dialog_box(screen,125,75,300,200,utils2.split_text(utils2.visit_pub1,300),10)
   
            utils2.skip_btn.draw(screen)
        elif utils2.c8==2:
            screen.blit(utils2.m2p2,(0,0))
            screen.blit(utils2.pub_assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,600,300,utils2.split_text(utils2.reply_pub1,600),10)
            utils2.top_row(screen,coins,costs,costs1)
            utils2.skip_btn.draw(screen)
        elif utils2.c8==3:
            screen.blit(utils2.m2i2,(0,0))
            screen.blit(utils2.assistent,(0,0))
            utils2.draw_dialog_box(screen,125,75,300,200,utils2.split_text(utils2.visit_env1,300),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c8==4:
            screen.blit(utils2.e1,(0,0))
            screen.blit(utils2.assistent,(0,0))
            utils2.draw_dialog_box(screen,125,75,300,200,utils2.split_text(utils2.visit_env2,300),10)
            utils2.skip_btn.draw(screen)
        elif utils2.c8==5:
            screen.blit(utils2.e2,(0,0))
            screen.blit(utils2.env_assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,600,300,utils2.split_text(utils2.reply_env1,600),10)
            utils2.top_row(screen,coins,costs,costs1)
            utils2.skip_btn.draw(screen)
        elif utils2.c8==6:
            screen.blit(utils2.m3pi2,(0,0))
            screen.blit(utils2.assistent,(30,20))
            utils2.draw_dialog_box(screen,125,75,600,300,utils2.split_text(utils2.visit_ind1,600),10)
            # screen.blit(utils2.assistent,(0,0))
            utils2.continue_btn.draw(screen)
    elif M3==9:
        screen.blit(utils2.background_2, (0, 0))
        screen.blit(utils2.assistent, (0,0))
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))
        costs2=utils2.ENV1+utils2.PUB1
            # utils2.draw_dialog_box(utils2.prev_text_1, utils2.font, WHITE, 10, 10, WIDTH - 50)
        # utils2.top_row(screen,coins,costs,costs1)
        utils2.draw_text(screen,"Air Quality(AQ): ", utils2.font, utils2.DARK_GREEN, 50, 280)
        if costs2<=15:
            for  i in range(1):
                pygame.draw.circle(screen, utils2.YELLOW, (300 + i * 30, 300), 10)
                pygame.draw.circle(screen, utils2.BLACK, (300 + i * 30, 300), 10, 2)
            for i in range(1,5):
                pygame.draw.circle(screen, utils2.GREY, (300 + i * 30, 300), 10)
                pygame.draw.circle(screen, utils2.BLACK, (300 + i * 30, 300), 10, 2)
        elif costs2==20:
            for  i in range(2):
                pygame.draw.circle(screen, utils2.YELLOW, (300 + i * 30, 300), 10)
                pygame.draw.circle(screen, utils2.BLACK, (300 + i * 30, 300), 10, 2)
            for i in range(2,5):
                pygame.draw.circle(screen, utils2.GREY, (300 + i * 30, 300), 10)
                pygame.draw.circle(screen, utils2.BLACK, (300 + i * 30, 300), 10, 2)
        elif costs2==25:
            for  i in range(3):
                pygame.draw.circle(screen, utils2.YELLOW, (300 + i * 30, 300), 10)
                pygame.draw.circle(screen, utils2.BLACK, (300 + i * 30, 300), 10, 2)
            for i in range(3,5):
                pygame.draw.circle(screen, utils2.GREY, (300 + i * 30, 300), 10)
                pygame.draw.circle(screen, utils2.BLACK, (300 + i * 30, 300), 10, 2)
        elif costs2>=30:
            for  i in range(5):
                pygame.draw.circle(screen, utils2.YELLOW, (300 + i * 30, 300), 10)
                pygame.draw.circle(screen, utils2.BLACK, (300 + i * 30, 300), 10, 2)
        utils2.draw_text(screen,"Water Quality (WQ): ", utils2.font, utils2.DARK_GREEN, 50, 330)
        if costs1<=20:
            for  i in range(1):
                pygame.draw.circle(screen, utils2.YELLOW, (350 + i * 30, 350), 10)
                pygame.draw.circle(screen, utils2.BLACK, (350 + i * 30, 350), 10, 2)
            for i in range(1,5):
                pygame.draw.circle(screen, utils2.GREY, (350 + i * 30, 350), 10)
                pygame.draw.circle(screen, utils2.BLACK, (350 + i * 30, 350), 10, 2)
        elif costs1<=30 and costs1>20:
            for  i in range(2):
                pygame.draw.circle(screen, utils2.YELLOW, (350 + i * 30, 350), 10)
                pygame.draw.circle(screen, utils2.BLACK, (350 + i * 30, 350), 10, 2)
            for i in range(2,5):
                pygame.draw.circle(screen, utils2.GREY, (350 + i * 30, 350), 10)
                pygame.draw.circle(screen, utils2.BLACK, (350 + i * 30, 350), 10, 2)
        elif costs1<=35 and costs1>30:
            for  i in range(3):
                pygame.draw.circle(screen, utils2.YELLOW, (350 + i * 30, 350), 10)
                pygame.draw.circle(screen, utils2.BLACK, (350 + i * 30, 350), 10, 2)
            for i in range(3,5):
                pygame.draw.circle(screen, utils2.GREY, (350 + i * 30, 350), 10)
                pygame.draw.circle(screen, utils2.BLACK, (350 + i * 30, 350), 10, 2)
        elif costs1<=40 and costs1>35:
            for  i in range(4):
                pygame.draw.circle(screen, utils2.YELLOW, (350 + i * 30, 350), 10)
                pygame.draw.circle(screen, utils2.BLACK, (200 + i * 30, 350), 10, 2)
            for i in range(4,5):
                pygame.draw.circle(screen, utils2.GREY, (350+ i * 30, 350), 10)
                pygame.draw.circle(screen, utils2.BLACK, (350 + i * 30, 350), 10, 2)
        elif costs1>=45:
            for  i in range(5):
                pygame.draw.circle(screen, utils2.YELLOW, (350 + i * 30, 350), 10)
                pygame.draw.circle(screen, utils2.BLACK, (350 + i * 30, 350), 10, 2)
  # Display WM
        utils2.draw_text(screen,"Waste Management(WM): ", utils2.font, utils2.DARK_GREEN, 50, 380)
        if costs==0:
            for i in range(5):
                pygame.draw.circle(screen, utils2.GREY, (400 + i * 30, 400), 10)
                pygame.draw.circle(screen, utils2.BLACK, (400 + i * 30, 400), 10, 2)
        elif costs==10:
            for i in range(2):
                pygame.draw.circle(screen,utils2.YELLOW , (400 + i * 30, 400), 10)
                pygame.draw.circle(screen, utils2.BLACK, (400 + i * 30, 400), 10, 2)
            for i in range(2,5):
                pygame.draw.circle(screen, utils2.GREY, (400 + i * 30, 400), 10)
                pygame.draw.circle(screen,utils2.BLACK, (400 + i * 30, 400), 10, 2)
        elif costs==15:
            for i in range(3):
                pygame.draw.circle(screen,utils2.YELLOW , (400 + i * 30, 400), 10)
                pygame.draw.circle(screen, utils2.BLACK, (400 + i * 30, 400), 10, 2)
            for i in range(3,5):
                pygame.draw.circle(screen, utils2.GREY, (400+ i * 30, 400), 10)
                pygame.draw.circle(screen, utils2.BLACK, (400 + i * 30, 400), 10, 2)
        elif costs==20:
            for i in range(4):
                pygame.draw.circle(screen,utils2.YELLOW , (400 + i * 30, 400), 10)
                pygame.draw.circle(screen, utils2.BLACK, (400 + i * 30, 400), 10, 2)
            for i in range(4,5):
                pygame.draw.circle(screen, utils2.GREY, (400 + i * 30, 400), 10)
                pygame.draw.circle(screen, utils2.BLACK, (400 + i * 30, 400), 10, 2)
        elif costs==25:
            for i in range(5):
                pygame.draw.circle(screen,utils2.YELLOW , (400+ i * 30, 400), 10)
                pygame.draw.circle(screen, utils2.BLACK, (400 + i * 30, 400), 10, 2)
        elif costs==30:
            for i in range(5):
                pygame.draw.circle(screen,utils2.YELLOW , (400 + i * 30, 400), 10)
                pygame.draw.circle(screen, utils2.BLACK, (400 + i * 30, 400), 10, 2)
        utils2.draw_dialog_box(screen,600,300,db_width,400,utils2.split_text(utils2.complete_dialog,800),10)
        # utils2.back_btn.draw(screen)
        utils2.res_btn.draw(screen)
    utils2.menu_btn.draw(screen)
    pygame.display.flip()
def is_completed(M3):
    return M3==-1