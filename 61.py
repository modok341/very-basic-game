import pygame , sys, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image=pygame.image.load(picture_path)
        self.rect=self.image.get_rect()
        self.gunshot=pygame.mixer.Sound("gun-gunshot-01.wav")
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center=pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path,pos_x,pos_y):
        super().__init__()
        self.image=pygame.image.load(picture_path)
        self.rect=self.image.get_rect()
        self.rect.center=[pos_x,pos_y]

pygame.init()
clock = pygame.time.Clock()

screen_width=1280
screen_height=720
screen=pygame.display.set_mode((screen_width, screen_height))
background=pygame.image.load("bggg.png")
pygame.mouse.set_visible(False)

crosshair=Crosshair("crosshair_red_large.png")
crosshair_group=pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group=pygame.sprite.Group()
for target in range(20):

    new_target=Target("target_red2.png",random.randrange(0,screen_width),random.randrange(0,screen_height))
    target_group.add(new_target)

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
    pygame.display.flip()
    screen.blit(background,(0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)
  
