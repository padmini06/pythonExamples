#!/use/bin/python3

import random
import string

class Vehicle:
	def __init__(self, brand = " ", color = " "):
		self.__brand = brand
		self.__color = color
		
	def setColor(self, color):
		self.__color = color
		
	def setBrand(self, brand):
		self.__brand = brand
	
	def getColor(self):
		return (self.__color)
	
	def getBrand(self):
		return (self.__brand)
	
	def showDetials(self):
		print("Car brand is :", __brand," Color is :",__color)

class Car(Vehicle):
	def __init__(self, brand = " ", color = " ", price = 0):
		super().__init__(brand,color)
		self.__price = price
	
	def setPrice(self, price):
		self.__price = price
	
	def getPrice(self) :
		return(self.__price)
	
	def showDetials(self) :
		print("Car brand is :", self.getBrand()," Color is :", self.getColor()," and cost is : ", self.__price)
	
	def __str__(self):
		return  "Car Model  is :" +self.getBrand() + "Color is :" + self.getColor()+" and cost is : "+ str(self.__price)
		
objCar = Car("MARUTI","RED",800000)
objCar1 = Car()
objCar1.setPrice(800)
objCar.showDetials();
print(objCar1)


	