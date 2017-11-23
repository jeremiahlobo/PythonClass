from IceCreamPail import IceCreamPail

IceCreamOnShelf = [] #list

for i in range(0,50):
    tempIceCream = IceCreamPail(.5, "Jordans Pale", ("Vanilla",i), 2.5 , 12.0, 1.0, False)
    IceCreamOnShelf.append(tempIceCream)

    
print(IceCreamOnShelf[5].getFlavour())
print(IceCreamOnShelf[5].getPercentCream())
