def stock_list(listOfArt, listOfCat):
    dictA = dict()
    for i in listOfArt:
        listSplit = i.split(" ")
        dictA[listSplit[0]] = int(listSplit[1])
    for l in listOfCat:
        sum = 0
        for k,v in dictA.items():
            if k[0] == l:





b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c))  #(A : 200) - (B : 1140)
