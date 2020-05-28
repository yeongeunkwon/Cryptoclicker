import sys, advise, navigation
import numpy as np

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

import advicetool_support

max_sharpe_values = np.ones((8,))
min_var_values = np.ones((8,))
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, top
    root = Tk()
    top = Cryptocurrency_Statistical_Linear_Regression (root)
    advicetool_support.init(root, top)
    simulate()
    top.rbtnBTC.invoke()
    root.mainloop()
    

w = None
def create_Cryptocurrency_Statistical_Linear_Regression(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    advicetool_support.set_Tk_var()
    top = Cryptocurrency_Statistical_Linear_Regression (w)
    advicetool_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Cryptocurrency_Statistical_Linear_Regression():
    global w
    w.destroy()
    w = None

def backToMenu():
    advicetool_support.destroy_window()
    navigation.vp_start_gui()

def createAvgGraph():
    advise.movAvgGraph(coinSelect.get()) #creates a movAvg.png in the local directory
    #fill this in

def calcPrices():
    global top, coinSelect
    ticker = coinSelect.get()
    prediction = advise.predictValue(ticker, 7)
    top.lblD1price.configure(text='$' + str(prediction[0])[:10])
    top.lblD2price.configure(text='$' + str(prediction[1])[:10])
    top.lblD4price.configure(text='$' + str(prediction[3])[:10])
    top.lblD7price.configure(text='$' + str(prediction[6])[:10])
    genParagraph(prediction)

def simulate():
    global max_sharpe_values,min_var_values
    simdays = 300
    test = advise.profileSim(simdays)
    max_sharpe_index = np.argmax(test, axis=1)
    max_sharpe_values = test[:,max_sharpe_index[2]] # return column with highest sharpe ratio
    min_var_index = np.argmin(test, axis=1)
    min_var_values = test[:,min_var_index[1]] #return column with lowest std dev
    
def genParagraph(prediction):
    global top, max_sharpe_values, min_var_values
    #simulate() if i run simulate here it works
    summary = "Based on 300 days of coin data, the optimal profile of cryptocurrency holdings would have been: \n"
    sumprof = "         {2:.2f}% BTC     {3:.2f}% ETH    {4:.2f}% LTC    {5:.2f}% BCH    {6:.2f}% XRP \n\nThe Sharpe ratio of the profile would have been {0:.2f} with a Volatility value of {1:.2f}".format(max_sharpe_values[2],max_sharpe_values[1],max_sharpe_values[3]*100,max_sharpe_values[4]*100,max_sharpe_values[5]*100,max_sharpe_values[6]*100,max_sharpe_values[7]*100)
    sumprof1 = "\nHigher Sharpe ratios mean higher returns for a given Volatility or risk\n"
    sumcoin = "\nBased on historical data the expected price for " + coinSelect.get() + " tomorrow will be ${0:.2f}. Further out, the prediction is that the \nprice will vary and likely be around ${1:.2f} in seven days. ".format(prediction[0],prediction[6])
    sumcoin1 = "However, it should be noted that the further out the \nprediction, the lower the confidence and reliability of the predicted value becomes. "
    sumavg = "\n\nBelow you can view the moving average graph of " + coinSelect.get() + ". Current values above the moving average indicate \nan upward trend and vice versa."
    top.lblParagraph.configure(text=summary+sumprof+sumprof1+sumcoin+sumcoin1+sumavg)

class Cryptocurrency_Statistical_Linear_Regression:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 17 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("700x518+477+272")
        top.title("Cryptocurrency Advising")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.lblCoins = Label(top)
        self.lblCoins.place(relx=0.0, rely=0.14, height=25, width=158)
        self.lblCoins.configure(activebackground="#f9f9f9")
        self.lblCoins.configure(activeforeground="black")
        self.lblCoins.configure(background="#d9d9d9")
        self.lblCoins.configure(disabledforeground="#a3a3a3")
        self.lblCoins.configure(foreground="#000000")
        self.lblCoins.configure(highlightbackground="#d9d9d9")
        self.lblCoins.configure(highlightcolor="black")
        self.lblCoins.configure(text='''Choose a coin:''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        global coinSelect
        coinSelect = StringVar()

        self.rbtnBCH = Radiobutton(top)
        self.rbtnBCH.place(relx=0.17, rely=0.08, relheight=0.05, relwidth=0.18)
        self.rbtnBCH.configure(activebackground="#d9d9d9")
        self.rbtnBCH.configure(activeforeground="#000000")
        self.rbtnBCH.configure(background="#d9d9d9")
        self.rbtnBCH.configure(disabledforeground="#a3a3a3")
        self.rbtnBCH.configure(foreground="#000000")
        self.rbtnBCH.configure(highlightbackground="#d9d9d9")
        self.rbtnBCH.configure(highlightcolor="black")
        self.rbtnBCH.configure(justify=LEFT)
        self.rbtnBCH.configure(text='''BCH''')
        self.rbtnBCH.configure(variable=coinSelect)
        self.rbtnBCH.configure(value="BCH")
        self.rbtnBCH.configure(command=calcPrices)

        self.rbtnLTC = Radiobutton(top)
        self.rbtnLTC.place(relx=0.17, rely=0.14, relheight=0.05, relwidth=0.18)
        self.rbtnLTC.configure(activebackground="#d9d9d9")
        self.rbtnLTC.configure(activeforeground="#000000")
        self.rbtnLTC.configure(background="#d9d9d9")
        self.rbtnLTC.configure(disabledforeground="#a3a3a3")
        self.rbtnLTC.configure(foreground="#000000")
        self.rbtnLTC.configure(highlightbackground="#d9d9d9")
        self.rbtnLTC.configure(highlightcolor="black")
        self.rbtnLTC.configure(justify=LEFT)
        self.rbtnLTC.configure(text='''LTC''')
        self.rbtnLTC.configure(variable=coinSelect)
        self.rbtnLTC.configure(value="LTC")
        self.rbtnLTC.configure(command=calcPrices)

        self.rbtnETH = Radiobutton(top)
        self.rbtnETH.place(relx=0.17, rely=0.19, relheight=0.05, relwidth=0.18)
        self.rbtnETH.configure(activebackground="#d9d9d9")
        self.rbtnETH.configure(activeforeground="#000000")
        self.rbtnETH.configure(background="#d9d9d9")
        self.rbtnETH.configure(disabledforeground="#a3a3a3")
        self.rbtnETH.configure(foreground="#000000")
        self.rbtnETH.configure(highlightbackground="#d9d9d9")
        self.rbtnETH.configure(highlightcolor="black")
        self.rbtnETH.configure(justify=LEFT)
        self.rbtnETH.configure(text='''ETH''')
        self.rbtnETH.configure(variable=coinSelect)
        self.rbtnETH.configure(value="ETH")
        self.rbtnETH.configure(command=calcPrices)

        self.rbtnXRP = Radiobutton(top)
        self.rbtnXRP.place(relx=0.17, rely=0.25, relheight=0.05, relwidth=0.18)
        self.rbtnXRP.configure(activebackground="#d9d9d9")
        self.rbtnXRP.configure(activeforeground="#000000")
        self.rbtnXRP.configure(background="#d9d9d9")
        self.rbtnXRP.configure(disabledforeground="#a3a3a3")
        self.rbtnXRP.configure(foreground="#000000")
        self.rbtnXRP.configure(highlightbackground="#d9d9d9")
        self.rbtnXRP.configure(highlightcolor="black")
        self.rbtnXRP.configure(justify=LEFT)
        self.rbtnXRP.configure(text='''XRP''')
        self.rbtnXRP.configure(variable=coinSelect)
        self.rbtnXRP.configure(value="XRP")
        self.rbtnXRP.configure(command=calcPrices)

        self.rbtnBTC = Radiobutton(top)
        self.rbtnBTC.place(relx=0.17, rely=0.02, relheight=0.05, relwidth=0.18)
        self.rbtnBTC.configure(activebackground="#d9d9d9")
        self.rbtnBTC.configure(activeforeground="#000000")
        self.rbtnBTC.configure(background="#d9d9d9")
        self.rbtnBTC.configure(disabledforeground="#a3a3a3")
        self.rbtnBTC.configure(foreground="#000000")
        self.rbtnBTC.configure(highlightbackground="#d9d9d9")
        self.rbtnBTC.configure(highlightcolor="black")
        self.rbtnBTC.configure(justify=LEFT)
        self.rbtnBTC.configure(text='''BTC''')
        self.rbtnBTC.configure(variable=coinSelect)
        self.rbtnBTC.configure(value="BTC")
        self.rbtnBTC.configure(command=calcPrices)

        self.lblPrices = Label(top)
        self.lblPrices.place(relx=0.58, rely=0.02, height=25, width=128)
        self.lblPrices.configure(activebackground="#f9f9f9")
        self.lblPrices.configure(activeforeground="black")
        self.lblPrices.configure(background="#d9d9d9")
        self.lblPrices.configure(disabledforeground="#a3a3a3")
        self.lblPrices.configure(foreground="#000000")
        self.lblPrices.configure(highlightbackground="#d9d9d9")
        self.lblPrices.configure(highlightcolor="black")
        self.lblPrices.configure(text='''Expected Prices''')

        self.lblDay1 = Label(top)
        self.lblDay1.place(relx=0.47, rely=0.08, height=25, width=128)
        self.lblDay1.configure(activebackground="#f9f9f9")
        self.lblDay1.configure(activeforeground="black")
        self.lblDay1.configure(background="#d9d9d9")
        self.lblDay1.configure(disabledforeground="#a3a3a3")
        self.lblDay1.configure(foreground="#000000")
        self.lblDay1.configure(highlightbackground="#d9d9d9")
        self.lblDay1.configure(highlightcolor="black")
        self.lblDay1.configure(text='''1 Day''')

        self.lblDay2 = Label(top)
        self.lblDay2.place(relx=0.47, rely=0.14, height=25, width=128)
        self.lblDay2.configure(activebackground="#f9f9f9")
        self.lblDay2.configure(activeforeground="black")
        self.lblDay2.configure(background="#d9d9d9")
        self.lblDay2.configure(disabledforeground="#a3a3a3")
        self.lblDay2.configure(foreground="#000000")
        self.lblDay2.configure(highlightbackground="#d9d9d9")
        self.lblDay2.configure(highlightcolor="black")
        self.lblDay2.configure(text='''2 Days''')

        self.lblDay4 = Label(top)
        self.lblDay4.place(relx=0.47, rely=0.19, height=25, width=128)
        self.lblDay4.configure(activebackground="#f9f9f9")
        self.lblDay4.configure(activeforeground="black")
        self.lblDay4.configure(background="#d9d9d9")
        self.lblDay4.configure(disabledforeground="#a3a3a3")
        self.lblDay4.configure(foreground="#000000")
        self.lblDay4.configure(highlightbackground="#d9d9d9")
        self.lblDay4.configure(highlightcolor="black")
        self.lblDay4.configure(text='''4 Days''')

        self.lblDay7 = Label(top)
        self.lblDay7.place(relx=0.47, rely=0.25, height=25, width=128)
        self.lblDay7.configure(activebackground="#f9f9f9")
        self.lblDay7.configure(activeforeground="black")
        self.lblDay7.configure(background="#d9d9d9")
        self.lblDay7.configure(disabledforeground="#a3a3a3")
        self.lblDay7.configure(foreground="#000000")
        self.lblDay7.configure(highlightbackground="#d9d9d9")
        self.lblDay7.configure(highlightcolor="black")
        self.lblDay7.configure(text='''7 Days''')

        self.lblD1price = Label(top)
        self.lblD1price.place(relx=0.69, rely=0.08, height=25, width=128)
        self.lblD1price.configure(activebackground="#f9f9f9")
        self.lblD1price.configure(activeforeground="black")
        self.lblD1price.configure(background="#d9d9d9")
        self.lblD1price.configure(disabledforeground="#a3a3a3")
        self.lblD1price.configure(foreground="#000000")
        self.lblD1price.configure(highlightbackground="#d9d9d9")
        self.lblD1price.configure(highlightcolor="black")
        self.lblD1price.configure(text='''$''')

        self.lblD2price = Label(top)
        self.lblD2price.place(relx=0.69, rely=0.14, height=25, width=128)
        self.lblD2price.configure(activebackground="#f9f9f9")
        self.lblD2price.configure(activeforeground="black")
        self.lblD2price.configure(background="#d9d9d9")
        self.lblD2price.configure(disabledforeground="#a3a3a3")
        self.lblD2price.configure(foreground="#000000")
        self.lblD2price.configure(highlightbackground="#d9d9d9")
        self.lblD2price.configure(highlightcolor="black")
        self.lblD2price.configure(text='''$''')

        self.lblD4price = Label(top)
        self.lblD4price.place(relx=0.69, rely=0.19, height=25, width=128)
        self.lblD4price.configure(activebackground="#f9f9f9")
        self.lblD4price.configure(activeforeground="black")
        self.lblD4price.configure(background="#d9d9d9")
        self.lblD4price.configure(disabledforeground="#a3a3a3")
        self.lblD4price.configure(foreground="#000000")
        self.lblD4price.configure(highlightbackground="#d9d9d9")
        self.lblD4price.configure(highlightcolor="black")
        self.lblD4price.configure(text='''$''')

        self.lblD7price = Label(top)
        self.lblD7price.place(relx=0.69, rely=0.25, height=25, width=128)
        self.lblD7price.configure(activebackground="#f9f9f9")
        self.lblD7price.configure(activeforeground="black")
        self.lblD7price.configure(background="#d9d9d9")
        self.lblD7price.configure(disabledforeground="#a3a3a3")
        self.lblD7price.configure(foreground="#000000")
        self.lblD7price.configure(highlightbackground="#d9d9d9")
        self.lblD7price.configure(highlightcolor="black")
        self.lblD7price.configure(text='''$''')

        self.frmParagraph = Frame(top)
        self.frmParagraph.place(relx=0.01, rely=0.35, relheight=0.47
                , relwidth=0.94)
        self.frmParagraph.configure(relief=GROOVE)
        self.frmParagraph.configure(borderwidth="2")
        self.frmParagraph.configure(relief=GROOVE)
        self.frmParagraph.configure(background="#d9d9d9")
        self.frmParagraph.configure(highlightbackground="#d9d9d9")
        self.frmParagraph.configure(highlightcolor="black")
        self.frmParagraph.configure(width=655)

        self.lblParaTitle = Label(self.frmParagraph)
        self.lblParaTitle.place(relx=0.02, rely=0.04, height=31, width=634)
        self.lblParaTitle.configure(activebackground="#f9f9f9")
        self.lblParaTitle.configure(activeforeground="black")
        self.lblParaTitle.configure(background="#d9d9d9")
        self.lblParaTitle.configure(disabledforeground="#a3a3a3")
        self.lblParaTitle.configure(font=font9)
        self.lblParaTitle.configure(foreground="#000000")
        self.lblParaTitle.configure(highlightbackground="#d9d9d9")
        self.lblParaTitle.configure(highlightcolor="black")
        self.lblParaTitle.configure(text='''Summary and Recommendations:''')

        self.lblParagraph = Label(self.frmParagraph)
        self.lblParagraph.place(relx=0.02, rely=0.16, height=191, width=634)
        self.lblParagraph.configure(activebackground="#f9f9f9")
        self.lblParagraph.configure(activeforeground="black")
        self.lblParagraph.configure(anchor=NW)
        self.lblParagraph.configure(background="#d9d9d9")
        self.lblParagraph.configure(disabledforeground="#a3a3a3")
        self.lblParagraph.configure(foreground="#000000")
        self.lblParagraph.configure(highlightbackground="#d9d9d9")
        self.lblParagraph.configure(highlightcolor="black")
        self.lblParagraph.configure(justify=LEFT)
        self.lblParagraph.configure(text='''Label''')

        self.btnMenu = Button(top)
        self.btnMenu.place(relx=0.04, rely=0.87, height=44, width=137)
        self.btnMenu.configure(activebackground="#d9d9d9")
        self.btnMenu.configure(activeforeground="#000000")
        self.btnMenu.configure(background="#d9d9d9")
        self.btnMenu.configure(disabledforeground="#a3a3a3")
        self.btnMenu.configure(foreground="#000000")
        self.btnMenu.configure(highlightbackground="#d9d9d9")
        self.btnMenu.configure(highlightcolor="black")
        self.btnMenu.configure(pady="0")
        self.btnMenu.configure(text='''Main Menu''')
        self.btnMenu.configure(width=137)
        self.btnMenu.configure(command=backToMenu)


        self.btnGraph = Button(top)
        self.btnGraph.place(relx=0.73, rely=0.87, height=44, width=137)
        self.btnGraph.configure(activebackground="#d9d9d9")
        self.btnGraph.configure(activeforeground="#000000")
        self.btnGraph.configure(background="#d9d9d9")
        self.btnGraph.configure(disabledforeground="#a3a3a3")
        self.btnGraph.configure(foreground="#000000")
        self.btnGraph.configure(highlightbackground="#d9d9d9")
        self.btnGraph.configure(highlightcolor="black")
        self.btnGraph.configure(pady="0")
        self.btnGraph.configure(text='''View Graph''')
        self.btnGraph.configure(width=137)
        self.btnGraph.configure(command=createAvgGraph)



if __name__ == '__main__':
    vp_start_gui()



