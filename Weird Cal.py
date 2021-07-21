#Calcualtor app
import tkinter as tk
from random import shuffle as rsh

nums=[]
signs=[]
firsttime=True
# button functions
def button_hit(number):
    current=e.get()
    e.delete(0,"end")
    e.insert(0,str(current)+str(number))
    numbut()
def op_hit(sign):
    global nums,signs
    nums.append(str(e.get()))
    signs.append(sign)
    print(nums,signs)
    e.delete(0,"end")
def result():
    global nums,signs,res,firsttime
    res=0
    nums.append(str(e.get()))
    print(nums,signs)
    for i in range(len(signs)):
        if i ==0 :
            exec("res="+nums[i]+signs[i]+nums[i+1],globals())
        else:
            exec("res=res"+signs[i]+nums[i+1],globals())
    e.delete(0,"end")
    e.insert(0,str(res))
    nums.clear()
    signs.clear()
    firsttime=True
    numbut()
    res=0
def clearall():
    global nums,signs,firsttime
    signs.clear()
    nums.clear()
    firsttime=True
    numbut()
    e.delete(0,"end")
# number button creation


key=[0,1,2,3,4,5,6,7,8,9]
def numbut():
    global number_list,key,firsttime
    number_list = [1,2,3,4,5,6,7,8,9,0]
    if firsttime==False:
        rsh(number_list)
    for i in range(10):
        key[i]=tk.Button(window,text=str(number_list[i]),padx=20,pady=20,command=lambda c=i:button_hit(number_list[c]))
        key[i].grid(row=int((i+3)/3),column=int(i%3))
    firsttime=False
# tkniter window
window=tk.Tk()
window.title("Weird Cal")
window.option_add('*font',25,)
window.iconbitmap("C:/Users/Arash/Pictures/Frostpunk/weirdcalcul.ico")
# display
e=tk.Entry(window,width=35,borderwidth=4)
e.grid(row=0,column=0,columnspan=3,padx=20,pady=20)
#call buttons first time
numbut()

#Operators
plus = tk.Button(window,text="+",padx=20,pady=20,command=lambda: op_hit("+"))
minus = tk.Button(window,text="-",padx=22,pady=20,command=lambda: op_hit("-"))
times = tk.Button(window,text="*",padx=22,pady=20,command=lambda: op_hit("*"))
dev=tk.Button(window,text="/",padx=20,pady=20,command=lambda: op_hit("/"))
equal=tk.Button(window,text="=",bg="green",padx=20,pady=20,command=result)
delete= tk.Button(window,text="Delete",fg="red",padx=10,pady=20,command=lambda:e.delete(0,"end"))
point=tk.Button(window,text=".",padx=23,pady=20,command=lambda:e.insert("end","."))
clear=tk.Button(window,text="Clear",fg="white",bg="red",padx=2,pady=20,command=clearall)


delete.grid(row=0,column=3)
plus.grid(row=1,column=3)
minus.grid(row=2,column=3)
times.grid(row=3,column=3)
dev.grid(row=4,column=3)
equal.grid(row=4,column=3)
point.grid(row=4,column=1)
clear.grid(row=4,column=2)




#randomizer

window.mainloop()
