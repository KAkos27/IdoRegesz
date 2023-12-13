def jelsor(jel,meret):
    for i in range(0,meret,1):
        print(jel, end="")

def szovegsor(jel2,szoveg,meret):
    hossz: int= int(meret) - (len(jel2) + len(jel2))
    print(f"{jel2}{szoveg:^{hossz}}{jel2}")

def listasor(jel2,lista,meret):
    hossz: int= int(meret) - (len(jel2) + len(jel2))
    for i in range(0,len(lista),1):
        print(f"{jel2}{(lista[i]):^{hossz}}{jel2}")

def fooldal(szoveg,lapmeret,lista,jel,jel2):
    jelsor(jel,lapmeret)
    print()
    szovegsor(jel2,szoveg,lapmeret)
    print()
    jelsor(jel,lapmeret)
    print()
    listasor(jel2,lista,lapmeret)
    jelsor(jel,lapmeret)
    print()

