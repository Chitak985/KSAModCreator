import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("KSA Mod Creator")
clock = pygame.time.Clock()
pygame.font.init()
running = True
font1 = pygame.font.SysFont('Comic Sans MS', 30)

class Checkbox:
  def __init__(self,x,y,scaleX,scaleY,checked=False,text=""):
    self.rect = pygame.Rect(x,y,scaleX,scaleY)
    self.checked = checked
    

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pass
  
  screen.fill("purple")
  pygame.display.flip()
  clock.tick(60)

pygame.quit()
