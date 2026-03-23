import math
import utill_functions
class circle:
    def __init__(self,val_in,name):
        val_in=[val_in[0],float(val_in[1])]
        if val_in[0] == "rad":
            self.rad=val_in[1]
            self.diam=self.rad*2
            self.cir=self.diam*math.pi
            self.area=math.pi*(self.rad**2)
        elif val_in[0] == "diam":
            self.diam=val_in[1]
            self.rad=self.diam/2
            self.cir=self.diam*math.pi
            self.area=math.pi*(self.rad**2)
        elif val_in[0]=="cir":
            self.cir=val_in[1]
            self.diam=self.cir/math.pi
            self.rad=self.diam/2
            self.area=math.pi*(self.rad**2)
        self.name=name
    def __str__(self):
        return f"""{self.name}
   _--_
 /     \\
|       |
 \\_____/
area:{self.area}\ncircumference:{self.cir}\ndiameter:{self.diam}\nradius:{self.rad}"""
class rectangle:
    def __init__(self,hight,length,name):
        self.hight=hight
        self.length=length
        self.area=self.hight*self.length
        self.perim=(self.hight*2)+(self.length*2)
        self.name=name
    def __str__(self):
        return f"""{self.name}
 ___________
|           |
|___________|
area:{self.area}\nhight:{self.hight}\nlength:{self.length}\nperimeter:{self.perim}"""
def add(*vals):
    out=0
    for x in vals:
        out+=x
    return out
class triangle:
    def __init__(self,hight,base,sides,name):
        self.hight=hight
        self.base=base
        self.area=(hight*base)/2
        self.perim=add(*sides)
        self.name=name
    def __str__(self):
        return f"""{self.name}
   /\\     
  /  \\
 /    \\  
/______\\    
area:{self.area}\nhight:{self.hight}\nlength:{self.base}\nperimeter:{self.perim}"""
def main():
    shapes=dict()
    while True:
        choise=utill_functions.get_valid_type(int,"0 to quit\n1 to add shape\n2 to choose/see shapes\nwhat do you want: ",valid=(0,2))
        if choise==0:
            return
        elif choise==1:
            choise=utill_functions.get_valid_type(int,"0 to return\n1 for circle\n2 for rectangle\n3 for triangle\nwhat do you want: ",valid=(0,3))
            if choise==0:
                continue
            elif choise==1:
                name=utill_functions.get_valid_type(str,"what is the name of this shape: ")
                mesertype=["rad","diam","cir"][utill_functions.get_valid_type(int,"1 for radius\n2 for diameter\n3 for circumference\nWhat value do you have",valid=(1,3))]
                shapes[name]=circle([mesertype,utill_functions.get_valid_type(float,f"what is the meserment for {name}: ",min_max=(1,None))],name)
                print(shapes[name])
            elif choise==2:
                name=utill_functions.get_valid_type(str,"what is the name of this shape: ")
                hight=utill_functions.get_valid_type(int,"what is the hight of the shape: ",min_max=(1,None))
                length=utill_functions.get_valid_type(int,"what is the length of the shape: ",min_max=(1,None))
                shapes[name]=rectangle(hight,length,name)
                print(shapes[name])
            elif choise==3:
                name=utill_functions.get_valid_type(str,"what is the name of this shape: ")
                hight=utill_functions.get_valid_type(int,"what is the hight of the shape: ",min_max=(1,None))
                base=utill_functions.get_valid_type(int,"what is the base of the shape: ",min_max=(1,None))
                sides=[utill_functions.get_valid_type(int,"what is the length of side 1: ",min_max=(1,None)),utill_functions.get_valid_type(int,"what is the length of side 2: ",min_max=(1,None)),utill_functions.get_valid_type(int,"what is the length of side 3: ",min_max=(1,None))]
                shapes[name]=triangle(hight,base,sides,name)
                print(shapes[name])
        elif choise==2:
            print("0 to return")
            choises=[]
            for count,key in enumerate(list(shapes.keys())):
                choises.append(key)
                print(f"{count+1} for {key}:{shapes[key].__class__.__name__}")
            choise=utill_functions.get_valid_type(int,"what do you want: ",valid=(0,count+1))
            if choise==0:
                continue
            else:
                choise=choises[choise-1]
                print(shapes[choise])
                shape1=shapes[choise]
                choise=utill_functions.get_valid_type(int,"0 to return\n1 to compare",valid=(0,1))
                if choise==0:
                    continue
                else:
                    choises=[]
                    for count,key in enumerate(list(shapes.keys())):
                        choises.append(key)
                        print(f"{count+1} for {key}")
                    choise=utill_functions.get_valid_type(int,"what do you want: ",valid=(0,count+1))
                    print(shape1)
                    print(shapes[choises[choise-1]])
if __name__=="__main__":
    main()