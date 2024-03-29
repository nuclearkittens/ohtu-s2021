from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return sum([ostos.lukumaara() for ostos in self._ostokset.values()])
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return sum([ostos.hinta() for ostos in self._ostokset.values()])
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        nimi = lisattava.nimi()
        if nimi in self._ostokset:
            self._ostokset[nimi].muuta_lukumaaraa(1)
        else:
            self._ostokset[nimi] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        nimi = poistettava.nimi()
        if nimi in self._ostokset:
            if self._ostokset[nimi].lukumaara() == 1:
                self._ostokset.pop(nimi)
            else:
                self._ostokset[nimi].muuta_lukumaaraa(-1)

    def tyhjenna(self):
        self._ostokset = {}
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self._ostokset.values())
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
