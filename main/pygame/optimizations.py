
def draw(self, surface): 
    spritedict = self.spritedict
    surface_blit = surface.blit
    dirty = self.lostsprites
    self.lostsprites = []
    dirty_append = dirty.append

    for s in self.sprites(): 
        r = spritedict[s]                           #henter ut gamle rektangel
        newrect = surface_blit(s.image, s.rect)
        if r == 0:                                  #første gang vil mengden være tom, så legger bare inn rektangel fra blitten. 
            dirty_append(newrect)                       #legger til blitten 
        else:                                       #hvis mengden ikke er tom? 
            if newrect.colliderect(r):                  #hvis de to rektanglene (gammel og ny rektangel) overlapper
                dirty_append(newrect.union(r))              #lag et rektangel av de overlappende delene til rektanglene, union, og legg det til i mengden 
            else:                                       #hvis de ikke overlapper? 
                dirty_append(newrect)                       #legg til nytt rektangel  
                dirty_append(r)                             #legg til gammelt rektangel
        spritedict[s] = newrect                     #erstatter gamle rektangel med nytt rektangel 
    return dirty                               #returnerer listen av rektangler

## koden sammenligner områder dekket av rektangler for å sjekke om noe nytt har skjedd på skjermen i dette området 
# dette gjør vi for å se hvilke deler av skjermen vi trenger å oppdatere, feks vi trenger ikke alltid å oppdatere 
# hele bakgrunnen hvis ingenting har skjedd der
# hvis vi har to rektangler som dekker et område på skjermen hvor noe har skjedd, så kan de enten overlappe helt, delvis eller ingenting. 
# 1. overlapper de helt blir det bare enkelt å oppdatere det området direkte 
# 2. overlapper deler av rektanglene har vi områder som vil oppdateres to ganger (det overlappende området), som tar mer prosesseringskraft
#   for å minimere dette lager vi en union av de to rektanglene, og legger til unionen av disse til en mengde av områder som skal oppdateres 
# 3. dersom de ikke overlapper, legger vi til begge i denne mengden av områder som skal oppdateres
# etter dette erstattes den gamle av de to rektanglene med en ny, og prosessen starter på nytt 
#   
# ulemper med denne metoden?; flere ting som beveger seg som kanskje overlapper vil ha områder som
# oppdaterer seg flere ganger enn en (uønsket)
# annen ulempe er at metoden må slette og tegne alle sprites (tegningene)
# https://dr0id.bitbucket.io/legacy/pygame_tutorial01.html guide for ulike optimizing methods
