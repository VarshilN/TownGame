import pygame
import sys
import math
import buttons
import main

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
m2i1 = pygame.image.load('./m2i1.png')
m2i1= pygame.transform.scale(m2i1, (WIDTH, HEIGHT))
m2i2 = pygame.image.load('./m2i2.png')
m2i2= pygame.transform.scale(m2i2, (WIDTH, HEIGHT))
m2_btn = pygame.image.load('./button_enter.png')
m2_btn  = buttons.Button(500, 490, m2_btn, 0.5)
next_btn = pygame.image.load('./Button/button_next.png')
next_btn = buttons.Button(500, 490,next_btn, 0.5)
next_btn1 = buttons.Button(500, 490,next_btn, 0.5)
next_btn2= buttons.Button(500, 490,next_btn, 0.5)
next_btn3= buttons.Button(500, 490,next_btn, 0.5)
next_btn4=buttons.Button(500, 490,next_btn, 0.5)
next_btn5=buttons.Button(500, 490,next_btn, 0.5)
next_btn6=buttons.Button(500, 490,next_btn, 0.5)
next_btn7=buttons.Button(500, 490,next_btn, 0.5)
visit_env = pygame.image.load('./button_env-dept.png')
visit_env =buttons.Button(350, 490,visit_env, 0.5)
con_sev = pygame.image.load('./button_con-servie.png')
con_sev = buttons.Button(450,490,con_sev, 0.5)
m2e1  = pygame.image.load("./button-40.png")     
m2e2  = pygame.image.load("./button-50.png") 
m2e3 = pygame.image.load('./button-60.png')
m2e1= buttons.Button(320, 490,m2e1, 0.5)
m2e3 = buttons.Button(480,490,m2e3 , 0.5)
m2e2 = buttons.Button(400, 490,m2e2, 0.5)
m2c1  = buttons.Button(320, 490,m2e1, 0.5)
im7 = pygame.image.load('./button_continue.png')
continue_btn = buttons.Button(320, 490, im6, 0.5)
##mission2
##intro 
intro_dialog= "Your Mission One has completed and town folks are discussig our work positively so far ...  but don't get distraced, we have another mission for  to complete"
prev_text1="As the newly appointed mayor of Greenerie, you're faced with a monumental task: to restore the once-pristine River Verda, now choked with pollution from industrial waste. The river, once a lifeline for the community, has become a symbol of environmental degradation and neglect."
prev_text3=f'So now we have allocated budgets to  public department and environment department we need to visit either of them to start our river cleanup program and ask for their help'
prev_text2="Your mission begins with rallying the community and collaborating with environmental agencies to launch a massive cleanup effort. Volunteers, activists, and concerned citizens join forces as cleanup crews, confronting the grim reality of toxic chemicals, dead fish, and the stench of decay. Despite the challenges, you press on, implementing measures to prevent further contamination and inspiring hope amidst resistance from powerful corporations and bureaucratic hurdles."

##description
##visit public department -> 
welcome_pub="welcome and congrats for cleaning the streets ,mayor!."
ask_pub0 = "Thank   You,but our work isn't done yet. we need to arrange the river cleanup programm and we need your help."
##p1c2 
reply_pub0 = "Well , The budget you alloted isn't sufficient enough for public department to do task alone we'll need some help"
##options
##visit environment department:
welcome_env = "Welcome to environment department ,mayor !. I heard you've been working on the river cleanup programm."
ask_env0 = "Yes and we need your help for river cleanup programm. "
reply_env0 = "Gladly! but we'll need to allot budget first"
allot_budget1 = "Allot budget for this task to the Environmental Protection department but remember that once budget alloted your cost will be reduced by that amount and you won't be able to allot more budget or take it :"
##if alloted is 40
reply_env1 = "Our workers inspected the wastes in streets, and since the situation is worse than we thought, we'll need to seek help from Contracted Service Providers."
visit_con  = "visit contracted Service Providers department"
welcome_con = "Welcome to contracted Service Providers department ,mayor !. I heard you've been working on the river cleanup"

ask_con = "Yes  and we need your help for river cleanup programm. "
reply_con =  "Gladly! let's but we need to pay our workers a small amount of money to do this task." 
negotiate_con = "Negotiate with Contracted Service Providers to get the amount of money they need to do this task."

## if con alloted is 10 
reply_con1 = "Hmm ... , although money is not enough we should be able to perform task within  a month . let us discuss with environmental department and then we'll start the work."
##if con alloted is 20:
reply_con2 = "I guess we have no choice then , let us discuss with environment department and then we'll start the work ."
reply_con3 = "Okay , We'll complete the task within 2 weeks."
complete_m2 = "mission 2 complete"
complete_m2 = "Cost and Stars : "

##if alloted is 50 :
reply_env2 = "Thank You , please let us discuss with public department how we should distribute the money once done we'll start the cleanup programm instantly"
reply_env3 = "Okay then , we'll complete the task within  3 weeks "
##if alloted is 60 : 
reply_env4 = "Okey then , since public department is running low on money we've decided to do this task by ourselves , we'll complete the task within 3  weeks. "

##taking a direct visit to contract service providers 
reply_con4 =  "Gladly! let's but we need to pay our workers a small amount of money to do this task , our demand is 40L (Negotiate with contract service)" 
##if 40 reply3 if 30 or 20 reply1
##p1c3 - (same process)

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
reply_env7 = "Okay  then , shall we try to get contracted service providers for help or do it without any help?"
## do it without any help 
## if 20  or 30 
reply_con9= "Hmm.. , We've decided to do this task with help of public department , it should be  completed within 2 weeks."

## if 40 
reply_con10 = "Okay , then since money is enough to do this task by ourselves we don't need any help from environment department , We'll complete the work within a month."


### if p2e3 same  as p2e2 

## p3



## e1
## visit environment department 

reply_env6 = "Our workers inspected the wastes in water, and since the situation is worse than we thought, we'll need to seek help from Contracted Service Providers or public department ."

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
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 128, 0)
WHITE = (250, 250, 250)
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
assistent = pygame.image.load('./assistent.png')
assistent = pygame.transform.scale(assistent, (200, 200))

START = 0
M2 =0 
running=True
flag_1=False
flag_2=False
flag_3=False
flag_4= False
flag_5=False
flag_6 = False
start_time = pygame.time.get_ticks()
while running:
  if M2==0:
    screen.blit(main.background_1, (0, 0))
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 80))
    screen.blit(overlay, (0, 0))
    main.draw_text("Air Quality (AQ): ", font, GREEN, 50, 280)
    for i in range(5):
        pygame.draw.circle(screen, GREY, (300 + i * 40, 300), 10)
        pygame.draw.circle(screen, BLACK, (300 + i * 40, 300), 10, 2)
    main.draw_text("Water Quality (WQ): ", font, GREEN, 50, 330)
    for i in range(5):
        pygame.draw.circle(screen, GREY, (350 + i * 40, 350), 10)
        pygame.draw.circle(screen, BLACK, (350 + i * 40, 350), 10, 2)
    main.draw_text("Waste Management (WM): ", font, GREEN, 50, 380)
    for i in range(5):
        pygame.draw.circle(screen, GREY, (435 + i * 40, 400), 10)
        pygame.draw.circle(screen, BLACK, (435 + i * 40, 400), 10, 2)
    main.draw_text(f"Coins: {coins}Cr", font, GOLDEN, 50, 450)
    db_width = 800
    db_height = 200
    screen.blit(assistent, (0,0))
    main.draw_dialog_box(screen,125,75, db_width, db_height, main.split_text(intro_dialog,800))
    back_btn.draw(screen)
    enter_btn.draw(screen)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if enter_btn.draw(screen):
            M2=1
    start_time=pygame.time.get_ticks()
  pygame.display.flip()
pygame.quit()