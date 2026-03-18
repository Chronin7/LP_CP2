import turtle
import utill_functions
import gc
def main():
    while True:
        try:
            turtle.bye()
        except:
            pass
        choise=utill_functions.get_valid_type(int,"0 to return\n1 to draw a sierpinski triangle\n2 to set background color\nWhat do you want: ",valid=(0,3))
        turtle.TurtleScreen._RUNNING=True
        turtle.Turtle._screen=None
        screen = turtle.Screen()
        if choise==0:
            return
        elif choise in [1]:
            size=300
            count=utill_functions.get_valid_type(int,"What is the recursion depth that you want\n0 to return\n(dont do it too high or it will crash): ",valid=(0,100))
            if count==0:
                continue
            collor=utill_functions.get_valid_type(str,"What color do you want\n0 to return: ",valid=["red", "blue", "green", "black", "white", "yellow", "purple", "pink", "orange", "cyan", "magenta", "brown", "grey","0"])
            if collor=="0":
                continue
            else:
                angle=[120,30][choise-1]
                start=(-100,100)
                #screen.tracer(0,0)
                temp_turt=turtle.Turtle("triangle")
                temp_turt.setundobuffer(None)
                draw(count,temp_turt,size=size,color=collor,angle=angle,start_point=start,trng=choise-1)
                if not choise:
                    temp_turt.hideturtle()
                    temp_turt.speed(0)
                    temp_turt.penup()
                    temp_turt.color(collor)
                    temp_turt.goto(start[0]-size/2,start[1]-size/1.15)
                    temp_turt.pendown()
                    temp_turt.setheading(0)
                    temp_turt.forward(size*2)
                    temp_turt.left(angle)
                    temp_turt.forward(size*2)
                    temp_turt.left(angle)
                    temp_turt.forward(size*2)
                #screen.update()
                if utill_functions.get_valid_type(int,"0 to continue\n1 to save image\nwhat do you want: ",valid=(0,3)):
                    screen.getcanvas().postscript(f"{utill_functions.get_valid_type(str,"what is the name of your esp: ").lower().strip().replace(" ","_").replace("\\","").replace("/","").removesuffix(".exp")}.esp")
                turtle.exitonclick()
        elif choise==2:
            collor=utill_functions.get_valid_type(str,"What color do you want\n0 to return: ",valid=["red", "blue", "green", "black", "white", "yellow", "purple", "pink", "orange", "cyan", "magenta", "brown", "grey","0"])
            if collor=="0":
                continue
            screen.bgcolor(collor)
def draw(recursion_depth,temp_turt,curent_depth=1,start_point=(0,0),size=300,hedding=0,color="black",angle=120,trng=0):
    global screen
    if curent_depth>recursion_depth:
        return
    if curent_depth%2==0 and not trng:
         hedding-=60
    else:
         hedding-=60
    forward=size/(2**curent_depth)
    temp_turt.color(color)
    temp_turt.speed(0)
    temp_turt.hideturtle()
    temp_turt.penup()
    temp_turt.goto(start_point[0],start_point[1])
    temp_turt.setheading(hedding)
    temp_turt.pendown()
    temp_turt.forward(forward)
    print(not trng)
    if not trng:
        first_turt=temp_turt.pos()
        first_head=temp_turt.heading()
        temp_turt.forward(forward)
        temp_turt.left(angle)
        temp_turt.forward(forward)
        second_turt=temp_turt.pos()
        second_head=temp_turt.heading()
        temp_turt.forward(forward)
        temp_turt.left(angle)
        temp_turt.forward(forward)
        third_turt=temp_turt.pos()
        third_head=temp_turt.heading()
        temp_turt.forward(forward)
        draw(recursion_depth,curent_depth=curent_depth+1,start_point=third_turt,hedding=third_head-60,color=color,angle=angle,temp_turt=temp_turt)
        draw(recursion_depth,curent_depth=curent_depth+1,start_point=first_turt,hedding=first_head-60,color=color,angle=angle,temp_turt=temp_turt)
        draw(recursion_depth,curent_depth=curent_depth+1,start_point=second_turt,hedding=second_head-60,color=color,angle=angle,temp_turt=temp_turt)
    else:
        second_turt=temp_turt.pos()
        second_head=temp_turt.heading()
        for x in range(recursion_depth-curent_depth):
            draw(recursion_depth,curent_depth=curent_depth+1,start_point=second_turt,hedding=second_head/(recursion_depth-curent_depth)*x,color=color,angle=angle,temp_turt=temp_turt,trng=trng)



if __name__=="__main__":
    main()

