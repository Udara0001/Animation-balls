from tkinter import *
from ball import *
import time
WIDTH=500
HEIGHT=500
window=Tk()

canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

red_ball=Ball(canvas,0,0,100,1,2,"red")
green_ball=Ball(canvas,0,0,50,3,5,"yellow")
pink_ball=Ball(canvas,0,10,75,5,6,"pink")
while True:
    red_ball.move()
    green_ball.move()
    pink_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()


