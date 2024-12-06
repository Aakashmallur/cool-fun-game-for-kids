import pgzrun
import random

#screen width and height
WIDTH=500
HEIGHT=600

#TITLE OF SCREEN 
TITLE="CLICK GAME"
time_left=60
game_over=False
#BOX FOR MESSAGE
message=""
#varabel for score
score=0
#actor fucshon
alien=Actor("coolaliean.png")
#draw funcshon
def draw():
    screen.clear()
    #screen defalt
    #clear funcsh on the removes all the stuf on the screen.
    screen.fill(color=(0, 204, 122))
    alien.draw()
    screen.draw.text(message,center=(400,20),fontsize=40)
    screen.draw.text(str(score),center=(250,500),fontsize=40)
    if not game_over:
        screen.draw.text(str(time_left),topleft=(10,10),fontsize=50,color="blue")
    else:
        screen.draw.text("game over",center=(250,300),fontsize=100,color="red")
def place_alien():
    alien.x=random.randint(0,WIDTH)
    alien.y=random.randint(0,HEIGHT)


def on_mouse_down(pos):
    global message,score
    if not game_over:

    #this is a globel messge varibal-chages made wil, afect over all
        if alien.collidepoint(pos): #if we click on alean
         message="good shot!"
         score=score+1
         place_alien()
        else:
           message="you missed!"
def update_timer():
    global time_left,game_over,message
    if time_left>0:
        time_left-=1
    else:
        game_over=True
        message=""
clock.schedule_interval(update_timer,1.0)
place_alien()

pgzrun.go()