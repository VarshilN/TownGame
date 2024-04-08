import pygame
import sys
import math
import buttons

# Initialize Pygame
pygame.init()

#game coins
coins = 100
# Set up the screen
WIDTH, HEIGHT = 1024, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Greenerie Rescue: The Mayor's Mission")

##BUTTONS
im1 = pygame.image.load('./button_start-game.png')
start_btn = buttons.Button(380, 450, im1, 0.5)
im2 = pygame.image.load('./Buttons/button_back.png')
back_btn = buttons.Button(320, 490, im2, 0.5)
im3 = pygame.image.load('./button_enter.png')
enter_btn = buttons.Button(500, 490, im3, 0.5)
im4 = pygame.image.load('./button_exit.png')
quit_btn = buttons.Button(300, 490, im4, 0.5)
im5 = pygame.image.load('./button_enter-story.png')
mission_btn = buttons.Button(550, 490, im5, 0.5)
im6 = pygame.image.load('./Buttons/button_resume.png')
resume_btn = buttons.Button(320, 490, im6, 0.5)
im7 = pygame.image.load('./button_continue.png')
continue_btn = buttons.Button(320, 490, im6, 0.5)
##Game_State
START = 0
MISSION=0
INTERVAL_SECONDS=5
# Load background images
background_0 = pygame.image.load('./Background/home_1.png')
background_0 = pygame.transform.scale(background_0, (WIDTH, HEIGHT))
background_1 = pygame.image.load('./Background/home_2.png')
background_1 = pygame.transform.scale(background_1, (WIDTH, HEIGHT))
background_2 = pygame.image.load('./mayor_office.png')
background_2 = pygame.transform.scale(background_2, (WIDTH, HEIGHT))
assistent = pygame.image.load('./assistent.png')
assistent = pygame.transform.scale(assistent, (200,200))



#CONTINUE
CONTINUE=0
#mission_1

##completion of mission

#STATE
M1 =0
m1i1 = pygame.image.load('./Mission_1/m1_0.png')
m1i1 = pygame.transform.scale(m1i1, (WIDTH, HEIGHT))
m1i2 = pygame.image.load('./Mission_1/m1_1.png')
m1i2 = pygame.transform.scale(m1i2, (WIDTH, HEIGHT))
m1i3 = pygame.image.load('./Mission_1/m1_2.png')
m1i3 = pygame.transform.scale(m1i3, (WIDTH, HEIGHT))
m1p1 = pygame.image.load('./Mission_1/m1_pub1.png')
m1p1 = pygame.transform.scale(m1p1, (WIDTH, HEIGHT))
m1p2 = pygame.image.load( './Mission_1/m1_pub2.png')
m1p2 = pygame.transform.scale(m1p2, (WIDTH, HEIGHT))
m1c1 = pygame.image.load( './Mission_1/m1_con1.png')
m1c1 = pygame.transform.scale(m1c1, (WIDTH, HEIGHT))
m1c2 = pygame.image.load( './Mission_1/m1_con2.png')
m1c2 = pygame.transform.scale(m1c2, (WIDTH, HEIGHT))
m1e1 = pygame.image.load( './Mission_1/m1_env1.png')
m1e1 = pygame.transform.scale(m1e1, (WIDTH, HEIGHT))
m1e2 = pygame.image.load('./Mission_1/m1_env2.png')
m1e2 = pygame.transform.scale(m1e2, (WIDTH, HEIGHT))

intro_dialog ="Welcome to Greenerie, Mayor! .Your mission is to reduce pollution while keeping the townspeople happy. Let's get started!"
intro_text = "In town called Greenerie, Pollution index has been severely high. As the new mayor of the town, you have the responsibility to reduce the index while keeping the needs of people living inside the town. In this journey, you'll need to negotiate with several corporate companies and take initiative to clean the town. Good Luck!"
prev_text_1 = "Task: Implement regular street cleaning and litter removal programs. This will help reduce pollution and improve the quality of the streets."
prev_text_2 = "Description: Deploy cleanup crews equipped with trash pickers and garbage bags to remove litter and debris from streets, parks, and public spaces. Encourage community participation through volunteer clean-up events and neighborhood beautification projects. Impact: Improves the town's aesthetic appeal, enhances public health and safety, and prevents litter from polluting waterways and natural habitats."
prev_text_3 = "Visit Public Department ."
ask_pub = "Ask Public Department for help"
reply_pub = "We'll need to allot some budget first for this task to the Public department."
welcome_pub = "Welcome to Public Department , Mayor!."
allot_budget = "Allot budget for this task to the Public department but remember that once budget alloted your cost will be reduced by that amount and you won't be able to allot more budget or take it :"
ask_20 = "allot 20L and ask them for help"
reply1_20 = "Ok, please wait for 2 days"
reply2_20 = "Our workers inspected the wastes in streets, and since the situation is worse than we thought, we'll need to seek help from Contracted Service Providers."
welcome_con = "Welcome to Contracted Service Providers , Mayor!."
ask_con = "Ask Contracted Service Providers for help"
reply_con =  "Gladly! let's but we need to pay our workers a small amount of money to do this task , our demand is 10L (Negotiate with contract service)" 
negotiate_con = "Negotiate with Contracted Service Providers to get the amount of money they need to do this task."
reply1_con = "Sorry ! it's not enough"
reply2_con = "I guess we have no choice"
reply3_con = "Okay , then we'll complete work within a week"
welcome_env = "Welcome to Environmental Protection Department , Mayor!."
ask_env = "Ask Environmental Protection Department for help"
reply_env = "Gladly! but we'll need to allot budget first"
allot_budget1 = "Allot budget for this task to the Environmental Protection department but remember that once budget alloted your cost will be reduced by that amount and you won't be able to allot more budget or take it :"
reply2_50 = "we'll need to seek help from environment service department"
completion_mssge1 = "Mission 1 complete:"
completion_mssge2 = "Budget and Costs:"

#mission1_buttons
m1b1 = pygame.image.load('./Buttons/button_next.png')
m1_btn = buttons.Button(400, 490, m1b1, 0.5)
next_btn1 = buttons.Button(400,490,m1b1,0.5)
next_btn2 = buttons.Button(400,490,m1b1,0.5)
next_btn3 = buttons.Button(400,490,m1b1,0.5)
next_btn4= buttons.Button(400,490,m1b1,0.5)
pub_next_0= buttons.Button(400,490,m1b1,0.5)
pub_next_1 = buttons.Button(400,490,m1b1,0.5)
env_next_0 = buttons.Button(400,490,m1b1,0.5)
env_next_1 = buttons.Button(400,490,m1b1,0.5)
back_btn1=buttons.Button(400,490,im2,0.5)
o1b1 = pygame.image.load('./Buttons/20.png')
o1b2 = pygame.image.load('./Buttons/50.png')
o1b3 = pygame.image.load('./Buttons/70.png')
o1b4 = pygame.image.load('./Buttons/button_env.png')
o1b5 = pygame.image.load('./Buttons/button_con.png')
o1b6 = pygame.image.load('./Buttons/2.png')
o1c2 = pygame.image.load('./Buttons/5.png')
o1c3 = pygame.image.load('./Buttons/10.png')
o1e3= pygame.image.load('./Buttons/30.png')
o1_btn= buttons.Button(320,490,o1b1,0.5)
o2_btn = buttons.Button(420,490,o1b2,0.5)
o3_btn = buttons.Button(520,490,o1b3,0.5)
visit_env_btn = buttons.Button(600,490,o1b4,0.5)
contr_sev_btn = buttons.Button(500,490,o1b5,0.5)
c1_btn = buttons.Button(320,490,o1b6,0.5)
c2_btn = buttons.Button(420,490,o1c2,0.5)
c3_btn = buttons.Button(520,490,o1c3,0.5)
e1_btn = buttons.Button(340,490,o1c3,0.5)
e2_btn = buttons.Button(440,490,o1b1,0.5)
e3_btn = buttons.Button(540,490,o1e3,0.5)
# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 128, 0)
WHITE = (250, 250, 250)
GOLDEN = (128,128,0)
GREY = (169, 169, 169)


#time programm started 
font_path = "Adventure.ttf"
# Define fonts
font = pygame.font.SysFont(font_path, 36)
font_size=36
def split_text(text, max_width):
  words = text.split()
  lines = []
  current_line = ''
  for word in words:
      test_line = current_line + word + ' '
      if font.size(test_line)[0] <= max_width:
          current_line = test_line
      else:
          lines.append(current_line)
          current_line = word + ' '
  lines.append(current_line)
  return lines
# def draw_text_typewriter(text, font, color, x, y, delay):
#     displayed_text = ""
#     current_time = pygame.time.get_ticks()
#     delta_time = current_time - start_time
#     for i in range(len(text)):
#         if delta_time >= i * delay:
#             displayed_text += text[i]
#     draw_text(displayed_text, font, color, x, y)
# def draw_text(text, font, color, x, y):
#   words = text.split(' ')
#   lines = []
#   current_line = ''
#   for word in words:
#     test_line = current_line + ' ' + word if current_line != '' else word
#     if font.size(test_line)[0] <= WIDTH - x:
#       current_line = test_line
#     else:
#       lines.append(current_line)
#       current_line = word
#   lines.append(current_line)
#   for line in lines:
#     text_surface = font.render(line, True, color)
#     text_rect = text_surface.get_rect()
#     text_rect.topleft = (x, y)
#     WINDOW  .blit(text_surface, text_rect)
#     y += text_rect.height + 10

def draw_dialog_box(surface, x, y, width, height, text_lines, typewriter_delay=None):
  shadow_surface = pygame.Surface((width, height)).convert_alpha()
  shadow_surface.fill((0, 0, 0, 0))
  shadow_rect = pygame.Rect((2, 2), (width, height))
  pygame.draw.rect(shadow_surface, (0, 0, 0, 100), shadow_rect)
  surface.blit(shadow_surface, (x + 2, y + 2))

  pygame.draw.rect(surface, GREY, (x, y, width, height))
  pygame.draw.rect(surface, BLACK, (x, y, width, height), 3)

  text_y = y + (height - (len(text_lines) * (font_size + 5))) // 2

  # Initialize the timer for typewriter effect

  # current_time=pygame.time.get_ticks()
  current_char_index = 0
  count=0
  if typewriter_delay is None:   
    for line in text_lines:
      text_surface = font.render(line, True, BLACK)
      text_rect = text_surface.get_rect(center=(x + width // 2, text_y))
      surface.blit(text_surface, text_rect)
      text_y += font_size + 10
  else:
    storage={}
    count=0
    for line in text_lines:
      # typewriter_timer=current_time=pygame.time.get_ticks()
      current_line=""
      for i in range(len(line)):
        if i<len(line):
          current_line=line[:i+1]
          if count not in storage:
            storage[count] = [current_line]
          else:
            storage[count].append(current_line)
      count+=1
    for k,v in storage.items():
      for r in v:
        text_surface = font.render(r, True, BLACK)
        text_rect = text_surface.get_rect(center=(x + width // 2, text_y))
        surface.fill(GREY, (text_rect.left, text_rect.top, text_rect.width, text_rect.height))
        surface.blit(text_surface, text_rect)
        pygame.time.wait(typewriter_delay)
        pygame.display.update()
      text_y+=font_size+10
def draw_text(text, font, color, x, y):
  words = text.split(' ')
  lines = []
  current_line = ''
  for word in words:
    test_line = current_line + ' ' + word if current_line != '' else word
    if font.size(test_line)[0] <= WIDTH - x:
      current_line = test_line
    else:
      lines.append(current_line)
      current_line = word
  lines.append(current_line)
  for line in lines:
    text_surface = font.render(line, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

    y += text_rect.height + 10 # Increase y-coordinate to add spacing between lines
def top_row():
  # Display Coins
  font_1=pygame.font.SysFont(font_path,50)
  draw_text(f"Coins: {coins}Cr",font_1, GOLDEN, 20, 20)
  # Display AQ
  draw_text("AQ: ", font_1, DARK_GREEN, 300, 20)
  for i in range(5):
      pygame.draw.circle(screen, GREY, (365 + i * 30, 35), 10)
      pygame.draw.circle(screen, BLACK, (365 + i * 30, 35), 10, 2)

  # Display WQ
  draw_text("WQ: ", font_1, DARK_GREEN, 500, 20)
  for i in range(5):
      pygame.draw.circle(screen, GREY, (570 + i * 30, 35), 10)
      pygame.draw.circle(screen, BLACK, (570 + i * 30, 35), 10, 2)

  # Display WM
  draw_text("WM: ", font_1, DARK_GREEN, 700, 20)
  for i in range(5):
      pygame.draw.circle(screen, GREY, (770 + i * 30, 35), 10)
      pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)

trans=False
running = True
start_time=pygame.time.get_ticks()
flag_1=False
flag_2=False
flag_3 = False
flag_4 = False
flag_5=False
flag_6=False
flag_7=False
flag_8 = False
flag_9=False
flag_10=False
flag_11=False
flag_12=False
flag_13=False
flag_14=False
flag_15=False
flag_16=False
flag_17=False
flag_18=False

while running:
    if START == 0:
        screen.blit(background_0, (0, 0))
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0,80)) # Make it a bit brighter
        screen.blit(overlay, (0, 0))

        intro_lines = split_text(intro_text, 800)
        # draw_text(intro_text, font, (255, 255, 255), 10, 80)
        db_width=800
        db_height=250
        draw_dialog_box(screen,100,100, db_width, db_height, intro_lines)
        start_btn.draw(screen)
    elif START == 1:
      screen.blit(background_1, (0, 0))
      overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
      overlay.fill((0, 0, 0, 80))
      screen.blit(overlay, (0, 0))
        # draw_dialog_box(prev_text_1, font, WHITE, 10, 10, WIDTH - 50)
      # top_row()
      draw_text("Air Quality (AQ): ", font, GREEN, 50, 280)
      for i in range(5):
          pygame.draw.circle(screen, GREY, (300 + i * 40, 300), 10)
          pygame.draw.circle(screen, BLACK, (300 + i * 40, 300), 10, 2)
      draw_text("Water Quality (WQ): ", font, GREEN, 50, 330)
      for i in range(5):
          pygame.draw.circle(screen, GREY, (350 + i * 40, 350), 10)
          pygame.draw.circle(screen, BLACK, (350 + i * 40, 350), 10, 2)
      draw_text("Waste Management (WM): ", font, GREEN, 50, 380)
      for i in range(5):
          pygame.draw.circle(screen, GREY, (435 + i * 40, 400), 10)
          pygame.draw.circle(screen, BLACK, (435 + i * 40, 400), 10, 2)
      draw_text(f"Coins: {coins}Cr", font, GOLDEN, 50, 450)
      db_width = 800
      db_height = 200
      screen.blit(assistent, (0,0))
      draw_dialog_box(screen,125,75, db_width, db_height, split_text(intro_dialog,800))
      back_btn.draw(screen)
      enter_btn.draw(screen)
    elif START == 2:
        screen.blit(background_2, (0, 0))
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0, 150))
        screen.blit(overlay, (0, 0))
        ##intro to assistant       
        top_row()
        mission_btn.draw(screen)
        quit_btn.draw(screen)
    elif START == 3:
        if M1 == 1:
          db_width=800
          db_height=250

          if pygame.time.get_ticks() - start_time < 10000:
            screen.blit(m1i1, (0, 0))
            screen.blit(assistent,(0,0))
            if not flag_1:
              draw_dialog_box(screen,125,75, db_width, db_height,split_text(prev_text_1,800),10)
              flag_1=True
            else:
              draw_dialog_box(screen,125,75, db_width, db_height,split_text(prev_text_1,800))
          else:
              screen.blit(m1i2, (0, 0))
              screen.blit(assistent,(0,0))
              top_row()
              db_height=500
              if not flag_2:
                draw_dialog_box(screen,125,75, db_width, db_height,split_text(prev_text_2,800),10)
                flag_2=True
              else:
                draw_dialog_box(screen,125,75, db_width, db_height,split_text(prev_text_2,800))
                m1_btn.draw(screen)
        elif M1 == 2:
              screen.blit(m1i3, (0, 0))
              draw_dialog_box(screen,125,75,500,200,split_text(prev_text_3,500))
              next_btn1.draw(screen)
        elif M1 == 3:
            if pygame.time.get_ticks() - start_time < 5000:
              screen.blit(m1p1, (0, 0))
              if flag_1:                
                draw_dialog_box(screen,125,75,500,200,split_text(welcome_pub,500),10)
                flag_1=False
              else:
                draw_dialog_box(screen,125,75,500,200,split_text(welcome_pub,500))
            else: 
              screen.blit(m1p1, (0, 0))
              screen.blit(assistent,(0,0))
              if flag_2:               
                draw_dialog_box(screen,125,75,500,200,split_text(ask_pub,500),10)
                flag_2=False
              else:
                draw_dialog_box(screen,125,75,500,200,split_text(ask_pub,500))
                pub_next_0.draw(screen)
        elif M1 == 4:
            screen.blit(m1p2, (0, 0))
            if not flag_1:
              draw_dialog_box(screen,125,75,500,200,split_text(reply_pub,500),10)
              flag_1=True
            else:
              draw_dialog_box(screen,125,75,500,200,split_text(reply_pub,500))
              next_btn2.draw(screen)
        elif M1 == 5:
            screen.blit(m1p2, (0, 0))
            screen.blit(assistent,(0,0))
            if pygame.time.get_ticks() - start_time < 12000:
              if flag_1:
                draw_dialog_box(screen,125,75,500,300,split_text(allot_budget,500),10)
                flag_1=False
              else:
                draw_dialog_box(screen,125,75,500,300,split_text(allot_budget,500))
                screen.blit(assistent,(0,0))
            else:
              if not  flag_2:
                draw_dialog_box(screen,125,75,400,100,[f"Current Budget: {coins}Cr"],20)
                flag_2=True
              else:
                draw_dialog_box(screen,125,75,400,100,[f"Current Budget: {coins}Cr"])
                top_row()
                o1_btn.draw(screen)
                o2_btn.draw(screen)
                o3_btn.draw(screen)
                visit_env_btn.draw(screen)
        elif M1 == 6:
            screen.blit(m1p1, (0, 0))
            if not flag_3:
              draw_dialog_box(screen,125,75,400,200,split_text(ask_20,400),20)
              flag_3=True
            else:
              draw_dialog_box(screen,125,75,400,200,split_text(ask_20,400))
              pub_next_1.draw(screen)
        elif M1 == 7:
            if pygame.time.get_ticks() - start_time < 5000:
              screen.blit(m1p2, (0, 0))
              if flag_3:
                draw_dialog_box(screen,125,75,500,200,split_text(reply1_20,500),20)
                flag_3=False
              else:
                  draw_dialog_box(screen,125,75,500,200,split_text(reply1_20,500))
            else:
                screen.blit(m1p1, (0, 0))
                if not flag_4:
                  draw_dialog_box(screen,125,75,500,200,split_text(reply2_20,500),20)
                  flag_4=True
                else:
                  draw_dialog_box(screen,125,75,500,200,split_text(reply2_20,500))
                  contr_sev_btn.draw(screen)
        elif M1 == 8:  # contra service
            if not trans:
                if pygame.time.get_ticks() - start_time < 5000:
                  screen.blit(m1c1, (0, 0))
                  if not flag_5:
                    draw_dialog_box(screen,125,75,400,200,split_text(welcome_con,400),20)
                    flag_5 = True
                  else:
                    draw_dialog_box(screen,125,75,400,200,split_text(welcome_con,400))
                elif pygame.time.get_ticks() - start_time < 10000:
                  screen.blit(m1c2, (0, 0))
                  screen.blit(assistent,(0,0))
                  if not flag_6 :
                    screen.blit(assistent,(0,0))
                    draw_dialog_box(screen,125,75,500,200,split_text(ask_con,500),20)
                    flag_6 = True
                  else:
                    draw_dialog_box(screen,125,75,500,200,split_text(ask_con,500))
                elif pygame.time.get_ticks() - start_time < 15000:
                  screen.blit(m1c2, (0, 0))
                  if not flag_7:
                    draw_dialog_box(screen,125,75,500,300,split_text(reply_con,500),20)
                    flag_7 = True
                  else:
                    # draw_dialog_box(screen,125,75,300,100,split_text(reply_con,500))
                    screen.blit(m1c2, (0, 0))       
                    screen.blit(assistent,(0,0))
                    draw_dialog_box(screen,125,75,500,300,split_text(negotiate_con,500))                
                  c1_btn.draw(screen)
                  c2_btn.draw(screen)
                  c3_btn.draw(screen)
            else:
              screen.blit(m1c2, (0, 0))       
              draw_dialog_box(screen,125,75,500,300,split_text(negotiate_con,500))
              screen.blit(assistent,(0,0))
              c1_btn.draw(screen)
              c2_btn.draw(screen)
              c3_btn.draw(screen)              
        elif M1 == 9: 
            screen.blit(m1c1, (0, 0))
            if not flag_13:
              draw_dialog_box(screen,125,75,400,200,split_text(reply1_con,400),20)
              flag_13=True
            else:
                draw_dialog_box(screen,125,75,400,200,split_text(reply1_con,400))
                flag_7=False
                back_btn1.draw(screen)
        elif M1 == 10:
            screen.blit(m1c2, (0, 0))
            if not flag_14:
              draw_dialog_box(screen,125,75,500,300,split_text(reply2_con+"\n"+reply3_con,500),20)
              flag_14=True
            else:
              draw_dialog_box(screen,125,75,500,300,split_text(reply2_con+"\n"+reply3_con,500))
              next_btn3.draw(screen)
        elif M1 == 11:
            screen.blit(m1c2, (0, 0))
            if not flag_15:
              draw_dialog_box(screen,125,75,400,100,split_text(reply3_con,400),20)
              flag_15=True
            else:
              draw_dialog_box(screen,125,75,400,100,split_text(reply3_con,400))
              next_btn3.draw(screen)
        elif M1 == 12:
            # add some animation for mission completion
            screen.blit(background_2, (0, 0))
            screen.blit(assistent,(0,0))
            if not flag_16:
              draw_dialog_box(screen,125,75,300,200,split_text(completion_mssge1,300),10)
              flag_16=True
            else:
              draw_dialog_box(screen,125,75,300,200,split_text(completion_mssge1,300))
              next_btn4.draw(screen)
        elif M1 == 13:
            screen.blit(background_2, (0, 0))
            if not flag_17:
              draw_dialog_box(screen,125,75,300,100,split_text(completion_mssge2,500),10)
              flag_17=True
            else:
              draw_dialog_box(screen,125,75,300,100,split_text(completion_mssge2,500))
        elif M1 == 14:
            if pygame.time.get_ticks() - start_time < 5000:
              screen.blit(m1p2, (0, 0))
              if not flag_8 :
                draw_dialog_box(screen,125,75,300,200,split_text(reply1_20,300),10)
                flag_8=True
              else:
                draw_dialog_box(screen,125,75,300,100,split_text(reply1_20,300))
            else:
              screen.blit(m1p1, (0, 0))
              if not flag_9:               
                draw_dialog_box(screen,125,75,400,200,split_text(reply2_50,400),10)
                flag_9=True
              else:
                draw_dialog_box(screen,125,75,400,200,split_text(reply2_50,400))
                visit_env_btn.draw(screen)
        elif M1 == 15:  # env department 
            if pygame.time.get_ticks() - start_time < 5000:
              screen.blit(m1e1, (0, 0))
              if not flag_10:
                draw_dialog_box(screen,125,75,400,200,split_text(welcome_env,400),20)
                flag_10=True
              else:
                draw_dialog_box(screen,125,75,400,200,split_text(welcome_env,400))
            else:
              screen.blit(m1e2, (0, 0))
              screen.blit(assistent,(0,0))
              if flag_9:
                draw_dialog_box(screen,125,75,300,100,split_text(ask_env,300),10)
                flag_9=False
              else:
                draw_dialog_box(screen,125,75,300,100,split_text(ask_env,300))
                env_next_0.draw(screen)
        elif M1 == 16:
          screen.blit(m1e1, (0, 0))
          if not flag_18:
            draw_dialog_box(screen,125,75,400,200,split_text(reply_env,400),20)
            flag_18=True
          else:
            draw_dialog_box(screen,125,75,400,200,split_text(reply_env,400))
            env_next_1.draw(screen)
        elif M1 == 17:
            screen.blit(m1e1, (0, 0))
            screen.blit(assistent,(0,0))
            if pygame.time.get_ticks() - start_time < 5000:
              if not flag_11:
                draw_dialog_box(screen,125,75,500,300,split_text(allot_budget1,400),20)
                flag_11=True
              else:
                draw_dialog_box(screen,125,75,500,300,split_text(allot_budget1,400))
            else:
              if not flag_12:
                draw_dialog_box(screen,125,75,300,100,[f"Current Budget: {coins}Cr"],20)
              else:
                draw_dialog_box(screen,125,75,300,100,[f"Current Budget: {coins}Cr"])
                e1_btn.draw(screen)
                e2_btn.draw(screen)
                e3_btn.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_btn.draw(screen):
                START = 1
            elif back_btn.draw(screen) and START == 2:
                START = 0
            elif back_btn1.draw(screen) and (M1 == 9):
                M1 = 8
            elif enter_btn.draw(screen) and M1==0:
                START = 2
            elif mission_btn.draw(screen) and M1==0:
                START = 3
                M1=1
            elif pub_next_1.draw(screen) and M1 == 6:
                M1 = 7      
            elif m1_btn.draw(screen) and M1 == 1:
                M1 = 2
            elif next_btn1.draw(screen) and M1 == 2:       
                M1 = 3
            elif pub_next_0.draw(screen) and M1 == 3:
                M1 = 4
            elif next_btn2.draw(screen) and M1 == 4:     
                M1 = 5
            elif o1_btn.draw(screen) and M1==5:
                coins = coins - 20
                M1 = 6
            elif contr_sev_btn.draw(screen) and M1 == 7:    
                M1 = 8
            elif visit_env_btn.draw(screen) and (M1 == 5 or M1 == 14):
                M1 = 15
            elif c1_btn.draw(screen) and M1 == 8:
                trans=True
                M1 = 9
            elif c2_btn.draw(screen) and M1 == 8:
                coins = coins - 5
                M1 = 10
            elif c3_btn.draw(screen) and M1 == 8:
                coins = coins - 10
                M1 = 11
            elif next_btn3.draw(screen) and (M1 == 10 or M1 == 11):
                M1 = 12
            elif next_btn4.draw(screen) and M1 == 12:
                M1 = 13
            elif env_next_0.draw(screen) and M1 == 15:
                M1 = 16
            elif env_next_1.draw(screen) and M1 == 16:
                M1 = 17
            elif e1_btn.draw(screen) and M1==17:
                coins = coins - 5
                M1 = 12
            elif e2_btn.draw(screen) and M1==17:
                coins = coins - 10
                M1 = 12
            elif e3_btn.draw(screen) and M1==17 :
                coins = coins - 15
                M1 = 12
            elif o2_btn.draw(screen) and M1==5:
                coins = coins - 50
                M1 = 14
            elif visit_env_btn.draw(screen) and M1==14:
                M1 = 15
            elif o3_btn.draw(screen) and M1==5:
                coins=coins-70
                M1=12
            elif quit_btn.draw(screen):
                running = False
                pygame.quit()
                sys.exit()
            start_time = pygame.time.get_ticks()
    pygame.display.flip()
pygame.quit()
