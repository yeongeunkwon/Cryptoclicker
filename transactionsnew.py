import datetime, coins, json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import tkinter.messagebox

startingfiat = 1000 #starting USD
transactionlist = []
minerlist = [0, 0, 0, 0, 0, 0, 0]
minedlist = [[datetime.datetime.now(), [0,0,0,0]]]
eleclist = []
miners = [
# Name,          BTC,       BCH,       LTC,     ETH,       Day,  Watt, Cost
["Antminer S9",  0.0008753, 0.0059013, 0,       0,        7.97,  1300, 2000],
["Antminer L3+", 0,         0,         0.02877, 0,        4.21,   800, 3000],
["AMD RX 570",   0,         0,         0,       0.002299, 1.55,    80,  250],
["Pagolin M3X",  0.0004998, 0.0033722, 0,       0,        4.56,  2000, 1000],
["Miner5", 0, 0, 0, 0, 0, 0, 0],
["Miner6", 0, 0, 0, 0, 0, 0, 0],
["Miner7", 0, 0, 0, 0, 0, 0, 0]]

def buycoin(coin, amount):
	global transactionlist
	coinprice = coins.getCoinVal(coin) #network group task
	transactionvalue = coinprice * amount
	if transactionvalue > getfiattotal():
		return -1	 #you do not have enough money to go through with this transaction
	transactionlist.append([str(datetime.datetime.now()),-1,coin,amount,coinprice]) #-1 for buy, 1 for sell
	return 1

def sellcoin(coin, amount):
	global transactionlist
	coinprice = coins.getCoinVal(coin)
	transactionvalue = coinprice * amount
	if amount > numberofcoin(coin):
		return -2	 #you do not have enough coins to go through with this transaction
	transactionlist.append([str(datetime.datetime.now()),1,coin,amount,coinprice]) #-1 for buy, 1 for sell
	return 2

def buysell(transactiontype,coin, amount):
    if transactiontype == 1:
        success = sellcoin(coin, amount)
    else:
        success = buycoin(coin, amount)
    if success == 1:
        savetofile()
        tkinter.messagebox.showinfo("Information",'You bought %.5f %s at $%.2f, and you now have $%.2f remaining.' %(amount, coin, coins.getCoinVal(coin)*amount, getfiattotal()))
    elif success == 2:
        savetofile()
        tkinter.messagebox.showinfo("Information",'You sold %.5f %s at $%.2f, and you now have $%.2f to spend.' %(amount, coin, coins.getCoinVal(coin)*amount, getfiattotal()))
    elif success == -1:
        tkinter.messagebox.showerror("Error","You do not have enough money to make this order.")
    else:
        tkinter.messagebox.showerror("Error","You do not have enough coin to sell.")
    return success

def buyminer(miner, amount):
    global minerlist, miners
    price = miners[miner][7]
    transactionvalue = price * amount
    if transactionvalue > getfiattotal():
        return -1    #you do not have enough money to go through with this transaction
    minerlist.append([str(datetime.datetime.now()),-1,miner,amount]) #-1 for buy, 1 for sell
    return 0

def sellminer(miner, amount):
    global minerlist, miners
    price = miners[miner][7]
    transactionvalue = price * amount
    if amount > numberofminers(miner):
        return -1    #you do not have enough miners to go through with this transaction
    minerlist.append([str(datetime.datetime.now()),1,miner,amount]) #-1 for buy, 1 for sell
    return 0

def electricitycost():
    global eleclist
    kWhour = .12
    Watts = getwatttotals()
    costpersec = getwatttotals() * kWhour / (60*60*1000)
    seconds = 0
    if len(eleclist) > 0:
        seconds = (datetime.datetime.now()-datetime.datetime.strptime(str(eleclist[len(eleclist)-1][0]), '%Y-%m-%d %X.%f')).total_seconds()
    if len(eleclist) == 0 or seconds > 5:
        eleclist.append([str(datetime.datetime.now()), costpersec * seconds])
        removefiat(costpersec * seconds)

'''
minerlist = [0, 0, 0, 0, 0, 0, 0]
minedlist = [[datetime.datetime.now(), [0,0,0,0]]]
miners = [
# Name,          BTC,       BCH,       LTC,     ETH,       Day,  Watt, Cost
["Antminer S9",  0.0008753, 0.0059013, 0,       0,        7.97,  1300, 2000],
["Antminer L3+", 0,         0,         0.02877, 0,        4.21,   800, 3000],
["AMD RX 570",   0,         0,         0,       0.002299, 1.55,    80,  250],
["Pagolin M3X",  0.0004998, 0.0033722, 0,       0,        4.56,  2000, 1000],
["Miner5", 0, 0, 0, 0, 0, 0, 0],
["Miner6", 0, 0, 0, 0, 0, 0, 0],
["Miner7", 0, 0, 0, 0, 0, 0, 0],
[0,0,0,0,0,0,0,0]]
'''

def minecoins():
    # BTC, BCH, LTC, ETH
    global miners, minerlist
    testlist = minerlist
    mined = [0, 0, 0, 0]
    if len(minedlist) > 0:
        seconds = (datetime.datetime.now()-datetime.datetime.strptime(str(minedlist[len(minedlist)-1][0]), '%Y-%m-%d %X.%f')).total_seconds()
    if len(minedlist) == 0 or seconds > 5:
        for i in range(len(testlist)):
            b = testlist[i]
            for j in range(4):
                if len(minedlist) == 0:
                    seconds = 0
                a = miners[i][j+1]
                mined[j] += (a * b / (60*60)) * seconds
        minedlist.append([str(datetime.datetime.now()), mined])

def getwatttotals():
    global miners, minerlist
    watts = 0
    for i in range(len(minerlist)):
        watts += miners[i][6] * minerlist[i]
    return watts

def getfiattotal():
    global transactionlist
    global startingfiat
    loadfromfile()
    fiat = startingfiat
    for element in transactionlist:
        fiat += element[1]*element[3]*element[4]
    return fiat

def getworth():
	worth = getfiattotal()
	coinlist = getcointotals()
	for coin in coinlist[0]:
		worth += coinlist[1][coinlist[0].index(coin)] * coins.getCoinVal(coin)
	return worth

def addfiat(amount):
        global transactionlist
        transactionlist.append([str(datetime.datetime.now()),1,'USD',amount,1.0])
        savetofile()
        return 0

def removefiat(amount):
        addfiat(amount*-1)
        return 0

def getcointotals():
    global transactionlist
    coins = [[],[]]
    for element in transactionlist:
        if element[2] not in coins[0]:
            coins[0].append(element[2])
            coins[1].append(element[3])
        else:
            i = coins[0].index(element[2])
            coins[1][i] += -element[1]*element[3]
    #minecoins()
    return coins

def getminertotals():
    return minerlist

def numberofcoin(coin):
	coins = getcointotals()
	if coin not in coins[0]:
		return 0
	else:
		i = coins[0].index(coin)
		return coins[1][i]

def savetofile():
    global transactionlist, minerlist, minedlist, eleclist
    file = open('transactions.txt', 'w')
    json.dump(transactionlist, file)
    file.close
    file = open('miners.txt', 'w')
    json.dump(minerlist, file)
    file.close
    file = open('minedcoins.txt', 'w')
    json.dump(minedlist, file)
    file.close
    file = open('electricity.txt', 'w')
    json.dump(eleclist, file)
    file.close

def loadfromfile():
    global transactionlist, minerlist, minedlist, eleclist
    #add in an existence check
    file = open('transactions.txt','r')
    transactionlist = json.load(file)
    file.close
    file = open('miners.txt','r')
    minerlist = json.load(file)
    file.close
    file = open('minedcoins.txt','r')
    minedlist = json.load(file)
    file.close
    file = open('electricity.txt','r')
    eleclist = json.load(file)
    file.close

def transactiongraph():
	cointypes = []
	dates = []
	history = []
	account = []
	j = 0
	for element in transactionlist:
		cointypes.append(element[2])
		dates.append(element[0][:10])
		history.append(element[1]*element[3]*element[4])
		if (j == 0): 
			account.append(1000+(element[1]*element[3]*element[4]))
		else:
			account.append(account[j-1]+(element[1]*element[3]*element[4]))
		j += 1
	
	
	x = [i for i in range(0,len(history))]
	fig, splot = plt.subplots(1,1)
	splot.set_xticks(x)
	splot.set_xticklabels(dates, rotation='vertical', fontsize=8)
	plt.plot(history)
	plt.plot(history,'b.')
	plt.plot(account,'k-')
	plt.ylabel('Price ($)')
	plt.xlabel('Date')

	red_b = mpatches.Patch(color='red', label='Bought')
	green_b = mpatches.Patch(color='green', label='Sold')
	k_b = mpatches.Patch(color='black', label='Account Value')
	plt.legend(handles=[red_b,green_b,k_b])

	for ctype, x, y, in zip(cointypes, x, history):
		if (y >= 0):
			plt.annotate(ctype, xy=(x, y), xytext=(3, 14), textcoords='offset points', ha='left', va='bottom',bbox=dict(boxstyle='round,pad=0.3', fc='green', alpha=0.5),arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
		else:
			plt.annotate(ctype, xy=(x, y), xytext=(3, -27), textcoords='offset points', ha='left', va='bottom',bbox=dict(boxstyle='round,pad=0.3', fc='red', alpha=0.5),arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
		
	
	plt.show()
















