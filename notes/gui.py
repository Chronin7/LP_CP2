#gui stands for graphic user interface
#turtle pygame pandas 3d and tkinter are all gui librarys
#it makes users happy
# a wigit is the windo thta the user interacts with
#this is how you set up a symple wqigit
import tkinter as tk #tkinter is one of pythons standerd librarby for gui
t=False
#this is how to show and hide text
def click():
    global t
    global text
    if t:
        text.pack_forget()
    else:
        text.pack()
    t=not(t)


root=tk.Tk()
text=tk.Label(root,text="The Higgs boson is the fundamental particle predicted by the Brout-Englert-Higgs mechanism.\nThis theory explains how fundamental particles acquire their mass.\nThe search for the Higgs boson is one of the most fascinating scientific adventures.\nIt started about 50 years ago and was considered impossible for decades,\nwhich is one of the main reasons the LHC was built.")
root.title("testing")
root.configure(background="orange")
root.minsize(250,250)
root.maxsize(1000,1000)
root.geometry("300x300+100+100")
lable_wigit=tk.Label(root,text="BEHOLD THE GOD PARTICLE:\nTHE HIGGS BOSON",font=("comic sans",20,"bold"))
lable_wigit.config(fg="blue",bg="orange")
lable_wigit.pack()
image=tk.PhotoImage(file="notes\img\download.png")
#this is a button
botton=tk.Button(root,text="click to see more",command=click)
botton.pack()
tk.Label(root,image=image).pack()
#everything we want to happen in here
root.mainloop()
#this keeps it on the screen 
