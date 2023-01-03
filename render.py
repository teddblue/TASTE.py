from tkinter import *
from turtle import RawTurtle, TurtleScreen
from PIL import Image

window = Tk()
window.title('TASTE renderer')
window.geometry('256x240+8+8')

def DrawBlocks(Tiles):
        x = 0
        y = 0
        for i in Tiles["InFrame"]:
                x += 1
                if(x > (256/16)):
                        x = 0
                        y += 1

def DrawFrame(Tiles):
        DrawBlocks(Tiles)
window.mainloop()
