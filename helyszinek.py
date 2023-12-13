import lap
itemek = ["kulcs","pénz"]
penz = 0

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
      kut(targyak) 
    elif masodik_leiras_kicsi== "megy epulet" or "megy épület":
      kastely()
    elif masodik_leiras_kicsi == "megy var" or "megy vár":
        kastely()
  
def kut(penz, targyak): 
    szoveg = "Napfényes mezőn állsz, egy kút előtt. Itt van: pénz. Nyugatra egy hatalmas kastélyt látsz."
    lapmeret=len(szoveg)+2
    lap.fooldal(szoveg,lapmeret,targyak,"-","*")
    felvesz=input("> ")
    felvesz_kicsi=felvesz.lower()
    if felvesz_kicsi == "felvesz penz" or "felvesz pénz":
        penz-=1
        if penz == 0:
            penz_felvetele()
        print("Már felvetted a pénzt")
    if felvesz_kicsi == "megy epulet" or "megy épület":
      kastely() 
    elif felvesz_kicsi == "megy kastely" or "megy kastély":
      kastely()

def penz_felvetele():
     print("Rendben, a pénzt elraktad")
     kut()
    
        
def kastely(targyak):
    szoveg = "A várudvaron állsz. Nyugatra nyitott kamrát, északra zárt ajtót látsz. Egy széles lépcső vezet fel a vártemplomhoz"
    lapmeret=len(szoveg)+2
    lap.fooldal(szoveg,lapmeret,targyak,"-","*")
    leiras:str=input("> ")
    leiras_kicsi=leiras.lower()
    if leiras_kicsi == "megy vartemplom" or "megy vártemplom":
      print()
    elif leiras_kicsi== "megy kamra":
     print()
    elif leiras_kicsi == "megy ajto" or "megy ajtó":
        print()
    
      