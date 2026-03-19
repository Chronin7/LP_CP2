import math
import utill_functions
class circle:
    def __init__(self,val_in):
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
    def __str__(self):
        return f"area:{self.area}\ncircumference:{self.cir}\ndiameter:{self.diam}\nradius:{self.rad}"
class rectangle:
    def __init__(self,hight,length):
        self.hight=hight
        self.length=length
        self.area=self.hight*self.length
        self.perim=(self.hight*2)+(self.length*2)
    def __str__(self):
        return f"area:{self.area}\nhight:{self.hight}\nlength:{self.length}\nperimeter:{self.perim}"
def add(*vals):
    out=0
    for x in vals:
        out+=x
    return out
class triangle:
    def __init__(self,hight,base,sides):
        self.hight=hight
        self.base=base
        self.area=(hight*base)/2
        self.perim=add(sides)
    def __str__(self):
        return f"area:{self.area}\nhight:{self.hight}\nlength:{self.length}\nperimeter:{self.perim}"
def main():
    shapes=dict()
    while True:
        choise=utill_functions.get_valid_type(int,"0 to return\n1 for circle\n2 for rectangle\n3 for triangle\nwhat do you want: ",valid=(0,3))
        if choise==0:
            return
        elif choise==1:
            name=utill_functions.get_valid_type(str,"what is the name of this shape: ")
            mesertype=["rad","diam","cir"][utill_functions.get_valid_type(int,)]
if __name__=="__main__":
    main()