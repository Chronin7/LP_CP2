import math,random
class math_functions:
    def __init__(self,function):
        self.operation=function[0]
        self.number=function[1]
    def return_mod(self,prev):
        if self.operation=="-":
            return prev-self.number
        elif self.operation=="+":
            return prev+self.number
        elif self.operation=="*":
            return prev*self.number
        elif self.operation=="/":
            return prev/self.number
class node:
    def __init__(self,destinations,math_function):