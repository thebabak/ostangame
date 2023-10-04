#main game
import random as R
from turtle import Turtle
import pandas


pos_shansi=[]

class First_game:
    
    def __init__(self,R1):
        self.add_circle(R1)
        
    def add_circle(self,s1):
        
        #pos_shansi.append(RAN_Markaz)
        
        shahr=Turtle("circle")
        shahr.penup()
        shahr.color("red")
        shahr.shapesize(.5)
        shahr.goto(s1)
        
ostan_CSV=pandas.read_csv("ostan.csv")# dataF
ostanha=ostan_CSV.ostan.to_list()#allstate

ostanha_markaz=ostan_CSV.markaz.to_list()

