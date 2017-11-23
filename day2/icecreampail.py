class IceCreamPail:
    'this class provides a template for an icecream pail as per'

#global variable is accessible everywhere


IceCreamStock = 0

#constructor

def __init__(self, percerntCream, brand, flavour, cost, price, volumeLitre, isGMO):
    self.percerntCream = percerntCream
    self.brand = brand
    self.flavour = flavour
    self.cost = cost
    self.price = price
    self.volumeLitre = volumeLitre
    self.isGMO = isGMO

    IceCreamPail.IceCreamStock +=1


def getPriceWithGST(self, gst):
    tempPrice = self.price
    tempGST = 1+gst
    tempPrice *= 100
    return (tempPrice * tempGST)/100
    

######GETTERS SETTERS ##############
def setPercentCream(self, newPercent):
    self.percentCream = newPercent

def getPercentCream(self):
    return self.percentCream

    
