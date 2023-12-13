def jelsor(jel,meret):
    print(jel*meret)

def szoveg(jel2,szoveg,meret):
    hossz: int= meret- (len(jel2) + len(jel2))
    print(f"{jel2}{szoveg:^{hossz}}{jel2}")

def fooldal(szoveg,lista,lapmeret):
    jelsor("-",lapmeret)
    szoveg("*","asd",lapmeret)
    jelsor("-",lapmeret)
    for i in range(0,len(lista),1):
        szoveg("*","asd",lista[i])
    jelsor("-",lapmeret)

