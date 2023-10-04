
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