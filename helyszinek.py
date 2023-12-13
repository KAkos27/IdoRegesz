import lap
itemek = []
penz = 1
eletero = 9
eletero_vedelem = 3


def elso():
   kezdes(itemek,eletero)

def kezdes(targyak,eletero):
    szoveg = "Egy óriási mezőn vagy. Nyugat felé egy hatalmas épület körvonalai tűnnek fel."
    lapmeret=len(szoveg)+2
    eletero-=1
    lap.fooldal(szoveg,lapmeret,targyak,"-","*",eletero)
    elsoleiras:str=input(">")
    elsoleiras_kicsi=elsoleiras.lower()

    if elsoleiras_kicsi == "megy epulet" or elsoleiras_kicsi =="megy épület":
        mezo(itemek,eletero)
    
def mezo(targyak,eletero):
    szoveg = "Napfényes mezőn állsz. Nyugatra egy hatalmas kastélyt, délre egy kutat látsz."
    lapmeret=len(szoveg)+2
    eletero-=1
    lap.fooldal(szoveg,lapmeret,targyak,"-","*",eletero)
    masodik_leiras:str=input("> ")
    masodik_leiras_kicsi=masodik_leiras.lower()

    if masodik_leiras_kicsi == "megy kut" or masodik_leiras_kicsi == "megy kút":
        kut(penz,itemek,eletero) 
    elif masodik_leiras_kicsi== "megy epulet" or masodik_leiras_kicsi =="megy épület":
        kastely(itemek,eletero)
    elif masodik_leiras_kicsi == "megy var" or masodik_leiras_kicsi == "megy vár":
        kastely(itemek)
    elif masodik_leiras_kicsi == "megy kastely" or masodik_leiras_kicsi == "megy kastély":
        kastely(itemek,eletero)
  
def kut(penz,targyak,eletero): 
    szoveg = "Napfényes mezőn állsz, egy kút előtt. Itt van: pénz. Nyugatra egy hatalmas kastélyt látsz."
    lapmeret=len(szoveg)+2
    eletero -= 1
    lap.fooldal(szoveg,lapmeret,targyak,"-","*",eletero)
    felvesz=input("> ")
    felvesz_kicsi=felvesz.lower()

    if felvesz_kicsi == "felvesz penz" or felvesz_kicsi == "felvesz pénz":
        penz-=1
        if penz == 0:
            print("Felvetted a pénzt\nMész tovább a kastélyba")
            itemek.append("Pénz")
            kastely(itemek,eletero)
        print("Már felvetted a pénzt\nMész tovább a kastályra")
    elif felvesz_kicsi == "megy epulet" or felvesz_kicsi ==  "megy épület":
        kastely(itemek,eletero) 
    elif felvesz_kicsi == "megy kastely" or felvesz_kicsi == "megy kastély":
        kastely(itemek,eletero)

        
def kastely(targyak,eletero):
    szoveg = "A várudvaron állsz. Nyugatra nyitott kamrát, északra zárt ajtót látsz. Egy széles lépcső vezet fel a vártemplomhoz"
    lapmeret=len(szoveg)+2
    eletero -=1
    lap.fooldal(szoveg,lapmeret,targyak,"-","*",eletero)
    leiras:str=input("> ")
    leiras_kicsi=leiras.lower()

    if leiras_kicsi == "megy vartemplom" or leiras_kicsi =="megy vártemplom":
        vartemplom(itemek,eletero)
    elif leiras_kicsi== "megy kamra":
        print()
    elif leiras_kicsi == "megy ajto" or leiras_kicsi =="megy ajtó":
        print()
    
def vartemplom(targyak,eletero):
    szoveg = "A templom előtt egy kéregető szerzetes mosolyog rád. Nyugatra nyitott kamrát, északra zárt ajtót látsz."
    lapmeret=len(szoveg)+2
    eletero -=1
    lap.fooldal(szoveg,lapmeret,targyak,"-","*",eletero)
    leiras:str=input("> ")
    leiras_kicsi=leiras.lower()
    
    if (leiras_kicsi == "ad penz" or leiras_kicsi == "ad pénz"):
        while penz == 1:
            print("Nincs nálad pénz")
            leiras:str=input("> ")
            leiras_kicsi=leiras.lower()
    print("asd")