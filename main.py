import pygame
import sys
import os
import json

# Initialization
global screen
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("KSA Mod Creator")
clock = pygame.time.Clock()
pygame.font.init()
font1 = pygame.font.SysFont('Arial', 30)

# Classes
class Checkbox:  # WIP
  def __init__(self,x,y,scaleX,scaleY,checked=False,disabled=False,text=""):
    self.rect = pygame.Rect(x,y,scaleX,scaleY)
    self.disabled = disabled
    self.checked = checked


class Button:
  def __init__(self,x,y,scaleX,scaleY,buttonId=None,disabled=False,text=None,centerText=True):
    self.rect = pygame.Rect(x,y,scaleX,scaleY)
    self.disabled = disabled
    self.buttonId = buttonId
    self.text = text
    self.centerText = centerText

  def update(self):
    global screen
    if(self.rect.collidepoint(pygame.mouse.get_pos())):
      if(pygame.mouse.get_pressed()[0]):
        buttonPressed(self.buttonId)
      else:
        pass  # Hovered over
    pygame.draw.rect(screen, (100,100,100), self.rect)
    if(self.text is not None):
      if(self.centerText):
        screen.blit(font1.render(self.text, False, (255,0,0)), (self.rect.x+((self.rect.width-font1.size("self.text")[0])/2)-10, self.rect.y+((self.rect.height-font1.size("self.text")[1])/2)))
      else:
        screen.blit(font1.render(self.text, False, (255,0,0)), (self.rect.x, self.rect.y))


class Slider:
  def __init__(self,x,y,scaleX,minValue=0,maxValue=100,value=None,disabled=False,text=""):
    self.rect = pygame.Rect(x,y,scaleX,20)
    self.disabled = disabled
    self.sliderRect = pygame.Rect(x+5,y+5,10,10)
    self.range = (minValue,maxValue)
    if(value is None):
      self.value = minValue
    else:
      self.value = value
      
  def update(self):
    global screen
    self.value = round(((self.sliderRect.x / self.rect.width) * self.range[1]) + self.range[0], 8)
    pygame.draw.rect(screen, (150,0,0), self.rect)
    pygame.draw.rect(screen, (255,0,0), self.sliderRect)


class Text:
  def __init__(self,x,y,scaleX,scaleY,font,text,color=(255,0,0)):
    self.pos = (x,y)
    self.textSurface = None
    self.text = text
    self.color = color
    self.font = font
    
  def update(self,text=None,color=None):
    global screen
    tmpText = self.text
    tmpColor = self.color
    if(text is not None):
      tmpText = text
    if(color is not None):
      tmpColor = color
    self.textSurface = self.font.render(tmpText, False, tmpColor)
    screen.blit(self.textSurface, (self.pos[0], self.pos[1]))
    
# Main variables
global objects
global scene
global settings
objects = []
scene = None
settings = {}

# Helper functions
def loadJSON(filePath):                                                                                          # Load a JSON file
  with open(filePath) as f:
    return json.load(f)
  
def saveJSON(filePath, dataDict):                                                                                # Save a JSON file
  with open(filePath, 'w') as f:
    json.dump(dataDict,f,indent=4)

def setScene(newScene="main"):                                                                                   # Set the new active scene
  global scene
  global objects
  if(newScene == "main"):
    objects = [Text(550,10,500,30,font1,"KSA Mod Creator"),
               Button(550,300,200,40,"newMod",False,"New mod"),]
  elif(newScene == "setup"):
    objects = [Text(10,10,500,30,font1,"KSA Mod Creator Setup"),]
  else:
    print("[ERR] setScene: [newScene] is invalid! ("+str(scene)+")")
  scene = newScene

def buttonPressed(buttonId=None):                                                                                # Called when a button is pressed
  global scene
  if(scene == "main"):
    if(buttonId == "newMod"):
      if(os.path.isfile("Settings.json")):
        settings = loadJSON("Settings.json")
        setScene("newMod")
      else:
        setScene("setup")
    else:
      print('[ERR] buttonPressed: [buttonId] in scene "main" is invalid! ('+str(buttonId)+')')
      
  elif(scene == "setup"):
    if(buttonId == "done"):
      saveJSON("Settings.json", settings)
      setScene("newMod")
    else:
      print('[ERR] buttonPressed: [buttonId] in scene "setup" is invalid! ('+str(buttonId)+')')

  else:
    print("[ERR] buttonPressed: [scene] is invalid! ("+str(scene)+")")
  
setScene()

# Main cycle
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  for i in objects:
    i.update()
  
  pygame.display.flip()
  clock.tick(60)
  screen.fill("black")
