import lap
itemek = []
penz = 1

def elso():
   kezdes(itemek)

def kezdes(targyak):
    szoveg = "Egy óriási mezőn vagy. Nyugat felé egy hatalmas épület körvonalai tűnnek fel."
    lapmeret=len(szoveg)+2
    lap.fooldal(szoveg,lapmeret,targyak,"-","*")
    elsoleiras:str=input(">")
    elsoleiras_kicsi=elsoleiras.lower()
    if elsoleiras_kicsi == "megy epulet" or "megy épület":
        mezo(itemek)
    
def mezo(targyak):
    szoveg = "Napfényes mezőn állsz. Nyugatra egy hatalmas kastélyt, délre egy kutat látsz."
    lapmeret=len(szoveg)+2
    lap.fooldal(szoveg,lapmeret,targyak,"-","*")
    masodik_leiras:str=input("> ")
    masodik_leiras_kicsi=masodik_leiras.lower()
    if masodik_leiras_kicsi == "megy kut" or "megy kút":
      kut(penz,itemek) 
    elif masodik_leiras_kicsi== "megy epulet" or "megy épület":
      kastely()
    elif masodik_leiras_kicsi == "megy var" or "megy vár":
        kastely()
  
def kut(penz,targyak): 
    szoveg = "Napfényes mezőn állsz, egy kút előtt. Itt van: pénz. Nyugatra egy hatalmas kastélyt látsz."
    lapmeret=len(szoveg)+2
    lap.fooldal(szoveg,lapmeret,targyak,"-","*")
    felvesz=input("> ")
    felvesz_kicsi=felvesz.lower()
    if felvesz_kicsi == "felvesz penz" or "felvesz pénz":
        penz-=1
        if penz == 0:
            print("Felvetted a pénzt\nMész tovább a kastélyba")
            itemek.append("Pénz")
            kastely(itemek)
        print("Már felvetted a pénzt\nMész tovább a kastályra")
    elif felvesz_kicsi == "megy epulet" or "megy épület":
      kastely(itemek) 
    elif felvesz_kicsi == "megy kastely" or "megy kastély":
      kastely(itemek)

        
def kastely(targyak):
    szoveg = "A várudvaron állsz. Nyugatra nyitott kamrát, északra zárt ajtót látsz. Egy széles lépcső vezet fel a vártemplomhoz"
    lapmeret=len(szoveg)+2
    lap.fooldal(szoveg,lapmeret,targyak,"-","*")
    leiras:str=input("> ")
    leiras_kicsi=leiras.lower()
    if leiras_kicsi == "megy vartemplom" or "megy vártemplom":
      vartemplom(itemek)
    elif leiras_kicsi== "megy kamra":
     print()
    elif leiras_kicsi == "megy ajto" or "megy ajtó":
        print()
    
def vartemplom(targyak):
    szoveg = "A templom előtt egy kéregető szerzetes mosolyog rád. Nyugatra nyitott kamrát, északra zárt ajtót látsz."
    lapmeret=len(szoveg)+2
    lap.fooldal(szoveg,lapmeret,targyak,"-","*")
    leiras:str=input("> ")
    leiras_kicsi=leiras.lower()

    if (leiras_kicsi == "ad penz" or leiras_kicsi == "ad pénz"):
        while penz == 1:
            print("Nincs nálad pénz")
            leiras:str=input("> ")
            leiras_kicsi=leiras.lower()
    print("asd")