# استانهای ایران
import turtle
import pandas
from markazostan import MarkazOstan

screen=turtle.Screen()
screen.setup(800,600)
screen.title("IRAN")
image="IRAN2.gif"
screen.addshape(image)
turtle.shape(image) 

ostan_CSV=pandas.read_csv("ostan.csv")# data
ostanha=ostan_CSV.ostan.to_list()#allstate

ostanha_x=ostan_CSV.x.to_list()
ostanha_y=ostan_CSV.y.to_list()
START_POS=[]
for i in range(len(ostanha_x)):
    START_POS.append([ostanha_x[i],ostanha_y[i]])
    
#print(ostanha)
guessed_ostan=[]
MarkazOstan(START_POS)


while len(guessed_ostan)<32:
    c=turtle.Turtle()
        
    answer=screen.textinput(title="استان", prompt="another")
    if answer in ostanha:
        guessed_ostan.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        ostad_data=ostan_CSV[ostan_CSV.ostan==answer]
        #print(ostad_data.x)

        t.goto(int(ostad_data.x),int(ostad_data.y))
        t.color("black")
        t.write(answer)
    


turtle.mainloop()