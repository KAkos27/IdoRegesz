
import lap

def kezdes(targyak):
    szoveg = "Egy óriási mezőn vagy. Nyugat felé egy hatalmas épület körvonalai tűnnek fel."
    lapmeret=len(szoveg)+2
    lap.fooldal(szoveg,lapmeret,targyak,"-","*")
    elsoleiras:str=input(">")
    elsoleiras_kicsi=elsoleiras.lower()
    if elsoleiras_kicsi == "megy epulet" or "megy épület":
        mezo(targyak)
    
def mezo(targyak):
    szoveg = "Napfényes mezőn állsz. Nyugatra egy hatalmas kastélyt, délre egy kutat látsz."
    lapmeret=len(szoveg)+2
    lap.fooldal(szoveg,lapmeret,targyak,"-","*")
    masodik_leiras:str=input("> ")
    masodik_leiras_kicsi=masodik_leiras.lower()
    if masodik_leiras_kicsi == "megy kut" or "megy kút":
      kut() 
    elif masodik_leiras_kicsi== "megy epulet" or "megy épület":
      kastely()
    elif masodik_leiras_kicsi == "megy var" or "megy vár":
        kastely()
  
def kut(): 
    print("Napfényes mezőn állsz, egy kút előtt. Itt van: pénz. Nyugatra egy hatalmas kastélyt látsz.")
    felvesz=input("> ")
    felvesz_kicsi=felvesz.lower()
    harmadik_leiras:str=input("> ")
    harmadik_leiras_kicsi=harmadik_leiras.lower()
    if felvesz_kicsi == "felvesz penz" or "felvesz pénz":
        penz_felvetele()
    if harmadik_leiras_kicsi == "megy epulet" or "megy épület":
      kastely() 
    elif harmadik_leiras_kicsi== "megy kastely" or "megy kastély":
      kastely()

def penz_felvetele():
     print("Rendben, a pénzt elraktad")
     negyedik_leiras:str=input("> ")
     negyedik_leiras_kicsi:str=negyedik_leiras.lower()
     if negyedik_leiras_kicsi == "megy epulet" or "megy épület" or "megy kastely" or "megy kastély":
        kastely()
        
def kastely():
    print("A várudvaron állsz. Nyugatra nyitott kamrát, északra zárt ajtót látsz. Egy széles lépcső vezet fel a vártemplomhoz")
    otodik_leiras:str=input("> ")
    otodik_leiras_kicsi=otodik_leiras.lower()
    if otodik_leiras_kicsi == "megy vartemplom" or "megy vártemplom":
      print()
    elif otodik_leiras_kicsi== "megy kamra":
     print()
    elif otodik_leiras_kicsi == "megy ajto" or "megy ajtó":
        print()
    
      