import sys, navigation, transactions, tkinter.messagebox

miners = [
["Antminer S9",  0.0008753, 0.0059013, 0,       0,        7.97,  1300, 2000],
["Antminer L3+", 0,         0,         0.02877, 0,        4.21,   800, 3000],
["AMD RX 570",   0,         0,         0,       0.002299, 1.55,    250,  80],
["Pagolin M3X",  0.0004998, 0.0033722, 0,       0,        4.56,  2000, 1000],
["GTX 1060",     0,         0,         0,       0.001853, 1.24,   200,  120],
["GTX 1070", 0, 0, 0, 0.001853*1.25, 1.24*1.25, 300, 120],
["GTX 1080", 0, 0, 0, 0.001853*1.4, 1.25*1.4, 500, 140]]

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

import miners_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, top, miner
    root = Tk()
    top = Mining (root)
    miners_support.init(root, top)
    top.rbtnMt1.invoke()
    root.mainloop()

w = None
def create_Mining(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Mining (w)
    miners_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Mining():
    global w
    w.destroy()
    w = None

def backToMenu():
    miners_support.destroy_window()
    navigation.vp_start_gui()

def updatePrice():
    global top, miner
    price = miner.get()
    top.lblprice.configure(text='$' + str(miners[int(price)][6]))
    top.lblBalance.configure(text='Current Balance: $' + str('{:.2f}'.format(transactions.getfiattotal())))

def buyMiner():
    success = checkAmount()
    if success > 0:
        global top, miner
        confirm = tkinter.messagebox.askyesno('Confirmation', 'You have $%0.2f to spend. Are you sure you want to place this order?'%(transactions.getfiattotal()))
        if confirm:
            price = miner.get()
            transactions.buyminer(int(price), success)
            updatePrice()

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
        tkinter.messagebox.showerror('Error', 'Invalid Amount. Could not place Order.')
        top.txtAmount.delete("1.0", END)
        top.txtAmount.focus()
        return -1


class Mining:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("932x425+477+272")
        top.title("Mining")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        global miner
        miner = StringVar()

        self.rbtnMt1 = Radiobutton(top)
        self.rbtnMt1.place(relx=0.06, rely=0.16, relheight=0.06, relwidth=0.12)
        self.rbtnMt1.configure(activebackground="#d9d9d9")
        self.rbtnMt1.configure(activeforeground="#000000")
        self.rbtnMt1.configure(background="#d9d9d9")
        self.rbtnMt1.configure(disabledforeground="#a3a3a3")
        self.rbtnMt1.configure(foreground="#000000")
        self.rbtnMt1.configure(highlightbackground="#d9d9d9")
        self.rbtnMt1.configure(highlightcolor="black")
        self.rbtnMt1.configure(justify=LEFT)
        self.rbtnMt1.configure(text=miners[0][0])
        self.rbtnMt1.configure(variable=miner)
        self.rbtnMt1.configure(value='0')
        self.rbtnMt1.configure(command=updatePrice)

        self.rbtnMt2 = Radiobutton(top)
        self.rbtnMt2.place(relx=0.06, rely=0.24, relheight=0.06, relwidth=0.12)
        self.rbtnMt2.configure(activebackground="#d9d9d9")
        self.rbtnMt2.configure(activeforeground="#000000")
        self.rbtnMt2.configure(background="#d9d9d9")
        self.rbtnMt2.configure(disabledforeground="#a3a3a3")
        self.rbtnMt2.configure(foreground="#000000")
        self.rbtnMt2.configure(highlightbackground="#d9d9d9")
        self.rbtnMt2.configure(highlightcolor="black")
        self.rbtnMt2.configure(justify=LEFT)
        self.rbtnMt2.configure(text=miners[1][0])
        self.rbtnMt2.configure(variable=miner)
        self.rbtnMt2.configure(value='1')
        self.rbtnMt2.configure(command=updatePrice)

        self.rbtnMt4 = Radiobutton(top)
        self.rbtnMt4.place(relx=0.06, rely=0.38, relheight=0.06, relwidth=0.12)
        self.rbtnMt4.configure(activebackground="#d9d9d9")
        self.rbtnMt4.configure(activeforeground="#000000")
        self.rbtnMt4.configure(background="#d9d9d9")
        self.rbtnMt4.configure(disabledforeground="#a3a3a3")
        self.rbtnMt4.configure(foreground="#000000")
        self.rbtnMt4.configure(highlightbackground="#d9d9d9")
        self.rbtnMt4.configure(highlightcolor="black")
        self.rbtnMt4.configure(justify=LEFT)
        self.rbtnMt4.configure(text=miners[3][0])
        self.rbtnMt4.configure(variable=miner)
        self.rbtnMt4.configure(value='3')
        self.rbtnMt4.configure(command=updatePrice)

        self.rbtnMt6 = Radiobutton(top)
        self.rbtnMt6.place(relx=0.06, rely=0.52, relheight=0.06, relwidth=0.12)
        self.rbtnMt6.configure(activebackground="#d9d9d9")
        self.rbtnMt6.configure(activeforeground="#000000")
        self.rbtnMt6.configure(background="#d9d9d9")
        self.rbtnMt6.configure(disabledforeground="#a3a3a3")
        self.rbtnMt6.configure(foreground="#000000")
        self.rbtnMt6.configure(highlightbackground="#d9d9d9")
        self.rbtnMt6.configure(highlightcolor="black")
        self.rbtnMt6.configure(justify=LEFT)
        self.rbtnMt6.configure(text=miners[5][0])
        self.rbtnMt6.configure(variable=miner)
        self.rbtnMt6.configure(value='5')
        self.rbtnMt6.configure(command=updatePrice)

        self.rbtnMt3 = Radiobutton(top)
        self.rbtnMt3.place(relx=0.06, rely=0.31, relheight=0.06, relwidth=0.12)
        self.rbtnMt3.configure(activebackground="#d9d9d9")
        self.rbtnMt3.configure(activeforeground="#000000")
        self.rbtnMt3.configure(background="#d9d9d9")
        self.rbtnMt3.configure(disabledforeground="#a3a3a3")
        self.rbtnMt3.configure(foreground="#000000")
        self.rbtnMt3.configure(highlightbackground="#d9d9d9")
        self.rbtnMt3.configure(highlightcolor="black")
        self.rbtnMt3.configure(justify=LEFT)
        self.rbtnMt3.configure(text=miners[2][0])
        self.rbtnMt3.configure(variable=miner)
        self.rbtnMt3.configure(value='2')
        self.rbtnMt3.configure(command=updatePrice)

        self.rbtnMt5 = Radiobutton(top)
        self.rbtnMt5.place(relx=0.06, rely=0.45, relheight=0.06, relwidth=0.12)
        self.rbtnMt5.configure(activebackground="#d9d9d9")
        self.rbtnMt5.configure(activeforeground="#000000")
        self.rbtnMt5.configure(background="#d9d9d9")
        self.rbtnMt5.configure(disabledforeground="#a3a3a3")
        self.rbtnMt5.configure(foreground="#000000")
        self.rbtnMt5.configure(highlightbackground="#d9d9d9")
        self.rbtnMt5.configure(highlightcolor="black")
        self.rbtnMt5.configure(justify=LEFT)
        self.rbtnMt5.configure(text=miners[4][0])
        self.rbtnMt5.configure(variable=miner)
        self.rbtnMt5.configure(value='4')
        self.rbtnMt5.configure(command=updatePrice)

        self.rbtnMt7 = Radiobutton(top)
        self.rbtnMt7.place(relx=0.06, rely=0.59, relheight=0.06, relwidth=0.12)
        self.rbtnMt7.configure(activebackground="#d9d9d9")
        self.rbtnMt7.configure(activeforeground="#000000")
        self.rbtnMt7.configure(background="#d9d9d9")
        self.rbtnMt7.configure(disabledforeground="#a3a3a3")
        self.rbtnMt7.configure(foreground="#000000")
        self.rbtnMt7.configure(highlightbackground="#d9d9d9")
        self.rbtnMt7.configure(highlightcolor="black")
        self.rbtnMt7.configure(justify=LEFT)
        self.rbtnMt7.configure(text=miners[6][0])
        self.rbtnMt7.configure(variable=miner)
        self.rbtnMt7.configure(value='6')
        self.rbtnMt7.configure(command=updatePrice)

        self.lblEnteramt = Label(top)
        self.lblEnteramt.place(relx=0.03, rely=0.72, height=41, width=164)
        self.lblEnteramt.configure(activebackground="#f9f9f9")
        self.lblEnteramt.configure(activeforeground="black")
        self.lblEnteramt.configure(background="#d9d9d9")
        self.lblEnteramt.configure(disabledforeground="#a3a3a3")
        self.lblEnteramt.configure(foreground="#000000")
        self.lblEnteramt.configure(highlightbackground="#d9d9d9")
        self.lblEnteramt.configure(highlightcolor="black")
        self.lblEnteramt.configure(text='''Enter Amount:''')

        self.btnMinerPurchase = Button(top)
        self.btnMinerPurchase.place(relx=0.42, rely=0.71, height=54, width=137)
        self.btnMinerPurchase.configure(activebackground="#d9d9d9")
        self.btnMinerPurchase.configure(activeforeground="#000000")
        self.btnMinerPurchase.configure(background="#d9d9d9")
        self.btnMinerPurchase.configure(disabledforeground="#a3a3a3")
        self.btnMinerPurchase.configure(foreground="#000000")
        self.btnMinerPurchase.configure(highlightbackground="#d9d9d9")
        self.btnMinerPurchase.configure(highlightcolor="black")
        self.btnMinerPurchase.configure(pady="0")
        self.btnMinerPurchase.configure(text='''Purchase Miner(s)''')
        self.btnMinerPurchase.configure(command=buyMiner)

        self.btnMenu = Button(top)
        self.btnMenu.place(relx=0.83, rely=0.83, height=54, width=137)
        self.btnMenu.configure(activebackground="#d9d9d9")
        self.btnMenu.configure(activeforeground="#000000")
        self.btnMenu.configure(background="#d9d9d9")
        self.btnMenu.configure(disabledforeground="#a3a3a3")
        self.btnMenu.configure(foreground="#000000")
        self.btnMenu.configure(highlightbackground="#d9d9d9")
        self.btnMenu.configure(highlightcolor="black")
        self.btnMenu.configure(pady="0")
        self.btnMenu.configure(text='''Main Menu''')
        self.btnMenu.configure(command=backToMenu)

        self.txtAmount = Text(top)
        self.txtAmount.place(relx=0.18, rely=0.74,height=30, relwidth=0.18)
        self.txtAmount.configure(background="white")
        self.txtAmount.configure(foreground="black")
        self.txtAmount.configure(highlightbackground="#d9d9d9")
        self.txtAmount.configure(highlightcolor="black")
        self.txtAmount.configure(insertbackground="black")
        self.txtAmount.configure(selectbackground="#c4c4c4")
        self.txtAmount.configure(selectforeground="black")
        self.txtAmount.configure(width=114)
        self.txtAmount.configure(wrap=WORD)

        self.btc1 = Label(top)
        self.btc1.place(relx=0.23, rely=0.16, height=25, width=108)
        self.btc1.configure(activebackground="#f9f9f9")
        self.btc1.configure(activeforeground="black")
        self.btc1.configure(background="#d9d9d9")
        self.btc1.configure(disabledforeground="#a3a3a3")
        self.btc1.configure(foreground="#000000")
        self.btc1.configure(highlightbackground="#d9d9d9")
        self.btc1.configure(highlightcolor="black")
        self.btc1.configure(text=miners[0][1])

        self.lblBTCpH = Label(top)
        self.lblBTCpH.place(relx=0.23, rely=0.09, height=25, width=108)
        self.lblBTCpH.configure(activebackground="#f9f9f9")
        self.lblBTCpH.configure(activeforeground="black")
        self.lblBTCpH.configure(background="#d9d9d9")
        self.lblBTCpH.configure(disabledforeground="#a3a3a3")
        self.lblBTCpH.configure(foreground="#000000")
        self.lblBTCpH.configure(highlightbackground="#d9d9d9")
        self.lblBTCpH.configure(highlightcolor="black")
        self.lblBTCpH.configure(text='''BTC/D''')

        self.lblprice = Label(top)
        self.lblprice.place(relx=0.43, rely=0.87, height=25, width=108)
        self.lblprice.configure(activebackground="#f9f9f9")
        self.lblprice.configure(activeforeground="black")
        self.lblprice.configure(background="#d9d9d9")
        self.lblprice.configure(disabledforeground="#a3a3a3")
        self.lblprice.configure(foreground="#000000")
        self.lblprice.configure(highlightbackground="#d9d9d9")
        self.lblprice.configure(highlightcolor="black")
        self.lblprice.configure(text='$' + str(miners[0][6]))

        self.lblMinintype = Label(top)
        self.lblMinintype.place(relx=0.06, rely=0.09, height=25, width=108)
        self.lblMinintype.configure(activebackground="#f9f9f9")
        self.lblMinintype.configure(activeforeground="black")
        self.lblMinintype.configure(background="#d9d9d9")
        self.lblMinintype.configure(disabledforeground="#a3a3a3")
        self.lblMinintype.configure(foreground="#000000")
        self.lblMinintype.configure(highlightbackground="#d9d9d9")
        self.lblMinintype.configure(highlightcolor="black")
        self.lblMinintype.configure(text='''Mining Hardware''')

        self.btc2 = Label(top)
        self.btc2.place(relx=0.23, rely=0.24, height=25, width=108)
        self.btc2.configure(activebackground="#f9f9f9")
        self.btc2.configure(activeforeground="black")
        self.btc2.configure(background="#d9d9d9")
        self.btc2.configure(disabledforeground="#a3a3a3")
        self.btc2.configure(foreground="#000000")
        self.btc2.configure(highlightbackground="#d9d9d9")
        self.btc2.configure(highlightcolor="black")
        self.btc2.configure(text=miners[1][1])

        self.btc3 = Label(top)
        self.btc3.place(relx=0.23, rely=0.31, height=25, width=108)
        self.btc3.configure(activebackground="#f9f9f9")
        self.btc3.configure(activeforeground="black")
        self.btc3.configure(background="#d9d9d9")
        self.btc3.configure(disabledforeground="#a3a3a3")
        self.btc3.configure(foreground="#000000")
        self.btc3.configure(highlightbackground="#d9d9d9")
        self.btc3.configure(highlightcolor="black")
        self.btc3.configure(text=miners[2][1])

        self.btc4 = Label(top)
        self.btc4.place(relx=0.23, rely=0.38, height=25, width=108)
        self.btc4.configure(activebackground="#f9f9f9")
        self.btc4.configure(activeforeground="black")
        self.btc4.configure(background="#d9d9d9")
        self.btc4.configure(disabledforeground="#a3a3a3")
        self.btc4.configure(foreground="#000000")
        self.btc4.configure(highlightbackground="#d9d9d9")
        self.btc4.configure(highlightcolor="black")
        self.btc4.configure(text=miners[3][1])

        self.btc5 = Label(top)
        self.btc5.place(relx=0.23, rely=0.45, height=25, width=108)
        self.btc5.configure(activebackground="#f9f9f9")
        self.btc5.configure(activeforeground="black")
        self.btc5.configure(background="#d9d9d9")
        self.btc5.configure(disabledforeground="#a3a3a3")
        self.btc5.configure(foreground="#000000")
        self.btc5.configure(highlightbackground="#d9d9d9")
        self.btc5.configure(highlightcolor="black")
        self.btc5.configure(text=miners[4][1])

        self.btc6 = Label(top)
        self.btc6.place(relx=0.23, rely=0.52, height=25, width=108)
        self.btc6.configure(activebackground="#f9f9f9")
        self.btc6.configure(activeforeground="black")
        self.btc6.configure(background="#d9d9d9")
        self.btc6.configure(disabledforeground="#a3a3a3")
        self.btc6.configure(foreground="#000000")
        self.btc6.configure(highlightbackground="#d9d9d9")
        self.btc6.configure(highlightcolor="black")
        self.btc6.configure(text=miners[5][1])

        self.btc7 = Label(top)
        self.btc7.place(relx=0.23, rely=0.59, height=25, width=108)
        self.btc7.configure(activebackground="#f9f9f9")
        self.btc7.configure(activeforeground="black")
        self.btc7.configure(background="#d9d9d9")
        self.btc7.configure(disabledforeground="#a3a3a3")
        self.btc7.configure(foreground="#000000")
        self.btc7.configure(highlightbackground="#d9d9d9")
        self.btc7.configure(highlightcolor="black")
        self.btc7.configure(text=miners[6][1])

        self.lblBCHpH = Label(top)
        self.lblBCHpH.place(relx=0.36, rely=0.09, height=25, width=108)
        self.lblBCHpH.configure(activebackground="#f9f9f9")
        self.lblBCHpH.configure(activeforeground="black")
        self.lblBCHpH.configure(background="#d9d9d9")
        self.lblBCHpH.configure(disabledforeground="#a3a3a3")
        self.lblBCHpH.configure(foreground="#000000")
        self.lblBCHpH.configure(highlightbackground="#d9d9d9")
        self.lblBCHpH.configure(highlightcolor="black")
        self.lblBCHpH.configure(text='''BCH/D''')

        self.lblLTCpH_10 = Label(top)
        self.lblLTCpH_10.place(relx=0.49, rely=0.09, height=25, width=108)
        self.lblLTCpH_10.configure(activebackground="#f9f9f9")
        self.lblLTCpH_10.configure(activeforeground="black")
        self.lblLTCpH_10.configure(background="#d9d9d9")
        self.lblLTCpH_10.configure(disabledforeground="#a3a3a3")
        self.lblLTCpH_10.configure(foreground="#000000")
        self.lblLTCpH_10.configure(highlightbackground="#d9d9d9")
        self.lblLTCpH_10.configure(highlightcolor="black")
        self.lblLTCpH_10.configure(text='''LTC/D''')

        self.lblETHpH_11 = Label(top)
        self.lblETHpH_11.place(relx=0.63, rely=0.09, height=25, width=108)
        self.lblETHpH_11.configure(activebackground="#f9f9f9")
        self.lblETHpH_11.configure(activeforeground="black")
        self.lblETHpH_11.configure(background="#d9d9d9")
        self.lblETHpH_11.configure(disabledforeground="#a3a3a3")
        self.lblETHpH_11.configure(foreground="#000000")
        self.lblETHpH_11.configure(highlightbackground="#d9d9d9")
        self.lblETHpH_11.configure(highlightcolor="black")
        self.lblETHpH_11.configure(text='''ETH/D''')

        self.lblUSDpD = Label(top)
        self.lblUSDpD.place(relx=0.77, rely=0.09, height=25, width=108)
        self.lblUSDpD.configure(activebackground="#f9f9f9")
        self.lblUSDpD.configure(activeforeground="black")
        self.lblUSDpD.configure(background="#d9d9d9")
        self.lblUSDpD.configure(disabledforeground="#a3a3a3")
        self.lblUSDpD.configure(foreground="#000000")
        self.lblUSDpD.configure(highlightbackground="#d9d9d9")
        self.lblUSDpD.configure(highlightcolor="black")
        self.lblUSDpD.configure(text='''$/Day''')

        self.bch1 = Label(top)
        self.bch1.place(relx=0.36, rely=0.16, height=25, width=108)
        self.bch1.configure(activebackground="#f9f9f9")
        self.bch1.configure(activeforeground="black")
        self.bch1.configure(background="#d9d9d9")
        self.bch1.configure(disabledforeground="#a3a3a3")
        self.bch1.configure(foreground="#000000")
        self.bch1.configure(highlightbackground="#d9d9d9")
        self.bch1.configure(highlightcolor="black")
        self.bch1.configure(text=miners[0][2])

        self.bch2 = Label(top)
        self.bch2.place(relx=0.36, rely=0.24, height=25, width=108)
        self.bch2.configure(activebackground="#f9f9f9")
        self.bch2.configure(activeforeground="black")
        self.bch2.configure(background="#d9d9d9")
        self.bch2.configure(disabledforeground="#a3a3a3")
        self.bch2.configure(foreground="#000000")
        self.bch2.configure(highlightbackground="#d9d9d9")
        self.bch2.configure(highlightcolor="black")
        self.bch2.configure(text=miners[1][2])

        self.bch3 = Label(top)
        self.bch3.place(relx=0.36, rely=0.31, height=25, width=108)
        self.bch3.configure(activebackground="#f9f9f9")
        self.bch3.configure(activeforeground="black")
        self.bch3.configure(background="#d9d9d9")
        self.bch3.configure(disabledforeground="#a3a3a3")
        self.bch3.configure(foreground="#000000")
        self.bch3.configure(highlightbackground="#d9d9d9")
        self.bch3.configure(highlightcolor="black")
        self.bch3.configure(text=miners[2][2])

        self.bch4 = Label(top)
        self.bch4.place(relx=0.36, rely=0.38, height=25, width=108)
        self.bch4.configure(activebackground="#f9f9f9")
        self.bch4.configure(activeforeground="black")
        self.bch4.configure(background="#d9d9d9")
        self.bch4.configure(disabledforeground="#a3a3a3")
        self.bch4.configure(foreground="#000000")
        self.bch4.configure(highlightbackground="#d9d9d9")
        self.bch4.configure(highlightcolor="black")
        self.bch4.configure(text=miners[3][2])

        self.bch5 = Label(top)
        self.bch5.place(relx=0.36, rely=0.45, height=25, width=108)
        self.bch5.configure(activebackground="#f9f9f9")
        self.bch5.configure(activeforeground="black")
        self.bch5.configure(background="#d9d9d9")
        self.bch5.configure(disabledforeground="#a3a3a3")
        self.bch5.configure(foreground="#000000")
        self.bch5.configure(highlightbackground="#d9d9d9")
        self.bch5.configure(highlightcolor="black")
        self.bch5.configure(text=miners[4][2])

        self.bch6 = Label(top)
        self.bch6.place(relx=0.36, rely=0.52, height=25, width=108)
        self.bch6.configure(activebackground="#f9f9f9")
        self.bch6.configure(activeforeground="black")
        self.bch6.configure(background="#d9d9d9")
        self.bch6.configure(disabledforeground="#a3a3a3")
        self.bch6.configure(foreground="#000000")
        self.bch6.configure(highlightbackground="#d9d9d9")
        self.bch6.configure(highlightcolor="black")
        self.bch6.configure(text=miners[5][2])

        self.bch7 = Label(top)
        self.bch7.place(relx=0.36, rely=0.59, height=25, width=108)
        self.bch7.configure(activebackground="#f9f9f9")
        self.bch7.configure(activeforeground="black")
        self.bch7.configure(background="#d9d9d9")
        self.bch7.configure(disabledforeground="#a3a3a3")
        self.bch7.configure(foreground="#000000")
        self.bch7.configure(highlightbackground="#d9d9d9")
        self.bch7.configure(highlightcolor="black")
        self.bch7.configure(text=miners[6][2])

        self.ltc1 = Label(top)
        self.ltc1.place(relx=0.49, rely=0.16, height=25, width=108)
        self.ltc1.configure(activebackground="#f9f9f9")
        self.ltc1.configure(activeforeground="black")
        self.ltc1.configure(background="#d9d9d9")
        self.ltc1.configure(disabledforeground="#a3a3a3")
        self.ltc1.configure(foreground="#000000")
        self.ltc1.configure(highlightbackground="#d9d9d9")
        self.ltc1.configure(highlightcolor="black")
        self.ltc1.configure(text=miners[0][3])

        self.ltc2 = Label(top)
        self.ltc2.place(relx=0.49, rely=0.24, height=25, width=108)
        self.ltc2.configure(activebackground="#f9f9f9")
        self.ltc2.configure(activeforeground="black")
        self.ltc2.configure(background="#d9d9d9")
        self.ltc2.configure(disabledforeground="#a3a3a3")
        self.ltc2.configure(foreground="#000000")
        self.ltc2.configure(highlightbackground="#d9d9d9")
        self.ltc2.configure(highlightcolor="black")
        self.ltc2.configure(text=miners[1][3])

        self.ltc3 = Label(top)
        self.ltc3.place(relx=0.49, rely=0.31, height=25, width=108)
        self.ltc3.configure(activebackground="#f9f9f9")
        self.ltc3.configure(activeforeground="black")
        self.ltc3.configure(background="#d9d9d9")
        self.ltc3.configure(disabledforeground="#a3a3a3")
        self.ltc3.configure(foreground="#000000")
        self.ltc3.configure(highlightbackground="#d9d9d9")
        self.ltc3.configure(highlightcolor="black")
        self.ltc3.configure(text=miners[2][3])

        self.ltc4 = Label(top)
        self.ltc4.place(relx=0.49, rely=0.38, height=25, width=108)
        self.ltc4.configure(activebackground="#f9f9f9")
        self.ltc4.configure(activeforeground="black")
        self.ltc4.configure(background="#d9d9d9")
        self.ltc4.configure(disabledforeground="#a3a3a3")
        self.ltc4.configure(foreground="#000000")
        self.ltc4.configure(highlightbackground="#d9d9d9")
        self.ltc4.configure(highlightcolor="black")
        self.ltc4.configure(text=miners[3][3])

        self.ltc5 = Label(top)
        self.ltc5.place(relx=0.49, rely=0.45, height=25, width=108)
        self.ltc5.configure(activebackground="#f9f9f9")
        self.ltc5.configure(activeforeground="black")
        self.ltc5.configure(background="#d9d9d9")
        self.ltc5.configure(disabledforeground="#a3a3a3")
        self.ltc5.configure(foreground="#000000")
        self.ltc5.configure(highlightbackground="#d9d9d9")
        self.ltc5.configure(highlightcolor="black")
        self.ltc5.configure(text=miners[4][3])

        self.ltc6 = Label(top)
        self.ltc6.place(relx=0.49, rely=0.52, height=25, width=108)
        self.ltc6.configure(activebackground="#f9f9f9")
        self.ltc6.configure(activeforeground="black")
        self.ltc6.configure(background="#d9d9d9")
        self.ltc6.configure(disabledforeground="#a3a3a3")
        self.ltc6.configure(foreground="#000000")
        self.ltc6.configure(highlightbackground="#d9d9d9")
        self.ltc6.configure(highlightcolor="black")
        self.ltc6.configure(text=miners[5][3])

        self.ltc7 = Label(top)
        self.ltc7.place(relx=0.49, rely=0.59, height=25, width=108)
        self.ltc7.configure(activebackground="#f9f9f9")
        self.ltc7.configure(activeforeground="black")
        self.ltc7.configure(background="#d9d9d9")
        self.ltc7.configure(disabledforeground="#a3a3a3")
        self.ltc7.configure(foreground="#000000")
        self.ltc7.configure(highlightbackground="#d9d9d9")
        self.ltc7.configure(highlightcolor="black")
        self.ltc7.configure(text=miners[6][3])

        self.eth1 = Label(top)
        self.eth1.place(relx=0.63, rely=0.16, height=25, width=108)
        self.eth1.configure(activebackground="#f9f9f9")
        self.eth1.configure(activeforeground="black")
        self.eth1.configure(background="#d9d9d9")
        self.eth1.configure(disabledforeground="#a3a3a3")
        self.eth1.configure(foreground="#000000")
        self.eth1.configure(highlightbackground="#d9d9d9")
        self.eth1.configure(highlightcolor="black")
        self.eth1.configure(text=miners[0][4])

        self.eth2 = Label(top)
        self.eth2.place(relx=0.63, rely=0.24, height=25, width=108)
        self.eth2.configure(activebackground="#f9f9f9")
        self.eth2.configure(activeforeground="black")
        self.eth2.configure(background="#d9d9d9")
        self.eth2.configure(disabledforeground="#a3a3a3")
        self.eth2.configure(foreground="#000000")
        self.eth2.configure(highlightbackground="#d9d9d9")
        self.eth2.configure(highlightcolor="black")
        self.eth2.configure(text=miners[1][4])

        self.eth3 = Label(top)
        self.eth3.place(relx=0.63, rely=0.31, height=25, width=108)
        self.eth3.configure(activebackground="#f9f9f9")
        self.eth3.configure(activeforeground="black")
        self.eth3.configure(background="#d9d9d9")
        self.eth3.configure(disabledforeground="#a3a3a3")
        self.eth3.configure(foreground="#000000")
        self.eth3.configure(highlightbackground="#d9d9d9")
        self.eth3.configure(highlightcolor="black")
        self.eth3.configure(text=miners[2][4])

        self.eth4 = Label(top)
        self.eth4.place(relx=0.63, rely=0.38, height=25, width=108)
        self.eth4.configure(activebackground="#f9f9f9")
        self.eth4.configure(activeforeground="black")
        self.eth4.configure(background="#d9d9d9")
        self.eth4.configure(disabledforeground="#a3a3a3")
        self.eth4.configure(foreground="#000000")
        self.eth4.configure(highlightbackground="#d9d9d9")
        self.eth4.configure(highlightcolor="black")
        self.eth4.configure(text=miners[3][4])

        self.eth5 = Label(top)
        self.eth5.place(relx=0.63, rely=0.45, height=25, width=108)
        self.eth5.configure(activebackground="#f9f9f9")
        self.eth5.configure(activeforeground="black")
        self.eth5.configure(background="#d9d9d9")
        self.eth5.configure(disabledforeground="#a3a3a3")
        self.eth5.configure(foreground="#000000")
        self.eth5.configure(highlightbackground="#d9d9d9")
        self.eth5.configure(highlightcolor="black")
        self.eth5.configure(text=miners[4][4])

        self.eth6 = Label(top)
        self.eth6.place(relx=0.63, rely=0.52, height=25, width=108)
        self.eth6.configure(activebackground="#f9f9f9")
        self.eth6.configure(activeforeground="black")
        self.eth6.configure(background="#d9d9d9")
        self.eth6.configure(disabledforeground="#a3a3a3")
        self.eth6.configure(foreground="#000000")
        self.eth6.configure(highlightbackground="#d9d9d9")
        self.eth6.configure(highlightcolor="black")
        self.eth6.configure(text=miners[5][4])

        self.eth7 = Label(top)
        self.eth7.place(relx=0.63, rely=0.59, height=25, width=108)
        self.eth7.configure(activebackground="#f9f9f9")
        self.eth7.configure(activeforeground="black")
        self.eth7.configure(background="#d9d9d9")
        self.eth7.configure(disabledforeground="#a3a3a3")
        self.eth7.configure(foreground="#000000")
        self.eth7.configure(highlightbackground="#d9d9d9")
        self.eth7.configure(highlightcolor="black")
        self.eth7.configure(text=miners[6][4])

        self.m1profit = Label(top)
        self.m1profit.place(relx=0.77, rely=0.16, height=25, width=108)
        self.m1profit.configure(activebackground="#f9f9f9")
        self.m1profit.configure(activeforeground="black")
        self.m1profit.configure(background="#d9d9d9")
        self.m1profit.configure(disabledforeground="#a3a3a3")
        self.m1profit.configure(foreground="#000000")
        self.m1profit.configure(highlightbackground="#d9d9d9")
        self.m1profit.configure(highlightcolor="black")
        self.m1profit.configure(text=miners[0][5])

        self.m2profit = Label(top)
        self.m2profit.place(relx=0.77, rely=0.24, height=25, width=108)
        self.m2profit.configure(activebackground="#f9f9f9")
        self.m2profit.configure(activeforeground="black")
        self.m2profit.configure(background="#d9d9d9")
        self.m2profit.configure(disabledforeground="#a3a3a3")
        self.m2profit.configure(foreground="#000000")
        self.m2profit.configure(highlightbackground="#d9d9d9")
        self.m2profit.configure(highlightcolor="black")
        self.m2profit.configure(text=miners[1][5])

        self.m3profit = Label(top)
        self.m3profit.place(relx=0.77, rely=0.31, height=25, width=108)
        self.m3profit.configure(activebackground="#f9f9f9")
        self.m3profit.configure(activeforeground="black")
        self.m3profit.configure(background="#d9d9d9")
        self.m3profit.configure(disabledforeground="#a3a3a3")
        self.m3profit.configure(foreground="#000000")
        self.m3profit.configure(highlightbackground="#d9d9d9")
        self.m3profit.configure(highlightcolor="black")
        self.m3profit.configure(text=miners[2][5])

        self.m4profit = Label(top)
        self.m4profit.place(relx=0.77, rely=0.38, height=25, width=108)
        self.m4profit.configure(activebackground="#f9f9f9")
        self.m4profit.configure(activeforeground="black")
        self.m4profit.configure(background="#d9d9d9")
        self.m4profit.configure(disabledforeground="#a3a3a3")
        self.m4profit.configure(foreground="#000000")
        self.m4profit.configure(highlightbackground="#d9d9d9")
        self.m4profit.configure(highlightcolor="black")
        self.m4profit.configure(text=miners[3][5])

        self.m5profit = Label(top)
        self.m5profit.place(relx=0.77, rely=0.45, height=25, width=108)
        self.m5profit.configure(activebackground="#f9f9f9")
        self.m5profit.configure(activeforeground="black")
        self.m5profit.configure(background="#d9d9d9")
        self.m5profit.configure(disabledforeground="#a3a3a3")
        self.m5profit.configure(foreground="#000000")
        self.m5profit.configure(highlightbackground="#d9d9d9")
        self.m5profit.configure(highlightcolor="black")
        self.m5profit.configure(text=miners[4][5])

        self.m6profit = Label(top)
        self.m6profit.place(relx=0.77, rely=0.52, height=25, width=108)
        self.m6profit.configure(activebackground="#f9f9f9")
        self.m6profit.configure(activeforeground="black")
        self.m6profit.configure(background="#d9d9d9")
        self.m6profit.configure(disabledforeground="#a3a3a3")
        self.m6profit.configure(foreground="#000000")
        self.m6profit.configure(highlightbackground="#d9d9d9")
        self.m6profit.configure(highlightcolor="black")
        self.m6profit.configure(text=miners[5][5])

        self.m7profit = Label(top)
        self.m7profit.place(relx=0.77, rely=0.59, height=25, width=108)
        self.m7profit.configure(activebackground="#f9f9f9")
        self.m7profit.configure(activeforeground="black")
        self.m7profit.configure(background="#d9d9d9")
        self.m7profit.configure(disabledforeground="#a3a3a3")
        self.m7profit.configure(foreground="#000000")
        self.m7profit.configure(highlightbackground="#d9d9d9")
        self.m7profit.configure(highlightcolor="black")
        self.m7profit.configure(text=miners[6][5])

        self.Disclaimer = Label(top)
        self.Disclaimer.place(relx=-0.11, rely=0.87, height=11, width=544)
        self.Disclaimer.configure(activebackground="#f9f9f9")
        self.Disclaimer.configure(activeforeground="black")
        self.Disclaimer.configure(background="#d9d9d9")
        self.Disclaimer.configure(disabledforeground="#a3a3a3")
        self.Disclaimer.configure(foreground="#000000")
        self.Disclaimer.configure(highlightbackground="#d9d9d9")
        self.Disclaimer.configure(highlightcolor="black")
        self.Disclaimer.configure(text='''Note: Ripple(XRP) cannot be mined''')

        self.lblBalance = Label(top)
        self.lblBalance.place(relx=0.62, rely=0.71, height=51, width=194)
        self.lblBalance.configure(activebackground="#f9f9f9")
        self.lblBalance.configure(activeforeground="black")
        self.lblBalance.configure(background="#d9d9d9")
        self.lblBalance.configure(disabledforeground="#a3a3a3")
        self.lblBalance.configure(foreground="#000000")
        self.lblBalance.configure(highlightbackground="#d9d9d9")
        self.lblBalance.configure(highlightcolor="black")
        self.lblBalance.configure(text='Current Balance: $' + str('{:.2f}'.format(transactions.getfiattotal())))






if __name__ == '__main__':
    vp_start_gui()


