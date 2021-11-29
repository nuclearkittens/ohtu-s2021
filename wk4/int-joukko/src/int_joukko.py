KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Kapasiteetin on oltava positiivinen kokonaisluku")
        else:
            self.kapasiteetti = kapasiteetti

        self.kasvatuskoko = kasvatuskoko
        self.lukujono = [float('inf') for _ in range(self.kapasiteetti)]

    def kuuluu_joukkoon(self, n):
        return True if n in self.lukujono else False

    def _alkioiden_lkm(self):
        try:
            lkm = self.lukujono.index(float('inf'))
        except ValueError:
            lkm = len(self.lukujono)
        return lkm

    def lisaa_joukkoon(self, n):
        lkm = self._alkioiden_lkm()

        if not lkm:
            self.lukujono[0] = n
            return True
        elif not self.kuuluu_joukkoon(n):
            if len(self.lukujono) == lkm:
                self.kasvata_taulukkoa()
            self.lukujono[lkm] = n
            return True

        return False

    def poista(self, n):
        if self.kuuluu_joukkoon(n):
            self.lukujono.remove(n)
            self.lukujono.append(float('inf'))
            return True
        
        return False

    def kasvata_taulukkoa(self):
        for i in range(self.kasvatuskoko):
            self.lukujono.append(float('inf'))

    def mahtavuus(self):
        return self._alkioiden_lkm()

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa_joukkoon(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa_joukkoon(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa_joukkoon(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa_joukkoon(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
