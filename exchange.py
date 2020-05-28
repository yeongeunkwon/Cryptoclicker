import sys, transactions, coins, tkinter.messagebox, navigation

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

import exchange_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, top
    root = Tk()
    top = Exchange (root)
    exchange_support.init(root, top)
    top.rbtnBTC.invoke()
    top.txtAmount.focus()
    root.mainloop()

w = None
def create_Purchase(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Exchange (w)
    exchange_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Purchase():
    global w
    w.destroy()
    w = None

def refresh():
    exchange_support.destroy_window()
    vp_start_gui()

def backToMenu():
    exchange_support.destroy_window()
    navigation.vp_start_gui()

def placeBuyOrder():
    success = checkAmount()
    if success > 0:
        global top, cryptoChoice
        updateGUI()
        confirm = tkinter.messagebox.askyesno('Confirmation', 'You have $%0.2f to spend. Are you sure you want to place this order?'%(transactions.getfiattotal()))
        if confirm:
            crypt = cryptoChoice.get()
            transactions.buysell(0, crypt, success)

def placeSellOrder():
    success = checkAmount()
    if success > 0:
        global top, cryptoChoice
        updateGUI()
        cryptolist = transactions.getcointotals()
        crypt = cryptoChoice.get()
        confirm = tkinter.messagebox.askyesno('Confirmation', 'You have %0.5f %s. Are you sure you want to place this order?'%(cryptolist[1][cryptolist[0].index(crypt)], crypt))
        if confirm:
            transactions.buysell(1, crypt, success)

def checkAmount():
    global top, amount
    amount = top.txtAmount.get("1.0",'end-1c')
    try:
        if str(amount).find('.') >= 0:
            amount = float(amount)
        elif str(amount).find('.') < 0:
            amount = int(amount)
        if amount >= 0:
            return amount
    except:
        tkinter.messagebox.showerror('Error', 'Invalid Exchange Amount. Could not place Order.')
        top.txtAmount.delete("1.0", END)
        top.txtAmount.focus()
        return -1

def updateGUI():
    global top
    success = checkAmount()
    if success > 0:
        btcPrice = coins.getCoinVal("BTC")
        ethPrice = coins.getCoinVal("ETH")
        ltcPrice = coins.getCoinVal("LTC")
        bchPrice = coins.getCoinVal("BCH")
        xrpPrice = coins.getCoinVal("XRP")

        top.lblBTCp.configure(text = '$' + str(btcPrice)[:10])
        top.lblETHp.configure(text = '$' + str(ethPrice)[:10])
        top.lblLTCp.configure(text = '$' + str(ltcPrice)[:10])
        top.lblBCHp.configure(text = '$' + str(bchPrice)[:10])
        top.lblXRPp.configure(text = '$' + str(xrpPrice)[:10])

        top.lblBTCo.configure(text = '$' + str(btcPrice*success)[:10])
        top.lblETHo.configure(text = '$' + str(ethPrice*success)[:10])
        top.lblLTCo.configure(text = '$' + str(ltcPrice*success)[:10])
        top.lblBCHo.configure(text = '$' + str(bchPrice*success)[:10])
        top.lblXRPo.configure(text = '$' + str(xrpPrice*success)[:10])


        


class Exchange:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 10 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("374x274+530+300")
        top.title("Exchange")
        top.configure(background="#d9d9d9")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=375)

        self.btnOrder = Button(self.Frame1)
        self.btnOrder.place(relx=0.80, rely=0.84, height=24, width=50)
        self.btnOrder.configure(activebackground="#d9d9d9")
        self.btnOrder.configure(activeforeground="#000000")
        self.btnOrder.configure(background="#d9d9d9")
        self.btnOrder.configure(disabledforeground="#a3a3a3")
        self.btnOrder.configure(foreground="#000000")
        self.btnOrder.configure(highlightbackground="#d9d9d9")
        self.btnOrder.configure(highlightcolor="black")
        self.btnOrder.configure(pady="0")
        self.btnOrder.configure(text='''Buy''')
        self.btnOrder.configure(width=77)
        self.btnOrder.configure(command=placeBuyOrder)

        self.btnCalc = Button(self.Frame1)
        self.btnCalc.place(relx=0.35, rely=0.84, height=24, width=95)
        self.btnCalc.configure(activebackground="#d9d9d9")
        self.btnCalc.configure(activeforeground="#000000")
        self.btnCalc.configure(background="#d9d9d9")
        self.btnCalc.configure(disabledforeground="#a3a3a3")
        self.btnCalc.configure(foreground="#000000")
        self.btnCalc.configure(highlightbackground="#d9d9d9")
        self.btnCalc.configure(highlightcolor="black")
        self.btnCalc.configure(pady="0")
        self.btnCalc.configure(text='''Calculate Order''')
        self.btnCalc.configure(width=77)
        self.btnCalc.configure(command=updateGUI)

        self.btnSell = Button(self.Frame1)
        self.btnSell.place(relx=0.64, rely=0.84, height=24, width=50)
        self.btnSell.configure(activebackground="#d9d9d9")
        self.btnSell.configure(activeforeground="#000000")
        self.btnSell.configure(background="#d9d9d9")
        self.btnSell.configure(disabledforeground="#a3a3a3")
        self.btnSell.configure(foreground="#000000")
        self.btnSell.configure(highlightbackground="#d9d9d9")
        self.btnSell.configure(highlightcolor="black")
        self.btnSell.configure(pady="0")
        self.btnSell.configure(text='''Sell''')
        self.btnSell.configure(width=77)
        self.btnSell.configure(command=placeSellOrder)

        self.btnMenu = Button(self.Frame1)
        self.btnMenu.place(relx=0.05, rely=0.07, height=24, width=97)
        self.btnMenu.configure(activebackground="#d9d9d9")
        self.btnMenu.configure(activeforeground="#000000")
        self.btnMenu.configure(background="#d9d9d9")
        self.btnMenu.configure(disabledforeground="#a3a3a3")
        self.btnMenu.configure(foreground="#000000")
        self.btnMenu.configure(highlightbackground="#d9d9d9")
        self.btnMenu.configure(highlightcolor="black")
        self.btnMenu.configure(pady="0")
        self.btnMenu.configure(text='''Main Menu''')
        self.btnMenu.configure(width=97)
        self.btnMenu.configure(command=backToMenu)

        global cryptoChoice
        cryptoChoice = StringVar()

        self.rbtnBTC = Radiobutton(self.Frame1)
        self.rbtnBTC.place(relx=0.08, rely=0.25, relheight=0.09, relwidth=0.13)
        self.rbtnBTC.configure(activebackground="#d9d9d9")
        self.rbtnBTC.configure(activeforeground="#000000")
        self.rbtnBTC.configure(background="#d9d9d9")
        self.rbtnBTC.configure(disabledforeground="#a3a3a3")
        self.rbtnBTC.configure(foreground="#000000")
        self.rbtnBTC.configure(highlightbackground="#d9d9d9")
        self.rbtnBTC.configure(highlightcolor="black")
        self.rbtnBTC.configure(justify=LEFT)
        self.rbtnBTC.configure(state=NORMAL)
        self.rbtnBTC.configure(text='''BTC''')
        self.rbtnBTC.configure(variable=cryptoChoice)
        self.rbtnBTC.configure(value="BTC")
        self.rbtnBTC.configure(width=50)

        self.rbtnETH = Radiobutton(self.Frame1)
        self.rbtnETH.place(relx=0.08, rely=0.36, relheight=0.09, relwidth=0.13)
        self.rbtnETH.configure(activebackground="#d9d9d9")
        self.rbtnETH.configure(activeforeground="#000000")
        self.rbtnETH.configure(background="#d9d9d9")
        self.rbtnETH.configure(disabledforeground="#a3a3a3")
        self.rbtnETH.configure(foreground="#000000")
        self.rbtnETH.configure(highlightbackground="#d9d9d9")
        self.rbtnETH.configure(highlightcolor="black")
        self.rbtnETH.configure(justify=LEFT)
        self.rbtnETH.configure(text='''ETH''')
        self.rbtnETH.configure(variable=cryptoChoice)
        self.rbtnETH.configure(value="ETH")
        

        self.rbtnBCH = Radiobutton(self.Frame1)
        self.rbtnBCH.place(relx=0.08, rely=0.58, relheight=0.09, relwidth=0.13)
        self.rbtnBCH.configure(activebackground="#d9d9d9")
        self.rbtnBCH.configure(activeforeground="#000000")
        self.rbtnBCH.configure(background="#d9d9d9")
        self.rbtnBCH.configure(disabledforeground="#a3a3a3")
        self.rbtnBCH.configure(foreground="#000000")
        self.rbtnBCH.configure(highlightbackground="#d9d9d9")
        self.rbtnBCH.configure(highlightcolor="black")
        self.rbtnBCH.configure(justify=LEFT)
        self.rbtnBCH.configure(text='''BCH''')
        self.rbtnBCH.configure(variable=cryptoChoice)
        self.rbtnBCH.configure(value="BCH")
        

        self.rbtnXRP = Radiobutton(self.Frame1)
        self.rbtnXRP.place(relx=0.08, rely=0.69, relheight=0.09, relwidth=0.13)
        self.rbtnXRP.configure(activebackground="#d9d9d9")
        self.rbtnXRP.configure(activeforeground="#000000")
        self.rbtnXRP.configure(background="#d9d9d9")
        self.rbtnXRP.configure(disabledforeground="#a3a3a3")
        self.rbtnXRP.configure(foreground="#000000")
        self.rbtnXRP.configure(highlightbackground="#d9d9d9")
        self.rbtnXRP.configure(highlightcolor="black")
        self.rbtnXRP.configure(justify=LEFT)
        self.rbtnXRP.configure(text='''XRP''')
        self.rbtnXRP.configure(variable=cryptoChoice)
        self.rbtnXRP.configure(value="XRP")
        

        self.rbtnLTC = Radiobutton(self.Frame1)
        self.rbtnLTC.place(relx=0.08, rely=0.47, relheight=0.09, relwidth=0.13)
        self.rbtnLTC.configure(activebackground="#d9d9d9")
        self.rbtnLTC.configure(activeforeground="#000000")
        self.rbtnLTC.configure(background="#d9d9d9")
        self.rbtnLTC.configure(disabledforeground="#a3a3a3")
        self.rbtnLTC.configure(foreground="#000000")
        self.rbtnLTC.configure(highlightbackground="#d9d9d9")
        self.rbtnLTC.configure(highlightcolor="black")
        self.rbtnLTC.configure(justify=LEFT)
        self.rbtnLTC.configure(text='''LTC''')
        self.rbtnLTC.configure(variable=cryptoChoice)
        self.rbtnLTC.configure(value="LTC")

        self.btnRefresh = Button(self.Frame1)
        self.btnRefresh.place(relx=0.05, rely=0.84, height=24, width=97)
        self.btnRefresh.configure(activebackground="#d9d9d9")
        self.btnRefresh.configure(activeforeground="#000000")
        self.btnRefresh.configure(background="#d9d9d9")
        self.btnRefresh.configure(disabledforeground="#a3a3a3")
        self.btnRefresh.configure(foreground="#000000")
        self.btnRefresh.configure(highlightbackground="#d9d9d9")
        self.btnRefresh.configure(highlightcolor="black")
        self.btnRefresh.configure(pady="0")
        self.btnRefresh.configure(text='''Refresh''')
        self.btnRefresh.configure(width=97)
        self.btnRefresh.configure(command = refresh)

        self.lblBTCp = Label(self.Frame1)
        self.lblBTCp.place(relx=0.32, rely=0.25, height=21, width=70)
        self.lblBTCp.configure(background="#d9d9d9")
        self.lblBTCp.configure(disabledforeground="#a3a3a3")
        self.lblBTCp.configure(foreground="#000000")
        self.lblBTCp.configure(text='$' + str(coins.getCoinVal("BTC"))[:10])

        self.lblETHp = Label(self.Frame1)
        self.lblETHp.place(relx=0.32, rely=0.36, height=21, width=70)
        self.lblETHp.configure(background="#d9d9d9")
        self.lblETHp.configure(disabledforeground="#a3a3a3")
        self.lblETHp.configure(foreground="#000000")
        self.lblETHp.configure(text='$' + str(coins.getCoinVal("ETH"))[:10])

        self.lblLTCp = Label(self.Frame1)
        self.lblLTCp.place(relx=0.32, rely=0.47, height=21, width=70)
        self.lblLTCp.configure(background="#d9d9d9")
        self.lblLTCp.configure(disabledforeground="#a3a3a3")
        self.lblLTCp.configure(foreground="#000000")
        self.lblLTCp.configure(text='$' + str(coins.getCoinVal("LTC"))[:10])

        self.lblBCHp = Label(self.Frame1)
        self.lblBCHp.place(relx=0.32, rely=0.58, height=21, width=70)
        self.lblBCHp.configure(background="#d9d9d9")
        self.lblBCHp.configure(disabledforeground="#a3a3a3")
        self.lblBCHp.configure(foreground="#000000")
        self.lblBCHp.configure(text='$' + str(coins.getCoinVal("BCH"))[:10])

        self.lblXRPp = Label(self.Frame1)
        self.lblXRPp.place(relx=0.32, rely=0.69, height=21, width=70)
        self.lblXRPp.configure(background="#d9d9d9")
        self.lblXRPp.configure(disabledforeground="#a3a3a3")
        self.lblXRPp.configure(foreground="#000000")
        self.lblXRPp.configure(text='$' + str(coins.getCoinVal("XRP"))[:10])

        self.lblCurrPrice = Label(self.Frame1)
        self.lblCurrPrice.place(relx=0.32, rely=0.18, height=21, width=75)
        self.lblCurrPrice.configure(background="#d9d9d9")
        self.lblCurrPrice.configure(disabledforeground="#a3a3a3")
        self.lblCurrPrice.configure(foreground="#000000")
        self.lblCurrPrice.configure(text='''Current Price''')

        self.lblOrderPrice = Label(self.Frame1)
        self.lblOrderPrice.place(relx=0.67, rely=0.18, height=21, width=79)
        self.lblOrderPrice.configure(background="#d9d9d9")
        self.lblOrderPrice.configure(disabledforeground="#a3a3a3")
        self.lblOrderPrice.configure(foreground="#000000")
        self.lblOrderPrice.configure(text='''Price of Order''')

        self.lblBTCo = Label(self.Frame1)
        self.lblBTCo.place(relx=0.69, rely=0.25, height=21, width=80)
        self.lblBTCo.configure(background="#d9d9d9")
        self.lblBTCo.configure(disabledforeground="#a3a3a3")
        self.lblBTCo.configure(foreground="#000000")
        self.lblBTCo.configure(text='''$''')

        self.lblETHo = Label(self.Frame1)
        self.lblETHo.place(relx=0.69, rely=0.36, height=21, width=80)
        self.lblETHo.configure(background="#d9d9d9")
        self.lblETHo.configure(disabledforeground="#a3a3a3")
        self.lblETHo.configure(foreground="#000000")
        self.lblETHo.configure(text='''$''')

        self.lblLTCo = Label(self.Frame1)
        self.lblLTCo.place(relx=0.69, rely=0.47, height=21, width=80)
        self.lblLTCo.configure(background="#d9d9d9")
        self.lblLTCo.configure(disabledforeground="#a3a3a3")
        self.lblLTCo.configure(foreground="#000000")
        self.lblLTCo.configure(text='''$''')

        self.lblBCHo = Label(self.Frame1)
        self.lblBCHo.place(relx=0.69, rely=0.58, height=21, width=80)
        self.lblBCHo.configure(background="#d9d9d9")
        self.lblBCHo.configure(disabledforeground="#a3a3a3")
        self.lblBCHo.configure(foreground="#000000")
        self.lblBCHo.configure(text='''$''')

        self.lblXRPo = Label(self.Frame1)
        self.lblXRPo.place(relx=0.69, rely=0.69, height=21, width=80)
        self.lblXRPo.configure(background="#d9d9d9")
        self.lblXRPo.configure(disabledforeground="#a3a3a3")
        self.lblXRPo.configure(foreground="#000000")
        self.lblXRPo.configure(text='''$''')

        self.lblOrder = Label(self.Frame1)
        self.lblOrder.place(relx=0.40, rely=0.07, height=21, width=107)
        self.lblOrder.configure(background="#d9d9d9")
        self.lblOrder.configure(disabledforeground="#a3a3a3")
        self.lblOrder.configure(foreground="#000000")
        self.lblOrder.configure(text='''Amount:''')

        self.txtAmount = Text(self.Frame1)
        self.txtAmount.place(relx=0.64, rely=0.07, relheight=0.09, relwidth=0.3)
        self.txtAmount.configure(background="white")
        self.txtAmount.configure(font=font10)
        self.txtAmount.configure(foreground="black")
        self.txtAmount.configure(highlightbackground="#d9d9d9")
        self.txtAmount.configure(highlightcolor="black")
        self.txtAmount.configure(insertbackground="black")
        self.txtAmount.configure(selectbackground="#c4c4c4")
        self.txtAmount.configure(selectforeground="black")
        self.txtAmount.configure(width=114)
        self.txtAmount.configure(wrap=WORD)

if __name__ == '__main__':
    vp_start_gui()



