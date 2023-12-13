def kezdes():
    elsoleiras:str=input("")
    elsoleiras_kicsi=elsoleiras.lower()
    if elsoleiras_kicsi == "megy epulet" or "megy épület":
        mezo()
    
def mezo():
  masodik_leiras:str=input("> ")
  masodik_leiras_kicsi=masodik_leiras.lower()
  if masodik_leiras_kicsi == "megy kut" or "megy kút":
      kut() 
  elif masodik_leiras_kicsi== "megy epulet" or "megy épület":
      kastely()
  elif masodik_leiras_kicsi == "megy var" or "megy vár":
        kastely()
  
def kut(): 
    
      