import sys, holdings, exchange, managefunds, advicetool, miners

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import navigation_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    navigation_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    navigation_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None

def openHoldings():
    navigation_support.destroy_window()
    holdings.vp_start_gui()

def openExchange():
    navigation_support.destroy_window()
    exchange.vp_start_gui()

def openMiners():
    navigation_support.destroy_window()
    miners.vp_start_gui()

def openAdvisor():
    navigation_support.destroy_window()
    advicetool.vp_start_gui()

def manageFunds():
    navigation_support.destroy_window()
    managefunds.vp_start_gui()

class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("683x515+500+300")
        top.title("Cryptoclicker")
        top.configure(background="#aceeca")



        self.btnHoldings = Button(top)
        self.btnHoldings.place(relx=0.28, rely=0.05, height=64, width=317)
        self.btnHoldings.configure(activebackground="#79e191")
        self.btnHoldings.configure(activeforeground="#000000")
        self.btnHoldings.configure(background="#d9d9d9")
        self.btnHoldings.configure(disabledforeground="#a3a3a3")
        self.btnHoldings.configure(foreground="#000000")
        self.btnHoldings.configure(highlightbackground="#d9d9d9")
        self.btnHoldings.configure(highlightcolor="black")
        self.btnHoldings.configure(pady="0")
        self.btnHoldings.configure(text='''Holdings''')
        self.btnHoldings.configure(width=317)
        self.btnHoldings.configure(command=openHoldings)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.btnExchange = Button(top)
        self.btnExchange.place(relx=0.28, rely=0.24, height=64, width=317)
        self.btnExchange.configure(activebackground="#79e191")
        self.btnExchange.configure(activeforeground="#000000")
        self.btnExchange.configure(background="#d9d9d9")
        self.btnExchange.configure(disabledforeground="#a3a3a3")
        self.btnExchange.configure(foreground="#000000")
        self.btnExchange.configure(highlightbackground="#d9d9d9")
        self.btnExchange.configure(highlightcolor="black")
        self.btnExchange.configure(pady="0")
        self.btnExchange.configure(text='''Exchange''')
        self.btnExchange.configure(width=317)
        self.btnExchange.configure(command=openExchange)

        self.btnMiners = Button(top)
        self.btnMiners.place(relx=0.28, rely=0.43, height=64, width=317)
        self.btnMiners.configure(activebackground="#79e191")
        self.btnMiners.configure(activeforeground="#000000")
        self.btnMiners.configure(background="#d9d9d9")
        self.btnMiners.configure(disabledforeground="#a3a3a3")
        self.btnMiners.configure(foreground="#000000")
        self.btnMiners.configure(highlightbackground="#d9d9d9")
        self.btnMiners.configure(highlightcolor="black")
        self.btnMiners.configure(pady="0")
        self.btnMiners.configure(text='''Miners''')
        self.btnMiners.configure(width=317)
        self.btnMiners.configure(command=openMiners)

        self.btnAdvice = Button(top)
        self.btnAdvice.place(relx=0.28, rely=0.62, height=64, width=317)
        self.btnAdvice.configure(activebackground="#79e191")
        self.btnAdvice.configure(activeforeground="#000000")
        self.btnAdvice.configure(background="#d9d9d9")
        self.btnAdvice.configure(disabledforeground="#a3a3a3")
        self.btnAdvice.configure(foreground="#000000")
        self.btnAdvice.configure(highlightbackground="#d9d9d9")
        self.btnAdvice.configure(highlightcolor="black")
        self.btnAdvice.configure(pady="0")
        self.btnAdvice.configure(text='''Advice''')
        self.btnAdvice.configure(command=openAdvisor)

        self.btnFunds = Button(top)
        self.btnFunds.place(relx=0.28, rely=0.81, height=64, width=317)
        self.btnFunds.configure(activebackground="#79e191")
        self.btnFunds.configure(activeforeground="#000000")
        self.btnFunds.configure(background="#d9d9d9")
        self.btnFunds.configure(disabledforeground="#a3a3a3")
        self.btnFunds.configure(foreground="#000000")
        self.btnFunds.configure(highlightbackground="#d9d9d9")
        self.btnFunds.configure(highlightcolor="black")
        self.btnFunds.configure(pady="0")
        self.btnFunds.configure(text='''Manage Funds''')
        self.btnFunds.configure(command=manageFunds)






if __name__ == '__main__':
    vp_start_gui()



