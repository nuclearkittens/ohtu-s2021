KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError(
                "Kapasiteetin on oltava positiivinen kokonaisluku")
        else:
            self.kapasiteetti = kapasiteetti

        self.kasvatuskoko = kasvatuskoko
        self._lukujono = [float('inf') for _ in range(self.kapasiteetti)]

    def kuuluu_joukkoon(self, n):
        return True if n in self._lukujono else False

    def _alkioiden_lkm(self):
        try:
            lkm = self._lukujono.index(float('inf'))
        except ValueError:
            lkm = len(self._lukujono)
        return lkm

    def lisaa_alkio(self, n):
        lkm = self._alkioiden_lkm()

        if not lkm:
            self._lukujono[0] = n
            return True
        elif not self.kuuluu_joukkoon(n):
            if len(self._lukujono) == lkm:
                self._kasvata_taulukkoa()
            self._lukujono[lkm] = n
            return True

        return False

    def poista_alkio(self, n):
        if self.kuuluu_joukkoon(n):
            self._lukujono.remove(n)
            self._lukujono.append(float('inf'))
            return True

        return False

    def _kasvata_taulukkoa(self):
        for i in range(self.kasvatuskoko):
            self._lukujono.append(float('inf'))

    def mahtavuus(self):
        return self._alkioiden_lkm()

    def lukujono(self):
        return [x for x in self._lukujono if x != float('inf')]

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.lukujono()
        b_taulu = b.lukujono()

        temp = list(set(a_taulu + b_taulu))

        for alkio in temp:
            yhdiste.lisaa_alkio(alkio)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.lukujono()
        b_taulu = b.lukujono()

        yhdiste = IntJoukko.yhdiste(a, b).lukujono()

        for alkio in yhdiste:
            if alkio in a_taulu and alkio in b_taulu:
                leikkaus.lisaa_alkio(alkio)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko.yhdiste(a, b)
        b_taulu = b.lukujono()

        for alkio in b_taulu:
            erotus.poista_alkio(alkio)

        return erotus

    def __str__(self):
        jono = self.lukujono()
        s = ', '.join((str(x) for x in jono))
        return f"{{{s}}}"
