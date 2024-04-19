import pygame
import sys
import math
import MenuButtons.buttons
# Initialize Pygame
pygame.init()
#game coins
coins = 100
# Set up the screen
WIDTH, HEIGHT = 1920,1080
# screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
# pygame.display.set_caption("Greenerie Rescue: The Mayor's Mission")
buttons=MenuButtons.buttons
# ##BUTTONS
pub_assistent = pygame.image.load('./Images/Characters/pub_assistent.png')
pub_assistent = pygame.transform.scale(pub_assistent, (150,150))
env_assistent = pygame.image.load('./Images/Characters/env_assistent.png')
env_assistent = pygame.transform.scale(env_assistent, (150,150))
con_assistent = pygame.image.load('./Images/Characters/con_assistent.png')
con_assistent = pygame.transform.scale(con_assistent, (150,150))

tp1= pygame.image.load('./Images/Characters/tp1.png')
tp1= pygame.transform.scale(tp1,(150,150))
menu_btn = pygame.image.load('./Images/Buttons/menu_btns/menu_btn.png')
menu_btn= buttons.Button(1450,10,menu_btn,0.5)
background_1 = pygame.image.load('./Images/Background/home_2.png')
background_1 = pygame.transform.scale(background_1, (WIDTH, HEIGHT))
m2p1 = pygame.image.load('./Images/Background/m1_pub1.png')
m2p1 = pygame.transform.scale(m2p1, (WIDTH, HEIGHT))
m2p2 = pygame.image.load( './Images/Background/m1_pub2.png')
m2p2 = pygame.transform.scale(m2p2, (WIDTH, HEIGHT))
m2d1 = pygame.image.load( './Images/Background/dr1.png')
m2d1 = pygame.transform.scale(m2d1, (WIDTH, HEIGHT))
m2d2 = pygame.image.load( './Images/Background/dr2.png')
m2d2= pygame.transform.scale(m2d2, (WIDTH, HEIGHT))
im1 = pygame.image.load('./Images/Buttons/button_start-game.png')
e1 = pygame.image.load( './Images/Background/m1_env1.png')
e1 = pygame.transform.scale(e1, (WIDTH, HEIGHT))
e2 = pygame.image.load('./Images/Background/m1_env2.png')
e2 = pygame.transform.scale(e2, (WIDTH, HEIGHT))
cn1 = pygame.image.load( './Images/Background/m1_con1.png')
cn1 = pygame.transform.scale(cn1, (WIDTH, HEIGHT))
cn2= pygame.image.load( './Images/Background/m1_con2.png')
cn2 = pygame.transform.scale(cn2, (WIDTH, HEIGHT))
start_btn = buttons.Button(380, 450, im1, 0.5)
im2 = pygame.image.load('./Images/Buttons/button_back.png')
back_btn = buttons.Button(320, 750, im2, 0.5)
back_btn1 = buttons.Button(320, 490, im2, 0.5)
back_btn2 = buttons.Button(220,490,im2,0.5)
im3 = pygame.image.load('./Images/Buttons/button_enter.png')
enter_btn = buttons.Button(500, 490, im3, 0.5)
im4 = pygame.image.load('./Images/Buttons/button_exit.png')
quit_btn = buttons.Button(300, 490, im4, 0.5)
im5 = pygame.image.load('./Images/Buttons/button_enter-story.png')
mission_btn = buttons.Button(550, 490, im5, 0.5)
im6 = pygame.image.load('./Images/Buttons/button_resume.png')
resume_btn = buttons.Button(320, 490, im6, 0.5)
# im7 = pygame.image.load('./button_continue.png')
# continue_btn = buttons.Button(320, 490, im6, 0.5)
im7 = pygame.image.load('./Images/Buttons/button_complete.png')
continue_btn = buttons.Button(550, 490, im7, 0.5)
m2i1 = pygame.image.load('./Images/Background/m2i1.png')
m2i1= pygame.transform.scale(m2i1, (WIDTH, HEIGHT))
m2i2 = pygame.image.load('./Images/Background/m2i2.png')
m2i2= pygame.transform.scale(m2i2, (WIDTH, HEIGHT))
m2_btn = pygame.image.load('./Images/Buttons/button_enter.png')
m2_btn  = buttons.Button(500, 520, m2_btn, 0.5)
m2n1= pygame.image.load('./Images/Buttons/button_next.png')
next_btn = buttons.Button(500, 490,m2n1, 0.5)
next_btn1 = buttons.Button(500, 490,m2n1, 0.5)
next_btn2= buttons.Button(500, 490,m2n1, 0.5)
skip_btn = buttons.Button(200,490,m2n1,0.5)
visit_env0 = pygame.image.load('./Images/Buttons/button_env-dept.png')
visit_env =buttons.Button(150, 490,visit_env0, 0.5)
visit_env1 =buttons.Button(250, 490,visit_env0, 0.5)
con_sev = pygame.image.load('./Images/Buttons/button_con-service.png')
con_sev = buttons.Button(350,490,con_sev, 0.5)
visit_pub = pygame.image.load('./Images/Buttons/button_pub-dept.png')
visit_pub = buttons.Button(550, 490,visit_pub, 0.5)
env_pub= pygame.image.load('./Images/Buttons/pub_env.png')
env_pub = buttons.Button(750,490,env_pub,0.5)
m2e1  = pygame.image.load("./Images/Buttons/10.png")     
m2e2  = pygame.image.load("./Images/Buttons/20.png") 
m2e3 = pygame.image.load('./Images/Buttons/30.png')
cb1= pygame.image.load('./Images/Buttons/5.png')
cb2= pygame.image.load('./Images/Buttons/15.png')
cb3= pygame.image.load('./Images/Buttons/60.png')
cb4 = pygame.image.load('./Images/Buttons/40.png')
cb5= pygame.image.load('./Images/Buttons/50.png')
cb6= pygame.image.load('./Images/Buttons/70.png')
m2c1  = buttons.Button(320, 490,cb1, 0.5)
m2c2  = buttons.Button(420, 490,m2e1, 0.5)
m2c3 = buttons.Button(520, 490,cb2, 0.5)
m2c4 = buttons.Button(320,490,m2e2,0.5)
m2c5 = buttons.Button(420,490,m2e3,0.5)
m2c6 = buttons.Button(520,490,cb4,0.5)
m2e1= buttons.Button(320, 490,m2e1, 0.5)
m2e3 = buttons.Button(520,490,m2e3 , 0.5)
m2e2 = buttons.Button(420, 490,m2e2, 0.5)
m2e6 = buttons.Button(620,490,cb3,0.5)
m2e5=buttons.Button(520,490,cb5,0.5)
m2e4=buttons.Button(420,490,cb4,0.5)
p1 = buttons.Button(320,490,cb5,0.5)
p3 = buttons.Button(520,490,cb3,0.5)
p2 = buttons.Button(420,490,cb4,0.5)
##mission2
##intro 
intro_dialog= "Your Mission One has completed and town folks are discussig our work positively so far ...  but don't get distraced, we have another mission for  to complete..."
prev_text1="As the newly appointed mayor of Greenerie, you're faced with a monumental task: to restore the once-pristine River Verda, now choked with pollution from industrial waste. The river, once a lifeline for the community, has become a symbol of environmental degradation and neglect."
prev_text3=f'So now we have allocated budgets to  public department and environment department we need to visit either of them to start our river cleanup program and ask for their help'
prev_text2="Your mission begins with rallying the community and collaborating with environmental agencies to launch a massive cleanup effort. Volunteers, activists, and concerned citizens join forces as cleanup crews, confronting the grim reality of toxic chemicals, dead fish, and the stench of decay. Despite the challenges, you press on, implementing measures to prevent further contamination and inspiring hope amidst resistance from powerful corporations and bureaucratic hurdles."

visit_text = "Explore the Riverbank Areas and talk to town folks about thier Concerns."
welcome_tp ="Mayor, it's a pleasant surprise to have you with us today. Your presence is indeed unexpected, but most welcome!"
assistent_tp = "We're grateful for your time,it's ou r responsibility to ensure the well-being of our townspeople through regular check-ins"
ask_op1= " Our visit is to learn about the current state of river pollution."
reply_tp1 = "Thank you, Mayor, for reaching out and prioritizing our concerns. We've noticed an increase in trash and chemicals in the river lately, impacting both wildlife and water quality. It's reassuring to know that you're taking action to address this issue."
ask_op2 = "Tell us about your self."
reply_tp2= "Sure, Mayor . I work as a teacher at the local elementary school, and I'm passionate about education. My family and I enjoy spending weekends hiking in the nearby mountains. We love our town and want to see it thrive for generations to come."
visit_pub_op = "Visit Public Department and ask for help."
visit_env_op = "Visit Public Department and ask for help."
##description
##visit public department -> 
welcome_pub="welcome and congrats for cleaning the streets ,mayor!. I heard you've been working on the river cleanup."
ask_pub = "Thank You ,but our work isn't done yet. we need to arrange the river cleanup programm and we need your help."
##p1c2 
reply_pub01="Absolutely, we've received numerous complaints about river pollution, and it's imperative that we take immediate action..."
reply_pub02=" we've also  received numerous complaints about river pollution, and it's imperative that we take immediate action..."
reply_pub0 = "However, The budget you alloted isn't sufficient enough for public department to do task alone we'll need some help."
##options
##visit environment department:
welcome_env = "Welcome to environment department ,mayor !. I heard you've been working on the river cleanup programm."

ask_env0 = "Yes, and your involvement in the river cleanup program would greatly enhance our efforts. Your support is crucial in making this initiative a success."

ask_env_op2= "Tell us about your recent works"
ask_env_op1 ="Would you be willing to  help clean the river?"
reply_env_op2 = "Thank you for your interest. Recently, we've been conducting water quality assessments along the river, identifying pollution sources, and collaborating with local stakeholders to develop strategies for mitigating contamination. We've also initiated public awareness campaigns to educate residents about the importance of preserving our waterways. These efforts are essential steps toward achieving our goal of a cleaner and healthier environment for our community."
reply_env0 = "Certainly, we're eager to collaborate. However, it's essential to allocate a budget for this endeavor to ensure its successful implementation. Once the budget is secured, we can proceed with planning and executing the river cleanup program effectively."
reply_env01="We've been informed with concerns regarding river pollution, emphasizing the urgency for swift action. It's crucial that we address this issue promptly to safeguard our environment and community health"
allot_budget1 = "Allot budget for this task to the Environmental Protection department but remember that once budget alloted your cost will be reduced by that amount and you won't be able to allot more budget or take it :"
##if alloted is 40
reply_env1 = "Our workers inspected the wastes in streets, and since the situation is worse than we thought, we'll need to seek help from Contracted Service Providers."
con_visit  = "visit contracted Service Providers department"
env_visit  = "Let's discuss about this to Environment Services department"
pub_visit = "visit Public Services department"
welcome_con = "Welcome to contracted Service Providers department ,mayor !. I heard you've been working on the river cleanup"

ask_con = "Absolutely, we're currently spearheading the river cleanup initiative. Your participation in this  would be greatly appreciated. We're extending this invitation to collaborate and contribute your expertise towards the success of the program."
ask_con_op1= "Can you share details about your team's manpower?"
reply_con_op1= "Absolutely, our department have a proficient team equipped with the necessary skills and experience to contribute effectively to the river cleanup programm. With a strong workforce at our disposal, we're poised to make significant strides in restoring the river's health. Let's explore how we can synergize our efforts for maximum impact."
reply_con =  "Gladly! let's but we need to pay our workers a small amount of money to do this task." 
negotiate_con = "Negotiate with Contracted Service Providers to get the amount of money they need to do this task."

## if con alloted is 10 
reply_con1 = "Hmm ... , although money is not enough we should be able to perform task within  a month . let us discuss with environmental department and then we'll start the work."
##if con alloted is 20:
reply_con2 = "I guess we have no choice then , let us discuss with environment department and then we'll start the work ."
reply_con3 = "Okay , We'll complete the task within 2 weeks."
complete_m2 = "mission 2 complete"
##if alloted is 50 :
reply_env2 = "Thank You , please let us discuss with public department how we should distribute the money once done we'll start the cleanup programm instantly"
reply_env3 = "Okay then , we'll complete the task within  3 weeks "
##if alloted is 60 : 
reply_env4 = "Okey then , since public department is running low on money we've decided to do this task by ourselves , we'll complete the task within 3  weeks. "

##taking a direct visit to contract service providers 
reply_con4 =  "Gladly! let's but we need to pay our workers a small amount of money to do this task , our demand is 40L (Negotiate with contract service)" 
##if 40 reply3 if 30 or 20 reply1
##p1c2 - (same process)

#p2e1 -> visit the public department or visit the environment department

## if public department is visited:
## 1. welcome_pub -> ask_pub ->  
reply_pub1 = "Gladly! but we suggst asking environment depatment or contracted service providers department to see if they can help "

ask_pub0  = "Visit enviornment department , Contracted service providers or do it without any help. "

## visit enviornment department:

#welcome env -> ask_env - >reply_env5 ->reply_en3 
reply_env5=  "Thank You , please let us discuss with public department how we should distribute the money once done we'll start the cleanup programm instantly"

## visit contracted service providers:

#welcome_con -> ask_con -> reply_con4 

## if alloted money is 10L ->reply_env4 -> reply_con3 
## if alloted money is 20L ->reply_env5 -> reply_con3
## if alloted money is 30 L ->reply_env5 ->reply_con3 

## do it with env depatment :
reply_env4 = "Our workers inspected the wastes in water, and since the situation is worse than we thought, we'll need to seek help from Contracted Service Providers."
## visit contracted service providers department 

## if alloted is 20  complete task 
reply_con5 = "Hmm ... , although money is not enough we should be able to perform task within  a month . let us discuss with environment service department  and then we'll start the work."
## if alloted is 30 
reply_con6 = "Hmm ... , although money is not enough we should be able to perform task within  a month . let us discuss with environment service department  and then we'll start the work."
## if alloted is 40 
reply_con7 = "since , environment department is running low on money we've diced to do this task by ourselves , we'll complete the task within 3  weeks. "


### do it with contracted service department :
## options : 30 40 60 
### if 40 or 60 
### if 30 
reply_con8 = "Hmm ... , although money is not enough we should be able to perform task within  a month ... ,Okay  then we'll start the work."



### p2e2

## visit public department ->  keep public department visits same change the environment  

## visit env 

## do it without any help 
## if 20  or 30 
reply_con9= "Hmm.. , We've decided to do this task with help of public department , it should be  completed within 2 weeks."


## if 40 
reply_con10 = "Okay , then since money is enough to do this task by ourselves we don't need any help from environment department , We'll complete the work within a month."


### if p2e3 same  as p2e2 

## p3



## e1
## visit environment department 

reply_env7 = "Our workers inspected the wastes in water, and since the situation is worse than we thought, we'll need to seek help from Contracted Service Providers or public department ."
reply_env8 = "Our workers inspected the wastes in water, and since the situation is worse than we thought, we'll need to seek help from  public department ."

reply_env6 ="Sure, please hold off for a week while we assess the situation."
reply_env9 = "Apologies, we have some unfortunate news to share with you."
## visiting contract department 
## if 20 -> reply_con9
## if 30 -> reply_con9
## if 40 -> reply_con10 

## visitin public department
## if 20 

## visiting contract department 

## if 10 -> not enough money
## if 20 -> reply_con9
## if 30 ->  reply_con9

## if 50
## complete task dialog 
reply_pub2 = "Thank You , please let us discuss with environment department how we should distribute the money once done we'll start the cleanup programm instantly"
reply_pub3 = "Gladly, Shall we take help from environmental department ,contract service department or do this task by ourselves?."
ask_pub_op1= "Can You tell us how you would proceed  towards cleaning river?"
reply_pub_op1= "Certainly! Here's how we plan to tackle the river cleanup: First, we'll assess the extent of pollution and identify key areas needing attention. Then, we'll mobilize our team to remove debris and contaminants from the water and surrounding areas. Finally, we'll implement measures to prevent future pollution and ensure the river remains clean for generations to come."
completion_mssge1 = "Mission 2 complete:"
completion_mssge2 = "Budget and Costs:"
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 128, 0)
WHITE = (250, 250, 250)
YELLOW=(240,240,0)
GOLDEN = (128,128,0)
GREY = (169, 169, 169)
font_path = "Adventure.ttf"
# Define fonts
font = pygame.font.SysFont(font_path, 36)
font_size=36
## if 70 -> rely_con10
## complete task
## e2 
## e3 
start_time = pygame.time.get_ticks()
assistent = pygame.image.load('./Images/Characters/assistent.png')
assistent = pygame.transform.scale(assistent, (200, 200))
M1=-1
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
def draw_dialog_box(surface, x, y, width, height, text_lines, typewriter_delay=None,count_i=0):
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
    cnt=count_i
    for k,v in storage.items():
      for r in v:
        if delta_time>=typewriter_delay * cnt:
          text_surface = font.render(r, True, BLACK)
          text_rect = text_surface.get_rect(center=(x + width // 2, text_y))
          surface.fill(GREY, (text_rect.left, text_rect.top, text_rect.width, text_rect.height))
          surface.blit(text_surface, text_rect)
          cnt+=1
      text_y+=font_size+10
def draw_text(screen,text, font, color, x, y):
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
def top_row(screen,coins,costs):
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
  if costs==0:
    for i in range(5):
        pygame.draw.circle(screen, GREY, (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
  elif costs==10:
    for i in range(2):
        pygame.draw.circle(screen,GOLDEN , (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
    for i in range(2,5):
        pygame.draw.circle(screen, GREY, (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
  elif costs==15:
    for i in range(3):
        pygame.draw.circle(screen,GOLDEN , (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
    for i in range(3,5):
        pygame.draw.circle(screen, GREY, (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
  elif costs==20:
    for i in range(4):
        pygame.draw.circle(screen,GOLDEN , (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
    for i in range(4,5):
        pygame.draw.circle(screen, GREY, (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
  elif costs==25:
    for i in range(5):
        pygame.draw.circle(screen,GOLDEN , (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
  elif costs==30:
    for i in range(5):
        pygame.draw.circle(screen,GOLDEN , (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
ask = pygame.image.load('./Images/Buttons/ask.png')
ask_btn1= buttons.Button(200+10,450+10,ask,0.5)
ask_btn2 = buttons.Button(200+10,520+10,ask,0.5)
ask_btn3 = buttons.Button(200+10,620+10,ask,0.5)
ask_btn4 = buttons.Button(200+10,690+10,ask,0.5)
def ask_box(surface,x,y,width,height,text,par=0):
  shadow_surface = pygame.Surface((width, height)).convert_alpha()
  shadow_surface.fill((0, 0, 0, 180))
  # shadow_rect = pygame.Rect((2, 2), (width, height))
  # pygame.draw.rect(shadow_surface, (0, 0, 0, 100), shadow_rect)
  surface.blit(shadow_surface, (x + 2, y + 2))
  if par==0:
    ask_btn1.draw(surface)
  elif par==1:
    ask_btn2.draw(surface)
  elif par==2:
    ask_btn3.draw(surface)
  elif par==3:
    ask_btn4.draw(surface)
  text_surface = font.render(text,True,WHITE)
  text_rect = text_surface.get_rect(center=(x + width // 2, y+height//2))
  surface.blit(text_surface, text_rect)
M2 =0 
running=True
PUB1=15
ENV=0
ENV1=0
CON=0
PUB=0
c0=0
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0