import unittest
from database_connection import connect_to_database
from database_operations import Gemi, Sefer

class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        # Veritabanı bağlantısını oluştur
        self.conn, self.cursor = connect_to_database()

    def tearDown(self):
        # Veritabanı bağlantısını kapat
        if self.conn:
            self.conn.close()

    def test_gemi_ekle(self):
        # Gemi ekleme işlemi için test
        yeni_gemi = Gemi("123", "Gemi", 200, 2023, "Yolcu", 100, 0, 0, 600)
        yeni_gemi.ekle()
        # Eklenen gemiyi veritabanında sorgulayarak kontrol edebilirsiniz
    def test_gemi_sil(self):
        # Silinecek geminin seri numarası
        seri_numarasi = "123"
        # Gemi silme işlemini dene
        success = Gemi.sil_gemi_by_seri_numarasi(seri_numarasi)
        # Silme işleminin başarılı olup olmadığını kontrol et

    def test_gemi_duzenle(self):
        # Düzenlenecek geminin seri numarası
        seri_numarasi = "123"
        # Yeni veriler
        yeni_veriler = ("Yeni Ad", 1500, 2025, "Yeni Tip", 120, 600.0, 250, 2500.0)
        # Gemi düzenleme işlemini dene
        success = Gemi.duzenle_by_seri_numarasi(seri_numarasi, yeni_veriler)
        # Düzenleme işleminin başarılı olup olmadığını kontrol et


if __name__ == '__main__':
    unittest.main()
