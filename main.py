
import pygame, sys

pygame.init()
pygame.font.init()
# helpful variables
running = True
size = width, height = 900, 500
white = 255,255,255
black = 0, 0, 0
Red = 255, 0, 0
mariojump = 0
mariojumpMax = 200
luijijumpMax2 = 200
luijijump2 = 0
sky = 150, 150, 255
ground = 150, 100, 50
gravity = [0, 1]
groundpix = 30
mariolanded = False
luijilanded2 = False
marioBullet = 0
Bullettraveldistance = 0
Bullettraveldistance2 = 0
Bullettrravel = 0
luijiBullet = 0
Bullettraveldistance2 = 0
FPS = 434




MARIOHEALTH = 5
LUIJIHEALTH = 5

HP_Font = pygame.font.SysFont('arial',30)
Win_Font = pygame.font.SysFont('comicsans',100)

screen = pygame.display.set_mode(size)

pmario = pygame.image.load("pmario.gif")
pmario = pygame.transform.scale(pmario, (70, 70))
mariowin = False
luijiwin = False

pluiji = pygame.image.load("pluiji.gif")
pluiji = pygame.transform.scale(pluiji, (40, 70))
pluijiright = pluiji
pluijileft = pygame.transform.flip(pluiji, 70, 0)
pluiji = pluijileft

luijirectangle = pluiji.get_rect()
mariorectangle = pmario.get_rect()
luijirectangle = luijirectangle.move(850, 0)
mariorectangle = pygame.Rect(100, 150, 70, 70)

Bullet = pygame.image.load("fireball.gif")
Bullet = pygame.transform.scale(Bullet, (40, 40))
Bulletrect = Bullet.get_rect()
Bullet2 = pygame.image.load("fireball.gif")
Bullet2 = pygame.transform.scale(Bullet, (40, 40))
Bulletrect2 = Bullet.get_rect()
pmarioright = pmario
pmarioleft = pygame.transform.flip(pmario, 70, 0)


Pmario_Bullets = []
Pluji_Bullets = []

clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if pmario == pmarioleft:
                    directionfacing = -1
                else:
                    directionfacing = 1
                if len(Pmario_Bullets) < 3:
                    Bulletrect = pygame.Rect(mariorectangle.x + mariorectangle.width, mariorectangle.y + mariorectangle.height // 2 - 2,
                                             40, 40)
                    Pmario_Bullets.append(Bulletrect)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if pluiji == pluijileft:
                    directionfacing2 = -1
                else:
                    directionfacing2 = 1
                if len(Pluji_Bullets) < 3:
                    Bulletrect2 = pygame.Rect(luijirectangle.x + luijirectangle.width, luijirectangle.y + luijirectangle.height // 2 - 2,
                                             40, 40)
                    Pluji_Bullets.append(Bulletrect2)

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and mariolanded:
        mariojump = mariojumpMax

    if keys_pressed[pygame.K_RIGHT]:
        if mariorectangle.right < width:
            mariorectangle = mariorectangle.move([1, 0])
            pmario = pmarioright

    if keys_pressed[pygame.K_LEFT]:
        if mariorectangle.left > 0:
            mariorectangle = mariorectangle.move([-1, 0])
            pmario = pmarioleft

    if mariojump >= 0:
        mariorectangle = mariorectangle.move([0, -2])
        mariojump -= 1
        mariolanded = False
    
    if mariorectangle.bottom <= height - groundpix:
        mariorectangle = mariorectangle.move(gravity)
    if luijirectangle.bottom <= height - groundpix:
        luijirectangle = luijirectangle.move(gravity)
    if mariorectangle.bottom == height - groundpix:
        mariolanded = True
    if luijirectangle.bottom == height - groundpix:
        luijilanded2 = True


    if keys_pressed[pygame.K_w] and luijilanded2:
        luijijump2 = luijijumpMax2
    if keys_pressed[pygame.K_d]:
        if luijirectangle.right < width:
            luijirectangle = luijirectangle.move([1, 0])
            pluiji = pluijiright
    if keys_pressed[pygame.K_a]:
        if luijirectangle.left > 0:
            luijirectangle = luijirectangle.move([-1, 0])
            pluiji = pluijileft

    if luijijump2 >= 0:
        luijirectangle = luijirectangle.move([0, -2])
        luijijump2 -= 1
        luijilanded2 = False



    for Bulletrect in Pmario_Bullets:
        numberBullet1 = Pmario_Bullets[0]
        
        
        
        if Bulletrect.y > 434:
          marioBullet = 1
        if Bulletrect.y < 434 :
          marioBullet = 2
        if marioBullet == 1:
          Bulletrect.y = 434

        if marioBullet == 2:
          Bulletrect.y = Bulletrect.y + 1    
               
        
        if keys_pressed[pygame.K_DOWN] and directionfacing == 1 and len(Pmario_Bullets) == 1:
            Bullettraveldistance = 1
        elif keys_pressed[pygame.K_DOWN] and directionfacing == -1 and len(Pmario_Bullets) == 1:
            Bullettraveldistance = 2
        if Bullettraveldistance == 1:
            numberBullet1.x = numberBullet1.x + 1
        if Bullettraveldistance == 2:
            numberBullet1.x = numberBullet1.x - 1
        if numberBullet1.left == 0:
            Bullettraveldistance = 1
           
        if numberBullet1.right == 900:
            Bullettraveldistance = 2
           
        if numberBullet1.x < 0:
            numberBullet1.x = 1
        if numberBullet1.x > 900:
            numberBullet1.x = 899

        if len(Pmario_Bullets) >1:
          numberbullet2 = Pmario_Bullets[1]
          if keys_pressed[pygame.K_DOWN] and directionfacing == 1 and len(Pmario_Bullets) == 2:
              Bullettraveldistance2 = 1
          elif keys_pressed[pygame.K_DOWN] and directionfacing == -1 and len(Pmario_Bullets) == 2:
              Bullettraveldistance2 = 2
          if Bullettraveldistance2 == 1:
              numberbullet2.x = numberbullet2.x + 1
          if Bullettraveldistance2 == 2:
              numberbullet2.x = numberbullet2.x - 1
          if numberbullet2.left == 0:
              Bullettraveldistance2 = 1
              
          if numberbullet2.right == 900:
              Bullettraveldistance2 = 2
             
          if numberbullet2.x < 0:
            numberbullet2.x = 1
          if numberbullet2.x > 900:
            numberbullet2.x = 899
        if len(Pmario_Bullets) > 2:
          numberbullet3 = Pmario_Bullets[2]
          if keys_pressed[pygame.K_DOWN] and directionfacing == 1 and len(Pmario_Bullets) == 3:
              Bullettrravel = 1
          elif keys_pressed[pygame.K_DOWN] and directionfacing == -1 and len(Pmario_Bullets) == 3:
              Bullettrravel = 2
          if Bullettrravel == 1:
              numberbullet3.x = numberbullet3.x + 1
          if Bullettrravel == 2:
              numberbullet3.x = numberbullet3.x - 1
          if numberbullet3.left == 0:
              Bullettrravel = 1
              
          if numberbullet3.right == 900:
              Bullettrravel = 2
            
          if numberbullet3.x < 0:
            numberbullet3.x = 1
          if numberbullet3.x > 900:
            numberbullet3.x = 899             
        if Bulletrect.colliderect(luijirectangle):
          Pmario_Bullets.remove(Bulletrect)
          LUIJIHEALTH -= 1

#Luiji Bullets
    for Bulletrect2 in Pluji_Bullets:
        bulletlong1 = Pluji_Bullets[0]
        
        
        
        if Bulletrect2.y > 434:
          luijiBullet = 1
        if Bulletrect2.y < 434 :
          luijiBullet = 2
        if luijiBullet == 1:
          Bulletrect2.y = 434

        if luijiBullet == 2:
          Bulletrect2.y = Bulletrect2.y + 1    
               
        
        if keys_pressed[pygame.K_s] and directionfacing2 == 1 and len(Pluji_Bullets) == 1:
            Bullettraveldistance2 = 1
        elif keys_pressed[pygame.K_s] and directionfacing2 == -1 and len(Pluji_Bullets) == 1:
            Bullettraveldistance2 = 2
        if Bullettraveldistance2 == 1:
            bulletlong1.x = bulletlong1.x + 1
        if Bullettraveldistance2 == 2:
            bulletlong1.x = bulletlong1.x - 1
        if bulletlong1.left == 0:
            Bullettraveldistance2 = 1
           
        if bulletlong1.right == 900:
            Bullettraveldistance2 = 2
            
        if bulletlong1.x < 0:
            bulletlong1.x = 1
        if bulletlong1.x > 900:
            bulletlong1.x = 899



        if len(Pluji_Bullets) >1:
          bulletlong2 = Pluji_Bullets[1]
          if keys_pressed[pygame.K_s] and directionfacing2 == 1 and len(Pluji_Bullets) == 2:
              Bullettraveldistance2 = 1
          elif keys_pressed[pygame.K_s] and directionfacing2 == -1 and len(Pluji_Bullets) == 2:
              Bullettraveldistance2 = 2
          if Bullettraveldistance2 == 1:
              bulletlong2.x = bulletlong2.x + 1
          if Bullettraveldistance2 == 2:
              bulletlong2.x = bulletlong2.x - 1
          if bulletlong2.left == 0:
              Bullettraveldistance2 = 1
              
          if bulletlong2.right == 900:
              Bullettraveldistance2 = 2
            
          if bulletlong2.x < 0:
            bulletlong2.x = 1
          if bulletlong2.x > 900:
            bulletlong2.x = 899


        if len(Pluji_Bullets) > 2:
          bulletlong3 = Pluji_Bullets[2]
          if keys_pressed[pygame.K_s] and directionfacing2 == 1 and len(Pluji_Bullets) == 3:
              Bullettravel3 = 1
          elif keys_pressed[pygame.K_s] and directionfacing2 == -1 and len(Pluji_Bullets) == 3:
              Bullettravel3 = 2
          if Bullettravel3 == 1:
              bulletlong3.x = bulletlong3.x + 1
          if Bullettravel3 == 2:
              bulletlong3.x = bulletlong3.x - 1
          if bulletlong3.left == 0:
              Bullettravel3 = 1

          if bulletlong3.right == 900:
              Bullettravel3 = 2

          if bulletlong3.x < 0:
            bulletlong3.x = 1
          if bulletlong3.x > 900:
            bulletlong3.x = 899             
        if Bulletrect2.colliderect(mariorectangle):
          Pluji_Bullets.remove(Bulletrect2)
          MARIOHEALTH -= 1





    screen.fill(sky)
    screen.blit(pmario, mariorectangle)
    screen.blit(pluiji, luijirectangle)
    MarioHP = HP_Font.render("Pmario HP: "+ str(MARIOHEALTH),1,black)
    screen.blit(MarioHP,(20,15))
    LuijiHP = HP_Font.render("Pluiji HP: "+ str(LUIJIHEALTH),1,black)
    screen.blit(LuijiHP,(700,15))

  

    pygame.draw.rect(screen, ground, pygame.Rect(0, height - groundpix, width, height))

    if MARIOHEALTH == 0:
      screen.fill(white)
      PMarioWIN = Win_Font.render("PLUIJI WINS",1,black)
      screen.blit(PMarioWIN,(220,220))
      pygame.display.update()

      Pmario_Bullets.clear()
      Pluji_Bullets.clear()
      MARIOHEALTH = 5
      LUIJIHEALTH = 5

      pygame.time.delay(4340)      
    if LUIJIHEALTH == 0:  
      screen.fill(white)
      PLuijiWIN = Win_Font.render("PMARIO WINS",1,black)
      screen.blit(PLuijiWIN,(220,220))
      pygame.display.update()
      pygame.time.delay(4340) 


      Pmario_Bullets.clear()
      Pluji_Bullets.clear()
      MARIOHEALTH = 5
      LUIJIHEALTH = 5

    for Bulletrect in Pmario_Bullets:
        screen.blit(Bullet, Bulletrect)
    for Bulletrect2 in Pluji_Bullets:
        screen.blit(Bullet2, Bulletrect2)
    pygame.display.flip()

    pygame.display.update()


  
