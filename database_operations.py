from database_connection import connect_to_database

class DatabaseManager:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn, self.cursor = connect_to_database()

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query, parameters=None):
        try:
            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)

            # Ekleme işleminden sonra son eklenen satırın ID'sini almak için sorgulama yapılıyor
            self.cursor.execute("SELECT @@IDENTITY AS id")
            row = self.cursor.fetchone()
            last_id = row.id

            self.conn.commit()
            return last_id  # Son eklenen satırın ID'sini döndür
        except Exception as e:
            print("Veritabanı hatası:", e)
            return None

    def ekle(self, seri_numarasi, gemi_adi, agirlik, yapim_yili, tip, yolcu_kapasitesi, petrol_kapasitesi,
             konteyner_sayisi, maksimum_agirlik):
        try:
            query = "INSERT INTO Gemiler (SeriNumarası, Adı, Ağırlık, YapımYılı, Tip, YolcuKapasitesi, PetrolKapasitesi, KonteynerSayısı, MaksimumAğırlık) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            parameters = (
                seri_numarasi, gemi_adi, agirlik, yapim_yili, tip, yolcu_kapasitesi, petrol_kapasitesi,
                konteyner_sayisi,
                maksimum_agirlik)
            success = self.execute_query(query, parameters)
            if success:
                print("Yeni gemi başarıyla eklendi.")
                return True
            else:
                print("Gemi eklenirken bir hata oluştu.")
                return False
        except Exception as e:
            print("Gemi eklenirken bir hata oluştu:", e)
            return False

class Gemi:
    def __init__(self, seri_numarasi, gemi_adi, agirlik, yapim_yili, tip, yolcu_kapasitesi, petrol_kapasitesi, konteyner_sayisi, maksimum_agirlik):
        self.seri_numarasi = seri_numarasi
        self.gemi_adi = gemi_adi
        self.agirlik = agirlik
        self.yapim_yili = yapim_yili
        self.tip = tip
        self.yolcu_kapasitesi = yolcu_kapasitesi
        self.petrol_kapasitesi = petrol_kapasitesi
        self.konteyner_sayisi = konteyner_sayisi
        self.maksimum_agirlik = maksimum_agirlik

    def ekle(self):
        db_manager = DatabaseManager()
        db_manager.connect()
        query = "INSERT INTO Gemiler (SeriNumarası, Adı, Ağırlık, YapımYılı, Tip, YolcuKapasitesi, PetrolKapasitesi, KonteynerSayısı, MaksimumAğırlık) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        parameters = (self.seri_numarasi, self.gemi_adi, self.agirlik, self.yapim_yili, self.tip, self.yolcu_kapasitesi, self.petrol_kapasitesi, self.konteyner_sayisi, self.maksimum_agirlik)
        success = db_manager.execute_query(query, parameters)
        db_manager.disconnect()
        if success:
            print("Yeni gemi başarıyla eklendi.")
        else:
            print("Gemi eklenirken bir hata oluştu.")

    @staticmethod
    def sil_gemi_by_seri_numarasi(seri_numarasi):
        db_manager = DatabaseManager()
        db_manager.connect()
        query = "DELETE FROM Gemiler WHERE SeriNumarası = ?"
        parameters = (seri_numarasi,)
        success = db_manager.execute_query(query, parameters)
        db_manager.disconnect()
        return success

    @staticmethod
    def duzenle_by_seri_numarasi(seri_numarasi, yeni_veriler):
        db_manager = DatabaseManager()
        db_manager.connect()
        query = "UPDATE Gemiler SET Adı = ?, Ağırlık = ?, YapımYılı = ?, Tip = ?, YolcuKapasitesi = ?, PetrolKapasitesi = ?, KonteynerSayısı = ?, MaksimumAğırlık = ? WHERE SeriNumarası = ?"
        parameters = (*yeni_veriler, seri_numarasi)
        success = db_manager.execute_query(query, parameters)
        db_manager.disconnect()
        return success

class Sefer:
    def __init__(self, gemi_id, yola_cikis_tarihi, donus_tarihi, baslangic_liman_id, kaptan1_id, kaptan2_id, murettebat_id):
        self.gemi_id = gemi_id
        self.yola_cikis_tarihi = yola_cikis_tarihi
        self.donus_tarihi = donus_tarihi
        self.baslangic_liman_id = baslangic_liman_id
        self.kaptan1_id = kaptan1_id
        self.kaptan2_id = kaptan2_id
        self.murettebat_id = murettebat_id

    def ekle(self):
        conn, cursor = connect_to_database()
        if conn and cursor:
            try:
                insert_query = "INSERT INTO Seferler (GemiID, YolaÇıkışTarihi, DönüşTarihi, BaşlangıçLimanıID, Kaptan1ID, Kaptan2ID, MurettebatID) VALUES (?, ?, ?, ?, ?, ?, ?)"
                cursor.execute(insert_query,
                               (self.gemi_id, self.yola_cikis_tarihi, self.donus_tarihi, self.baslangic_liman_id, self.kaptan1_id, self.kaptan2_id, self.murettebat_id))
                conn.commit()
                print("Yeni sefer başarıyla eklendi.")
            except Exception as e:
                print("Sefer eklenirken bir hata oluştu:", e)

    @staticmethod
    def sil_sefer_by_gemi_numarasi(gemi_numarasi):
        db_manager = DatabaseManager()
        db_manager.connect()
        query = "DELETE FROM Seferler WHERE GemiID = ?"
        parameters = (gemi_numarasi,)
        success = db_manager.execute_query(query, parameters)
        db_manager.disconnect()
        return success

    @staticmethod
    def duzenle_by_gemi_id(gemi_id, yeni_veriler):
        db_manager = DatabaseManager()
        db_manager.connect()
        query = "UPDATE Seferler SET YolaÇıkışTarihi = ?, DönüşTarihi = ?, BaşlangıçLimanıID = ?, Kaptan1ID = ?, Kaptan2ID = ?, MurettebatID = ? WHERE GemiID = ?"
        parameters = (*yeni_veriler, gemi_id)
        success = db_manager.execute_query(query, parameters)
        db_manager.disconnect()
        return success

class Liman:
    def __init__(self, liman_adi, ulke, nufus, pasaport_gerekli_mi, demirleme_ucreti):
        self.liman_adi = liman_adi
        self.ulke = ulke
        self.nufus = nufus
        self.pasaport_gerekli_mi = pasaport_gerekli_mi
        self.demirleme_ucreti = demirleme_ucreti

    def ekle(self):
        conn, cursor = connect_to_database()
        if conn and cursor:
            try:
                insert_query = "INSERT INTO Limanlar (LimanAdı, Ülke, Nüfus, PasaportGerekliMi, DemirlemeÜcreti) VALUES (?, ?, ?, ?, ?)"
                cursor.execute(insert_query, (self.liman_adi, self.ulke, self.nufus, self.pasaport_gerekli_mi, self.demirleme_ucreti))
                conn.commit()
                print("Yeni liman başarıyla eklendi.")
            except Exception as e:
                print("Liman eklenirken bir hata oluştu:", e)

    @staticmethod
    def sil_liman_by_liman_adi(liman_adi):
        db_manager = DatabaseManager()
        db_manager.connect()
        query = "DELETE FROM Limanlar WHERE LimanAdı = ?"
        parameters = (liman_adi,)
        success = db_manager.execute_query(query, parameters)
        db_manager.disconnect()
        return success

    @staticmethod
    def duzenle_by_ulke(ulke, yeni_veriler):
        db_manager = DatabaseManager()
        db_manager.connect()
        query = "UPDATE Limanlar SET LimanAdı = ?, Nüfus = ?, PasaportGerekliMi = ?, DemirlemeÜcreti = ? WHERE Ülke = ?"
        parameters = (*yeni_veriler, ulke)
        success = db_manager.execute_query(query, parameters)
        db_manager.disconnect()
        return success

class Kaptan:
    def __init__(self, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, lisans):
        self.ad = ad
        self.soyad = soyad
        self.adres = adres
        self.vatandaslik = vatandaslik
        self.dogum_tarihi = dogum_tarihi
        self.ise_giris_tarihi = ise_giris_tarihi
        self.lisans = lisans

    def ekle(self):
        conn, cursor = connect_to_database()
        if conn and cursor:
            try:
                insert_query = "INSERT INTO Kaptanlar (Ad, Soyad, Adres, Vatandaşlık, DoğumTarihi, İşeGirişTarihi, Lisans) VALUES (?, ?, ?, ?, ?, ?, ?)"
                cursor.execute(insert_query, (self.ad, self.soyad, self.adres, self.vatandaslik, self.dogum_tarihi, self.ise_giris_tarihi, self.lisans))
                conn.commit()
                print("Yeni kaptan başarıyla eklendi.")
            except Exception as e:
                print("Kaptan eklenirken bir hata oluştu:", e)

    @staticmethod
    def sil_kaptan_by_ad_soyad(ad, soyad):
        db_manager = DatabaseManager()
        db_manager.connect()
        query = "DELETE FROM Kaptanlar WHERE Ad = ? AND Soyad = ?"
        parameters = (ad, soyad)
        success = db_manager.execute_query(query, parameters)
        db_manager.disconnect()
        return success

    @staticmethod
    def duzenle_by_tc_numarasi(tc_numarasi, yeni_veriler):
        db_manager = DatabaseManager()
        db_manager.connect()
        query = "UPDATE Kaptanlar SET Ad = ?, Soyad = ?, Adres = ?, Vatandaşlık = ?, DoğumTarihi = ?, İşeGirişTarihi = ?, Lisans = ? WHERE TCNumarası = ?"
        parameters = (*yeni_veriler, tc_numarasi)
        success = db_manager.execute_query(query, parameters)
        db_manager.disconnect()
        return success

class Murettebat:
    def __init__(self, ad, soyad, gorev, ise_giris_tarihi):
        self.ad = ad
        self.soyad = soyad
        self.gorev = gorev
        self.ise_giris_tarihi = ise_giris_tarihi

    def ekle(self):
        conn, cursor = connect_to_database()
        if conn and cursor:
            try:
                insert_query = "INSERT INTO Mürettebat (Ad, Soyad, Görev, İşeGirişTarihi) VALUES (?, ?, ?, ?)"
                cursor.execute(insert_query, (self.ad, self.soyad, self.gorev, self.ise_giris_tarihi))
                conn.commit()
                print("Yeni mürettebat üyesi başarıyla eklendi.")
            except Exception as e:
                print("Mürettebat eklenirken bir hata oluştu:", e)

    @staticmethod
    def sil_murettebat_by_ad_soyad(ad, soyad):
        db_manager = DatabaseManager()
        db_manager.connect()
        query = "DELETE FROM Mürettebat WHERE Ad = ? AND Soyad = ?"
        parameters = (ad, soyad)
        success = db_manager.execute_query(query, parameters)
        db_manager.disconnect()
        return success

    @staticmethod
    def duzenle_by_tc_numarasi(tc_numarasi, yeni_veriler):
        db_manager = DatabaseManager()
        db_manager.connect()
        query = "UPDATE Mürettebat SET Ad = ?, Soyad = ?, Görev = ?, İşeGirişTarihi = ? WHERE TCNumarası = ?"
        parameters = (*yeni_veriler, tc_numarasi)
        success = db_manager.execute_query(query, parameters)
        db_manager.disconnect()
        return success