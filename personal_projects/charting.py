import math
import turtle
def pie_chart(list_of_persentages,list_of_collors,list_of_names,x_offset,y_offset,key_offset,size,key_size):
    fred=turtle.Turtle()
    fred.speed(0)
    fred.penup()
    fred.goto(x_offset,y_offset)
    fred.pendown()
    fred.circle(size)
    fred.goto(x_offset,y_offset+size)
    last_x=x_offset
    last_y=y_offset
    for num,x in enumerate(list_of_persentages):
        fred.penup()
        fred.goto(last_x,last_y)
        fred.pendown()
        fred.color(list_of_collors[num])
        fred.begin_fill()
        fred.pendown()
        fred.circle(size,(x*3.6))
        last_x=fred.xcor()
        last_y=fred.ycor()
        fred.goto(x_offset,y_offset+size)
        fred.end_fill()
    fred.penup()
    fred.goto(key_offset[0],key_offset[1]+50)
    fred.color("black")
    fred.write("key:",font=("Arial",int(key_size*1.3),"normal"))
    fred.goto(key_offset)
    for num,x in enumerate(list_of_names):
        fred.pendown()
        fred.begin_fill()
        fred.color(list_of_collors[num])
        fred.right(90)
        fred.forward(key_size)
        fred.right(90)
        fred.forward(key_size)
        fred.right(90)
        fred.forward(key_size)
        fred.right(90)
        fred.forward(key_size)
        fred.end_fill()
        fred.penup()
        fred.goto(key_offset[0]+key_size/.8,key_offset[1]-key_size/.9-num*40)
        fred.color("black")
        fred.write(x,align="left",font=("Arial",key_size,"normal"))
        fred.goto(key_offset[0],key_offset[1]-num*40)

list_of_persentages=[20,30,15,25,9,1]
list_of_collors=["blue","red","cyan","yellow","purple","green"]
list_of_names=["liam","bob","joe","james","dirk","fred"]
x_offset=100
y_offset=100
key_offset=(-40,-40)
size=100
key_size=30
pie_chart(list_of_persentages,list_of_collors,list_of_names,x_offset,y_offset,key_offset,size,key_size)


obj1=[30,60,70,95,29,43]
obj2=[64,82,97,19,63,81]
obj3=[16,3,62,57,41,43]
obj4=[34,81,78,43,61,3]
obj5=[16,53,84,26,35,63]
obj6=[13,71,25,34,61,23]
objs=[obj1,obj2,obj3,obj4,obj5]
graph_offset=(-300,-300)
graph_size=200

joe=turtle.Turtle()
joe.penup()
joe.speed(0)
joe.goto(graph_offset)
joe.left(90)
joe.pendown()
joe.forward(graph_size)
joe.backward(graph_size)
turtle.done()

