class Oscilloscope:
    year = 2000

    def __init__(self, maxfrequency=0, storagecapacity=0, brand="unknown", country="unknown", price=0, channel=0):
        self.maxfrequency = maxfrequency
        self.storagecapacity = storagecapacity
        self.brand = brand
        self.country = country
        self.price = price
        self.channel = channel

    def __del__(self):
        pass

    @staticmethod
    def getyear():
        return Oscilloscope.year

    def getmaxfrequency(self):
        return self.maxfrequency

    def setmaxfrequency(self, maxfrequency):
        self.maxfrequency = maxfrequency

    def getstoragecapacity(self):
        return self.storagecapacity

    def setstoragecapacity(self, storagecapacity):
        self.storagecapacity = storagecapacity

    def getbrand(self):
        return self.brand

    def setbrand(self, brand):
        self.brand = brand

    def getcountry(self):
        return self.country

    def setcountry(self, country):
        self.country = country

    def getprice(self):
        return self.price

    def setprice(self, price):
        self.price = price

    def getchannel(self):
        return self.channel

    def setchannel(self, channel):
        self.channel = channel

    def __str__(self):
        return "Oscilloscope [maximum frequency bandwidth = {}MHz, storage capacity = {}kb, brand = {}, country = {}, price = {}, channel = {}]".format(self.maxfrequency, self.storagecapacity, self.brand, self.country, self.price, self.channel)
