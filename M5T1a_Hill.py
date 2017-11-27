#Camron Hill
#CTI-110
#10/11/17

def main():
    #Drawing a square
    import turtle
    t = turtle.Turtle()
    t.pensize(5)
    t.pencolor("Blue")
    t.shape("turtle")
    side_length = 100;
    t.forward(side_length)          
    t.left(90)            
    t.forward(side_length)
    t.left(90)
    t.forward(side_length)
    t.left(90)
    t.forward(side_length)
    #Moving turtal 
    t.penup()
    t.forward(90)
    t.pendown()
    #Drawing a triangle
    t.forward(100)          
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
main()
            
