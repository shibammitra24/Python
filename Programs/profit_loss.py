cp = int(input("enter the cost price: "))
sp = int(input("enter the selling price: "))
if sp>cp:
    print("seller made a profit")
    totalProfit = sp-cp
    print("profit made:",totalProfit)
elif sp==cp:
    print("seller made no profit or loss")
else:
    print("seller made a loss")
    totalLoss = cp-sp
    print("loss amount:",totalLoss)