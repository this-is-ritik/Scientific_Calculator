from tkinter import *
from tkinter.ttk import *
from math import log,log10,sin,cos,tan,pi,e
import tkinter.messagebox as msgbox
root = Tk()
root.title('Calculator')
root.resizable(False, False)
root.geometry("300x200")
root.configure(background='black')



def press(val):
    expr.insert(END,str(val))


def equal():
    try:
        res=str(expr.get()).replace('^','**')
        res = eval(res)
        expr.delete(0, END)
        expr.insert(END, res)
    except SyntaxError:
        msgbox.showerror(title="Error", message='syntatically wrong expression')
    except ZeroDivisionError:
        msgbox.showerror(title="Error", message="can't divide by zero")
    except:
        msgbox.showerror(title="Error", message='unknown error')

expr = Entry(root)
expr.config(width=60)
expr.place(x=0, y=0)

# numbers

nine = Button(root, text='9', command=lambda: press(9))
nine.place(x=0, y=20)
eight = Button(root, text='8', command=lambda: press(8))
eight.place(x=75, y=20)
seven = Button(root, text='7', command=lambda: press(7))
seven.place(x=150, y=20)
six = Button(root, text='6', command=lambda: press(6))
six.place(x=0, y=40)
five = Button(root, text='5', command=lambda: press(5))
five.place(x=75, y=40)
four = Button(root, text='4', command=lambda: press(4))
four.place(x=150, y=40)
three = Button(root, text='3', command=lambda: press(3))
three.place(x=0, y=60)
two = Button(root, text='2', command=lambda: press(2))
two.place(x=75, y=60)
one = Button(root, text='1', command=lambda: press(1))
one.place(x=150, y=60)
zero = Button(root, text='0', command=lambda: press(0))
zero.place(x=75, y=80)
double_zero = Button(root, text='00', command=lambda: press('00'))
double_zero.place(x=0, y=80)

# operators
plus = Button(root, text='+', command=lambda: press('+'))
plus.place(x=225, y=20)
minus = Button(root, text='-', command=lambda: press('-'))
minus.place(x=225, y=40)
multiply = Button(root, text='*', command=lambda: press('*'))
multiply.place(x=225, y=60)
divide = Button(root, text='/', command=lambda: press('/'))
divide.place(x=225, y=80)
remainder=Button(root,text='%',command = lambda : press('%'))
remainder.place(x=225,y=103)

exponent=Button(root,text='e^x',command=lambda:press('e^'))
exponent.place(x=150,y=103)
square = Button(root, text='x^2', command=lambda: press('^2'))
square.place(x=75,y=172)

cube = Button(root, text='x^3', command=lambda: press('^3'))
cube.place(x=150, y=172)


power = Button(root, text='x^y', command=lambda: press('^'))
power.place(x=225, y=172)


# brackets
paranthesis = Button(root, text='(', command=lambda: press('('))
paranthesis.place(x=0, y=103)
paranthesis_close = Button(root, text=')', command=lambda: press(')'))
paranthesis_close.place(x=75, y=103)



# clear
def C():
    expr.delete(0,END)
clear = Button(root,text='C',command = C)
clear.place(x=0,y=126)


# backspace
def delete():
    res=expr.get()
    C()
    res=res[:-1]
    expr.insert(END,res)

backspace = Button(root,text='<-',command=delete)
backspace.place(x=75,y=126)
equal = Button(root, text='=', command=equal)
equal.place(x=150, y=80)
decimal = Button(root,text='.',command=lambda : press('.'))
decimal.place(x=150,y=126)


# scientific functions
sin_=Button(root,text='sin',command=lambda :press('sin('))
sin_.place(x=0,y=149)
cos_=Button(root,text='cos',command=lambda :press('cos('))
cos_.place(x=75,y=149)
tan_=Button(root,text='tan',command=lambda :press('tan('))
tan_.place(x=150,y=149)

pi_=Button(root,text='pi',command=lambda :press(pi))
pi_.place(x=225,y=126)

log_=Button(root,text='log',command=lambda : press('log('))
log_.place(x=225,y=149)
log10_=Button(root,text='log10',command=lambda : press('log10('))
log10_.place(x=0,y=172)


root.mainloop()