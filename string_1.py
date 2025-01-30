def WordAmount(myStr):
    numSpace = myStr.split(" ")
    print(len(numSpace))
    return WordAmount

def main():
    myStr= "This is fun, really really fun.  I'm old."
    WA = WordAmount(myStr)
    print (WA)
    RS = myStr.replace("  ", " ")
    print (RS)
    TotalAmount = RS.split(" ")
    print(len(TotalAmount))



main()