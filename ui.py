import tkinter as tk
from tkinter import ttk
from database_operations import Gemi , Sefer,Liman, Kaptan, Murettebat

class GemilerVeSeferlerUygulamasi(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Gemiler ve Seferler Yönetim Sistemi")
        self.geometry("950x800")

        self.gemi_frame = GemiEkleFrame(self)
        self.gemi_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.liman_frame = LimanEkleFrame(self)
        self.liman_frame.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.sefer_frame = SeferEkleFrame(self)
        self.sefer_frame.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        self.kaptan_frame = KaptanEkleFrame(self)
        self.kaptan_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.mürettebat_frame = MürettebatEkleFrame(self)
        self.mürettebat_frame.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="w")

class GemiEkleFrame(ttk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, text="Gemi İşlemleri", *args, **kwargs)

        ttk.Label(self, text="Seri Numarası:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.gemi_seri_entry = ttk.Entry(self)
        self.gemi_seri_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Gemi Adı:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.gemi_entry = ttk.Entry(self)
        self.gemi_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="Ağırlık (ton):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.gemi_agirlik_entry = ttk.Entry(self)
        self.gemi_agirlik_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self, text="Yapım Yılı:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.gemi_yapim_yili_entry = ttk.Entry(self)
        self.gemi_yapim_yili_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self, text="Tip:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.gemi_tip_combobox = ttk.Combobox(self, values=["Yolcu", "Petrol", "Konteyner"])
        self.gemi_tip_combobox.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(self, text="Yolcu Kapasitesi:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.gemi_yolcu_kapasitesi_entry = ttk.Entry(self)
        self.gemi_yolcu_kapasitesi_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(self, text="Petrol Kapasitesi (ton):").grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.gemi_petrol_kapasitesi_entry = ttk.Entry(self)
        self.gemi_petrol_kapasitesi_entry.grid(row=6, column=1, padx=5, pady=5)

        ttk.Label(self, text="Konteyner Sayısı:").grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.gemi_konteyner_sayisi_entry = ttk.Entry(self)
        self.gemi_konteyner_sayisi_entry.grid(row=7, column=1, padx=5, pady=5)

        ttk.Label(self, text="Maksimum Ağırlık (ton):").grid(row=8, column=0, padx=5, pady=5, sticky="e")
        self.gemi_maksimum_agirlik_entry = ttk.Entry(self)
        self.gemi_maksimum_agirlik_entry.grid(row=8, column=1, padx=5, pady=5)

        self.gemi_ekle_button = ttk.Button(self, text="Gemi Ekle", command=self.gemi_ekle_command)
        self.gemi_ekle_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        self.gemi_sil_button = ttk.Button(self, text="Gemi Sil", command=self.gemi_sil_command)
        self.gemi_sil_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

        self.gemi_duzenle_button = ttk.Button(self, text="Gemi Düzenle", command=self.gemi_duzenle_command)
        self.gemi_duzenle_button.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

    def gemi_ekle_command(self):
        seri_numarasi = self.gemi_seri_entry.get()
        gemi_adi = self.gemi_entry.get()
        agirlik = float(self.gemi_agirlik_entry.get())
        yapim_yili = int(self.gemi_yapim_yili_entry.get())
        tip = self.gemi_tip_combobox.get()
        yolcu_kapasitesi = int(self.gemi_yolcu_kapasitesi_entry.get())
        petrol_kapasitesi = float(self.gemi_petrol_kapasitesi_entry.get() or 0)
        konteyner_sayisi = int(self.gemi_konteyner_sayisi_entry.get() or 0)
        maksimum_agirlik = float(self.gemi_maksimum_agirlik_entry.get() or 0)

        gemi = Gemi(seri_numarasi, gemi_adi, agirlik, yapim_yili, tip, yolcu_kapasitesi, petrol_kapasitesi,
                    konteyner_sayisi, maksimum_agirlik)
        gemi.ekle()

    def gemi_sil_command(self):
        seri_numarasi = self.gemi_seri_entry.get()
        success = Gemi.sil_gemi_by_seri_numarasi(seri_numarasi)
        if success:
            print("Gemi başarıyla silindi.")
        else:
            print("Silinecek gemi bulunamadı veya silinirken bir hata oluştu.")

    def gemi_duzenle_command(self):
        seri_numarasi = self.gemi_seri_entry.get()
        yeni_veriler = (
            self.gemi_entry.get(),
            float(self.gemi_agirlik_entry.get()),
            int(self.gemi_yapim_yili_entry.get()),
            self.gemi_tip_combobox.get(),
            int(self.gemi_yolcu_kapasitesi_entry.get()),
            float(self.gemi_petrol_kapasitesi_entry.get() or 0),
            int(self.gemi_konteyner_sayisi_entry.get() or 0),
            float(self.gemi_maksimum_agirlik_entry.get() or 0)
        )

        success = Gemi.duzenle_by_seri_numarasi(seri_numarasi, yeni_veriler)
        if success:
            print("Gemi başarıyla güncellendi.")
        else:
            print("Gemi güncellenirken bir hata oluştu veya belirtilen seri numarasına sahip gemi bulunamadı.")

class SeferEkleFrame(ttk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, text="Sefer İşlemleri", *args, **kwargs)

        ttk.Label(self, text="Gemi ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.sefer_gemi_id_entry = ttk.Entry(self)
        self.sefer_gemi_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Yola Çıkış Tarihi:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.sefer_yola_cikis_tarihi_entry = ttk.Entry(self)
        self.sefer_yola_cikis_tarihi_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="Dönüş Tarihi:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.sefer_donus_tarihi_entry = ttk.Entry(self)
        self.sefer_donus_tarihi_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self, text="Başlangıç Liman ID:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.sefer_baslangic_liman_id_entry = ttk.Entry(self)
        self.sefer_baslangic_liman_id_entry.grid(row=3, column=1, padx=5, pady=5)

        # Kaptan 1 ID giriş alanı
        ttk.Label(self, text="Kaptan 1 ID:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.sefer_kaptan1_id_entry = ttk.Entry(self)
        self.sefer_kaptan1_id_entry.grid(row=4, column=1, padx=5, pady=5)

        # Kaptan 2 ID giriş alanı
        ttk.Label(self, text="Kaptan 2 ID:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.sefer_kaptan2_id_entry = ttk.Entry(self)
        self.sefer_kaptan2_id_entry.grid(row=5, column=1, padx=5, pady=5)

        # Mürettebat ID giriş alanı
        ttk.Label(self, text="Mürettebat ID:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.sefer_murettebat_id_entry = ttk.Entry(self)
        self.sefer_murettebat_id_entry.grid(row=6, column=1, padx=5, pady=5)

        self.sefer_ekle_button = ttk.Button(self, text="Sefer Ekle", command=self.sefer_ekle_command)
        self.sefer_ekle_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.sefer_sil_button = ttk.Button(self, text="Sefer Sil", command=self.sefer_sil_command)
        self.sefer_sil_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

        self.sefer_duzenle_button = ttk.Button(self, text="Sefer Düzenle", command=self.sefer_duzenle_command)
        self.sefer_duzenle_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    def sefer_ekle_command(self):
        gemi_id = int(self.sefer_gemi_id_entry.get())
        yola_cikis_tarihi = self.sefer_yola_cikis_tarihi_entry.get()
        donus_tarihi = self.sefer_donus_tarihi_entry.get()
        baslangic_liman_id = int(self.sefer_baslangic_liman_id_entry.get())
        kaptan1_id = int(self.sefer_kaptan1_id_entry.get())
        kaptan2_id = int(self.sefer_kaptan2_id_entry.get())
        murettebat_id = int(self.sefer_murettebat_id_entry.get())

        sefer = Sefer(gemi_id, yola_cikis_tarihi, donus_tarihi, baslangic_liman_id, kaptan1_id, kaptan2_id, murettebat_id)
        sefer.ekle()

    def sefer_sil_command(self):
        gemi_numarasi = self.sefer_gemi_id_entry.get()
        success = Sefer.sil_sefer_by_gemi_numarasi(gemi_numarasi)
        if success:
            print("Sefer başarıyla silindi.")
        else:
            print("Silinecek sefer bulunamadı veya silinirken bir hata oluştu.")

    def sefer_duzenle_command(self):
        gemi_id = int(self.sefer_gemi_id_entry.get())
        yeni_veriler = (
            self.sefer_yola_cikis_tarihi_entry.get(),
            self.sefer_donus_tarihi_entry.get(),
            int(self.sefer_baslangic_liman_id_entry.get()),
            int(self.sefer_kaptan1_id_entry.get()),
            int(self.sefer_kaptan2_id_entry.get()),
            int(self.sefer_murettebat_id_entry.get())
        )

        success = Sefer.duzenle_by_gemi_id(gemi_id, yeni_veriler)
        if success:
            print("Sefer başarıyla güncellendi.")
        else:
            print("Sefer güncellenirken bir hata oluştu veya belirtilen gemi numarasına sahip sefer bulunamadı.")

class LimanEkleFrame(ttk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, text="Liman İşlemleri", *args, **kwargs)

        ttk.Label(self, text="Liman Adı:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.liman_ad_entry = ttk.Entry(self)
        self.liman_ad_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Ülke:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.liman_ulke_entry = ttk.Entry(self)
        self.liman_ulke_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="Nüfus:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.liman_nufus_entry = ttk.Entry(self)
        self.liman_nufus_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self, text="Pasaport Gerekli mi:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.liman_pasaport_gerekli_mi_combobox = ttk.Combobox(self, values=["True", "False"])
        self.liman_pasaport_gerekli_mi_combobox.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self, text="Demirleme Ücreti:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.liman_demirleme_ucreti_entry = ttk.Entry(self)
        self.liman_demirleme_ucreti_entry.grid(row=4, column=1, padx=5, pady=5)

        self.liman_ekle_button = ttk.Button(self, text="Liman Ekle", command=self.liman_ekle_command)
        self.liman_ekle_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.liman_ekle_button = ttk.Button(self, text="Liman Sil", command=self.liman_sil_command)
        self.liman_ekle_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

        self.liman_duzenle_button = ttk.Button(self, text="Liman Düzenle", command=self.liman_duzenle_command)
        self.liman_duzenle_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def liman_ekle_command(self):
        liman_adi = self.liman_ad_entry.get()
        ulke = self.liman_ulke_entry.get()
        nufus = int(self.liman_nufus_entry.get())
        pasaport_gerekli_mi = self.liman_pasaport_gerekli_mi_combobox.get()
        demirleme_ucreti = float(self.liman_demirleme_ucreti_entry.get())

        liman = Liman(liman_adi, ulke, nufus, pasaport_gerekli_mi, demirleme_ucreti)
        liman.ekle()

    def liman_sil_command(self):
        liman_adi = self.liman_ad_entry.get()
        success = Liman.sil_liman_by_liman_adi(liman_adi)
        if success:
            print("liman başarıyla silindi.")
        else:
            print("Silinecek liman bulunamadı veya silinirken bir hata oluştu.")

    def liman_duzenle_command(self):
        ulke = self.liman_ulke_entry.get()
        yeni_veriler = (
            self.liman_ad_entry.get(),
            int(self.liman_nufus_entry.get()),
            self.liman_pasaport_gerekli_mi_combobox.get(),
            float(self.liman_demirleme_ucreti_entry.get())
        )

        success = Liman.duzenle_by_ulke(ulke, yeni_veriler)
        if success:
            print("Liman başarıyla güncellendi.")
        else:
            print("Liman güncellenirken bir hata oluştu veya belirtilen ülkeye sahip liman bulunamadı.")


class KaptanEkleFrame(ttk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, text="Kaptan İşlemleri", *args, **kwargs)

        ttk.Label(self, text="Ad:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.kaptan_ad_entry = ttk.Entry(self)
        self.kaptan_ad_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Soyad:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.kaptan_soyad_entry = ttk.Entry(self)
        self.kaptan_soyad_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="TC Numarası:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.kaptan_tc_entry = ttk.Entry(self)
        self.kaptan_tc_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self, text="Adres:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.kaptan_adres_entry = ttk.Entry(self)
        self.kaptan_adres_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self, text="Vatandaşlık:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.kaptan_vatandaslik_entry = ttk.Entry(self)
        self.kaptan_vatandaslik_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(self, text="Doğum Tarihi (YYYY-MM-DD):").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.kaptan_dogum_tarihi_entry = ttk.Entry(self)
        self.kaptan_dogum_tarihi_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(self, text="İşe Giriş Tarihi (YYYY-MM-DD):").grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.kaptan_ise_giris_tarihi_entry = ttk.Entry(self)
        self.kaptan_ise_giris_tarihi_entry.grid(row=6, column=1, padx=5, pady=5)

        ttk.Label(self, text="Lisans:").grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.kaptan_lisans_entry = ttk.Entry(self)
        self.kaptan_lisans_entry.grid(row=7, column=1, padx=5, pady=5)

        self.kaptan_ekle_button = ttk.Button(self, text="Kaptan Ekle", command=self.kaptan_ekle_command)
        self.kaptan_ekle_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        self.kaptan_sil_button = ttk.Button(self, text="Kaptan Sil", command=self.kaptan_sil_command)
        self.kaptan_sil_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        self.kaptan_duzenle_button = ttk.Button(self, text="Kaptan Düzenle", command=self.kaptan_duzenle_command)
        self.kaptan_duzenle_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

    def kaptan_ekle_command(self):
        ad = self.kaptan_ad_entry.get()
        soyad = self.kaptan_soyad_entry.get()
        adres = self.kaptan_adres_entry.get()
        vatandaslik = self.kaptan_vatandaslik_entry.get()
        dogum_tarihi = self.kaptan_dogum_tarihi_entry.get()
        ise_giris_tarihi = self.kaptan_ise_giris_tarihi_entry.get()
        lisans = self.kaptan_lisans_entry.get()
        TCno = self.kaptan_tc_entry.get()

        kaptan = Kaptan(ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, lisans, TCno)
        kaptan.ekle()


    def kaptan_sil_command(self):
        ad = self.kaptan_ad_entry.get()
        soyad = self.kaptan_soyad_entry.get()

        success = Kaptan.sil_kaptan_by_ad_soyad(ad, soyad)

        if success:
            print("Kaptan başarıyla silindi.")
        else:
            print("Kaptan silinirken bir hata oluştu veya belirtilen kaptan bulunamadı.")

    def kaptan_duzenle_command(self):
        tc_numarasi = self.kaptan_tc_entry.get()
        yeni_veriler = (
            self.kaptan_ad_entry.get(),
            self.kaptan_soyad_entry.get(),
            self.kaptan_adres_entry.get(),
            self.kaptan_vatandaslik_entry.get(),
            self.kaptan_dogum_tarihi_entry.get(),
            self.kaptan_ise_giris_tarihi_entry.get(),
            self.kaptan_lisans_entry.get()
        )

        success = Kaptan.duzenle_by_tc_numarasi(tc_numarasi, yeni_veriler)
        if success:
            print("Kaptan başarıyla güncellendi.")
        else:
            print("Kaptan güncellenirken bir hata oluştu veya belirtilen TC numarasına sahip kaptan bulunamadı.")


class MürettebatEkleFrame(ttk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, text="Mürettebat İşlemleri", *args, **kwargs)

        ttk.Label(self, text="Ad:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.mürettebat_ad_entry = ttk.Entry(self)
        self.mürettebat_ad_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Soyad:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.mürettebat_soyad_entry = ttk.Entry(self)
        self.mürettebat_soyad_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="TC Numarası:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.mürettebat_tc_entry = ttk.Entry(self)
        self.mürettebat_tc_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self, text="Görev:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.mürettebat_gorev_entry = ttk.Entry(self)
        self.mürettebat_gorev_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self, text="İşe Giriş Tarihi (YYYY-MM-DD):").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.mürettebat_ise_giris_tarihi_entry = ttk.Entry(self)
        self.mürettebat_ise_giris_tarihi_entry.grid(row=4, column=1, padx=5, pady=5)

        self.mürettebat_ekle_button = ttk.Button(self, text="Mürettebat Ekle", command=self.mürettebat_ekle_command)
        self.mürettebat_ekle_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.mürettebat_sil_button = ttk.Button(self, text="Mürettebat Sil", command=self.mürettebat_sil_command)
        self.mürettebat_sil_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.mürettebat_duzenle_button = ttk.Button(self, text="Mürettebat Düzenle",command=self.mürettebat_duzenle_command)
        self.mürettebat_duzenle_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    def mürettebat_ekle_command(self):
        ad = self.mürettebat_ad_entry.get()
        soyad = self.mürettebat_soyad_entry.get()
        görev = self.mürettebat_gorev_entry.get()
        ise_giris_tarihi = self.mürettebat_ise_giris_tarihi_entry.get()
        TCno = self.mürettebat_tc_entry.get()

        mürettebat = Murettebat(ad, soyad, görev, ise_giris_tarihi, TCno)
        mürettebat.ekle()


    def mürettebat_sil_command(self):
        ad = self.mürettebat_ad_entry.get()
        soyad = self.mürettebat_soyad_entry.get()

        success = Murettebat.sil_murettebat_by_ad_soyad(ad, soyad)

        if success:
            print("Mürettebat başarıyla silindi.")
        else:
            print("Mürettebat silinirken bir hata oluştu veya belirtilen kaptan bulunamadı.")

    def mürettebat_duzenle_command(self):
        tc_numarasi = self.mürettebat_tc_entry.get()
        yeni_veriler = (
            self.mürettebat_ad_entry.get(),
            self.mürettebat_soyad_entry.get(),
            self.mürettebat_gorev_entry.get(),
            self.mürettebat_ise_giris_tarihi_entry.get()
        )

        success = Murettebat.duzenle_by_tc_numarasi(tc_numarasi, yeni_veriler)
        if success:
            print("Mürettebat başarıyla güncellendi.")
        else:
            print(
                "Mürettebat güncellenirken bir hata oluştu veya belirtilen TC numarasına sahip mürettebat bulunamadı.")

if __name__ == "__main__":
    app = GemilerVeSeferlerUygulamasi()
    app.mainloop()