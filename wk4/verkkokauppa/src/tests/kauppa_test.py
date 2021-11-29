import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 127
        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 16
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, 'kalja', 4)
            if tuote_id == 2:
                return Tuote(2, 'soijanakki', 7)
            if tuote_id == 3:
                return Tuote(3, 'tsufe', 6)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_tilisiirtoa_kutsutaan_ostoksen_jalkeen_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 127, '12345', ANY, 4)

    def test_kaksi_eri_tuotetta_tilisiirtoa_kutsutaan_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu('merz', '112358')

        self.pankki_mock.tilisiirto.assert_called_with('merz', 127, '112358', ANY, 11)

    def test_kaksi_samaa_tuotetta_tilisiirtoa_kutsutaan_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu('merz', '112358')

        self.pankki_mock.tilisiirto.assert_called_with('merz', 127, '112358', ANY, 8)

    def test_kaksi_tuotetta_toinen_loppu_tilisiirtoa_kutsutaan_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu('merz', '112358')

        self.pankki_mock.tilisiirto.assert_called_with('merz', 127, '112358', ANY, 4)

    def test_aloita_asiointi_nollaa_aiemmat_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu('merz', '112358')

        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 0)

    def test_uusi_viitenro_joka_ostokselle(self):
        self.viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu('merz', '112358')

        self.pankki_mock.tilisiirto.assert_called_with('merz', 1, '112358', ANY, 4)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu('merz', '112358')

        self.pankki_mock.tilisiirto.assert_called_with('merz', 2, '112358', ANY, 7)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu('merz', '112358')

        self.pankki_mock.tilisiirto.assert_called_with('merz', 3, '112358', ANY, 4)
