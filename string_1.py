def WordAmount(myStr):
    numSpace = myStr.split(" ")
    print(len(numSpace))
    return WordAmount

def ExtraSpaces(myStr):
    return myStr.find("  ")
 

def FullAmount(WordAmount, ExtraSpaces):
    WordAmount - ExtraSpaces
    print(WordAmount - ExtraSpaces)
    return FullAmount

def main():
    myStr= "This is fun, really really fun.  I'm old."
    WA = WordAmount(myStr)
    print (WA)
    DS = ExtraSpaces(myStr)
    print (DS)
main()