import pygame
import MenuButtons.buttons
import sys

# Initialize Pygame
pygame.init()
#game coins
coins = 100
buttons=MenuButtons.buttons
# Set up the screen
WIDTH, HEIGHT = 1920,1080
# screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
# pygame.display.set_caption("Greenerie Rescue: The Mayor's Mission")

pub_assistent = pygame.image.load('./Images/Characters/pub_assistent.png')
pub_assistent = pygame.transform.scale(pub_assistent, (150,150))
env_assistent = pygame.image.load('./Images/Characters/env_assistent.png')
env_assistent = pygame.transform.scale(env_assistent, (150,150))
ind_assistent = pygame.image.load('./Images/Characters/ind_assistent.png')
ind_assistent = pygame.transform.scale(ind_assistent, (150,150))
assistent = pygame.image.load('./Images/Characters/assistent.png')
assistent = pygame.transform.scale(assistent, (200, 200))
menu_btn = pygame.image.load('./Images/Buttons/menu_btns/menu_btn.png')
menu_btn= buttons.Button(1450,10,menu_btn,0.5)
# ##BUTTONS
ask = pygame.image.load('./Images/Buttons/ask.png')
m3ps1 = pygame.image.load('./Images/Background/m3ps1.png')
m3ps2= pygame.image.load('./Images/Background/m3ps2.png')
m3pr1= pygame.image.load('./Images/Background/m3pr1.png')
m3pr2= pygame.image.load('./Images/Background/m3pr2.png')
m3pi1 = pygame.image.load('./Images/Background/m3pi1.png')
m3pi2 = pygame.image.load('./Images/Background/m3pi2.png')
res_btn= pygame.image.load('./Images/Buttons/menu_btns/button_restart.png')
res_btn= buttons.Button(400,500,res_btn,0.5)
m3ps1 = pygame.transform.scale(m3ps1,(WIDTH,HEIGHT))
m3ps2 = pygame.transform.scale(m3ps2,(WIDTH,HEIGHT))
m3pr1 = pygame.transform.scale(m3pr1,(WIDTH,HEIGHT))
m3pr2 = pygame.transform.scale(m3pr2,(WIDTH,HEIGHT))
m3pi1 = pygame.transform.scale(m3pi1,(WIDTH,HEIGHT))
m3pi2 = pygame.transform.scale(m3pi2,(WIDTH,HEIGHT))
background_1 = pygame.image.load('./Images/Background/home_2.png')
background_1 = pygame.transform.scale(background_1, (WIDTH, HEIGHT))
background_2 = pygame.image.load('./Images/Background/mayor_office.png')
background_2 = pygame.transform.scale(background_2, (WIDTH, HEIGHT))
m2p1 = pygame.image.load('./Images/Background/m1_pub1.png')
m2p1 = pygame.transform.scale(m2p1, (WIDTH, HEIGHT))
m2p2 = pygame.image.load( './Images/Background/m1_pub2.png')
m2p2 = pygame.transform.scale(m2p2, (WIDTH, HEIGHT))
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
m2n2= pygame.image.load('./Images/Buttons/button_env.png')
visit_btn=buttons.Button(500,520,m2n2,0.5)
next_btn = buttons.Button(500, 490,m2n1, 0.5)
next_btn1 = buttons.Button(500, 600,m2n1, 0.5)
next_btn2= buttons.Button(500, 490,m2n1, 0.5)
skip_btn = buttons.Button(200,490,m2n1,0.5)
m3e1= pygame.image.load('./Images/Buttons/button_env-dept.png')
m3e1 =buttons.Button(150, 490,m3e1, 0.5)
con_sev = pygame.image.load('./Images/Buttons/button_con-service.png')
con_sev = buttons.Button(350,490,con_sev, 0.5)
p1 = pygame.image.load('./Images/Buttons/button_pub-dept.png')
p1 = buttons.Button(550, 490,p1, 0.5)
env_pub= pygame.image.load('./Images/Buttons/pub_env.png')
env_pub = buttons.Button(750,490,env_pub,0.5)
m2e1  = pygame.image.load("./Images/Buttons/30.png")     
m2e2  = pygame.image.load("./Images/Buttons/30.png") 
m2e3 = pygame.image.load('./Images/Buttons/30.png')
m2c1  = buttons.Button(320, 490,m2e1, 0.5)
m2c2  = buttons.Button(420, 490,m2e1, 0.5)
m2c3  = buttons.Button(520, 490,m2e1, 0.5)
m2e1= buttons.Button(320, 490,m2e1, 0.5)
m2e3 = buttons.Button(480,490,m2e3 , 0.5)
m2e2 = buttons.Button(400, 490,m2e2, 0.5)
## mission_3 

intro_dialog= "Good job, Mayor!. we've completed two missions so far and won trust of many folks , but now we need to negotiate with Plastic producing industry."
prev_text1 = "Mayor, it's crucial that we address the issue of plastic production head-on. Our city is facing increasing environmental challenges due to plastic waste, and it's time we take action to mitigate its impact."

prev_text2 = "The plastic industry plays a significant role in our city's economy, but we can't ignore the negative externalities it brings. Our rivers are polluted, our streets are littered, and wildlife suffers. We must find a way to balance economic growth with environmental sustainability."

prev_text3 = "When negotiating with the plastic industry, we need to approach them with respect and understanding of their business concerns. However, we must also firmly advocate for stricter regulations on plastic usage, waste management practices, and incentivize the adoption of more sustainable alternatives. Our goal is not to stifle their business but to ensure a healthier future for our city and its inhabitants."

visit_ind = "Visit the Plastic and Goods Industry."
welcome_ind = "Welcome,Mayor!.Surprising of you to visit us... regardless we thank you for recent efforts of improving town's pollution."
ask_ind ="Certainly , We've came here with concern about recent plastic wastage found in streets and river."
reply_ind = "Ohh..,well consumption of people is certainly increasing and so is our production. it would be difficult for us to do anything about that."
ask_op1 = "Tell them to lower their emission."
ask_op2 = "Talk to them about work."

reply_ind1= "We're always looking for ways to reduce our emissions,but it's not an easy task.Perhaps you could help us find ways?"
reply_ind2 = "Our process starts with sourcing high-quality polymers like polyethylene and polypropylene from reputable suppliers known for environmental adherence. After meticulous sorting to remove impurities, materials are melted and shaped with precision molds and temperature control. Advanced machinery optimizes efficiency while minimizing energy use. Products undergo thorough quality inspections, with defective items repaired or recycled responsibly. Eco-friendly packaging is prioritized for distribution, emphasizing waste reduction. Overall, our process prioritizes quality, efficiency, and environmental sustainability, reflecting our commitment to responsible production."
ask_op3 = "ask them about sorting process."
ask_op4 = "ask them about molding process."
ask_op5 ="ask them about recycling efforts."
reply_ind3="Our sorting process is meticulous, ensuring product quality and integrity. Skilled technicians visually inspect raw materials for flaws and foreign particles. Advanced sorting equipment with sensors and algorithms detects and removes impurities. Strict quality control measures, including regular equipment maintenance, are in place. This commitment to precision reduces plastic waste and upholds sustainable manufacturing practices."
reply_ind4 = "Our molding process is pivotal, converting sorted raw materials into final products. Advanced machines ensure optimal conditions, melting materials within precision molds. Skilled technicians monitor production closely, adjusting as needed for quality. After molding, products undergo stringent inspection. We invest in R&D to optimize techniques, minimize waste, and enhance efficiency. Our commitment to sustainability is integral to our operations."

ask_ind1 ="Mayor, We'll have to find some clues for addressing issue, maybe we should take a visit to public department or environment department."

reply_ind6 = "Hmm...,We can certainly do something about that"

visit_pub ="Visit Public Department."
visit_env = "Visit Environmental Department."

welcome_pub = "Welcome,Mayor!. We heard you're trying to solve plastic wastage problem in town , we have your back please tell us anything we can do to help you."
ask_pub = "Explain and ask for their suggestion."
reply_pub0 = "They are certainly not telling us the whole story, especially when it comes to their recycling practices. It seems like there might be some issues with their recycling processes, perhaps they're not operating efficiently or effectively. It's concerning that they're not being transparent about this aspect of their operations, especially considering the importance of responsible waste management in today's environmental landscape. We need to investigate further to ensure that they're adhering to proper recycling standards and minimizing their environmental impact as they claim."
visit_env0 ="That's certainly one of the issues..."
visit_env1="perhaps,we should also discuss with environment department to find more of them."

welcome_env = "Welcome,Mayor!.Congratulations for the success of  river cleaning programm. town folks are certainly happy with current improvements happening in town."
ask_env="Yeah,but our work isn't done yet. we are trying to resolve issue of plastic wastage in town and we're trying to get some clues to address the situation to plastic industry."
reply_env0= "Hmm, we were just thinking about discussing something with you. The current wastage in rivers and streets appears to be directly linked to their practices of packaging items incorrectly and lack of thorough inspection. It's alarming to see the environmental repercussions of their negligence, as it not only contributes to plastic pollution but also poses a significant threat to ecosystems and wildlife. We must address this issue promptly to prevent further damage and ensure that they take responsibility for their actions."

visit_ind2 = "Well, now we have got the issues we can address..."
visit_ind0 = "Okay then, let's take this issues and talk to them."

welcome_ind0 = "Welcome back, Mayor!. can we do something for you?"
ask_ind2 = "Address the issues regarding packaging and recycling of items..."
reply_ind7 = "We apologize for not disclosing this earlier, but due to a shortage of budget and manpower, we've been compelled to halt certain processes temporarily. This decision is regrettable but necessary to manage our resources effectively under the current circumstances."
ask_ind3 = "Hmm..., So now we can see why there was large amount of plastic in rivers and street during cleanup programm."
reply_ind8 = "Again, We apologize for our mistakes and  troubles caused by it."
ask_ind4 = "now then,should we provide industry a little help since it can't be helped ?..."
ask_op6 = "help plastic industry with their shortage."
reply_ind9 = "we would be glad to take your help for it and we'll do our upmost to resolve this as soon as possible."
visit_pub1 = "Explain the situation to public department and ask for their help."
reply_pub1 ="Okay then, we would be funding them for some time while they're having shortage."
visit_env2 = "Explain the situation to environment department and ask for their help."
reply_env1 = "Okay then we would be giving them our workers for some time."
visit_ind1 = "After a month has passed, the shortage has been lifted, and the industry has resumed its operations, taking care ofrecycling and packaging as before. The industry extends its gratitude to you for your assistance during the challenging period, acknowledging the role your support played in overcoming the obstacles they faced."
complete_dialog = "Congratulations, Mayor! Our collaborative efforts have paid off—we've cleaned our streets, rivers, and reduced emissions. By working with public departments, the plastic industry, and environmental agencies, we've delighted the townsfolk with our progress. Let's keep up the good work for a cleaner, happier community!"
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 128, 0)
YELLOW= (240, 240, 0)
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
start_time = pygame.time.get_ticks()
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

#   pygame.draw.rect(surface, GREY, (x, y, width, height))
#   pygame.draw.rect(surface, BLACK, (x, y, width, height), 3)
#   text_y = y+(height-(len(text_lines)*(font_size+5)))//2
#   for line in text_lines:
#     draw_text(surface,line,font,WHITE,x,text_y)
#     text_y+=10
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

    ## if <20 ->1*
    ## if 20-30 ->2*
    ## if 30,35->3*
    ## if 40->4*
    ## if 45,55,60 ->5*
def top_row(screen,coins,costs,costs1):
  # Display Coins
  font=pygame.font.SysFont(font_path,50)
  draw_text(screen,f"Coins: {coins}Cr",font, GOLDEN, 20, 20)
  # Display AQ
  draw_text(screen,"AQ: ", font, DARK_GREEN, 300, 20)
  for i in range(5):
      pygame.draw.circle(screen, GREY, (365 + i * 30, 35), 10)
      pygame.draw.circle(screen, BLACK, (365 + i * 30, 35), 10, 2)
  # Display WQ
  draw_text(screen,"WQ: ", font, DARK_GREEN, 500, 20)
  if costs1<=20:
    for  i in range(1):
      pygame.draw.circle(screen, YELLOW, (570 + i * 30, 35), 10)
      pygame.draw.circle(screen, BLACK, (570 + i * 30, 35), 10, 2)
    for i in range(1,5):
      pygame.draw.circle(screen, GREY, (570 + i * 30, 35), 10)
      pygame.draw.circle(screen, BLACK, (570 + i * 30, 35), 10, 2)
  elif costs1<=30 and costs1>20:
    for  i in range(2):
      pygame.draw.circle(screen, YELLOW, (570 + i * 30, 35), 10)
      pygame.draw.circle(screen, BLACK, (570 + i * 30, 35), 10, 2)
    for i in range(2,5):
      pygame.draw.circle(screen, GREY, (570 + i * 30, 35), 10)
      pygame.draw.circle(screen, BLACK, (570 + i * 30, 35), 10, 2)
  elif costs1<=35 and costs1>30:
    for  i in range(3):
      pygame.draw.circle(screen, YELLOW, (570 + i * 30, 35), 10)
      pygame.draw.circle(screen, BLACK, (570 + i * 30, 35), 10, 2)
    for i in range(3,5):
      pygame.draw.circle(screen, GREY, (570 + i * 30, 35), 10)
      pygame.draw.circle(screen, BLACK, (570 + i * 30, 35), 10, 2)
  elif costs1<=40 and costs1>35:
    for  i in range(4):
      pygame.draw.circle(screen, YELLOW, (570 + i * 30, 35), 10)
      pygame.draw.circle(screen, BLACK, (570 + i * 30, 35), 10, 2)
    for i in range(4,5):
      pygame.draw.circle(screen, GREY, (570 + i * 30, 35), 10)
      pygame.draw.circle(screen, BLACK, (570 + i * 30, 35), 10, 2)
  elif costs1>=45:
    for  i in range(5):
      pygame.draw.circle(screen, YELLOW, (570 + i * 30, 35), 10)
      pygame.draw.circle(screen, BLACK, (570 + i * 30, 35), 10, 2)
  # Display WM
  draw_text(screen,"WM: ", font, DARK_GREEN, 700, 20)
  if costs==0:
    for i in range(5):
        pygame.draw.circle(screen, GREY, (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
  elif costs==10:
    for i in range(2):
        pygame.draw.circle(screen,YELLOW , (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
    for i in range(2,5):
        pygame.draw.circle(screen, GREY, (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
  elif costs==15:
    for i in range(3):
        pygame.draw.circle(screen,YELLOW, (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
    for i in range(3,5):
        pygame.draw.circle(screen, GREY, (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
  elif costs==20:
    for i in range(4):
        pygame.draw.circle(screen,YELLOW , (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
    for i in range(4,5):
        pygame.draw.circle(screen, GREY, (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
  elif costs==25:
    for i in range(5):
        pygame.draw.circle(screen,YELLOW , (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
  elif costs==30:
    for i in range(5):
        pygame.draw.circle(screen,YELLOW , (770 + i * 30, 35), 10)
        pygame.draw.circle(screen, BLACK, (770 + i * 30, 35), 10, 2)
M2 =0 
running=True
PUB1=0
ENV1=0
ENV=0
CON=0
PUB=0
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0
