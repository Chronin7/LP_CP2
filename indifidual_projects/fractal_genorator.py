import turtle
import utill_functions
def main():
    global screen
    while True:
        #choise=utill_functions.get_valid_type(int,"0 to return\n1 to draw fractal\nWhat do you want: ",valid=(0,1))
        #if choise==0:
        #    return
        #elif choise==1:
            count=utill_functions.get_valid_type(int,"What is the recursion depth that you want\n0 to return\n(dont do it too high or it will crash): ",valid=(0,100))
            if count==0:
                continue
            else:
                screen=turtle.Screen()
                turtle.clear()
                screen.ontimer(draw,0)
def draw(recursion_depth,curent_depth=1,start_point=(-500,-500),size=1000,hedding=0):
    global screen
    if curent_depth>recursion_depth:
        return
    temp_turt=turtle.Turtle("triangle")
    temp_turt.speed(0)
    temp_turt.penup()
    #temp_turt.hideturtle()
    temp_turt.goto(start_point[0],start_point[1])
    temp_turt.setheading(hedding)
    temp_turt.pendown()
    temp_turt.forward((size/curent_depth)/2)
    first_turt=temp_turt.pos()
    first_head=temp_turt.heading()
    draw(recursion_depth,curent_depth=curent_depth+1,start_point=first_turt,hedding=first_head)
    temp_turt.forward((size/curent_depth)/2)
    temp_turt.left(120)
    temp_turt.forward((size/curent_depth)/2)
    second_turt=temp_turt.pos()
    second_head=temp_turt.heading()
    draw(recursion_depth,curent_depth=curent_depth+1,start_point=second_turt,hedding=second_head+180)
    temp_turt.forward((size/curent_depth)/2)
    temp_turt.left(120)
    temp_turt.forward((size/curent_depth)/2)
    third_turt=temp_turt.pos()
    third_head=temp_turt.heading()
    draw(recursion_depth,curent_depth=curent_depth+1,start_point=third_turt,hedding=third_head)
    temp_turt.forward((size/curent_depth)/2)
    

if __name__=="__main__":
    main()