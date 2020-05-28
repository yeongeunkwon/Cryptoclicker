import sys, navigation, coins, transactions, advise

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

import holdings_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, top
    root = Tk()
    top = Holdings (root)
    holdings_support.init(root, top)
    updateGUI()
    root.mainloop()

w = None
def create_Holdings(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Holdings (w)
    holdings_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Holdings():
    global w
    w.destroy()
    w = None

def backToMenu():
    holdings_support.destroy_window()
    navigation.vp_start_gui()

def showGraph():
    transactions.transactiongraph()

def updateGUI():
    global top
    #prices
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

    #percent changes
    btcChange = advise.dayPercentChange("BTC")*100
    ethChange = advise.dayPercentChange("ETH")*100
    ltcChange = advise.dayPercentChange("LTC")*100
    bchChange = advise.dayPercentChange("BCH")*100
    xrpChange = advise.dayPercentChange("XRP")*100

    top.lblBTCchg.configure(text = str(btcChange)[:8] + '%')
    top.lblETHchg.configure(text = str(ethChange)[:8] + '%')
    top.lblLTCchg.configure(text = str(ltcChange)[:8] + '%')
    top.lblBCHchg.configure(text = str(bchChange)[:8] + '%')
    top.lblXRPchg.configure(text = str(xrpChange)[:8] + '%')

    #amounts and values
    btcValue = 0
    ethValue = 0
    ltcValue = 0
    bchValue = 0
    xrpValue = 0

    cryptolist = transactions.getcointotals()
    for element in cryptolist[0]:
        if element == "BTC":
            i = cryptolist[0].index('BTC')
            top.lblBTCamt.configure(text = str(cryptolist[1][i]) + " BTC")
            btcValue = cryptolist[1][i] * btcPrice
            top.lblBTCv.configure(text = '$' + str('{:.2f}'.format(btcValue)))
        if element == "ETH":
            i = cryptolist[0].index('ETH')
            top.lblETHamt.configure(text = str(cryptolist[1][i]) + " ETH")
            ethValue = cryptolist[1][i] * ethPrice
            top.lblETHv.configure(text = '$' + str('{:.2f}'.format(ethValue)))
        if element == "LTC":
            i = cryptolist[0].index('LTC')
            top.lblLTCamt.configure(text = str(cryptolist[1][i]) + " LTC")
            ltcValue = cryptolist[1][i] * ltcPrice
            top.lblLTCv.configure(text = '$' + str('{:.2f}'.format(ltcValue)))
        if element == "BCH":
            i = cryptolist[0].index('BCH')
            top.lblBCHamt.configure(text = str(cryptolist[1][i]) + " BCH")
            bchValue = cryptolist[1][i] * bchPrice
            top.lblBCHv.configure(text = '$' + str('{:.2f}'.format(bchValue)))
        if element == "XRP":
            i = cryptolist[0].index('XRP')
            top.lblXRPamt.configure(text = str(cryptolist[1][i]) + " XRP")
            xrpValue = cryptolist[1][i] * xrpPrice
            top.lblXRPv.configure(text = '$' + str('{:.2f}'.format(xrpValue)))

    #cash and total assets
    cash = transactions.getfiattotal()
    total = cash + btcValue + ethValue + ltcValue + bchValue + xrpValue
    top.lblUSD.configure(text = 'USD = $' + str('{:.2f}'.format(cash)))
    top.lblTotalAssets.configure(text = 'Total Assets = $' + str('{:.2f}'.format(total)))
    transactions.minecoins()
    transactions.electricitycost()

class Holdings:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("897x400+514+209")
        top.title("Holdings")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.btnMainMenu = Button(top)
        self.btnMainMenu.place(relx=0.02, rely=0.02, height=40, width=128)
        self.btnMainMenu.configure(activebackground="#d9d9d9")
        self.btnMainMenu.configure(activeforeground="#000000")
        self.btnMainMenu.configure(background="#d9d9d9")
        self.btnMainMenu.configure(disabledforeground="#a3a3a3")
        self.btnMainMenu.configure(foreground="#000000")
        self.btnMainMenu.configure(highlightbackground="#d9d9d9")
        self.btnMainMenu.configure(highlightcolor="black")
        self.btnMainMenu.configure(pady="0")
        self.btnMainMenu.configure(text='''Main Menu''')
        self.btnMainMenu.configure(command=backToMenu)

        self.btnShowGraph = Button(top)
        self.btnShowGraph.place(relx=0.02, rely=0.8, height=40, width=128)
        self.btnShowGraph.configure(activebackground="#d9d9d9")
        self.btnShowGraph.configure(activeforeground="#000000")
        self.btnShowGraph.configure(background="#d9d9d9")
        self.btnShowGraph.configure(disabledforeground="#a3a3a3")
        self.btnShowGraph.configure(foreground="#000000")
        self.btnShowGraph.configure(highlightbackground="#d9d9d9")
        self.btnShowGraph.configure(highlightcolor="black")
        self.btnShowGraph.configure(pady="0")
        self.btnShowGraph.configure(text='''Show Graph''')
        self.btnShowGraph.configure(command=showGraph)

        self.lblBTC = Label(top)
        self.lblBTC.place(relx=0.04, rely=0.12, height=40, width=128)
        self.lblBTC.configure(activebackground="#f9f9f9")
        self.lblBTC.configure(activeforeground="black")
        self.lblBTC.configure(anchor=W)
        self.lblBTC.configure(background="#d9d9d9")
        self.lblBTC.configure(disabledforeground="#a3a3a3")
        self.lblBTC.configure(foreground="#000000")
        self.lblBTC.configure(highlightbackground="#d9d9d9")
        self.lblBTC.configure(highlightcolor="black")
        self.lblBTC.configure(text='''Bitcoin''')

        self.lblBCH = Label(top)
        self.lblBCH.place(relx=0.04, rely=0.18, height=40, width=128)
        self.lblBCH.configure(activebackground="#f9f9f9")
        self.lblBCH.configure(activeforeground="black")
        self.lblBCH.configure(anchor=W)
        self.lblBCH.configure(background="#d9d9d9")
        self.lblBCH.configure(disabledforeground="#a3a3a3")
        self.lblBCH.configure(foreground="#000000")
        self.lblBCH.configure(highlightbackground="#d9d9d9")
        self.lblBCH.configure(highlightcolor="black")
        self.lblBCH.configure(text='''Bitcoin Cash''')

        self.lblLTC = Label(top)
        self.lblLTC.place(relx=0.04, rely=0.24, height=40, width=128)
        self.lblLTC.configure(activebackground="#f9f9f9")
        self.lblLTC.configure(activeforeground="black")
        self.lblLTC.configure(anchor=W)
        self.lblLTC.configure(background="#d9d9d9")
        self.lblLTC.configure(disabledforeground="#a3a3a3")
        self.lblLTC.configure(foreground="#000000")
        self.lblLTC.configure(highlightbackground="#d9d9d9")
        self.lblLTC.configure(highlightcolor="black")
        self.lblLTC.configure(text='''Litecoin''')

        self.lblETH = Label(top)
        self.lblETH.place(relx=0.04, rely=0.30, height=40, width=128)
        self.lblETH.configure(activebackground="#f9f9f9")
        self.lblETH.configure(activeforeground="black")
        self.lblETH.configure(anchor=W)
        self.lblETH.configure(background="#d9d9d9")
        self.lblETH.configure(disabledforeground="#a3a3a3")
        self.lblETH.configure(foreground="#000000")
        self.lblETH.configure(highlightbackground="#d9d9d9")
        self.lblETH.configure(highlightcolor="black")
        self.lblETH.configure(text='''Ethereum''')

        self.lblXRP = Label(top)
        self.lblXRP.place(relx=0.04, rely=0.36, height=40, width=128)
        self.lblXRP.configure(activebackground="#f9f9f9")
        self.lblXRP.configure(activeforeground="black")
        self.lblXRP.configure(anchor=W)
        self.lblXRP.configure(background="#d9d9d9")
        self.lblXRP.configure(disabledforeground="#a3a3a3")
        self.lblXRP.configure(foreground="#000000")
        self.lblXRP.configure(highlightbackground="#d9d9d9")
        self.lblXRP.configure(highlightcolor="black")
        self.lblXRP.configure(text='''Ripple''')

        self.lblPrice = Label(top)
        self.lblPrice.place(relx=0.2, rely=0.06, height=40, width=128)
        self.lblPrice.configure(activebackground="#f9f9f9")
        self.lblPrice.configure(activeforeground="black")
        self.lblPrice.configure(anchor=W)
        self.lblPrice.configure(background="#d9d9d9")
        self.lblPrice.configure(disabledforeground="#a3a3a3")
        self.lblPrice.configure(foreground="#000000")
        self.lblPrice.configure(highlightbackground="#d9d9d9")
        self.lblPrice.configure(highlightcolor="black")
        self.lblPrice.configure(text='''Price''')

        self.lblChange = Label(top)
        self.lblChange.place(relx=0.36, rely=0.06, height=40, width=128)
        self.lblChange.configure(activebackground="#f9f9f9")
        self.lblChange.configure(activeforeground="black")
        self.lblChange.configure(anchor=W)
        self.lblChange.configure(background="#d9d9d9")
        self.lblChange.configure(disabledforeground="#a3a3a3")
        self.lblChange.configure(foreground="#000000")
        self.lblChange.configure(highlightbackground="#d9d9d9")
        self.lblChange.configure(highlightcolor="black")
        self.lblChange.configure(text='''24h Change''')

        self.lblAmt_11 = Label(top)
        self.lblAmt_11.place(relx=0.52, rely=0.06, height=40, width=128)
        self.lblAmt_11.configure(activebackground="#f9f9f9")
        self.lblAmt_11.configure(activeforeground="black")
        self.lblAmt_11.configure(anchor=W)
        self.lblAmt_11.configure(background="#d9d9d9")
        self.lblAmt_11.configure(disabledforeground="#a3a3a3")
        self.lblAmt_11.configure(foreground="#000000")
        self.lblAmt_11.configure(highlightbackground="#d9d9d9")
        self.lblAmt_11.configure(highlightcolor="black")
        self.lblAmt_11.configure(text='''Amount''')

        self.lblValue = Label(top)
        self.lblValue.place(relx=0.68, rely=0.06, height=40, width=128)
        self.lblValue.configure(activebackground="#f9f9f9")
        self.lblValue.configure(activeforeground="black")
        self.lblValue.configure(anchor=W)
        self.lblValue.configure(background="#d9d9d9")
        self.lblValue.configure(disabledforeground="#a3a3a3")
        self.lblValue.configure(foreground="#000000")
        self.lblValue.configure(highlightbackground="#d9d9d9")
        self.lblValue.configure(highlightcolor="black")
        self.lblValue.configure(text='''Value''')

        self.lblRate = Label(top)
        self.lblRate.place(relx=0.84, rely=0.06, height=40, width=128)
        self.lblRate.configure(activebackground="#f9f9f9")
        self.lblRate.configure(activeforeground="black")
        self.lblRate.configure(anchor=W)
        self.lblRate.configure(background="#d9d9d9")
        self.lblRate.configure(disabledforeground="#a3a3a3")
        self.lblRate.configure(foreground="#000000")
        self.lblRate.configure(highlightbackground="#d9d9d9")
        self.lblRate.configure(highlightcolor="black")
        self.lblRate.configure(text='''Mining Rate / D''')

        self.lblBTCp = Label(top)
        self.lblBTCp.place(relx=0.2, rely=0.12, height=40, width=128)
        self.lblBTCp.configure(activebackground="#f9f9f9")
        self.lblBTCp.configure(activeforeground="black")
        self.lblBTCp.configure(anchor=W)
        self.lblBTCp.configure(background="#d9d9d9")
        self.lblBTCp.configure(disabledforeground="#a3a3a3")
        self.lblBTCp.configure(foreground="#000000")
        self.lblBTCp.configure(highlightbackground="#d9d9d9")
        self.lblBTCp.configure(highlightcolor="black")
        self.lblBTCp.configure(text='''$$''')

        self.lblBCHp = Label(top)
        self.lblBCHp.place(relx=0.2, rely=0.18, height=40, width=128)
        self.lblBCHp.configure(activebackground="#f9f9f9")
        self.lblBCHp.configure(activeforeground="black")
        self.lblBCHp.configure(anchor=W)
        self.lblBCHp.configure(background="#d9d9d9")
        self.lblBCHp.configure(disabledforeground="#a3a3a3")
        self.lblBCHp.configure(foreground="#000000")
        self.lblBCHp.configure(highlightbackground="#d9d9d9")
        self.lblBCHp.configure(highlightcolor="black")
        self.lblBCHp.configure(text='''$$''')

        self.lblLTCp = Label(top)
        self.lblLTCp.place(relx=0.2, rely=0.24, height=40, width=128)
        self.lblLTCp.configure(activebackground="#f9f9f9")
        self.lblLTCp.configure(activeforeground="black")
        self.lblLTCp.configure(anchor=W)
        self.lblLTCp.configure(background="#d9d9d9")
        self.lblLTCp.configure(disabledforeground="#a3a3a3")
        self.lblLTCp.configure(foreground="#000000")
        self.lblLTCp.configure(highlightbackground="#d9d9d9")
        self.lblLTCp.configure(highlightcolor="black")
        self.lblLTCp.configure(text='''$$''')

        self.lblETHp = Label(top)
        self.lblETHp.place(relx=0.2, rely=0.30, height=40, width=128)
        self.lblETHp.configure(activebackground="#f9f9f9")
        self.lblETHp.configure(activeforeground="black")
        self.lblETHp.configure(anchor=W)
        self.lblETHp.configure(background="#d9d9d9")
        self.lblETHp.configure(disabledforeground="#a3a3a3")
        self.lblETHp.configure(foreground="#000000")
        self.lblETHp.configure(highlightbackground="#d9d9d9")
        self.lblETHp.configure(highlightcolor="black")
        self.lblETHp.configure(text='''$$''')

        self.lblXRPp = Label(top)
        self.lblXRPp.place(relx=0.2, rely=0.36, height=40, width=128)
        self.lblXRPp.configure(activebackground="#f9f9f9")
        self.lblXRPp.configure(activeforeground="black")
        self.lblXRPp.configure(anchor=W)
        self.lblXRPp.configure(background="#d9d9d9")
        self.lblXRPp.configure(disabledforeground="#a3a3a3")
        self.lblXRPp.configure(foreground="#000000")
        self.lblXRPp.configure(highlightbackground="#d9d9d9")
        self.lblXRPp.configure(highlightcolor="black")
        self.lblXRPp.configure(text='''$$''')

        self.lblBTCchg = Label(top)
        self.lblBTCchg.place(relx=0.36, rely=0.12, height=40, width=128)
        self.lblBTCchg.configure(activebackground="#f9f9f9")
        self.lblBTCchg.configure(activeforeground="black")
        self.lblBTCchg.configure(anchor=W)
        self.lblBTCchg.configure(background="#d9d9d9")
        self.lblBTCchg.configure(disabledforeground="#a3a3a3")
        self.lblBTCchg.configure(foreground="#000000")
        self.lblBTCchg.configure(highlightbackground="#d9d9d9")
        self.lblBTCchg.configure(highlightcolor="black")
        self.lblBTCchg.configure(text='''%''')

        self.lblBCHchg = Label(top)
        self.lblBCHchg.place(relx=0.36, rely=0.18, height=40, width=128)
        self.lblBCHchg.configure(activebackground="#f9f9f9")
        self.lblBCHchg.configure(activeforeground="black")
        self.lblBCHchg.configure(anchor=W)
        self.lblBCHchg.configure(background="#d9d9d9")
        self.lblBCHchg.configure(disabledforeground="#a3a3a3")
        self.lblBCHchg.configure(foreground="#000000")
        self.lblBCHchg.configure(highlightbackground="#d9d9d9")
        self.lblBCHchg.configure(highlightcolor="black")
        self.lblBCHchg.configure(text='''%''')

        self.lblLTCchg = Label(top)
        self.lblLTCchg.place(relx=0.36, rely=0.24, height=40, width=128)
        self.lblLTCchg.configure(activebackground="#f9f9f9")
        self.lblLTCchg.configure(activeforeground="black")
        self.lblLTCchg.configure(anchor=W)
        self.lblLTCchg.configure(background="#d9d9d9")
        self.lblLTCchg.configure(disabledforeground="#a3a3a3")
        self.lblLTCchg.configure(foreground="#000000")
        self.lblLTCchg.configure(highlightbackground="#d9d9d9")
        self.lblLTCchg.configure(highlightcolor="black")
        self.lblLTCchg.configure(text='''%''')

        self.lblETHchg = Label(top)
        self.lblETHchg.place(relx=0.36, rely=0.30, height=40, width=128)
        self.lblETHchg.configure(activebackground="#f9f9f9")
        self.lblETHchg.configure(activeforeground="black")
        self.lblETHchg.configure(anchor=W)
        self.lblETHchg.configure(background="#d9d9d9")
        self.lblETHchg.configure(disabledforeground="#a3a3a3")
        self.lblETHchg.configure(foreground="#000000")
        self.lblETHchg.configure(highlightbackground="#d9d9d9")
        self.lblETHchg.configure(highlightcolor="black")
        self.lblETHchg.configure(text='''%''')

        self.lblXRPchg = Label(top)
        self.lblXRPchg.place(relx=0.36, rely=0.36, height=40, width=128)
        self.lblXRPchg.configure(activebackground="#f9f9f9")
        self.lblXRPchg.configure(activeforeground="black")
        self.lblXRPchg.configure(anchor=W)
        self.lblXRPchg.configure(background="#d9d9d9")
        self.lblXRPchg.configure(disabledforeground="#a3a3a3")
        self.lblXRPchg.configure(foreground="#000000")
        self.lblXRPchg.configure(highlightbackground="#d9d9d9")
        self.lblXRPchg.configure(highlightcolor="black")
        self.lblXRPchg.configure(text='''%''')

        self.lblBTCamt = Label(top)
        self.lblBTCamt.place(relx=0.52, rely=0.12, height=40, width=128)
        self.lblBTCamt.configure(activebackground="#f9f9f9")
        self.lblBTCamt.configure(activeforeground="black")
        self.lblBTCamt.configure(anchor=W)
        self.lblBTCamt.configure(background="#d9d9d9")
        self.lblBTCamt.configure(disabledforeground="#a3a3a3")
        self.lblBTCamt.configure(foreground="#000000")
        self.lblBTCamt.configure(highlightbackground="#d9d9d9")
        self.lblBTCamt.configure(highlightcolor="black")
        self.lblBTCamt.configure(text='''-------''')

        self.lblBCHamt = Label(top)
        self.lblBCHamt.place(relx=0.52, rely=0.18, height=40, width=128)
        self.lblBCHamt.configure(activebackground="#f9f9f9")
        self.lblBCHamt.configure(activeforeground="black")
        self.lblBCHamt.configure(anchor=W)
        self.lblBCHamt.configure(background="#d9d9d9")
        self.lblBCHamt.configure(disabledforeground="#a3a3a3")
        self.lblBCHamt.configure(foreground="#000000")
        self.lblBCHamt.configure(highlightbackground="#d9d9d9")
        self.lblBCHamt.configure(highlightcolor="black")
        self.lblBCHamt.configure(text='''-------''')

        self.lblLTCamt = Label(top)
        self.lblLTCamt.place(relx=0.52, rely=0.24, height=40, width=128)
        self.lblLTCamt.configure(activebackground="#f9f9f9")
        self.lblLTCamt.configure(activeforeground="black")
        self.lblLTCamt.configure(anchor=W)
        self.lblLTCamt.configure(background="#d9d9d9")
        self.lblLTCamt.configure(disabledforeground="#a3a3a3")
        self.lblLTCamt.configure(foreground="#000000")
        self.lblLTCamt.configure(highlightbackground="#d9d9d9")
        self.lblLTCamt.configure(highlightcolor="black")
        self.lblLTCamt.configure(text='''-------''')

        self.lblETHamt = Label(top)
        self.lblETHamt.place(relx=0.52, rely=0.30, height=40, width=128)
        self.lblETHamt.configure(activebackground="#f9f9f9")
        self.lblETHamt.configure(activeforeground="black")
        self.lblETHamt.configure(anchor=W)
        self.lblETHamt.configure(background="#d9d9d9")
        self.lblETHamt.configure(disabledforeground="#a3a3a3")
        self.lblETHamt.configure(foreground="#000000")
        self.lblETHamt.configure(highlightbackground="#d9d9d9")
        self.lblETHamt.configure(highlightcolor="black")
        self.lblETHamt.configure(text='''-------''')

        self.lblXRPamt = Label(top)
        self.lblXRPamt.place(relx=0.52, rely=0.36, height=40, width=128)
        self.lblXRPamt.configure(activebackground="#f9f9f9")
        self.lblXRPamt.configure(activeforeground="black")
        self.lblXRPamt.configure(anchor=W)
        self.lblXRPamt.configure(background="#d9d9d9")
        self.lblXRPamt.configure(disabledforeground="#a3a3a3")
        self.lblXRPamt.configure(foreground="#000000")
        self.lblXRPamt.configure(highlightbackground="#d9d9d9")
        self.lblXRPamt.configure(highlightcolor="black")
        self.lblXRPamt.configure(text='''-------''')

        self.lblBTCv = Label(top)
        self.lblBTCv.place(relx=0.68, rely=0.12, height=40, width=128)
        self.lblBTCv.configure(activebackground="#f9f9f9")
        self.lblBTCv.configure(activeforeground="black")
        self.lblBTCv.configure(anchor=W)
        self.lblBTCv.configure(background="#d9d9d9")
        self.lblBTCv.configure(disabledforeground="#a3a3a3")
        self.lblBTCv.configure(foreground="#000000")
        self.lblBTCv.configure(highlightbackground="#d9d9d9")
        self.lblBTCv.configure(highlightcolor="black")
        self.lblBTCv.configure(text='''-------''')

        self.lblBCHv = Label(top)
        self.lblBCHv.place(relx=0.68, rely=0.18, height=40, width=128)
        self.lblBCHv.configure(activebackground="#f9f9f9")
        self.lblBCHv.configure(activeforeground="black")
        self.lblBCHv.configure(anchor=W)
        self.lblBCHv.configure(background="#d9d9d9")
        self.lblBCHv.configure(disabledforeground="#a3a3a3")
        self.lblBCHv.configure(foreground="#000000")
        self.lblBCHv.configure(highlightbackground="#d9d9d9")
        self.lblBCHv.configure(highlightcolor="black")
        self.lblBCHv.configure(text='''-------''')

        self.lblLTCv = Label(top)
        self.lblLTCv.place(relx=0.68, rely=0.24, height=40, width=128)
        self.lblLTCv.configure(activebackground="#f9f9f9")
        self.lblLTCv.configure(activeforeground="black")
        self.lblLTCv.configure(anchor=W)
        self.lblLTCv.configure(background="#d9d9d9")
        self.lblLTCv.configure(disabledforeground="#a3a3a3")
        self.lblLTCv.configure(foreground="#000000")
        self.lblLTCv.configure(highlightbackground="#d9d9d9")
        self.lblLTCv.configure(highlightcolor="black")
        self.lblLTCv.configure(text='''-------''')

        self.lblETHv = Label(top)
        self.lblETHv.place(relx=0.68, rely=0.30, height=40, width=128)
        self.lblETHv.configure(activebackground="#f9f9f9")
        self.lblETHv.configure(activeforeground="black")
        self.lblETHv.configure(anchor=W)
        self.lblETHv.configure(background="#d9d9d9")
        self.lblETHv.configure(disabledforeground="#a3a3a3")
        self.lblETHv.configure(foreground="#000000")
        self.lblETHv.configure(highlightbackground="#d9d9d9")
        self.lblETHv.configure(highlightcolor="black")
        self.lblETHv.configure(text='''-------''')

        self.lblXRPv = Label(top)
        self.lblXRPv.place(relx=0.68, rely=0.36, height=40, width=128)
        self.lblXRPv.configure(activebackground="#f9f9f9")
        self.lblXRPv.configure(activeforeground="black")
        self.lblXRPv.configure(anchor=W)
        self.lblXRPv.configure(background="#d9d9d9")
        self.lblXRPv.configure(disabledforeground="#a3a3a3")
        self.lblXRPv.configure(foreground="#000000")
        self.lblXRPv.configure(highlightbackground="#d9d9d9")
        self.lblXRPv.configure(highlightcolor="black")
        self.lblXRPv.configure(text='''-------''')

        self.lblBTCm = Label(top)
        self.lblBTCm.place(relx=0.84, rely=0.12, height=40, width=128)
        self.lblBTCm.configure(activebackground="#f9f9f9")
        self.lblBTCm.configure(activeforeground="black")
        self.lblBTCm.configure(anchor=W)
        self.lblBTCm.configure(background="#d9d9d9")
        self.lblBTCm.configure(disabledforeground="#a3a3a3")
        self.lblBTCm.configure(foreground="#000000")
        self.lblBTCm.configure(highlightbackground="#d9d9d9")
        self.lblBTCm.configure(highlightcolor="black")
        self.lblBTCm.configure(text='''BTC/D''')

        self.lblBCHm = Label(top)
        self.lblBCHm.place(relx=0.84, rely=0.18, height=40, width=128)
        self.lblBCHm.configure(activebackground="#f9f9f9")
        self.lblBCHm.configure(activeforeground="black")
        self.lblBCHm.configure(anchor=W)
        self.lblBCHm.configure(background="#d9d9d9")
        self.lblBCHm.configure(disabledforeground="#a3a3a3")
        self.lblBCHm.configure(foreground="#000000")
        self.lblBCHm.configure(highlightbackground="#d9d9d9")
        self.lblBCHm.configure(highlightcolor="black")
        self.lblBCHm.configure(text='''BCH/D''')

        self.lblLTCm = Label(top)
        self.lblLTCm.place(relx=0.84, rely=0.24, height=40, width=128)
        self.lblLTCm.configure(activebackground="#f9f9f9")
        self.lblLTCm.configure(activeforeground="black")
        self.lblLTCm.configure(anchor=W)
        self.lblLTCm.configure(background="#d9d9d9")
        self.lblLTCm.configure(disabledforeground="#a3a3a3")
        self.lblLTCm.configure(foreground="#000000")
        self.lblLTCm.configure(highlightbackground="#d9d9d9")
        self.lblLTCm.configure(highlightcolor="black")
        self.lblLTCm.configure(text='''LTC/D''')

        self.lblETHm = Label(top)
        self.lblETHm.place(relx=0.84, rely=0.30, height=40, width=128)
        self.lblETHm.configure(activebackground="#f9f9f9")
        self.lblETHm.configure(activeforeground="black")
        self.lblETHm.configure(anchor=W)
        self.lblETHm.configure(background="#d9d9d9")
        self.lblETHm.configure(disabledforeground="#a3a3a3")
        self.lblETHm.configure(foreground="#000000")
        self.lblETHm.configure(highlightbackground="#d9d9d9")
        self.lblETHm.configure(highlightcolor="black")
        self.lblETHm.configure(text='''ETH/D''')

        self.lblXRPm = Label(top)
        self.lblXRPm.place(relx=0.84, rely=0.36, height=40, width=128)
        self.lblXRPm.configure(activebackground="#f9f9f9")
        self.lblXRPm.configure(activeforeground="black")
        self.lblXRPm.configure(anchor=W)
        self.lblXRPm.configure(background="#d9d9d9")
        self.lblXRPm.configure(disabledforeground="#a3a3a3")
        self.lblXRPm.configure(foreground="#000000")
        self.lblXRPm.configure(highlightbackground="#d9d9d9")
        self.lblXRPm.configure(highlightcolor="black")
        self.lblXRPm.configure(text='''-------''')

        self.lblUSD = Label(top)
        self.lblUSD.place(relx=0.09, rely=0.42, height=40, width=128)
        self.lblUSD.configure(activebackground="#f9f9f9")
        self.lblUSD.configure(activeforeground="black")
        self.lblUSD.configure(anchor=W)
        self.lblUSD.configure(background="#d9d9d9")
        self.lblUSD.configure(disabledforeground="#a3a3a3")
        self.lblUSD.configure(foreground="#000000")
        self.lblUSD.configure(highlightbackground="#d9d9d9")
        self.lblUSD.configure(highlightcolor="black")
        self.lblUSD.configure(text='''USD =''')

        self.lblTotalAssets = Label(top)
        self.lblTotalAssets.place(relx=0.25, rely=0.42, height=40, width=218)
        self.lblTotalAssets.configure(activebackground="#f9f9f9")
        self.lblTotalAssets.configure(activeforeground="black")
        self.lblTotalAssets.configure(anchor=W)
        self.lblTotalAssets.configure(background="#d9d9d9")
        self.lblTotalAssets.configure(disabledforeground="#a3a3a3")
        self.lblTotalAssets.configure(foreground="#000000")
        self.lblTotalAssets.configure(highlightbackground="#d9d9d9")
        self.lblTotalAssets.configure(highlightcolor="black")
        self.lblTotalAssets.configure(text='''Total Assets =''')






if __name__ == '__main__':
    vp_start_gui()



