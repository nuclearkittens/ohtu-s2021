import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuotteet = [Tuote('vuustonaxut', 2), Tuote('glögitiiviste', 4)]

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_korissa_yksi_tuote_maara_oikein(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_korissa_yksi_tuote_hinta_oikein(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.assertEqual(self.kori.hinta(), 2)

    def test_korissa_kaksi_tavaraa_kahden_tuotteen_lisaamisen_jalkeen(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.lisaa_tuote(self.tuotteet[1])
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_korissa_kaksi_tavaraa_hinta_oikein(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.lisaa_tuote(self.tuotteet[1])
        self.assertEqual(self.kori.hinta(), 6)

    def test_korissa_kaksi_samaa_tuotetta_maara_oikein(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_korissa_kaksi_samaa_hinta_oikein(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.assertEqual(self.kori.hinta(), 4)

    def test_yhden_tuotteen_lisaamisen_jalkeen_yksi_ostosolio_korissa(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yksi_tuote_korissa_oikea_nimi_ja_lkm(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), 'vuustonaxut')
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kaksi_tuotetta_lisätty_korissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.lisaa_tuote(self.tuotteet[1])
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kaksi_samaa_tuotetta_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kaksi_samaa_tuotetta_korissa_nimi_ja_lkm_oikein(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.lisaa_tuote(self.tuotteet[0])
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), 'vuustonaxut')
        self.assertEqual(ostos.lukumaara(), 2)

    def test_kaksi_samaa_tuotetta_poistetaan_toinen_jaljella_yksi(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.poista_tuote(self.tuotteet[0])
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 1)

    def test_korissa_yksi_tuote_poiston_jalkeen_tyhja(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.kori.poista_tuote(self.tuotteet[0])
        self.assertEqual(len(self.kori.ostokset()), 0)
        self.assertEqual(self.kori.hinta(), 0)
