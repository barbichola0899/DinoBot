import pyautogui
from PIL import ImageGrab, ImageOps
from numpy import *
import time

class Dino():
    def __init__(self, replay, dino, box):
        self.dino = dino  #utilizaremos o pixel superior direito do olho como referencia
        self.replay = replay #utilizaremos a ponta da seta como referencial
        self.box = box #box = (l,h), onde l = largura e h = altura

    def DetectObstacle(self):
        area_o = (self.dino[0]+50, self.dino[1], self.dino[0] + 50 + self.box[0], self.dino[1] + self.box[1])
        image_o = ImageGrab.grab(area_o)
        gray_o = ImageOps.grayscale(image_o)
        a_o = array(gray_o.getcolors())
        s_o = a_o.sum()
        if s_o != 1375:
            return True
        
        else:
            return False

    def DetectLost(self):
        area = (self.replay[0] - 18, self.replay[1] - 9, self.replay[0] + 16, self.replay[1]+ 20)
        image = ImageGrab.grab(area)
        gray = ImageOps.grayscale(image)
        a = array(gray.getcolors())
        s = a.sum()
        if s == 1905:
            return True

        else:
            return False
    
    def DetectAve(self):
        area_a = (self.dino[0]+50, self.dino[1] - 40, self.dino[0] + 50 + self.box[0], self.dino[1] - 5 )
        image_a = ImageGrab.grab(area_a)
        gray_a = ImageOps.grayscale(image_a)
        a_a = array(gray_a.getcolors())
        s_a = a_a.sum()
        if s_a != 1655:
            return True
        else:
            return False
    def pressReplay(self):
        pyautogui.click(self.replay[0], self.replay[1])
    
    def pressSmallJump(self):
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyUp('space')

    def pressCrouch(self):
        pyautogui.keyDown('down')
        time.sleep(0.05)
        pyautogui.keyUp('down')




dino = Dino((343,231),(150,244),(40,28))
try:
    while True:      
        while not dino.DetectLost():
            if dino.DetectObstacle():
                dino.pressSmallJump()
            if dino.DetectAve():
                dino.pressCrouch()

except KeyboardInterrupt:
    pass

"""dino  = (150,244)
replay = (343,420)
ave = (168,205, 208,242)"""