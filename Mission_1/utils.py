
import pygame
import MenuButtons.buttons
pygame.init()
buttons=MenuButtons.buttons

im2 = pygame.image.load('./Images/Buttons/button_back.png')
back_btn = buttons.Button(320, 490, im2, 0.5)
im3 = pygame.image.load('./Images/Buttons/button_enter.png')
enter_btn = buttons.Button(500, 490, im3, 0.5)
im4 = pygame.image.load('./Images/Buttons/button_exit.png')
quit_btn = buttons.Button(300, 490, im4, 0.5)
im5 = pygame.image.load('./Images/Buttons/button_enter-story.png')
mission_btn = buttons.Button(550, 490, im5, 0.5)
im6 = pygame.image.load('./Images/Buttons/button_resume.png')
resume_btn = buttons.Button(320, 490, im6, 0.5)
im7 = pygame.image.load('./Images/Buttons/button_continue.png')
continue_btn = buttons.Button(320, 490, im6, 0.5)
im1 = pygame.image.load('./Images/Buttons/button_start-game.png')
start_btn = buttons.Button(650, 550, im1, 0.5)

##Game_State
START = 0
MISSION=0
INTERVAL_SECONDS=5
WIDTH,HEIGHT=1920,1080
# Load background images
background_0 = pygame.image.load('./Images/Background/home_1.png')
background_0 = pygame.transform.scale(background_0, (WIDTH, HEIGHT))
background_1 = pygame.image.load('./Images/Background/home_2.png')
background_1 = pygame.transform.scale(background_1, (WIDTH, HEIGHT))
background_2 = pygame.image.load('./Images/Background/mayor_office.png')
background_2 = pygame.transform.scale(background_2, (WIDTH, HEIGHT))
background_3 = pygame.image.load('./Images/Background/home_screen.png')
background_3 = pygame.transform.scale(background_3, (WIDTH, HEIGHT))
assistent = pygame.image.load('./Images/Characters/assistent.png')
assistent = pygame.transform.scale(assistent, (200,200))
pub_assistent = pygame.image.load('./Images/Characters/pub_assistent.png')
pub_assistent = pygame.transform.scale(pub_assistent, (150,150))
env_assistent = pygame.image.load('./Images/Characters/env_assistent.png')
env_assistent = pygame.transform.scale(env_assistent, (150,150))
con_assistent = pygame.image.load('./Images/Characters/con_assistent.png')
con_assistent = pygame.transform.scale(con_assistent, (150,150))

c1 = pygame.image.load( './Images/Background/m1_con1.png')
c1 = pygame.transform.scale(c1, (WIDTH, HEIGHT))
c2 = pygame.image.load( './Images/Background/m1_con2.png')
c2 = pygame.transform.scale(c2, (WIDTH, HEIGHT))
#CONTINUE
CONTINUE=0
#mission_1

##completion of mission

#STATE
M1 =0
m1i1 = pygame.image.load('./Images/Background/m1_0.png')
m1i1 = pygame.transform.scale(m1i1, (WIDTH, HEIGHT))
m1i2 = pygame.image.load('./Images/Background/m1_1.png')
m1i2 = pygame.transform.scale(m1i2, (WIDTH, HEIGHT))
m1i3 = pygame.image.load('./Images/Background/m1_2.png')
m1i3 = pygame.transform.scale(m1i3, (WIDTH, HEIGHT))
m1p1 = pygame.image.load('./Images/Background/m1_pub1.png')
m1p1 = pygame.transform.scale(m1p1, (WIDTH, HEIGHT))
m1p2 = pygame.image.load( './Images/Background/m1_pub2.png')
m1p2 = pygame.transform.scale(m1p2, (WIDTH, HEIGHT))
m1c1 = pygame.image.load( './Images/Background/m1_con1.png')
m1c1 = pygame.transform.scale(m1c1, (WIDTH, HEIGHT))
m1c2 = pygame.image.load( './Images/Background/m1_con2.png')
m1c2 = pygame.transform.scale(m1c2, (WIDTH, HEIGHT))
m1e1 = pygame.image.load( './Images/Background/m1_env1.png')
m1e1 = pygame.transform.scale(m1e1, (WIDTH, HEIGHT))
m1e2 = pygame.image.load('./Images/Background/m1_env2.png')
m1e2 = pygame.transform.scale(m1e2, (WIDTH, HEIGHT))

intro_dialog ="Welcome to Greenerie, Mayor! .Your mission is to reduce pollution while keeping the townspeople happy. Let's get started!"
intro_text = "In town called Greenerie, Pollution index has been severely high. As the new mayor of the town, you have the responsibility to reduce the index while keeping the needs of people living inside the town. In this journey, you'll need to negotiate with  corporate companies and other sectors of town and take initiative to clean the town. Good Luck!"
prev_text_1 = "Task: Implement regular street cleaning and litter removal programs. This will help reduce pollution and improve the quality of the streets."
prev_text_2 = "Description: Deploy cleanup crews equipped with trash pickers and garbage bags to remove litter and debris from streets, parks, and public spaces. Encourage community participation through volunteer clean-up events and neighborhood beautification projects. Impact: Improves the town's aesthetic appeal, enhances public health and safety, and prevents litter from polluting waterways and natural habitats."
visit_pub = "Let's ask Public Department for help."
ask_pub = "Ask Public Department for help with cleaning streets."
ask_about_pub = "Let' ask about working of public department."
reply_about_pub = "Welcome to Public Department, Mayor! Before we proceed, let me provide some insight into our daily operations. Our department plays a pivotal role in maintaining the functionality and well-being of our town. From overseeing infrastructure projects to ensuring public safety, our responsibilities are diverse and demanding. Each day, our team works tirelessly to address citizen concerns, respond to emergencies, and uphold the quality of life for our residents. So, when you seek our assistance, like with the recent task you mentioned, it's important to understand the scope of our capabilities and how we can best serve the community. By collaborating effectively and understanding the intricacies of our operations, we can work together to achieve our shared goals for the town."
reply_pub = "We'll need to allot some budget first for this task to the Public department."
welcome_pub = "Welcome to Public Department , Mayor!."
allot_budget = "Allot budget for this task to the Public department but remember that once budget alloted your cost will be reduced by that amount and you won't be able to allot more budget or take it :"
ask_20 = "allot 20L and ask them for help"
reply1_20 = "Ok, please wait for 2 days"
reply2_20 = "Our workers inspected the wastes in streets, and since the situation is worse than we thought, we'll need to seek help from Contracted Service Providers."
welcome_con = "Welcome to Contracted Service Providers , Mayor!."
ask_about_con = "Let's ask about working of Contract Service Providers Department"
reply_about_con = "Welcome to the Contract Service Providers Department, Mayor! Let me give you a glimpse into what we do. We're the vital link between the town and external contractors, handling everything from construction to maintenance contracts. When you enlist our help, it's crucial to grasp the intricacies of our collaboration. Each contract demands careful planning and coordination for successful outcomes. By aligning our goals, we can harness the expertise of our service providers to enhance our town's infrastructure and services effectively."
ask_con = "Ask Contracted Service Providers for help with cleaning streets"
reply_con =  "Gladly! let's but we need to pay our workers a small amount of money to do this task , our demand is 10L (Negotiate with contract service)" 
negotiate_con = "Negotiate with Contracted Service Providers to get the amount of money they need to do this task."
reply1_con = "Sorry ! it's not enough"
reply2_con = "I guess we have no choice"
reply3_con = "Okay , then we'll complete work within a week"
visit_env1 = "Visit Environment Protection Department."
welcome_env = "Welcome to Environmental Protection Department , Mayor!."
ask_env = "Ask Environmental Protection Department for help"
ask_about_env = "Let's ask  about working of Environmental Protection Department."
reply_about_env = "Welcome to the Environmental Protection Department, Mayor! Our mission is clear: safeguarding our town's natural beauty and sustainability. From monitoring air quality to waste management, we're dedicated to environmental health. When you engage us, like with your recent task, know that each effort requires careful planning and community involvement. By working together, we can ensure a greener, healthier future for our town."
reply_env = "Gladly! but we'll need to allot budget first"
allot_budget1 = "Allot budget for this task to the Environmental Protection department but remember that once budget alloted your cost will be reduced by that amount and you won't be able to allot more budget or take it :"
reply2_50 = "we'll need to seek help from environment service department"
completion_mssge1 = "Mission 1 complete:"
completion_mssge2 = "Budget and Costs:"

#mission1_buttons
m1b1 = pygame.image.load('./Images/Buttons/button_next.png')
m1_btn = buttons.Button(400, 490, m1b1, 0.5)
next_btn1 = buttons.Button(400,490,m1b1,0.5)
next_btn2 = buttons.Button(400,490,m1b1,0.5)
next_btn3 = buttons.Button(400,490,m1b1,0.5)
next_btn4= buttons.Button(400,490,m1b1,0.5)
next_btn5= buttons.Button(400,490,m1b1,0.5)
skip_btn = buttons.Button(200,490,m1b1,0.5)
pub_next_0= buttons.Button(400,490,m1b1,0.5)
pub_next_1 = buttons.Button(400,490,m1b1,0.5)
env_next_0 = buttons.Button(400,490,m1b1,0.5)
env_next_1 = buttons.Button(400,490,m1b1,0.5)
back_btn1=buttons.Button(120,490,im2,0.5)
o1b1 = pygame.image.load('./Images/Buttons/20.png')
o1b2 = pygame.image.load('./Images/Buttons/50.png')
o1b3 = pygame.image.load('./Images/Buttons/70.png')
o1b4 = pygame.image.load('./Images/Buttons/button_env.png')
o1b5 = pygame.image.load('./Images/Buttons/button_con.png')

o1b6 = pygame.image.load('./Images/Buttons/2.png')
o1c2 = pygame.image.load('./Images/Buttons/5.png')
o1c3 = pygame.image.load('./Images/Buttons/10.png')
o1e3= pygame.image.load('./Images/Buttons/30.png')
o1e4 = pygame.image.load('./Images/Buttons/40.png')
c4_btn = buttons.Button(620,490,o1b1,0.5)
o1_btn= buttons.Button(320,490,o1b1,0.5)
o2_btn = buttons.Button(420,490,o1b2,0.5)
o3_btn = buttons.Button(520,490,o1b3,0.5)
visit_env_btn = buttons.Button(600,490,o1b4,0.5)
con_sev_btn = buttons.Button(500,490,o1b5,0.5)
c1_btn = buttons.Button(320,490,o1b6,0.5)
c2_btn = buttons.Button(420,490,o1c2,0.5)
c3_btn = buttons.Button(520,490,o1c3,0.5)
e1_btn = buttons.Button(340,490,o1b1,0.5)
e2_btn = buttons.Button(440,490,o1e3,0.5)
e3_btn = buttons.Button(540,490,o1e4,0.5)
menu_btn = pygame.image.load('./Images/Buttons/menu_btns/menu_btn.png')
menu_btn= buttons.Button(1450,10,menu_btn,0.5)
# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 128, 0)
WHITE = (250, 250, 250)
YELLOW=(240,240,0)
GOLDEN = (128,128,0)
GREY = (169, 169, 169)
font_path = "ComicSansMS.ttf"
font = pygame.font.SysFont(font_path, 36)
font_size=36
start_time=pygame.time.get_ticks()
def scale_size(screen,size):
   width_scale = 1.25*screen.get_width()/1920
   height_scale = 1.25*screen.get_height()/1080
   return int(size*max(height_scale,width_scale))
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
def draw_dialog_box(surface, x, y, width, height, text_lines,start_time, typewriter_delay=None):
  x=scale_size(surface,x)
  y=scale_size(surface,y)
  width =scale_size(surface,width)
  height = scale_size(surface,height)
  shadow_surface = pygame.Surface((width, height)).convert_alpha()
  shadow_surface.fill((0, 0, 0, 0))
  shadow_rect = pygame.Rect((2, 2), (width, height))
  pygame.draw.rect(shadow_surface, (0, 0, 0, 100), shadow_rect)
  surface.blit(shadow_surface, (x + 2, y + 2))
  pygame.draw.rect(surface, GREY, (x, y, width, height))
  pygame.draw.rect(surface, BLACK, (x, y, width, height), 3)
  text_y = y + (height - (len(text_lines) * (font_size + 5))) // 2
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
    delta_time=pygame.time.get_ticks()-start_time
    cnt=0
    for k,v in storage.items():
      for r in v:
        if delta_time>=typewriter_delay * cnt:
          text_surface = font.render(r, True, BLACK)
          text_rect = text_surface.get_rect(center=(x + width // 2, text_y))
          surface.fill(GREY, (text_rect.left, text_rect.top, text_rect.width, text_rect.height))
          surface.blit(text_surface, text_rect)
          cnt+=1
      text_y+=font_size+10
def draw_text (screen, text , font, color, x, y):
      x=scale_size(screen,x)
      y=scale_size(screen,y)
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
        text_surface = font.render(line, True,color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        screen.blit(text_surface, text_rect)
        y += text_rect.height + 10 # Increase y-coordinate to add spacing between lines
def top_row(screen,coins):
    # Display Coins
    font_1=pygame.font.SysFont(font_path,50)
    draw_text(screen,f"Coins: {coins}Cr",font_1, GOLDEN, 20, 20)
    # Display AQ
    draw_text(screen,"AQ: ", font_1, DARK_GREEN, 300, 20)
    for i in range(5):
        pygame.draw.circle(screen, GREY, (365 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (365 + i * 30, 35), 10, 2)
    # Display WQ
    draw_text(screen,"WQ: ", font_1, DARK_GREEN, 500, 20)
    for i in range(5):
        pygame.draw.circle(screen, GREY, (570 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (570 + i * 30, 35), 10, 2)

    # Display WM
    draw_text(screen,"WM: ", font_1, DARK_GREEN, 700, 20)
    for i in range(5):
        pygame.draw.circle(screen, GREY, (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0