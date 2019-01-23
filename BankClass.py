#!/usr/bin/python3

class Bank:
	#consturctor or initializer
	def __init__(self,name,amount=1000):
		self.__name = name
		self.__amount = amount
	
	def checkBalance(self):
		if int(self.__amount) < 1000 :
			print(self.__name," you have low balance in your account, pls add Rs.", 1000-self.__amount)
		else:
			print(self.__name, "You have sufficient balance in your account" )
			
	def showData(self):
		print("Name is %s :",self.__name)
		print("Balance is %d :",self.__amount)
		
		
		

b1 = Bank("padmini",500)
b2 = Bank("Ashish", 7000)
b1.showData()
b2.showData()

b1.checkBalance()
b2.checkBalance()
