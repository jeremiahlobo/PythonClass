from IceCreamPail import IceCreamPail

IceCreamOnShelf = [] #list

for i in range(0,50):
    tempIceCream = IceCreamPail(.5, "Jordans Pale", ("Vanilla",i), 2.5 , 12.0, 1.0, False)
    IceCreamOnShelf.append(tempIceCream)

    
print(IceCreamOnShelf[5].getFlavour())
print(IceCreamOnShelf[5].getPercentCream())

IceCreamOnShelf[5].setPercentCream(.25) #print

for icecream in IceCreamOnShelf:
	print(icecream.getPercentCream())


IceCreamOnShelf[15].price

IceCreamOnShelf[15].getPriceWithGST

