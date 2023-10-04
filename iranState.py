# استانهای ایران
import turtle
import pandas
from markazostan import MarkazOstan
import random as R
from maingame import First_game



screen=turtle.Screen()
screen.setup(800,600)
screen.title("IRAN")
image="IRAN2.gif"
screen.addshape(image)
turtle.shape(image) 

ostan_CSV=pandas.read_csv("ostan.csv")# dataF
ostanha=ostan_CSV.ostan.to_list()#allstate

ostanha_x=ostan_CSV.x.to_list()
ostanha_y=ostan_CSV.y.to_list()
ostanha_markaz=ostan_CSV.markaz.to_list()
print(ostanha_markaz[1])
START_POS=[]
for i in range(len(ostanha_x)):
    START_POS.append([ostanha_x[i],ostanha_y[i]])
    
#print(ostanha)
guessed_ostan=[]
MarkazOstan(START_POS)
print(len(ostanha_x))

while len(guessed_ostan)<32:
    c=turtle.Turtle()
    RAN_Markaz=R.randint(0,30)
    print(RAN_Markaz)
    pos_shansi=(int(ostanha_x[RAN_Markaz]),int(ostanha_y[RAN_Markaz]))
    City_Markaz=ostanha_markaz[RAN_Markaz]
    
    FG1=First_game(pos_shansi)
    
    answer=screen.textinput(title="استان", prompt="کدوم مرکز استانه؟")
    print(answer,City_Markaz)

        
        
    if answer == City_Markaz:
        
        guessed_ostan.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        
        #print(ostad_data.x)
        t.goto(pos_shansi)
        t.color("black")
        t.write(answer, font=20)
    else: 
        guessed_ostan.append(City_Markaz)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        
        #print(ostad_data.x)
        t.goto(pos_shansi)
        t.color("black")
        t.write(City_Markaz, font=("Arial",20))
        
            
'''   if answer in ostanha:
        guessed_ostan.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        ostan_data=ostan_CSV[ostan_CSV.ostan==answer]
        #print(ostad_data.x)
        t.goto(int(ostan_data.x),int(ostan_data.y))
        t.color("black")
        t.write(answer)'''

turtle.mainloop()