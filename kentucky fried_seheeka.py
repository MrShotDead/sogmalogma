import pgzrun
import random#my goat
import time
WIDTH = 1011
HEIGHT = 600
君はすでに死んでいる = (0)
shorta_Sheeka = (0)
snooka_shoe = []
The_Old_Sheeka = []
sogma = 0
def Colonel_Harland_David_Sanders():
    global sogma
    global The_Old_Sheeka
    for i in range(8):
        not_an_actor = Actor("kuntucky_fried_satalite")
        not_an_actor.pos=random.randint(0,999),(random.randint(0,550))
        The_Old_Sheeka.append(not_an_actor)
    sogma=time.time()
    print (sogma)
def update():
    pass 
def draw():
    global 君はすでに死んでいる
    screen.blit("kentucky fried universe (20)",(0,0))
    if shorta_Sheeka<8:
        君はすでに死んでいる = time.time()-sogma
        screen.draw.text(str(君はすでに死んでいる),(400,0),color="green",fontsize=40)
    else:
        screen.draw.text(str(君はすでに死んでいる),(400,0),color="green",fontsize=40)
    for i in snooka_shoe:
        screen.draw.line(i[0],i[1],color="#007003")
    shooka_toilet = 1
    for i in The_Old_Sheeka:
        i.draw()
        screen.draw.text(str(shooka_toilet),(i.x,i.y),color="green",fontsize=40)
        shooka_toilet = shooka_toilet +1
def on_mouse_down(pos):
    global snooka_shoe
    global shorta_Sheeka
    if The_Old_Sheeka[shorta_Sheeka].collidepoint(pos):
        if shorta_Sheeka:
            snooka_shoe.append((The_Old_Sheeka[shorta_Sheeka -1].pos,The_Old_Sheeka[shorta_Sheeka].pos))
            print(snooka_shoe)
        shorta_Sheeka=shorta_Sheeka +1 #-2 feet like rl cus shes 43453434535435434534534545333333333333333333333333333333333333333.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005 Plancks









#else:
#screen.draw










Colonel_Harland_David_Sanders()
pgzrun.go()