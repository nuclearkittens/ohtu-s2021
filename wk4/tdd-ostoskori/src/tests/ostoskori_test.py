import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuotteet = [Tuote('vuustonaxut', 2)]

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_korissa_yksi_tuote_maara_oikein(self):
        self.kori.lisaa_tuote(self.tuotteet[0])
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
