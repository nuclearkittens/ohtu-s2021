from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._hinta = 0
        self._ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return sum([ostos.lukumaara() for ostos in self._ostokset])
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        self._hinta = sum([ostos.hinta() for ostos in self._ostokset])
        return self._hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos = Ostos(lisattava)
        if ostos in self._ostokset:
            ostos.muuta_lukumaaraa(1)
        else:
            self._ostokset.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
