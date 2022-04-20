# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 08:27:19 2021

@author: peiyi
"""

import turtle, math

p=turtle.Turtle()
p.shape("classic")
p.speed(10)
p.color("black","black")
p.penup()

y_stp=-100

screen=turtle.Screen()
screen.register_shape("rectangle",((15,25),(15,-25),(-15,-25),(-15,25)))
screen.title("Projectile Simulator V1.5.2")
aux=turtle.Turtle()
aux.shape("rectangle")
aux.color("black","green")

aux.penup()
aux.goto(-140,350)
aux.pendown()
aux.write("Projectile Simulator V1.5.2",font=("arial",16))

aux.hideturtle()
aux.penup()
aux.speed(0)

aux.penup()
aux.goto(0,y_stp)
aux.showturtle()
aux.pendown()
aux.seth(0)
aux.fd(1000)
aux.bk(2000)
aux.penup()
aux.showturtle()

launch_button=aux.clone()
clear_button=aux.clone()

time_step=0.1

def move(x,y,angle,velocity,time,grav,air_res,y_stop,save):
    log_l=[]
    p.goto(x,y)
    p.pendown()
    p.stamp()
    p.setheading(angle)
    while p.ycor()>=y_stop:
        xdelta=velocity*math.cos(angle*math.pi/180)*time-(1/2)*air_res*time**2
        ydelta=velocity*math.sin(angle*math.pi/180)*time-(1/2)*grav*time**2
        xn=xdelta+x
        yn=ydelta+y
        xr=round(xn,2)
        yr=round(yn,2)
        print("({x},{y})".format(x=xr,y=yr))
        log_l.append("{x} {y}".format(x=xr,y=yr))
        p.goto(xn,yn)
        x=xn
        y=yn
        time=time+time_step
        p.stamp()
    else:
        p.penup()
        if save!="n":
            with open("{}.txt".format(save),"w") as log:
                for item in log_l:
                    log.writelines("\n{}".format(item))
                log.writelines("\n")
        p.goto(0,0)
        return None
    
def menu():
    return(
    '''
----------------------------------------------------------
Projectile Simulator Settings
- 1 to launch projectile
- 2 to change gravity and wind
- 3 to change timestep
- 4 to change starting position and angle
- 5 to change velocity
- d to display current settings
- s to change save location
- l to load file
- x to quit
----------------------------------------------------------
    ''')


grav=5
air_res=0
time_step=0.1
x_n=0
y_n=-100
angle=45
velocity=10
save="n"
   
def start():
    global x_n,y_n,angle,velocity,air_res,grav,time_step,y_stp,save
    inp=turtle.textinput("Projectile Simulator Settings",menu())
    if inp=="1":
        move(x_n,y_n,angle,velocity,0,grav,air_res,y_stp,save)
    if inp=="2":
        grav=float(turtle.textinput("Projectile Simulator Settings","new gravitational pull: "))
        air_res=float(turtle.textinput("Projectile Simulator Settings","new wind speed: "))
    if inp=="3":
        time_step=float(turtle.textinput("Projectile Simulator Settings","new timestep: "))
    if inp=="4":
        angle=int(turtle.textinput("Projectile Simulator Settings","new angle: "))
        x_n=int(turtle.textinput("Projectile Simulator Settings","new coordinate x: ")) 
        y_n=int(turtle.textinput("Projectile Simulator Settings","new coordinate y: ")) 
    if inp=="5":
        velocity=int(turtle.textinput("Projectile Simulator Settings","new velocity: "))
    if inp=="d":
        print("start: ({x},{y})".format(x=x_n,y=y_n))
        print("angle: {a}".format(a=angle))
        print("velocity: {v}".format(v=velocity))       
        print("time step: {t}".format(t=time_step))
        print("gravity: {g}".format(g=grav))
        print("timestep: {t}".format(t=time_step))
        print("ground level: {g}".format(g=y_stp))
    if inp=="l":
        name=turtle.textinput("Projectile Simulator Settings","filename: ")
        with open(name+".txt") as f:
            while True:
                pass
    if inp=="s":
        save=turtle.textinput("Projectile Simulator Settings","save-to file name(if not wanted to save, type n): ")
    if inp=="x":
        return None
    start()

aux.showturtle()
aux.goto(-700,390)
aux.write("settings") 
aux.goto(-680,370)

launch_button.showturtle()
launch_button.goto(-700,300)
launch_button.write("launch") 
launch_button.goto(-680,280)

clear_button.showturtle()
clear_button.goto(-700,210)  
clear_button.write("clear") 
clear_button.goto(-680,190)

def click_set(x,y):
    if -630>=x>=-730 and 400>=y>=340:
        start()
    if -630>=x>=-730 and 310>=y>=250:
        move(x_n,y_n,angle,velocity,0,grav,air_res,y_stp,save)
    if -630>=x>=-730 and 230>=y>=160:
        p.clear()

turtle.onscreenclick(click_set)

turtle.done()
turtle.bye()

