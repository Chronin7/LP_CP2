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
                draw(count,trnlgls_count_side=2**(count-1))

def draw(recursion_depth,curent_depth=1,start_point=(-500,-500),size=500,hedding=0,trnlgls_count_side=0):
    
    global screen
    if curent_depth>recursion_depth:
        return
    smallest_size=size/recursion_depth
    temp_turt=turtle.Turtle("triangle")
    temp_turt.speed(0)
    temp_turt.penup()
    temp_turt.goto(start_point[0],start_point[1])
    temp_turt.pendown()
    temp_turt.forward(smallest_size)
    first_location=(temp_turt.xcor(),temp_turt.ycor())
    temp_turt.left(120)
    temp_turt.forward(smallest_size)
    second_location=(temp_turt.xcor(),temp_turt.ycor())
    temp_turt.left(120)
    temp_turt.forward(smallest_size)
    temp_turt.penup()
    temp_turt.goto(-1000,-1000)
    if curent_depth==1:
        draw(recursion_depth,curent_depth+1,first_location,size,hedding)
if __name__=="__main__":
    main()