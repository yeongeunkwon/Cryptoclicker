import requests, os

class Coin():
	''' This class creates a class for each crypto which allows it to search the CoinCap API in order to get coin data to use.'''
	def __init__(self, string):
		self.coin_code = string
		self.crypt_info = requests.get('http://coincap.io/page/%s' % self.coin_code)
		self.__coin_data = {}
		self.__coin_data['name'] = self.crypt_info.json()['display_name']
		self.__coin_data['id'] = self.crypt_info.json()['id']
		self.__coin_data['USD'] = self.crypt_info.json()['price_usd']
		self.__coin_data['pChange'] = self.crypt_info.json()['cap24hrChange']
	
	def refreshData(self):
		'''Refreshes the crypto price in USD and its daily percent change and returns updated dictionary.'''
		self.crypt_info = requests.get('http://coincap.io/page/%s' % self.coin_code)
		self.__coin_data['USD'] = self.crypt_info.json()['price_usd']
		self.__coin_data['pChange'] = self.crypt_info.json()['cap24hrChange']

	def getInfo(self):
		'''Returns all characteristics of the Coin class. It is saved as a dictionary.'''
		return self.__coin_data

	def getCoinVal(string):
		'''Returns coinvalue'''
		coin_info = requests.get('http://coincap.io/page/%s' % string)
		return coin_info.json()['price_usd']

	def printData(self):
		'''Prints the crypto data.'''
		print('%s (%s)' % (self.__coin_data['name'], self.__coin_data['id']))
		print('USD$%.5f (%.2f%%)' % (self.__coin_data['USD'], self.__coin_data['pChange']))
		print('------------------------------------------------------')

def ticker():
	btc = Coin('BTC')
	eth = Coin('ETH')
	ltc = Coin('LTC')
	bch = Coin('BCH')
	xrp = Coin('XRP')
	
	try:
		while True:

			btc.refreshData()
			eth.refreshData()
			ltc.refreshData()
			bch.refreshData()
			xrp.refreshData()

			os.system('cls')

			btc.printData()
			eth.printData()
			ltc.printData()
			bch.printData()
			xrp.printData()
	except KeyboardInterrupt:
		return 0

def getCoinVal(string):
	'''Returns coinvalue'''
	coin_info = requests.get('http://coincap.io/page/%s' % string)
	return coin_info.json()['price_usd']