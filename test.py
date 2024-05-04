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

    def test_sefer_ekle(self):
        # Sefer ekleme işlemi için test
        yeni_sefer = Sefer(1, "2020-05-02", "2022-05-10", 1, 1, 3, 1)  # Örnek veriler, gerçek verilere göre değiştirilmeli
        yeni_sefer.ekle()
        # Eklenen seferi veritabanında sorgulayarak kontrol edebilirsiniz

    # Diğer test metodlarını da aynı şekilde ekleyebilirsiniz

if __name__ == '__main__':
    unittest.main()
