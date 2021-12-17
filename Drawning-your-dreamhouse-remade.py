# %%
# %%
#Settingup
import turtle
from turtle import Screen
house=turtle.Turtle()
house.pensize(3)
house.speed(0)
screen = Screen()
screen.colormode(255)
turtle.exitonclick

#DrawningHouse

def tamgiac(tamgiaca,tamgiacb):
    house.penup()
    house.goto(-200,0)
    house.pendown()
    for i in range (3):
        house.fd(tamgiacb)
        house.lt(tamgiaca) 

def hinhbinhhanh(widthBH,lenghBH, degreeBHa, degreeBHb):
        house.fd(widthBH)
        house.lt(degreeBHa)
        house.fd(lenghBH)
        house.lt(degreeBHb)
        house.fd(widthBH/1.5)
    
def hinhchunhat(widthHCN,lengthHCN,degreeHCN):
    house.penup()
    house.goto(-200,0)
    house.pendown()
    for i in range (2):
        house.lt(degreeHCN)
        house.fd(widthHCN)
        house.lt(degreeHCN)
        house.fd(lengthHCN)

def cuaso1(widthcs, degreecs):
    house.penup()
    house.goto(-110,-50)
    house.pendown()
    for i in range (4):
       house.rt(degreecs)
       house.fd(widthcs)

def cuaso2(widthcs, degreecs):
    for i in range (3):
        house.lt(degreecs)
        house.fd(widthcs) 
  
def cuaso3(widthcs, degreecs):
    for i in range (4):
        house.rt(degreecs)
        house.fd(widthcs)

def cuaso4(widthcs, degreecs):
    for i in range (3):
        house.fd(widthcs) 
        house.rt(degreecs) 

def cuaso5(widthcs, degreecs):
    house.penup()
    house.goto(30,-50)
    house.pendown()
    for i in range (4):
       house.rt(degreecs)
       house.fd(widthcs)

def cuaso6(widthcs, degreecs):
    for i in range (3):
        house.lt(degreecs)
        house.fd(widthcs)
def cuaso7(widthcs, degreecs):
    for i in range (4):
        house.rt(degreecs)
        house.fd(widthcs)

def cuaso8(widthcs, degreecs):
    for i in range (3):
        house.fd(widthcs) 
        house.rt(degreecs) 

def door(widthdoor,lengthdoor,degreedoor):
    house.penup()
    house.goto(-10,-100)
    house.pendown()
    for i in range (2):
        house.fd(widthdoor)
        house.lt(degreedoor)
        house.fd(lengthdoor)
        house.lt(degreedoor)

def wood(widthtree,lengthtree, degreetree):
    house.penup
    house.goto(-200,-200)
    house.pendown()
    for i in range (2):
        house.fd(widthtree)
        house.rt(degreetree)
        house.fd(lengthtree)
        house.rt(degreetree)

def sun(r):
    house.penup()
    house.goto()
    house.pendown()
    house.circle(r)




if __name__ == '__main__':
    tamgiac(120,100)
    hinhbinhhanh(300,100,120,60)
    hinhchunhat(150,300,90)
    cuaso1(20,90)
    cuaso2(20,90)
    cuaso3(20,90)
    cuaso4(20,90)
    cuaso5(20,90)
    cuaso6(20,90)
    cuaso7(20,90)
    cuaso8(20,90)
    door(30,50,90)
    wood(widthtree,lengthtree, degreetree)
    #sun(r)






