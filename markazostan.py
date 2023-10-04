
from turtle import Turtle
import pandas

class MarkazOstan:
    def __init__(self,R1):
        self.positionOstan=[]
        self.create_MARKAZ(R1)

    def create_MARKAZ(self,R2):
        for position in R2:
            self.add_circle(position)
            
    def add_circle(self,position):
        shahr=Turtle("circle")
        shahr.penup()

        shahr.color("white")
        shahr.shapesize(.5)
        shahr.goto(position)

ostan_CSV=pandas.read_csv("ostan.csv")# data
ostanha=ostan_CSV.ostan.to_list()#allstate

ostanha_x=ostan_CSV.x.to_list()
ostanha_y=ostan_CSV.y.to_list()
START_POS=[]
for i in range(len(ostanha_x)):
    START_POS.append([ostanha_x[i],ostanha_y[i]])


