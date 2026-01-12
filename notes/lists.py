#list
sibs=["tom","edd","liam","jeff","that random dude"]
print(sibs[3])
sibs[-1]="that other random dude"
frends=["tate","blain","hakwer","ben","axten","my luge sled","my legos","gretta","gaven"]
#tupples
cords=(15,72)
x,y=cords
print(x,y)
#not changeable
#cords[1]=50
#can have duplecets
#set
def replace_patch(set_name,item_name,new_name):
    set_name.remove(item_name)
    set_name.add(new_name)
collors ={"Orange","Purple","Green","Blue"}
collors.add("hot pink")
print(collors)
#it is un ordered and no duplecets (it will remove the diublec
for i in collors:
    if i == "Orange":
        print("fruit")
        i="banana"
    print(i)
print(collors)
