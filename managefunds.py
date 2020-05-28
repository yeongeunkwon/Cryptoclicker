import sys, navigation, transactions, tkinter.messagebox

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

import managefunds_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, top
    root = Tk()
    top = Manage_Funds (root)
    managefunds_support.init(root, top)
    top.txtAmount.focus()
    root.mainloop()

w = None
def create_Manage_Funds(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Manage_Funds (w)
    managefunds_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Manage_Funds():
    global w
    w.destroy()
    w = None

def backToMenu():
    managefunds_support.destroy_window()
    navigation.vp_start_gui()

def withdraw(): #take out money from account
    global top
    amount = top.txtAmount.get("1.0",'end-1c')
    try:
        if str(amount).find('.') >= 0:
            amount = float(amount)
        elif str(amount).find('.') < 0:
            amount = int(amount)

        if amount < 0:
            tkinter.messagebox.showerror("Invalid", "Please enter a positive number.")
            top.txtAmount.focus()
        elif transactions.getfiattotal() < amount:
            confirm = tkinter.messagebox.askyesno("Confirmation","Take out all free money from your account?")
            if confirm:
                amount = transactions.getfiattotal()
                transactions.removefiat(amount)
                refreshGUI()
        else:
            confirm = tkinter.messagebox.askyesno("Confirmation", "Are you sure you want to remove $%0.2f to your account?"%amount)
            if confirm:
                transactions.removefiat(amount)
                refreshGUI()
            else:
                tkinter.messagebox.showinfo("Information","The money was not removed from your account.")
    except:
        tkinter.messagebox.showerror('Error', 'Invalid Withdrawl Amount.')
        top.txtAmount.delete("1.0", END)
        top.txtAmount.focus()

def deposit(): #add money to account
    global top
    amount = top.txtAmount.get("1.0",'end-1c')
    try:
        if str(amount).find('.') >= 0:
            amount = float(amount)
        elif str(amount).find('.') < 0:
            amount = int(amount)

        if amount < 0:
            tkinter.messagebox.showerror("Invalid", "Please enter a positive number.")
            top.txtAmount.focus()
        elif amount > 50000:
            tkinter.messagebox.showerror("Error","Please do not add more than $50,000 at one time.")
            top.txtAmount.focus()
        else:
            confirm = tkinter.messagebox.askyesno("Confirmation", "Are you sure you want to add $%0.2f to your account?"%amount)
            if confirm:
                transactions.addfiat(amount)
                refreshGUI()
            else:
                tkinter.messagebox.showinfo("Information","The money was not added to your account.")
            
    except:
        tkinter.messagebox.showerror('Error', 'Invalid Deposit Amount.')
        top.txtAmount.delete("1.0", END)
        top.txtAmount.focus()

def refreshGUI():
    global top
    holdings = transactions.getfiattotal()
    top.lblHoldingsAmount.configure(text='$' + str('{:.2f}'.format(holdings)))

class Manage_Funds:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Courier New} -size 14 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("514x329+635+333")
        top.title("Manage Funds")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.btnWithdraw = Button(top)
        self.btnWithdraw.place(relx=0.1, rely=0.7, height=44, width=137)
        self.btnWithdraw.configure(activebackground="#d9d9d9")
        self.btnWithdraw.configure(activeforeground="#000000")
        self.btnWithdraw.configure(background="#d9d9d9")
        self.btnWithdraw.configure(disabledforeground="#a3a3a3")
        self.btnWithdraw.configure(foreground="#000000")
        self.btnWithdraw.configure(highlightbackground="#d9d9d9")
        self.btnWithdraw.configure(highlightcolor="black")
        self.btnWithdraw.configure(pady="0")
        self.btnWithdraw.configure(text='''Withdraw''')
        self.btnWithdraw.configure(command=withdraw)

        self.lblEnterAmount = Label(top)
        self.lblEnterAmount.place(relx=0.06, rely=0.44, height=41, width=124)
        self.lblEnterAmount.configure(activebackground="#f9f9f9")
        self.lblEnterAmount.configure(activeforeground="black")
        self.lblEnterAmount.configure(background="#d9d9d9")
        self.lblEnterAmount.configure(disabledforeground="#a3a3a3")
        self.lblEnterAmount.configure(font=font10)
        self.lblEnterAmount.configure(foreground="#000000")
        self.lblEnterAmount.configure(highlightbackground="#d9d9d9")
        self.lblEnterAmount.configure(highlightcolor="black")
        self.lblEnterAmount.configure(text='''Enter Amount:''')

        self.txtAmount = Text(top)
        self.txtAmount.place(relx=0.35, rely=0.475,height=20, relwidth=0.38)
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

        self.btnDeposit = Button(top)
        self.btnDeposit.place(relx=0.64, rely=0.7, height=44, width=137)
        self.btnDeposit.configure(activebackground="#d9d9d9")
        self.btnDeposit.configure(activeforeground="#000000")
        self.btnDeposit.configure(background="#d9d9d9")
        self.btnDeposit.configure(disabledforeground="#a3a3a3")
        self.btnDeposit.configure(foreground="#000000")
        self.btnDeposit.configure(highlightbackground="#d9d9d9")
        self.btnDeposit.configure(highlightcolor="black")
        self.btnDeposit.configure(pady="0")
        self.btnDeposit.configure(text='''Deposit''')
        self.btnDeposit.configure(command=deposit)

        self.lblHoldingsText = Label(top)
        self.lblHoldingsText.place(relx=0.01, rely=0.27, height=41, width=184)
        self.lblHoldingsText.configure(activebackground="#f9f9f9")
        self.lblHoldingsText.configure(activeforeground="black")
        self.lblHoldingsText.configure(background="#d9d9d9")
        self.lblHoldingsText.configure(disabledforeground="#a3a3a3")
        self.lblHoldingsText.configure(font=font10)
        self.lblHoldingsText.configure(foreground="#000000")
        self.lblHoldingsText.configure(highlightbackground="#d9d9d9")
        self.lblHoldingsText.configure(highlightcolor="black")
        self.lblHoldingsText.configure(text='''Current Holdings:''')
        self.lblHoldingsText.configure(width=184)

        self.btnMenu = Button(top)
        self.btnMenu.place(relx=0.1, rely=0.09, height=44, width=137)
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

        holdings = transactions.getfiattotal()
        self.lblHoldingsAmount = Label(top)
        self.lblHoldingsAmount.place(relx=0.35, rely=0.29, height=31, width=114)
        self.lblHoldingsAmount.configure(background="#d9d9d9")
        self.lblHoldingsAmount.configure(disabledforeground="#a3a3a3")
        self.lblHoldingsAmount.configure(font=font10)
        self.lblHoldingsAmount.configure(foreground="#000000")
        self.lblHoldingsAmount.configure(text='$' + str('{:.2f}'.format(holdings)))
        self.lblHoldingsAmount.configure(width=114)






if __name__ == '__main__':
    vp_start_gui()



