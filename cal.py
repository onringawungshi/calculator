from tkinter import*

screen=Tk()
screen.title("Calculator")
# screen.geometry("362x450")
screen.resizable(0,0)
val=""
data=StringVar()

def btnclick(number):
    global val
    val=val+str(number)
    data.set(val)


def btnClear():
    global val
    val=""
    data.set("")



def btnEqual():
    global val
    result=str(eval(val))
    data.set(result)


dispaly=Entry(screen,textvariable=data,justify="right",bg="white",font=("bold",25)).grid(row=0,columnspan=4)
 
btn1=Button(screen,text="1",font=("bold",20),height=2,width=4,command=lambda:btnclick(1)).grid(row=3,column=0) 

btn2=Button(screen,text="2",font=("bold",20),height=2,width=4,command=lambda:btnclick(2)).grid(row=3,column=1)

btn3=Button(screen,text="3",font=("bold",20),height=2,width=4,command=lambda:btnclick(3)).grid(row=3,column=2)

btn4=Button(screen,text="4",font=("bold",20),height=2,width=4,command=lambda:btnclick(4)).grid(row=2,column=0)

btn5=Button(screen,text="5",font=("bold",20),height=2,width=4,command=lambda:btnclick(5)).grid(row=2,column=1)

btn6=Button(screen,text="6",font=("bold",20),height=2,width=4,command=lambda:btnclick(6)).grid(row=2,column=2)
 
btn7=Button(screen,text="7",font=("bold",20),height=2,width=4,command=lambda:btnclick(7)).grid(row=1,column=0)

btn8=Button(screen,text="8",font=("bold",20),height=2,width=4,command=lambda:btnclick(8)).grid(row=1,column=1)
 
btn9=Button(screen,text="9",font=("bold",20),height=2,width=4,command=lambda:btnclick(9)).grid(row=1,column=2) 

btn0=Button(screen,text="0",font=("bold",20),height=2,width=4,command=lambda:btnclick(0)).grid(row=4,column=0)

btn_division=Button(screen,text="//",font=("bold",20),height=2,width=4,command=lambda:btnclick("//")).grid(row=4,column=1)

btn_Equal=Button(screen,text="=",font=("bold",20),height=2,width=4,command=btnEqual).grid(row=4,column=2)

btn_add=Button(screen,text="+",font=("bold",20),height=2,width=4,command=lambda:btnclick("+")).grid(row=1,column=3)

btn_sub=Button(screen,text="-",font=("bold",20),height=2,width=4,command=lambda:btnclick("-")).grid(row=2,column=3) 

btn_multi=Button(screen,text="*",font=("bold",20),height=2,width=4,command=lambda:btnclick("*")).grid(row=3,column=3)

btn_Clear=Button(screen,text="Clear",font=("bold",20),height=2,width=5,command=btnClear).grid(row=4,column=3)

btn_decimal=Button(screen,text=".",font=("bold",20),height=2,width=4,command=lambda:btnclick(".")).grid(row=5,column=2)

btn_double00=Button(screen,text="00",font=("bold",20),height=2,width=4,command=lambda:btnclick("00")).grid(row=5,column=1)

btn_module=Button(screen,text="%",font=("bold",20),height=2,width=4,command=lambda:btnclick("%")).grid(row=5,column=0)

btn_div=Button(screen,text="/",font=("bold",20),height=2,width=4,command=lambda:btnclick("/")).grid(row=5,column=3)
