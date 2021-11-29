KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Kapasiteetin on oltava positiivinen kokonaisluku")
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
                self.kasvata_taulukkoa()
            self._lukujono[lkm] = n
            return True

        return False

    def poista_alkio(self, n):
        if self.kuuluu_joukkoon(n):
            self._lukujono.remove(n)
            self._lukujono.append(float('inf'))
            return True
        
        return False

    def kasvata_taulukkoa(self):
        for i in range(self.kasvatuskoko):
            self._lukujono.append(float('inf'))

    def mahtavuus(self):
        return self._alkioiden_lkm()

    def lukujono(self):
        return [x for x in self._lukujono if x != float('inf')]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.lukujono()
        b_taulu = b.lukujono()

        for i in range(0, len(a_taulu)):
            x.lisaa_alkio(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa_alkio(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.lukujono()
        b_taulu = b.lukujono()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa_alkio(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.lukujono()
        b_taulu = b.lukujono()

        for i in range(0, len(a_taulu)):
            z.lisaa_alkio(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista_alkio(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self._lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self._lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self._lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
