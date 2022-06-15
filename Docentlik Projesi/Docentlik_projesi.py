import os
import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)



class EğitimOgretimFaaliyetleri():
    def __init__(self,
                 # ---------------------------------- 1-Uluslararası
                 uluslararsıa=20, uluslararsıb=15,
                 uluslararsıc=5, uluslararası_liste_T_F=[False],
                 uluslarası_doc_sonrası=[0],
                 uluslarası_doc_oncesi=[0],

                 # -------------------------------------------- 2-Ulusal
                 ulusala=8, ulusalb=4,
                 ulusal_makale_sayısı=[], ulusal_liste_T_F=[False],
                 toplam_makale=0, ulusal_makale_1_1=0,
                 ulusal_doc_sonrası=[],
                 ulusal_doc_oncesi=[],

                 # -------------------------------------- 3-Lisasüstü
                 makale_list=[],
                 lisans_liste_T_F=[False],
                 lisans_doc_sonrası=[],
                 lisans_doc_oncesi=[],

                 # --------------------------------------- 4-Kitap

                 kitap_liste_T_F=[True],
                 kitap_doc_sonrası=[],
                 kitap_doc_oncesi=[],

                 # -----------------------------------------5-Atıflar
                 atıflar_doc_sonrası=[],
                 atıflar_doc_oncesi=[],
                 atıflar_liste_T_F=[False],

                 # -------------------------------------6-Lisansnsüstü tez
                 lisansüstü_Tez_tp_puan=[],
                 lisansüstü_Tez_T_F=[True],

                 # -------------------------------------7-Bilimsel Araştırma
                 bilimsel_Araştırma_doc_sonrası=[],
                 bilimsel_Araştırma_doc_oncesi=[],
                 bilimsel_Araştırma_liste_T_F=[True],

                 # -------------------------------- 8-Bilimsel Toplantı
                 bilimsel_toplantı_doc_sonrası=[],
                 bilimsel_toplantı_doc_oncesi=[],
                 bilimsel_toplantı_T_F=[False],
                 # -----------------------------9-Eğitim Öğretim
                 egitim_ogretim_doc_sonrası=[],
                 egitim_ogretim_T_F=[False],

                 # -------------------------------------- global
                 makale_sayısı=0, basvuran_kısı=0,
                 doktora_sonrası=[0], doktora_oncesi=[0]

                 ):

        # 1-Uluslararası bolum
        self.uluslararsıa = uluslararsıa
        self.uluslararsıb = uluslararsıb
        self.uluslararsıc = uluslararsıc
        self.uluslararası_liste_T_F = uluslararası_liste_T_F
        self.uluslarası_doc_sonrası = uluslarası_doc_sonrası
        self.uluslarası_doc_oncesi = uluslarası_doc_oncesi

        # 2-Ulusal bolum
        self.ulusala = ulusala
        self.ulusalb = ulusalb
        self.ulusal_doc_sonrası = ulusal_doc_sonrası
        self.ulusal_doc_oncesi = ulusal_doc_oncesi
        self.ulusal_makale_sayısı = ulusal_makale_sayısı
        self.toplam_makale = toplam_makale
        self.ulusal_liste_T_F = ulusal_liste_T_F
        self.ulusal_makale_1_1 = ulusal_makale_1_1

        # 3-Lisasüstü
        self.makale_list = makale_list
        self.lisans_liste_T_F = lisans_liste_T_F
        self.lisans_doc_sonrası = lisans_doc_sonrası
        self.lisans_doc_oncesi = lisans_doc_oncesi

        # 4-Kitap
        self.kitap_liste_T_F = kitap_liste_T_F
        self.kitap_doc_sonrası = kitap_doc_sonrası
        self.kitap_doc_oncesi = kitap_doc_oncesi

        # 5-Atıflar
        self.atıflar_doc_sonrası = atıflar_doc_sonrası
        self.atıflar_doc_oncesi = atıflar_doc_oncesi
        self.atıflar_liste_T_F = atıflar_liste_T_F

        # 6-Lisansüstü tez danışmanlığı
        self.lisansüstü_Tez_tp_puan = lisansüstü_Tez_tp_puan
        self.lisansüstü_Tez_T_F = lisansüstü_Tez_T_F

        # 7-Bilimsel Araştırma Projesi
        self.bilimsel_Araştırma_doc_sonrası = bilimsel_Araştırma_doc_sonrası
        self.bilimsel_Araştırma_doc_oncesi = bilimsel_Araştırma_doc_oncesi
        self.bilimsel_Araştırma_liste_T_F = bilimsel_Araştırma_liste_T_F

        # 8-Bilimsel_toplantı
        self.bilimsel_toplantı_doc_sonrası = bilimsel_toplantı_doc_sonrası
        self.bilimsel_toplantı_doc_oncesi = bilimsel_toplantı_doc_oncesi
        self.bilimsel_toplantı_T_F = bilimsel_toplantı_T_F

        # 9-Eğitim Öğretim Faaliyet
        self.egitim_ogretim_doc_sonrası = egitim_ogretim_doc_sonrası
        self.egitim_ogretim_T_F = egitim_ogretim_T_F


        # global
        self.makale_sayısı = makale_sayısı
        self.basvuran_kısı = basvuran_kısı
        self.doktora_sonrası = doktora_sonrası
        self.doktora_oncesi = doktora_oncesi

    def clear(self):
        """
            Bu fonksiyon terminal penceresini ilk haline getirir.
        """
        # İşletim Sistemi Windows ise
        if os.name == 'nt':
            _ = os.system('cls')
        # İşletim Sistemi MacOS ise
        elif os.name == 'mac':
            _ = os.system('clear')
        # İşletim Sistemi Linux ise
        elif os.name == 'posix':
            _ = os.system('clear')
        # Yabancı bir işletim sistemi ise
        else:
            _ = os.system('clear')

    def uluslararası_Makale(self):

        time.sleep(1)
        print("""
╒══════════════════════════════════════════════════════════════════════════════╕
│                            1. Uluslararası Makale                            │
╞══════════════════════════════════════════════════════════════════════════════╡
│ Başvurulan doçentlik bilim alanı ile ilgili ve adayın hazırladığı lisansüstü │
│ tezlerden üretilmemiş olmak kaydıyla                                         │
├──────────────────────────────────────────────────────────────────────────────┤
│ a) SSCI, SCI, SCI- Expanded ve AHCI kapsamındaki dergilerde editöre mektup,  │
│ özet veya kitap kritiği hariç olmak üzere yayımlanmış makale                 │
├──────────────────────────────────────────────────────────────────────────────┤
│ b) Uluslararası alan endekslerinde taranan dergilerde editöre mektup, özet   │
│ veya kitap kritiği hariç olmak üzere yayımlanmış makale                      │
├──────────────────────────────────────────────────────────────────────────────┤
│ c) Bu maddenin a veya b bentleri kapsamındaki yayınlarda alanında bilime     │
│ katkı sağlayan kitap kritiği yapılmış makale                                 │
├──────────────────────────────────────────────────────────────────────────────┤
│ p) Puan Hesapla                                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│ q) Çıkış Yap                                                                 │
├──────────────────────────────────────────────────────────────────────────────┤
│ * Bu maddenin a veya b bentleri kapsamında en az 20 puan almak zorunludur.   │
╘══════════════════════════════════════════════════════════════════════════════╛
        """)

        while True:

            Uluslararası_secenek = input("Uluslararası Makale Hesapla :")
            # -------------------------------------------------------------------------A SECENEGİ

            if Uluslararası_secenek == "a" or Uluslararası_secenek == "A":
                print("""--> SSCI, SCI, SCI- Expanded ve AHCI kapsamındaki dergilerde editöre\nmektup, özet veya kitap kritiği hariç olmak üzere yayımlanmış makale:
                                    1.Toplam kaç kişi
                                    2.Kaç tane
                                    3.Doktora Zamanı
                                    4.Çıkmak İçin
                    """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------kişi sayısı
                    if secenek == "1":

                        self.ulusalararsı_basvuru_1 = input("Toplam kaç kişi:")
                        try:
                            self.ulusalararsı_basvuru_1_1 = int(self.ulusalararsı_basvuru_1)
                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")



                    # ------------------------------------------------------------------ makale sayısı
                    elif secenek == "2":
                        self.ulusalararsı_makale_1 = input(
                            "--> SSCI, SCI, SCI- Expanded ve AHCI kapsamındaki dergilerde editöre\nmektup, özet veya kitap kritiği hariç olmak üzere yayımlanmış makale:")
                        try:
                            try:
                                self.ulusalararsı_makale_1_1 = int(self.ulusalararsı_makale_1)

                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------Zaman
                    elif secenek == "3":
                        self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                    "a)Doktora Sonrası \n"
                                                    "b)Doktora Öncesi :")
                        try:
                            try:
                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":

                                    self.ulusalararsı_puan_1 = 20 / self.ulusalararsı_basvuru_1_1
                                    self.ulusalararsı_puan_2 = self.ulusalararsı_puan_1 * self.ulusalararsı_makale_1_1

                                    self.uluslarası_doc_sonrası.append(self.ulusalararsı_puan_2)
                                    break


                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":

                                    self.ulusalararsı_puan_1 = 20 / self.ulusalararsı_basvuru_1_1
                                    self.ulusalararsı_puan_2 = self.ulusalararsı_puan_1 * self.ulusalararsı_makale_1_1

                                    self.uluslarası_doc_oncesi.append(self.ulusalararsı_puan_2)

                                    break
                                else:
                                    print("İşleminiz Gerçekleşiyor")
                                    time.sleep(1)
                                    print("Geçersiz İşlem......")
                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Önce Kişi Sayısı Girilmeli!!!")
                    elif secenek == "4":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")



            #  --------------------------------------------------------------------------------B SECENEGİ
            elif Uluslararası_secenek == "b" or Uluslararası_secenek == "B":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> Uluslararası alan endekslerinde taranan dergilerde editöre mektup, özet\n veya kitap kritiği hariç olmak üzere yayımlanmış makale:
                                   1.Toplam kaç kişi                                    
                                   2.Kaç tane
                                   3.Doktora Zamanı
                                   4.Çıkmak İçin
                           """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------kişi sayısı
                    if secenek == "1":
                        self.ulusalararsı_basvuru_2 = input("Toplam kaç kişi:")
                        try:
                            self.ulusalararsı_basvuru_2_1 = int(self.ulusalararsı_basvuru_2)
                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------ makale sayısı
                    elif secenek == "2":
                        self.ulusalararsı_makale_2 = input(
                            "-->Uluslararası alan endekslerinde taranan dergilerde editöre mektup, özet\nveya kitap kritiği hariç olmak üzere yayımlanmış makale:")
                        try:
                            try:
                                self.ulusalararsı_makale_2_1 = int(self.ulusalararsı_makale_2)

                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------Zaman
                    elif secenek == "3":
                        self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                    "a)Doktora Sonrası \n"
                                                    "b)Doktora Öncesi :")
                        try:
                            try:
                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.ulusalararsı_puan_3 = 15 / self.ulusalararsı_basvuru_2_1
                                    self.ulusalararsı_puan_4 = self.ulusalararsı_puan_3 * self.ulusalararsı_makale_2_1
                                    self.uluslarası_doc_sonrası.append(self.ulusalararsı_puan_4)
                                    break

                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.ulusalararsı_puan_3 = 15 / self.ulusalararsı_basvuru_2_1
                                    self.ulusalararsı_puan_4 = self.ulusalararsı_puan_3 * self.ulusalararsı_makale_2_1
                                    self.uluslarası_doc_oncesi.append(self.ulusalararsı_puan_4)
                                    break
                                else:
                                    print("İşleminiz Gerçekleşiyor")
                                    time.sleep(1)
                                    print("Geçersiz İşlem......")

                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")
                        except AttributeError:
                            print("Önce Kişi Sayısı Girilmeli!!!")
                    elif secenek == "4":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            #  ------------------------------------------------------------------C SECENEGİ

            elif Uluslararası_secenek == "c" or Uluslararası_secenek == "C":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> Bu maddenin a veya b bentleri kapsamındaki yayınlarda alanında bilime\nkatkı sağlayan kitap kritiği yapılmış makale:
                                    1.Toplam kaç kişi                                    
                                    2.Kaç tane
                                    3.Doktora Zamanı
                                    4.Çıkmak İçin

                                           """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ---------------------------------------------------------------------------------------------- (kişi sayısı)
                    if secenek == "1":
                        self.ulusalararsı_basvuru_3 = input("Toplam kaç kişi:")
                        try:
                            self.ulusalararsı_basvuru_3_1 = int(self.ulusalararsı_basvuru_3)
                            continue
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")

                    # ----------------------------------------------------------------------------------------------(makale sayısı)
                    elif secenek == "2":
                        self.ulusalararsı_makale_3 = input(
                            "Uluslararası alan endekslerinde taranan dergilerde editöre mektup, özet\nveya kitap kritiği hariç olmak üzere yayımlanmış makale:")
                        try:
                            try:
                                self.ulusalararsı_makale_3_1 = int(self.ulusalararsı_makale_3)

                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------Zaman
                    elif secenek == "3":
                        self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                    "a)Doktora Sonrası \n"
                                                    "b)Doktora Öncesi :")
                        try:
                            try:

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.ulusalararsı_puan_5 = 5 / self.ulusalararsı_basvuru_3_1
                                    self.ulusalararsı_puan_6 = self.ulusalararsı_puan_5 * self.ulusalararsı_makale_3_1
                                    self.doktora_sonrası.append(self.ulusalararsı_puan_6)
                                    break

                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.ulusalararsı_puan_5 = 5 / self.ulusalararsı_basvuru_3_1
                                    self.ulusalararsı_puan_6 = self.ulusalararsı_puan_5 * self.ulusalararsı_makale_3_1
                                    self.doktora_oncesi.append(self.ulusalararsı_puan_6)
                                    break
                                else:
                                    print("İşleminiz Gerçekleşiyor")
                                    time.sleep(1)
                                    print("Geçersiz İşlem......")
                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")
                        except AttributeError:
                            print("Önce Kişi Sayısı Girilmeli!!!")
                    elif secenek == "4":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")
            # ------------------------------------------------------------------ toplama işlemi

            elif Uluslararası_secenek == "p" or Uluslararası_secenek == "P":
                uluslar_docSonrası_alınan_puan = self.uluslarası_doc_sonrası
                uluslar_doc_sonrası_toplam = sum(uluslar_docSonrası_alınan_puan)

                # -------------------------------------------

                uluslar_docOncesı_alınan_puan = self.uluslarası_doc_oncesi
                uluslar_doc_oncesi_toplam = sum(uluslar_docOncesı_alınan_puan)

                if uluslar_doc_sonrası_toplam + uluslar_doc_oncesi_toplam > 19:

                    try:
                        if uluslar_doc_sonrası_toplam + uluslar_doc_oncesi_toplam >= 20:
                            print(
                                "Bu maddenin a veya b bentleri kapsamında en az 20 puan almak zorunluluk aşamasını gectınız. ")
                            self.doktora_sonrası.append(uluslar_doc_sonrası_toplam)
                            self.doktora_oncesi.append(uluslar_doc_oncesi_toplam)
                            time.sleep(1)
                        print("Genel Puanınız ")
                        time.sleep(1)
                        self.doktora_sonrası_puan()
                        self.doktora_oncesi_puan()
                            #--------------------------------------
                        soru = input("sistem yenılensın mı (E,H): ")
                        if soru == "e" or soru =="E":
                            self.uluslararası_liste_T_F.clear()
                            uluslar_docSonrası_alınan_puan.clear()
                            uluslar_docOncesı_alınan_puan.clear()
                            self.uluslararası_liste_T_F.append(True)
                            self.clear()
                        else:
                            self.uluslararası_liste_T_F.clear()
                            uluslar_docSonrası_alınan_puan.clear()
                            uluslar_docOncesı_alınan_puan.clear()
                            self.uluslararası_liste_T_F.append(True)
                            break
                    except:
                        print("Bu maddenin a veya b bentlerinden puan alınmak zorunda !!!")

                elif uluslar_doc_sonrası_toplam + uluslar_doc_oncesi_toplam < 20:

                    try:

                        soru_2 = input("Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
                        if soru_2 == "e" or soru_2 == "E":
                            self.uluslararası_liste_T_F.clear()
                            print("Lütfen veri giriniz...")
                            print("Bu maddenin a veya b bentleri kapsamında en az 20 puan almak zorunludur.")
                            self.uluslararası_liste_T_F.append(False)
                            break
                        else:
                            if self.uluslararası_liste_T_F == [True]:
                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()
                                break

                            elif self.uluslararası_liste_T_F == [False]:
                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()

                                break
                    except:
                        print("hata")
                        break


            elif Uluslararası_secenek =="q" or Uluslararası_secenek =="Q" :
                break

            else:
                print("İşleminiz Gerçekleşiyor")
                time.sleep(1)
                print("Geçersiz İşlem......")

    def ulusal_makale(self):
        time.sleep(1)

        print("""
           ╒══════════════════════════════════════════════════════════════════════════════╕
           │                               2. Ulusal Makale                               │
           ╞══════════════════════════════════════════════════════════════════════════════╡
           │ Başvurulan doçentlik bilim alanı ile ilgili ve adayın yaptığı lisansüstü     │
           │ tezlerden üretilmemiş olmak kaydıyla                                         │
           ├──────────────────────────────────────────────────────────────────────────────┤
           │ a) ULAKBİM tarafından taranan ulusal hakemli dergilerde yayımlanmış makale   │
           ├──────────────────────────────────────────────────────────────────────────────┤
           │ b) a bendi dışındaki ulusal hakemli dergilerde yayımlanmış makale            │
           ├──────────────────────────────────────────────────────────────────────────────┤
           │ p) Puan Hesapla                                                              │
           ├──────────────────────────────────────────────────────────────────────────────┤
           │ q) Çıkış Yap                                                                 │
           ├──────────────────────────────────────────────────────────────────────────────┤
           │ * İkisi bu maddenin a bendi kapsamında olmak üzere en az üç yayın yapmak     │
           │ zorunludur.Yabancı uyruklu adaylar ile yurtdışı doçentlik denkliği başvurusu │
           │ yapan adaylar , ULAKBİM tarafından taranan ulusal hakemli dergilerde         │
           │ yayımlanmış makale şartını sağlayamamaları durumunda, bunun yerine aynı      │
           │ sayıdaki yayını 1.maddenin a ve/veya b bentleri kapsamında sağlayacaklardır  │
           ╘══════════════════════════════════════════════════════════════════════════════╛

    """)

        while True:

            ulusal_secenek = input("--> Ulusal Makale Hesapla:")
            # ------------------------------------------------------------------A SECENEGİ
            if ulusal_secenek == "a" or ulusal_secenek == "A":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> ULAKBİM tarafından taranan ulusal hakemli dergilerde yayımlanmış makale :
                                                     1.Toplam kaç kişi                                    
                                                     2.Kaç tane
                                                     3.Doktora Zamanı
                                                     4.Çıkmak İçin
                                                     """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------A MADDENİN (Kişi sayısı)
                    if secenek == "1":
                        self.ulusal_basvuru_1 = input("Toplam kaç kişi:")
                        try:
                            self.ulusal_basvuru_1_1 = int(self.ulusal_basvuru_1)
                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")

                    # ------------------------------------------------------------------ -A MADDENİN (makale sayısı)
                    elif secenek == "2":

                        self.ulusal_makale_1 = input(
                            "--> ULAKBİM tarafından taranan ulusal hakemli dergilerde yayımlanmış makale :")
                        try:
                            try:
                                self.ulusal_makale_1_1 = int(self.ulusal_makale_1)
                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")

                    # -------------------------------------------------------------------------------------------------A MADDENİN (Zaman)
                    elif secenek == "3":
                        try:
                            try:
                                self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                            "a)Doktora Sonrası \n"
                                                            "b)Doktora Öncesi :")

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    # ----------------------------------------------------------------------------------------makale sayısı 2 den az  olursa

                                    if self.ulusal_makale_1_1 < 2:
                                        try:
                                            print("Bu Aşamada a bendindeki en az 2 makale sartını sağlamadınız.")
                                            break
                                        except ValueError:
                                            print("Bir sayı girmelisiniz!!!")

                                    # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa
                                    elif self.ulusal_makale_1_1 == 2:
                                        try:
                                            try:
                                                print(
                                                    "Bu Aşamada a bendindeki en az 2 makale sartını sağladınız ama 3 tane zorunlu makale aşamasını halen tamamlamadınız")

                                                self.ulusal_puan_1 = 8 / self.ulusal_basvuru_1_1
                                                self.ulusal_puan_2 = (self.ulusal_puan_1 * self.ulusal_makale_1_1)
                                                self.ulusal_doc_sonrası.append(self.ulusal_puan_2)
                                                self.ulusal_makale_sayısı.append(self.ulusal_makale_1_1)
                                                break

                                            except ValueError:
                                                print("Bir sayı girmelisiniz!!!")

                                        except AttributeError:
                                            print("İlk Önce Kişi Sayısı Girin!!!")
                                    # -------------------------------------------------------------------------------------------------makale sayısı 3 olursa
                                    elif self.ulusal_makale_1_1 >= 3:
                                        try:
                                            try:
                                                print(
                                                    "Bu Aşamada a bendindeki en az 2 makale sartını sağladınız ve 3 tane zorunlu makale aşamasını geçtiniz"
                                                )

                                                self.ulusal_puan_3 = 8 / self.ulusal_basvuru_1_1
                                                self.ulusal_puan_4 = self.ulusal_puan_3 * self.ulusal_makale_1_1

                                                self.ulusal_doc_sonrası.append(self.ulusal_puan_4)
                                                self.ulusal_makale_sayısı.append(self.ulusal_makale_1_1)
                                                break
                                            except ValueError:
                                                print("Bir sayı girmelisiniz!!!")
                                        except AttributeError:
                                            print("İlk Önce Kişi Sayısı Girin!!!")

                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa
                                    if self.ulusal_makale_1_1 == 2:
                                        try:
                                            try:
                                                print(
                                                    "Bu Aşamada a bendindeki en az 2 makale sartını sağladınız ama 3 tane zorunlu makale aşamasını halen tamamlamadınız")
                                                self.ulusal_puan_1 = 8 / self.ulusal_basvuru_1_1
                                                self.ulusal_puan_2 = self.ulusal_puan_1 * self.ulusal_makale_1_1
                                                self.ulusal_doc_oncesi.append(self.ulusal_puan_2)
                                                self.ulusal_makale_sayısı.append(self.ulusal_makale_1_1)

                                                break
                                            except ValueError:
                                                print("Bir sayı girmelisiniz!!!")

                                        except AttributeError:
                                            print("İlk Önce Kişi Sayısı Girin!!!")
                                    # -------------------------------------------------------------------------------------------------makale sayısı 3 olursa
                                    elif self.ulusal_makale_1_1 >= 3:
                                        try:
                                            try:
                                                print(
                                                    "Bu Aşamada a bendindeki en az 2 makale sartını sağladınız ve 3 tane zorunlu makale aşamasını geçtiniz"
                                                )

                                                self.ulusal_puan_3 = 8 / self.ulusal_basvuru_1_1
                                                self.ulusal_puan_4 = self.ulusal_puan_3 * self.ulusal_makale_1_1

                                                self.ulusal_doc_oncesi.append(self.ulusal_puan_4)

                                                self.ulusal_makale_sayısı.append(self.ulusal_makale_1_1)
                                                break
                                            except ValueError:
                                                print("Bir sayı girmelisiniz!!!")
                                        except AttributeError:
                                            print("İlk Önce Kişi Sayısı Girin!!!")
                                    # ------------------------------------------------------------------makale sayısı 2 den az  olursa
                                    elif self.ulusal_makale_1_1 < 2:
                                        try:
                                            print("Bu Aşamada a bendindeki en az 2 makale sartını sağlamadınız.")
                                            break
                                        except ValueError:
                                            print("Bir sayı girmelisiniz!!!")

                                else:
                                    print("Geçersiz İşlem......")

                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Sıralamayı Bozmayın!!!")

                    elif secenek == "4":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")





            elif ulusal_secenek == "b" or ulusal_secenek == "B":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> a bendi dışındaki ulusal hakemli dergilerde yayımlanmış makale :
                                                                                    1.Toplam kaç kişi                                    
                                                                                    2.Kaç tane
                                                                                    3.Doktora Zamanı
                                                                                    4.Çıkmak İçin
                                                                            """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ----------------------------------------------------------------------------------------------B MADDENİN (kişi sayısı)
                    if secenek == "1":
                        self.ulusal_basvuru_2 = input("Toplam kaç kişi:")
                        try:
                            self.ulusal_basvuru_2_1 = int(self.ulusal_basvuru_2)
                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # -------------------------------------------------------------------------------------------B MADDENİN (makale sayısı)
                    elif secenek == "2":

                        self.ulusal_makale_2 = input(
                            "--> a bendi dışındaki ulusal hakemli dergilerde yayımlanmış makale:")
                        try:
                            self.ulusal_makale_2_1 = int(self.ulusal_makale_2)

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # -------------------------------------------------------------------------------------------------B MADDENİN (Zaman)
                    elif secenek == "3":
                        self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                    "a)Doktora Sonrası \n"
                                                    "b)Doktora Öncesi :")
                        try:
                            try:
                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI SONRA
                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    # ---------------------------------------------------------------------------------------makale sayısı 1 den büyük
                                    # prblem var------------------------------------------------------------------------------------------------

                                    if self.ulusal_makale_1_1 >= 2:

                                        if self.ulusal_makale_2_1 >= 1:
                                            try:
                                                self.ulusal_puan_5 = 4 / self.ulusal_basvuru_2_1
                                                self.ulusal_puan_6 = self.ulusal_puan_5 * self.ulusal_makale_2_1
                                                self.ulusal_makale_sayısı.append(self.ulusal_makale_1_1)
                                                self.ulusal_doc_sonrası.append(self.ulusal_puan_6)

                                                break
                                            except:
                                                print("Bir sayı girmelisiniz!!!")
                                        break
                                        # ---------------------------------------------------------------------------------------makale sayısı 1 den kücük

                                    if self.ulusal_makale_1_1 < 2:
                                        print("a bendi 2 makale sağlanmadı")
                                        if self.ulusal_makale_2_1 < 1:

                                            try:
                                                print("Toplam 3 makalelik aşama geçilmedi!!!")
                                                break

                                            except:
                                                print("Toplam 3 makalelik aşama geçilmedi!!!")
                                        break
                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI ÖNCE

                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    # ---------------------------------------------------------------------------------------makale sayısı 1 den büyük
                                    if self.ulusal_makale_1_1 >= 2:

                                        if self.ulusal_makale_2_1 >= 1:
                                            try:
                                                self.ulusal_puan_5 = 4 / self.ulusal_basvuru_2_1
                                                self.ulusal_puan_6 = self.ulusal_puan_5 * self.ulusal_makale_2_1
                                                self.ulusal_makale_sayısı.append(self.ulusal_makale_1_1)
                                                self.ulusal_doc_oncesi.append(self.ulusal_puan_6)

                                                break
                                            except:
                                                print("Bir sayı girmelisiniz!!!")
                                        break
                                    if self.ulusal_makale_2_1 < 1:
                                        try:
                                            print("Toplam 3 makalelik aşama geçilmedi!!!")
                                            break

                                        except:
                                            print("Toplam 3 makalelik aşama geçilmedi!!!")
                                    break
                                else:
                                    print("Geçersiz İşlem......")
                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")
                        except AttributeError:
                            print("Önce Kişi Sayısı Girilmeli!!!")
                    elif secenek == "4":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")





            elif ulusal_secenek == "p" or ulusal_secenek == "P":
                self.makale_toplama()
                ulusal_docSonrası_alınan_puan = self.ulusal_doc_sonrası
                doc_sonrası_toplam = sum(ulusal_docSonrası_alınan_puan)

                # -------------------------------------------

                ulusal_docOncesı_alınan_puan = self.ulusal_doc_oncesi
                doc_oncesi_toplam = sum(ulusal_docOncesı_alınan_puan)

                if self.toplam_makale > 2:
                    try:
                        if self.toplam_makale >= 3:
                            print(
                                "İkisi bu maddenin a bendi kapsamında olmak üzere en az üç yayın yapmak zorunluluğunu gectiniz.")

                            self.doktora_sonrası.append(doc_sonrası_toplam)
                            self.doktora_oncesi.append(doc_oncesi_toplam)
                            time.sleep(1)

                        print("Genel Puanınız ")
                        time.sleep(1)
                        self.doktora_sonrası_puan()
                        self.doktora_oncesi_puan()
                        soru = input("sistem yenılensın mı (E,H): ")
                        if soru == "e" or soru == "E":
                            self.ulusal_liste_T_F.clear()
                            ulusal_docSonrası_alınan_puan.clear()
                            ulusal_docOncesı_alınan_puan.clear()
                            self.ulusal_makale_sayısı.clear()
                            self.ulusal_liste_T_F.append(True)
                            self.clear()
                        else:
                            self.ulusal_liste_T_F.clear()
                            ulusal_docSonrası_alınan_puan.clear()
                            ulusal_docOncesı_alınan_puan.clear()
                            self.ulusal_makale_sayısı.clear()
                            self.ulusal_liste_T_F.append(True)
                            break

                    except:
                        print("Bu maddenin a veya b bentlerinden puan alınmak zorunda  !!!")


                elif self.toplam_makale < 3:
                    try:
                        soru_2 = input(
                            "Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
                        if soru_2 == "e" or soru_2 == "E":
                            self.ulusal_liste_T_F.clear()
                            print(
                                "İkisi bu maddenin a bendi kapsamında olmak üzere en az üç yayın yapmak zorunludur.")
                            self.ulusal_liste_T_F.append(False)
                            break
                        else:
                            if self.ulusal_liste_T_F == [True]:

                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()
                                break

                            elif self.ulusal_liste_T_F == [False]:

                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()
                            break
                    except:
                        print("hata")
                        break


            elif ulusal_secenek == "q" or ulusal_secenek == "Q":
                break
            else:
                print("İşleminiz Gerçekleşiyor")
                time.sleep(1)
                print("Geçersiz İşlem......")
            if self.ulusal_makale_1_1 < 2:
                print("Aşamadaki zorunluluk sağlanmadığı için sonlandırılıyor....")
                time.sleep(1)
                break

    def lisanustu_Tez(self):
        time.sleep(1)
        print("""
    ╒══════════════════════════════════════════════════════════════════════════════╕
    │                    3.Lisansüstü Tezlerden Üretilmiş Yayın                    │
    ╞══════════════════════════════════════════════════════════════════════════════╡
    │ a) Uluslararası yayınevleri tarafından yayımlanmış kitap                     │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ b) Uluslararası yayınevleri tarafından yayımlanmış kitapta bölüm             │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ c) Ulusal yayınevleri tarafından yayımlanmış kitap                           │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ d) Ulusal yayınevleri tarafından yayımlanmış kitapta bölüm                   │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ e) SSCI, SCI, SCI-Expanded ve AHCI kapsamındaki dergilerde yayımlanmış       │
    │ makale                                                                       │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ f) Uluslararası alan endekslerinde taranan dergilerde yayımlanmış makale     │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ g) ULAKBİM tarafından taranan dergilerde yayımlanmış makale                  │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ p) Puan Hesapla                                                              │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ q) Çıkış Yap                                                                 │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ * Bu madde kapsamında en az 1 yayın zorunludur. Bu maddeden en fazla 10      │
    │ puanalınabilir.                                                              │
    ╘══════════════════════════════════════════════════════════════════════════════╛

            """)

        while True:
            secenek_lisans = input("Lisansüstü Tezlerden Üretilmiş Yayın Hesapla:")
            if secenek_lisans == "a" or secenek_lisans == "A":
                print("""Uluslararası yayınevleri tarafından yayımlanmış kitap:
                                1. Toplam kaç kişi                                                        
                                2. Kaç tane
                                3. Doktora Zamanı
                                4. Çıkmak İçin
                                """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ---------------------------------------------------------------------------------------------- (kişi sayısı)

                    if secenek == "1":
                        self.lisans_basvuru_1 = input("Toplam kaç kişi:")
                        try:
                            self.lisans_basvuru_1_1 = int(self.lisans_basvuru_1)
                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")

                    # ---------------------------------------------------------------------------------------------- (makale sayısı)

                    elif secenek == "2":
                        self.lisans_makale_1 = input(
                            "--> Uluslararası yayınevleri tarafından yayımlanmış kitap:")
                        try:
                            try:
                                self.lisans_makale_1_1 = int(self.lisans_makale_1)
                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")

                    # ------------------------------------------------------------------Zaman
                    elif secenek == "3":
                        try:
                            try:
                                self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                            "a)Doktora Sonrası \n"
                                                            "b)Doktora Öncesi :")

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.lisans_puan_1 = 10 / self.lisans_basvuru_1_1
                                    self.lisans_puan_2 = self.lisans_puan_1 * self.lisans_makale_1_1
                                    self.lisans_doc_sonrası.append(self.lisans_puan_2)
                                    self.makale_list.append(self.lisans_makale_1_1)

                                    break


                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.lisans_puan_1 = 10 / self.lisans_basvuru_1_1
                                    self.lisans_puan_2 = self.lisans_puan_1 * self.lisans_makale_1_1
                                    self.lisans_doc_oncesi.append(self.lisans_puan_2)
                                    self.makale_list.append(self.lisans_makale_1_1)

                                    break
                                # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa


                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Sıralamayı Bozmayın!!!")

                    elif secenek == "4":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            elif secenek_lisans == "b" or secenek_lisans == "B":
                print("""Uluslararası yayınevleri tarafından yayımlanmış kitapta bölüm:
                                1. Toplam kaç kişi                                                        
                                2. Kaç tane
                                3. Doktora Zamanı
                                4. Çıkmak İçin

                                """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------kişi sayısı
                    if secenek == "1":
                        self.lisans_basvuru_2 = input("Toplam kaç kişi:")
                        try:
                            self.lisans_basvuru_2_1 = int(self.lisans_basvuru_2)
                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------makale sayısı
                    elif secenek == "2":
                        self.lisans_makale_2 = input(
                            "--> Uluslararası yayınevleri tarafından yayımlanmış kitapta bölüm:")
                        try:
                            try:
                                self.lisans_makale_2_1 = int(self.lisans_makale_2)

                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------Zaman
                    elif secenek == "3":
                        try:
                            try:
                                self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                            "a)Doktora Sonrası \n"
                                                            "b)Doktora Öncesi :")

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.lisans_puan_3 = 8 / self.lisans_basvuru_2_1
                                    self.lisans_puan_4 = self.lisans_puan_3 * self.lisans_makale_2_1
                                    self.lisans_doc_sonrası.append(self.lisans_puan_4)
                                    self.makale_list.append(self.lisans_makale_2_1)

                                    break


                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.lisans_puan_3 = 8 / self.lisans_basvuru_2_1
                                    self.lisans_puan_4 = self.lisans_puan_3 * self.lisans_makale_2_1
                                    self.lisans_doc_oncesi.append(self.lisans_puan_4)
                                    self.makale_list.append(self.lisans_makale_2_1)

                                    break
                                # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa


                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Sıralamayı Bozmayın!!!")

                    elif secenek == "4":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            elif secenek_lisans == "c" or secenek_lisans == "C":
                print("""Ulusal yayınevleri tarafından yayımlanmış kitap:   
                                1. Toplam kaç kişi                                                        
                                2. Kaç tane
                                3. Doktora Zamanı
                                4. Çıkmak İçin
                                """)
                while True:

                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------kişi sayısı
                    if secenek == "1":
                        self.lisans_basvuru_3 = input("Toplam kaç kişi:")
                        try:
                            self.lisans_basvuru_3_1 = int(self.lisans_basvuru_3)
                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------makale sayısı
                    elif secenek == "2":
                        self.lisans_makale_3 = input(
                            "--> Ulusal yayınevleri tarafından yayımlanmış kitap:")
                        try:
                            try:
                                self.lisans_makale_3_1 = int(self.lisans_makale_3)

                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------zaman
                    elif secenek == "3":
                        try:
                            try:
                                self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                            "a)Doktora Sonrası \n"
                                                            "b)Doktora Öncesi :")

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.lisans_puan_5 = 5 / self.lisans_basvuru_3_1
                                    self.lisans_puan_6 = self.lisans_puan_5 * self.lisans_makale_3_1
                                    self.lisans_doc_sonrası.append(self.lisans_puan_6)
                                    self.makale_list.append(self.lisans_makale_3_1)

                                    break


                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.lisans_puan_5 = 5 / self.lisans_basvuru_3_1
                                    self.lisans_puan_6 = self.lisans_puan_5 * self.lisans_makale_3_1
                                    self.lisans_doc_oncesi.append(self.lisans_puan_6)
                                    self.makale_list.append(self.lisans_makale_3_1)

                                    break
                                # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa


                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Sıralamayı Bozmayın!!!")

                    elif secenek == "4":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            elif secenek_lisans == "d" or secenek_lisans == "D":
                print("""Ulusal yayınevleri tarafından yayımlanmış kitapta bölüm:  
                                1. Toplam kaç kişi                                                        
                                2. Kaç tane
                                3. Doktora Zamanı
                                4. Çıkmak İçin
                                """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------kişi sayısı
                    if secenek == "1":
                        self.lisans_basvuru_4 = input("Toplam kaç kişi:")
                        try:
                            self.lisans_basvuru_4_1 = int(self.lisans_basvuru_4)
                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------makale sayısı
                    elif secenek == "2":
                        self.lisans_makale_4 = input(
                            "--> Ulusal yayınevleri tarafından yayımlanmış kitapta bölüm:")
                        try:
                            try:
                                self.lisans_makale_4_1 = int(self.lisans_makale_4)

                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------zaman
                    elif secenek == "3":
                        try:
                            try:
                                self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                            "a)Doktora Sonrası \n"
                                                            "b)Doktora Öncesi :")

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.lisans_puan_7 = 4 / self.lisans_basvuru_4_1
                                    self.lisans_puan_8 = self.lisans_puan_7 * self.lisans_makale_4_1
                                    self.lisans_doc_sonrası.append(self.lisans_puan_8)
                                    self.makale_list.append(self.lisans_makale_4)

                                    break


                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.lisans_puan_7 = 4 / self.lisans_basvuru_4_1
                                    self.lisans_puan_8 = self.lisans_puan_7 * self.lisans_makale_4_1
                                    self.lisans_doc_oncesi.append(self.lisans_puan_8)
                                    self.makale_list.append(self.lisans_makale_4)

                                    break
                                # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa


                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Sıralamayı Bozmayın!!!")

                    elif secenek == "4":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            elif secenek_lisans == "e" or secenek_lisans == "E":
                print("""SSCI, SCI, SCI-Expanded ve AHCI kapsamındaki dergilerde yayımlanmış makale:
                                1. Toplam kaç kişi                                                        
                                2. Kaç tane
                                3. Doktora Zamanı
                                4. Çıkmak İçin
                               """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------kişi sayısı
                    if secenek == "1":
                        self.lisans_basvuru_5 = input("Toplam kaç kişi:")
                        try:
                            self.lisans_basvuru_5_1 = int(self.lisans_basvuru_5)
                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------makale sayısı
                    elif secenek == "2":
                        self.lisans_makale_5 = input(
                            "--> SSCI, SCI, SCI-Expanded ve AHCI kapsamındaki dergilerde yayımlanmış makale:")

                        try:
                            try:
                                self.lisans_makale_5_1 = int(self.lisans_makale_5)

                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------zaman
                    elif secenek == "3":
                        try:
                            try:
                                self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                            "a)Doktora Sonrası \n"
                                                            "b)Doktora Öncesi :")

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.lisans_puan_9 = 8 / self.lisans_basvuru_5_1
                                    self.lisans_puan_10 = self.lisans_puan_9 * self.lisans_makale_5_1
                                    self.lisans_doc_sonrası.append(self.lisans_puan_10)
                                    self.makale_list.append(self.lisans_makale_5_1)

                                    break


                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.lisans_puan_9 = 8 / self.lisans_basvuru_5_1
                                    self.lisans_puan_10 = self.lisans_puan_9 * self.lisans_makale_5_1
                                    self.lisans_doc_oncesi.append(self.lisans_puan_10)
                                    self.makale_list.append(self.lisans_makale_5_1)

                                    break
                                # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa


                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Sıralamayı Bozmayın!!!")

                    elif secenek == "4":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            elif secenek_lisans == "f" or secenek_lisans == "F":
                print("""Uluslararası alan endekslerinde taranan dergilerde yayımlanmış makale:
                                1. Toplam kaç kişi                                                        
                                2. Kaç tane
                                3. Doktora Zamanı
                                4. Çıkmak İçin
                               """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------kişi sayısı
                    if secenek == "1":
                        self.lisans_basvuru_6 = input("Toplam kaç kişi:")
                        try:
                            self.lisans_basvuru_6_1 = int(self.lisans_basvuru_6)
                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------makale sayısı
                    elif secenek == "2":
                        self.lisans_makale_6 = input(
                            "--> Uluslararası alan endekslerinde taranan dergilerde yayımlanmış makale:")
                        try:
                            try:
                                self.lisans_makale_6_1 = int(self.lisans_makale_6)

                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------zaman
                    elif secenek == "3":
                        try:
                            try:
                                self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                            "a)Doktora Sonrası \n"
                                                            "b)Doktora Öncesi :")

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.lisans_puan_11 = 6 / self.lisans_basvuru_6_1
                                    self.lisans_puan_12 = self.lisans_puan_11 * self.lisans_makale_6_1
                                    self.lisans_doc_sonrası.append(self.lisans_puan_12)
                                    self.makale_list.append(self.lisans_makale_6_1)

                                    break


                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.lisans_puan_11 = 6 / self.lisans_basvuru_6_1
                                    self.lisans_puan_12 = self.lisans_puan_11 * self.lisans_makale_6_1
                                    self.lisans_doc_oncesi.append(self.lisans_puan_12)
                                    self.makale_list.append(self.lisans_makale_6_1)

                                    break
                                # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa


                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Sıralamayı Bozmayın!!!")

                    elif secenek == "4":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            elif secenek_lisans == "g" or secenek_lisans == "G":
                print("""ULAKBİM tarafından taranan dergilerde yayımlanmış makale:
                                1. Toplam kaç kişi                                                        
                                2. Kaç tane
                                3. Doktora Zamanı
                                4. Çıkmak İçin
                               """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------kişi sayısı
                    if secenek == "1":
                        self.lisans_basvuru_7 = input("Toplam kaç kişi:")
                        try:
                            self.lisans_basvuru_7_1 = int(self.lisans_basvuru_7)
                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------makale sayısı
                    elif secenek == "2":
                        self.lisans_makale_7 = input(
                            "--> ULAKBİM tarafından taranan dergilerde yayımlanmış makale")
                        try:
                            try:
                                self.lisans_makale_7_1 = int(self.lisans_makale_7)

                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # -----------------------------------------------------------------Zaman
                    elif secenek == "3":
                        try:
                            try:
                                self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                            "a)Doktora Sonrası \n"
                                                            "b)Doktora Öncesi :")

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.lisans_puan_13 = 4 / self.lisans_basvuru_7_1
                                    self.lisans_puan_14 = self.lisans_puan_13 * self.lisans_makale_7_1
                                    self.lisans_doc_sonrası.append(self.lisans_puan_14)
                                    self.makale_list.append(self.lisans_makale_7_1)

                                    break


                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.lisans_puan_13 = 4 / self.lisans_basvuru_7_1
                                    self.lisans_puan_14 = self.lisans_puan_13 * self.lisans_makale_7_1
                                    self.lisans_doc_oncesi.append(self.lisans_puan_14)
                                    self.makale_list.append(self.lisans_makale_7_1)

                                    break
                                # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa


                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Sıralamayı Bozmayın!!!")

                    elif secenek == "4":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")


            # ------------------------------------------------------------------ toplama işlemi
            elif secenek_lisans == "p" or secenek_lisans == "P":

                lisansustu_makale_sayısı = self.makale_list
                toplam_makale = sum(lisansustu_makale_sayısı)

                if toplam_makale > 0:
                    try:
                        if toplam_makale >= 1:
                            print("Bu madde kapsamında en az 1 yayın zorunluluğu geçildi:", toplam_makale)
                            lisansustu_docSonrası_alınan_puan = self.lisans_doc_sonrası
                            lisansustu_docSonrası_toplam_puan = sum(lisansustu_docSonrası_alınan_puan)
                            # -------------------------------------------
                            lisansustu_docOncesi_alınan_puan = self.lisans_doc_oncesi
                            lisansustu_docOncesi_toplam_puan = sum(lisansustu_docOncesi_alınan_puan)

                            if lisansustu_docSonrası_toplam_puan > 10:
                                print("Bu maddeden en fazla 10 puan alınabilir ")
                                self.doktora_sonrası.append(10)
                                time.sleep(1)
                            elif lisansustu_docSonrası_toplam_puan == 1 or lisansustu_docSonrası_toplam_puan <= 10:
                                self.doktora_sonrası.append(lisansustu_docSonrası_toplam_puan)
                                time.sleep(1)
                            # -----------------------------------------------------------------
                            if lisansustu_docOncesi_toplam_puan > 10:
                                print("Bu maddeden en fazla 10 puan alınabilir ")
                                self.doktora_oncesi.append(10)
                                time.sleep(1)
                            elif lisansustu_docOncesi_toplam_puan > 0 or lisansustu_docOncesi_toplam_puan <= 10:
                                self.doktora_oncesi.append(lisansustu_docOncesi_toplam_puan)
                                time.sleep(1)

                            self.doktora_sonrası_puan()
                            self.doktora_oncesi_puan()

                            soru = input("sistem yenılensın mı (E,H): ")
                            if soru == "e" or soru == "E":
                                self.lisans_liste_T_F.clear()
                                lisansustu_docSonrası_alınan_puan.clear()
                                lisansustu_docOncesi_alınan_puan.clear()
                                lisansustu_makale_sayısı.clear()  # burada duruma gore degerlendırebılır ıstenırse yenı
                                # kayıt veya ustune ekleme yapılır tercıh duruma gore
                                self.lisans_liste_T_F(
                                    True)  # ilerde yapılacak gelıstırmelerde goz onune alınacaktır.
                                self.clear()
                            else:
                                self.lisans_liste_T_F.clear()
                                lisansustu_docSonrası_alınan_puan.clear()
                                lisansustu_docOncesi_alınan_puan.clear()
                                lisansustu_makale_sayısı.clear()
                                self.lisans_liste_T_F(True)
                                break
                    except:
                        time.sleep(1)

                elif toplam_makale == 0:
                    try:
                        soru_2 = input(
                            "Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
                        if soru_2 == "e" or soru_2 == "E":
                            self.ulusal_liste_T_F.clear()
                            print(
                                "Bu madde kapsamında en az 1 yayın zorunluluğu geçilmedi:", toplam_makale)
                            self.ulusal_liste_T_F.append(False)
                            break
                        else:
                            if self.ulusal_liste_T_F == [True]:
                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()
                                break

                            elif self.ulusal_liste_T_F == [False]:

                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()
                                break
                    except:
                        print("hata")
                        break

            elif secenek_lisans == "q" or secenek_lisans == "Q":
                break
            else:
                print("İşleminiz Gerçekleşiyor")
                time.sleep(1)
                print("Geçersiz İşlem......")

    def kitap(self):
        time.sleep(1)
        print("""

    ╒══════════════════════════════════════════════════════════════════════════════╕
    │                                   4. Kitap                                   │
    ╞══════════════════════════════════════════════════════════════════════════════╡
    │  ** Adayın hazırladığı lisansüstü tezlerinden üretilmemiş ve başvurulan      │
    │               doçentlik bilim alanı ile ilgili olmak kaydıyla **             │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ a) Uluslararası yayınevleri tarafından yayımlanmış kitap                     │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ b) Uluslararası yayınevleri tarafından yayımlanmış kitap editörlüğü veya     │
    │ bölüm yazarlığı                                                              │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ c) Ulusal yayınevleri tarafından yayımlanmış kitap                           │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ d) Ulusal yayınevleri tarafından yayımlanmış kitap editörlüğü veya bölüm     │
    │ yazarlığı                                                                    │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ p) Puan Hesapla                                                              │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ q) Çıkış Yap                                                                 │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ ** Bu madde kapsamında sadece ders kitabı niteliği dışındaki özgün bilimsel  │
    │ kitaplar puanlanabilir, aynı kitaptaki bölümlerden en fazla ikisi dikkate    │
    │ alınır. Alana özgü ansiklopedi maddelerinin üç veya daha çok maddesi bir     │
    │ kitap bölümü kabul edilir. **                                                │
    ╘══════════════════════════════════════════════════════════════════════════════╛
            """)

        while True:

            secenek_kitap = input(
                "-->Adayın hazırladığı lisansüstü tezlerinden üretilmemiş ve başvurulan\ndoçentlik bilim alanı ile ilgili olmak kaydıyla:")

            # ------------------------------------------------------------------------------------(A seceneği)-------------------------------------------------------------
            if secenek_kitap == "a" or secenek_kitap == "A":
                print("""Uluslararası yayınevleri tarafından yayımlanmış kitap : 
                                1. Toplam kaç kişi                                                        
                                2. Kaç tane
                                3. Doktora Zamanı
                                4. Çıkmak İçin

                                                """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    if secenek == "1":
                        self.kitap_basvuru_1 = input("Toplam kaç kişi:")
                        try:
                            self.kitap_basvuru_1_1 = int(self.kitap_basvuru_1)
                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")


                    elif secenek == "2":
                        self.kitap_makale_1 = input(
                            "--> Uluslararası yayınevleri tarafından yayımlanmış kitap:")
                        try:
                            try:
                                self.kitap_makale_1_1 = int(self.kitap_makale_1)
                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                            # ------------------------------------------------------------------Zaman
                    elif secenek == "3":
                        try:
                            try:
                                self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                            "a)Doktora Sonrası \n"
                                                            "b)Doktora Öncesi :")

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.kitap_puan_1 = 20 / self.kitap_basvuru_1_1
                                    self.kitap_puan_2 = self.kitap_puan_1 * self.kitap_makale_1_1
                                    self.kitap_doc_sonrası.append(self.kitap_puan_2)
                                    break


                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.kitap_puan_1 = 20 / self.kitap_basvuru_1_1
                                    self.kitap_puan_2 = self.kitap_puan_1 * self.kitap_makale_1_1
                                    self.kitap_doc_oncesi.append(self.kitap_puan_2)
                                    break
                                # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa


                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Sıralamayı Bozmayın!!!")

                    elif secenek == "4":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")
            # ------------------------------------------------------------------------------------(B seceneği)-------------------------------------------------------------
            elif secenek_kitap == "b" or secenek_kitap == "B":
                print("""Uluslararası yayınevleri tarafından yayımlanmış kitap editörlüğü veya bölüm yazarlığı: 
                                1. Toplam kaç kişi                                                        
                                2. Kaç tane
                                3. Doktora Zamanı
                                4. Çıkmak İçin
                                                """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # -------------------------------------------------------------------------(kişi sayısı)
                    if secenek == "1":
                        self.kitap_basvuru_2 = int(input("Toplam kaç kişi:"))
                        try:
                            self.kitap_basvuru_2_1 = int(self.kitap_basvuru_2)

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # -------------------------------------------------------------------------(makale sayısı)
                    elif secenek == "2":
                        self.kitap_makale_2 = int(input(
                            "--> Uluslararası yayınevleri tarafından yayımlanmış kitap:"))
                        try:
                            try:
                                self.kitap_makale_2_1 = int(self.kitap_makale_2)
                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # -------------------------------------------------------------------------(zaman)
                    elif secenek == "3":
                        try:
                            try:
                                self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                            "a)Doktora Sonrası \n"
                                                            "b)Doktora Öncesi :")

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.kitap_puan_3 = 10 / self.kitap_basvuru_2_1
                                    self.kitap_puan_4 = self.kitap_puan_3 * self.kitap_makale_2_1
                                    self.kitap_doc_sonrası.append(self.kitap_puan_4)
                                    break


                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.kitap_puan_3 = 10 / self.kitap_basvuru_2_1
                                    self.kitap_puan_4 = self.kitap_puan_3 * self.kitap_makale_2_1
                                    self.kitap_doc_oncesi.append(self.kitap_puan_4)
                                    break
                                # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa


                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Sıralamayı Bozmayın!!!")

                    elif secenek == "4":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")
            # ------------------------------------------------------------------------------------(C seceneği)-------------------------------------------------------------

            elif secenek_kitap == "c" or secenek_kitap == "C":
                print("""Uluslararası yayınevleri tarafından yayımlanmış kitap editörlüğü veya bölüm yazarlığı: 
                                1. Toplam kaç kişi                                                        
                                2. Kaç tane
                                3. Doktora Zamanı
                                4. Çıkmak İçin
                                                """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # -------------------------------------------------------------------------(kişi sayısı)

                    if secenek == "1":
                        self.kitap_basvuru_3 = int(input("Toplam kaç kişi:"))
                        try:
                            self.kitap_basvuru_3_1 = int(self.kitap_basvuru_3)

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")

                    # -------------------------------------------------------------------------(makale sayısı)
                    elif secenek == "2":
                        self.kitap_makale_3 = int(input(
                            "--> Ulusal yayınevleri tarafından yayımlanmış kitap :"))
                        try:
                            try:
                                self.kitap_makale_3_1 = int(self.kitap_makale_3)
                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # -------------------------------------------------------------------------(zaman)
                    elif secenek == "3":
                        try:
                            try:
                                self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                            "a)Doktora Sonrası \n"
                                                            "b)Doktora Öncesi :")

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.kitap_puan_5 = 15 / self.kitap_basvuru_3_1
                                    self.kitap_puan_6 = self.kitap_puan_5 * self.kitap_makale_3_1
                                    self.kitap_doc_sonrası.append(self.kitap_puan_6)
                                    break


                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.kitap_puan_5 = 15 / self.kitap_basvuru_3_1
                                    self.kitap_puan_6 = self.kitap_puan_5 * self.kitap_makale_3_1
                                    self.kitap_doc_oncesi.append(self.kitap_puan_6)
                                    break
                                # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa


                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Sıralamayı Bozmayın!!!")

                    elif secenek == "4":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")
            # ------------------------------------------------------------------------------------(D seceneği)-------------------------------------------------------------
            elif secenek_kitap == "d" or secenek_kitap == "D":
                print("""Ulusal yayınevleri tarafından yayımlanmış kitap editörlüğü veya bölüm yazarlığı: 
                                1. Toplam kaç kişi                                                        
                                2. Kaç tane
                                3. Doktora Zamanı
                                4. Çıkmak İçin
                                                           """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    if secenek == "1":
                        self.kitap_basvuru_4 = int(input("Toplam kaç kişi:"))
                        try:
                            self.kitap_basvuru_4_1 = int(self.kitap_basvuru_4)

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")

                    elif secenek == "2":
                        self.kitap_makale_4 = int(input(
                            "--> Ulusal yayınevleri tarafından yayımlanmış kitap editörlüğü veya bölüm yazarlığı:"))
                        try:
                            try:
                                self.kitap_makale_4_1 = int(self.kitap_makale_4)
                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")

                    elif secenek == "3":
                        try:
                            try:
                                self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                            "a)Doktora Sonrası \n"
                                                            "b)Doktora Öncesi :")

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.kitap_puan_7 = 15 / self.kitap_basvuru_4_1
                                    self.kitap_puan_8 = self.kitap_puan_7 * self.kitap_makale_4_1
                                    self.kitap_doc_sonrası.append(self.kitap_puan_8)
                                    break


                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.kitap_puan_7 = 15 / self.kitap_basvuru_4_1
                                    self.kitap_puan_8 = self.kitap_puan_7 * self.kitap_makale_4_1
                                    self.kitap_doc_oncesi.append(self.kitap_puan_8)
                                    break
                                # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa


                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Sıralamayı Bozmayın!!!")

                    elif secenek == "4":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")
            # ------------------------------------------------------------------------------------(Puan Hesapla)-------------------------------------------------------------
            elif secenek_kitap == "p" or secenek_kitap == "P":

                kitap_docSonrası_alınan_puan = self.kitap_doc_sonrası
                kitap_doc_sonrası_toplam = sum(kitap_docSonrası_alınan_puan)

                # -------------------------------------------

                kitap_docOncesı_alınan_puan = self.kitap_doc_oncesi
                kitap_doc_oncesi_toplam = sum(kitap_docOncesı_alınan_puan)

                if kitap_doc_sonrası_toplam + kitap_doc_oncesi_toplam > 0:
                    try:
                        if kitap_doc_oncesi_toplam + kitap_doc_sonrası_toplam > 0:
                            self.doktora_sonrası.append(kitap_doc_sonrası_toplam)
                            self.doktora_oncesi.append(kitap_doc_oncesi_toplam)
                            time.sleep(1)
                        print("Genel Puanınız Toplanıyor")
                        self.doktora_sonrası_puan()
                        self.doktora_oncesi_puan()

                        soru = input("sistem yenılensın mı (E,H): ")
                        if soru == "e" or soru == "E":
                            self.kitap_liste_T_F.clear()
                            kitap_docSonrası_alınan_puan.clear()
                            kitap_docOncesı_alınan_puan.clear()
                            self.kitap_liste_T_F.append(True)
                            self.clear()
                        else:
                            self.kitap_liste_T_F.clear()
                            kitap_docSonrası_alınan_puan.clear()
                            kitap_docOncesı_alınan_puan.clear()
                            self.kitap_liste_T_F.append(True)
                            break
                    except:
                        print("Bu maddenin a veya b bentlerinden puan alınmak zorunda !!!")

                elif kitap_doc_sonrası_toplam + kitap_doc_oncesi_toplam == 0:

                    try:
                        soru_2 = input(
                            "Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
                        if soru_2 == "e" or soru_2 == "E":
                            self.kitap_liste_T_F.clear()
                            print("Lütfen veri giriniz !!!!!!")
                            break
                        else:
                            if self.kitap_liste_T_F == [True]:
                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()
                                break
                    except:
                        print("hata .......")

            elif secenek_kitap == "q" or secenek_kitap == "Q":
                break

            else:
                print("İşleminiz Gerçekleşiyor")
                time.sleep(1)
                print("Geçersiz İşlem......")

    def atıflar(self):

        time.sleep(1)
        print("""
    ╒══════════════════════════════════════════════════════════════════════════════╕
    │                                   5. Atıflar                                 │
    ╞══════════════════════════════════════════════════════════════════════════════╡
    │ a)SCI, SCI-Expanded, SSCI ve AHCI tarafından taranan dergilerde;             │
    │ Uluslararası yayınevleri tarafından yayımlanmış kitaplarda yayımlanan ve     │
    │ adayın yazar olarak yer almadığı yayınlardan her birinde, metin içindeki     │
    │ atıf sayısına bakılmaksızın adayın atıf yapılan her eseri sayısı             │ 
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ b) SCI, SCI-Expanded, SSCI ve AHCI dışındaki endeksler tarafından taranan    │
    │ dergilerde; Uluslararası yayınevleri tarafından yayımlanmış kitaplarda       │
    │ bölüm yazarı olarak yayımlanan ve adayın yazar olarak yer almadığı           │
    │ yayınlardan her birinde, metin içindeki atıf sayısına bakılmaksızın adayın   │
    │ atıf yapılan her eseri sayısı                                                │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ c) Ulusal hakemli dergilerde; Ulusal yayınevleri tarafından yayımlanmış      │
    │ kitaplarda yayımlanan ve adayın yazar olarak yer almadığı yayınlardan her    │
    │ birinde, metin içindeki atıf sayısına bakılmaksızın adayın atıf yapılan her  │
    │ eseri sayısı                                                                 │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ p) Puan Hesapla                                                              │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ q) Çıkış Yap                                                                 │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ * Bu madde kapsamında en az 4 puan alınması zorunludur.Bu madde kapsamında   │
    │   en fazla 20 puan alınabilir                                                │
    ╘══════════════════════════════════════════════════════════════════════════════╛
            """)

        while True:
            atıflar = input("Atıfları Hesapla :")
            if atıflar == "a" or atıflar == "A":
                print("""--> SCI, SCI-Expanded, SSCI ve AHCI tarafından taranan dergilerde; uluslararası yayınevleri\ntarafından yayımlanmış kitaplarda yayımlanan ve adayın yazar olarak yer almadığı yayınlardan her\nbirinde,metin içindeki atıf sayısına bakılmaksızın adayın atıf yapılan eser sayısı: 
                                        1.Kaç tane
                                        2.Doktora Zamanı
                                        3.Çıkmak İçin
                    """)

                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------kişi sayısı
                    if secenek == "1":

                        self.atıflar_1 = input(
                            "--> SCI, SCI-Expanded, SSCI ve AHCI tarafından taranan dergilerde; uluslararası yayınevleritarafından\nyayımlanmış kitaplarda yayımlanan ve adayın yazar olarak yer almadığı yayınlardan her birinde\nmetin içindeki atıf sayısına bakılmaksızın adayın atıf yapılan eser sayısı: ")

                        try:

                            try:

                                self.atıflar_1_1 = int(self.atıflar_1)


                            except AttributeError:

                                print("Önce Atıflar Girilmeli!!!")

                        except ValueError:

                            print("Bir sayı girmelisiniz!!!")



                    # ------------------------------------------------------------------ makale sayısı
                    elif secenek == "2":
                        self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                    "a)Doktora Sonrası \n"
                                                    "b)Doktora Öncesi :")
                        try:
                            try:
                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.atıflar_puan_1 = 3 * self.atıflar_1_1
                                    self.atıflar_doc_sonrası.append(self.atıflar_puan_1)
                                    break
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.atıflar_puan_1 = 3 * self.atıflar_1_1
                                    self.atıflar_doc_oncesi.append(self.atıflar_puan_1)
                                    break
                                else:
                                    print("İşleminiz Gerçekleşiyor")
                                    time.sleep(1)
                                    print("Geçersiz İşlem......")
                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Önce Atıflar  Girilmeli!!!")



                    elif secenek == "3":
                        break


            elif atıflar == "b" or atıflar == "B":
                print("""--> SCI, SCI-Expanded, SSCI ve AHCI dışındaki endeksler tarafından taranan\ndergilerde; Uluslararası yayınevleri tarafından yayımlanmış kitaplarda\nbölüm yazarı olarak yayımlanan ve adayın yazar olarak yer almadığı\nyayınlardan her birinde, metin içindeki atıf sayısına bakılmaksızın adayın\natıf yapılan her eseri sayısı :
                                 1.Kaç tane
                                 2.Doktora Zamanı
                                 3.Çıkmak İçin
                        """)

                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------Atıf sayısı
                    if secenek == "1":

                        self.atıflar_2 = input(
                            "--> SCI, SCI-Expanded, SSCI ve AHCI dışındaki endeksler tarafından taranan dergilerde; Uluslararası\nyayınevleri tarafından yayımlanmış kitaplarda bölüm yazarı olarak yayımlanan ve adayın yazarolarak\nyer almadığı yayınlardan her birinde, metin içindeki atıf sayısına bakılmaksızın\nadayın atıf yapılan her eseri sayısı: ")

                        try:

                            try:

                                self.atıflar_2_1 = int(self.atıflar_2)


                            except AttributeError:

                                print("Önce Atıflar Girilmeli!!!")

                        except ValueError:

                            print("Bir sayı girmelisiniz!!!")



                    # ------------------------------------------------------------------ Doktora zamanı
                    elif secenek == "2":
                        self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                    "a)Doktora Sonrası \n"
                                                    "b)Doktora Öncesi :")
                        try:
                            try:
                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.atıflar_puan_2 = 2 * self.atıflar_2_1
                                    self.atıflar_doc_sonrası.append(self.atıflar_puan_2)
                                    break
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.atıflar_puan_2 = 2 * self.atıflar_2_1
                                    self.atıflar_doc_oncesi.append(self.atıflar_puan_2)
                                    break
                                else:
                                    print("İşleminiz Gerçekleşiyor")
                                    time.sleep(1)
                                    print("Geçersiz İşlem......")
                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Önce Atıflar  Girilmeli!!!")



                    elif secenek == "3":
                        break

            elif atıflar == "c" or atıflar == "C":
                print("""--> Ulusal hakemli dergilerde; Ulusal yayınevleri tarafından yayımlanmış kitaplarda yayımlanan \nve adayın yazar olarak yer almadığı yayınlardan her birinde, metin içindeki atıf sayısına\nbakılmaksızın adayın atıf yapılan her eseri sayısı:
                                                1.Kaç tane
                                                2.Doktora Zamanı
                                                3.Çıkmak İçin
                            """)

                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------Atıf sayısı
                    if secenek == "1":

                        self.atıflar_3 = input(
                            "--> Ulusal hakemli dergilerde; Ulusal yayınevleri tarafından yayımlanmış kitaplarda\nyayımlanan ve adayın yazar olarak yer almadığı yayınlardan her birinde, metin içindeki atıf\nsayısına bakılmaksızın adayın atıf yapılan her eseri sayısı:")

                        try:

                            try:

                                self.atıflar_3_1 = int(self.atıflar_3)


                            except AttributeError:

                                print("Önce Atıflar Girilmeli!!!")

                        except ValueError:

                            print("Bir sayı girmelisiniz!!!")



                    # ------------------------------------------------------------------ Doktora zamanı
                    elif secenek == "2":
                        self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                    "a)Doktora Sonrası \n"
                                                    "b)Doktora Öncesi :")
                        try:
                            try:
                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":

                                    self.atıflar_puan_3 = 1 * self.atıflar_3_1
                                    self.atıflar_doc_sonrası.append(self.atıflar_puan_3)

                                    break

                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":

                                    self.atıflar_puan_3 = 1 * self.atıflar_3_1
                                    self.atıflar_doc_oncesi.append(self.atıflar_puan_3)

                                    break
                                else:
                                    print("İşleminiz Gerçekleşiyor")
                                    time.sleep(1)
                                    print("Geçersiz İşlem......")
                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Önce Atıflar  Girilmeli!!!")



                    elif secenek == "3":
                        break

            elif atıflar == "p" or atıflar == "P":

                atıflar_doc_sonrası_alınan_puan = self.atıflar_doc_sonrası
                atıflar_doc_sonrası_toplam = sum(atıflar_doc_sonrası_alınan_puan)

                # -------------------------------------------

                atıflar_doc_oncesialınan_puan = self.atıflar_doc_oncesi
                atıflar_doc_oncesi_toplam = sum(atıflar_doc_oncesialınan_puan)

                if atıflar_doc_sonrası_toplam + atıflar_doc_oncesi_toplam > 4:
                    try:
                        if atıflar_doc_sonrası_toplam > 20:
                            print("Bu maddeden en fazla 20 puan alınabilir ")
                            self.doktora_sonrası.append(20)
                        elif atıflar_doc_sonrası_toplam > 4 or atıflar_doc_sonrası_toplam <= 20:
                            self.doktora_sonrası.append(atıflar_doc_sonrası_toplam)
                        # -----------------------------------------------------------------
                        if atıflar_doc_oncesi_toplam > 20:
                            print("Bu maddeden en fazla 20 puan alınabilir ")
                            self.doktora_oncesi.append(20)
                        elif atıflar_doc_oncesi_toplam > 4 or atıflar_doc_oncesi_toplam <= 20:
                            self.doktora_oncesi.append(atıflar_doc_oncesi_toplam)

                        self.doktora_sonrası_puan()
                        self.doktora_oncesi_puan()
                        soru = input("sistem yenılensın mı (E,H): ")
                        if soru == "e" or soru == "E":
                            self.atıflar_liste_T_F.clear()
                            atıflar_doc_sonrası_alınan_puan.clear()
                            atıflar_doc_oncesialınan_puan.clear()
                            self.atıflar_liste_T_F.append(True)

                            self.clear()
                        else:
                            self.atıflar_liste_T_F.clear()
                            atıflar_doc_sonrası_alınan_puan.clear()
                            atıflar_doc_oncesialınan_puan.clear()
                            self.atıflar_liste_T_F.append(True)
                            break
                    except:
                        time.sleep(1)
                elif atıflar_doc_sonrası_toplam + atıflar_doc_oncesi_toplam < 4:
                    try:
                        soru_2 = input(
                            "Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
                        if soru_2 == "e" or soru_2 == "E":
                            self.atıflar_liste_T_F.clear()
                            print("Bu madde kapsamında en az 4 puan alınma aşaması geçilmedi.")
                            self.atıflar_liste_T_F.append(False)
                            break
                        else:
                            if self.atıflar_liste_T_F == [True]:
                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()
                                break

                            elif self.atıflar_liste_T_F == [False]:

                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()
                                break
                    except:
                        print("hata")
            elif atıflar == "q" or atıflar == "Q":
                break
            else:
                print("İşleminiz Gerçekleşiyor")
                time.sleep(1)
                print("Geçersiz İşlem......")

    def Lısansustu_Tez_Danışmanlığı(self):

        time.sleep(1)
        print("""
    ╒══════════════════════════════════════════════════════════════════════════════╕
    │                      6. Lisansüstü Tez Danışmanlığı                          │
    ╞══════════════════════════════════════════════════════════════════════════════╡
    │ Adayın danışmanlığını yürüttüğü tamamlanan lisansüstü tezlerden              │ 
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ a) Doktora tez danışmanlığı                                                  │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ b) Yüksek lisans tez danışmanlığı                                            │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ c) Doktora (eş danışmanlık)                                                  │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ d) Yüksek Lisans (eş danışmanlık)                                            │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ p) Puan Hesapla                                                              │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ q) Çıkış Yap                                                                 │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ * Bu madde kapsamında en fazla 10 puan alınabilir. İkinci/eş danışman olması │
    │ durumunda asıl danışman a ve b bentleri için öngörülen puanların tamamını,   │
    │ ikinci danışman ise yarısını alır                                            │
    ╘══════════════════════════════════════════════════════════════════════════════╛
            """)

        while True:

            Lisansüstü_Tez = input("Lisansüstü Tez Danışmanlığı Hesapla :")
            # -------------------------------------------------------------------------A SECENEGİ

            if Lisansüstü_Tez == "a" or Lisansüstü_Tez == "A":
                print("""--> Doktora tez danışmanlığı :
                                            1.Kaç tane
                                            2.Çıkmak İçin
                            """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------Kaç tane
                    if secenek == "1":

                        Lisansüstü_Tez_sayısı_1 = input("Toplam kaç tane :")
                        try:
                            Lisansüstü_Tez_sayısı_1_1 = int(Lisansüstü_Tez_sayısı_1)
                            self.Lisansüstü_Tez_puan_1 = Lisansüstü_Tez_sayısı_1_1 * 4

                            self.lisansüstü_Tez_tp_puan.append(self.Lisansüstü_Tez_puan_1)
                            break
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")


                    elif secenek == "2":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")




            #  --------------------------------------------------------------------------------B SECENEGİ
            elif Lisansüstü_Tez == "b" or Lisansüstü_Tez == "B":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> Yüksek lisans tez danışmanlığı:                                
                                           1.Kaç tane
                                           2.Çıkmak İçin
                                   """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------kişi sayısı
                    if secenek == "1":
                        Lisansüstü_Tez_sayısı_2 = input("Toplam kaç tane:")
                        try:
                            self.Lisansüstü_Tez_sayısı_2_1 = int(Lisansüstü_Tez_sayısı_2)
                            self.Lisansüstü_Tez_puan_2 = self.Lisansüstü_Tez_sayısı_2_1 * 2

                            self.lisansüstü_Tez_tp_puan.append(self.Lisansüstü_Tez_sayısı_2)

                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------ makale sayısı

                    elif secenek == "2":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            #  ------------------------------------------------------------------C SECENEGİ

            elif Lisansüstü_Tez == "c" or Lisansüstü_Tez == "C":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> Doktora (eş danışmanlık) :

                                            1.Kaç tane
                                            2.Çıkmak İçin

                                                   """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ---------------------------------------------------------------------------------------------- (kişi sayısı)
                    if secenek == "1":
                        Lisansüstü_Tez_sayısı_3 = input("Toplam kaç tane:")
                        try:
                            Lisansüstü_Tez_sayısı_3_1 = int(Lisansüstü_Tez_sayısı_3)
                            self.lisansüstü_Tez_puan = Lisansüstü_Tez_sayısı_3_1 * 2

                            self.lisansüstü_Tez_tp_puan.append(self.Lisansüstü_Tez_puan_3)

                            continue
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")


                    elif secenek == "2":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            elif Lisansüstü_Tez == "d" or Lisansüstü_Tez == "D":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> Yüksek Lisans (eş danışmanlık) :

                                            1.Kaç tane
                                            2.Çıkmak İçin

                                                   """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ---------------------------------------------------------------------------------------------- (kişi sayısı)
                    if secenek == "1":
                        Lisansüstü_Tez_sayısı_4 = input("Toplam kaç tane:")
                        try:
                            self.Lisansüstü_Tez_sayısı_4_1 = int(Lisansüstü_Tez_sayısı_4)
                            self.Lisansüstü_Tez_puan_4 = self.Lisansüstü_Tez_sayısı_4_1 * 1

                            self.lisansüstü_Tez_tp_puan.append(self.Lisansüstü_Tez_puan_4)

                            continue
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")


                    elif secenek == "2":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")


            # ------------------------------------------------------------------ toplama işlemi
            elif Lisansüstü_Tez == "p" or Lisansüstü_Tez == "P":

                lisansüstü_Tez_puanı = self.lisansüstü_Tez_tp_puan
                lisansüstü_Tez_toplam_puan = sum(lisansüstü_Tez_puanı)

                if lisansüstü_Tez_toplam_puan > 0:
                    try:
                        if lisansüstü_Tez_toplam_puan > 10:
                            print("Bu maddeden en fazla 10 puan alınabilir ")
                            self.doktora_sonrası.append(10)
                        elif lisansüstü_Tez_toplam_puan < 10:
                            self.doktora_sonrası.append(lisansüstü_Tez_toplam_puan)
                        self.doktora_sonrası_puan()
                        self.doktora_oncesi_puan()

                        soru = input("sistem yenılensın mı (E,H): ")
                        if soru == "e" or soru == "E":
                            self.lisansüstü_Tez_T_F.clear()
                            lisansüstü_Tez_puanı.clear()
                            self.lisansüstü_Tez_T_F.append(True)
                            self.clear()
                        else:
                            self.lisansüstü_Tez_T_F.clear()
                            lisansüstü_Tez_puanı.clear()
                            self.lisansüstü_Tez_T_F.append(True)
                            break


                    except:
                        time.sleep(1)

                elif lisansüstü_Tez_toplam_puan == 0:
                    try:
                        soru_2 = input(
                            "Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
                        if soru_2 == "e" or soru_2 == "E":
                            self.uluslararası_liste_T_F.clear()
                            print("Lütfen veri giriniz...")
                            break
                        else:
                            if self.uluslararası_liste_T_F == [True]:
                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()
                                break

                    except:
                        print("hata")
                        break

            elif Lisansüstü_Tez == "q" or Lisansüstü_Tez == "Q":
                break
            else:
                print("İşleminiz Gerçekleşiyor")
                time.sleep(1)
                print("Geçersiz İşlem......")

    def Bilimsel_Araştırma_Projesi(self):
        time.sleep(1)
        print("""
    ╒══════════════════════════════════════════════════════════════════════════════╕
    │                     7. Bilimsel Araştırma Projesi                            │
    ╞══════════════════════════════════════════════════════════════════════════════╡
    │ a) Devam eden veya başarı ile tamamlanmış AB Çerçeve Programı Bilimsel       │
    │  Araştırma Projesinde koordinatör / baş araştırmacı olmak                    │  
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ b) Devam eden veya başarı ile tamamlanmış AB Çerçeve programı bilimsel       │
    │ araştırma projesinde ortak araştırmacı olmak                                 │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ c) Devam eden veya başarı ile tamamlanmış a ve b bentleri dışındaki          │
    │ uluslararası destekli bilimsel araştırma projelerinde (derleme ve rapor      │
    │ hazırlama çalışmaları hariç) görev almak                                     │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ d) Üniversiteler dışındaki kamu kurumlarıyla yapılan başarıyla tamamlanan    │
    │ veya yürütülen bilimsel araştırma projelerinde görev almak                   │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ p) Puan Hesapla                                                              │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ q) Çıkış Yap                                                                 │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ * Bu maddeden en fazla 20 puan alınabilir.                                   │
    ╘══════════════════════════════════════════════════════════════════════════════╛
            """)
        while True:

            bilimsel_Araştırma = input("Lisansüstü Tez Danışmanlığı Hesapla :")
            # -------------------------------------------------------------------------A SECENEGİ

            if bilimsel_Araştırma == "a" or bilimsel_Araştırma == "A":
                print("""--> Doktora tez danışmanlığı :
                                                    1.Kaç tane
                                                    2.Doktora Zamanı
                                                    3.Çıkmak İçin
                                    """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------Proje sayısı
                    if secenek == "1":

                        bilimsel_Araştırma_1 = input("Toplam kaç tane :")
                        try:
                            bilimsel_Araştırma_sayısı_1_1 = int(bilimsel_Araştırma_1)

                            continue
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")

                    elif secenek == "2":
                        self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                    "a)Doktora Sonrası \n"
                                                    "b)Doktora Öncesi :")
                        try:
                            try:
                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":

                                    self.bilimsel_Araştırma_puan_1 = bilimsel_Araştırma_sayısı_1_1 * 15

                                    self.bilimsel_Araştırma_doc_sonrası.append(self.bilimsel_Araştırma_puan_1)
                                    break


                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":

                                    self.bilimsel_Araştırma_puan_1 = bilimsel_Araştırma_sayısı_1_1 * 15

                                    self.bilimsel_Araştırma_doc_oncesi.append(self.bilimsel_Araştırma_puan_1)

                                    break
                                else:
                                    print("İşleminiz Gerçekleşiyor")
                                    time.sleep(1)
                                    print("Geçersiz İşlem......")
                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Önce Proje Sayısı Girilmeli!!!")


                    elif secenek == "3":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")




            #  --------------------------------------------------------------------------------B SECENEGİ
            elif bilimsel_Araştırma == "b" or bilimsel_Araştırma == "B":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> Yüksek lisans tez danışmanlığı:                                
                                                   1.Kaç tane
                                                   2.Doktora Zamanı
                                                   3.Çıkmak İçin
                                           """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------Proje sayısı

                    if secenek == "1":
                        bilimsel_Araştırma_2 = input("Toplam kaç tane :")
                        try:
                            bilimsel_Araştırma_sayısı_2_1 = int(bilimsel_Araştırma_2)

                            continue
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")


                    elif secenek == "2":
                        self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                    "a)Doktora Sonrası \n"
                                                    "b)Doktora Öncesi :")
                        try:
                            try:
                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":

                                    self.bilimsel_Araştırma_puan_2 = bilimsel_Araştırma_sayısı_2_1 * 10

                                    self.bilimsel_Araştırma_doc_sonrası.append(self.bilimsel_Araştırma_puan_2)
                                    break


                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":

                                    self.bilimsel_Araştırma_puan_2 = bilimsel_Araştırma_sayısı_2_1 * 10

                                    self.bilimsel_Araştırma_doc_oncesi.append(self.bilimsel_Araştırma_puan_2)

                                    break
                                else:
                                    print("İşleminiz Gerçekleşiyor")
                                    time.sleep(1)
                                    print("Geçersiz İşlem......")
                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Önce Proje Sayısı Girilmeli!!!")

                    elif secenek == "3":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            #  ------------------------------------------------------------------C SECENEGİ

            elif bilimsel_Araştırma == "c" or bilimsel_Araştırma == "C":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> Doktora (eş danışmanlık) :

                                                    1.Kaç tane
                                                    2.Doktora Zamanı
                                                    3.Çıkmak İçin

                                                           """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ---------------------------------------------------------------------------------------------- (Proje sayısı)
                    if secenek == "1":
                        bilimsel_Araştırma_3 = input("Toplam kaç tane :")
                        try:
                            bilimsel_Araştırma_sayısı_3_1 = int(bilimsel_Araştırma_3)

                            continue
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")


                    elif secenek == "2":
                        self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                    "a)Doktora Sonrası \n"
                                                    "b)Doktora Öncesi :")
                        try:
                            try:
                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":

                                    self.bilimsel_Araştırma_puan_3 = bilimsel_Araştırma_sayısı_3_1 * 6

                                    self.bilimsel_Araştırma_doc_sonrası.append(self.bilimsel_Araştırma_puan_3)
                                    break


                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":

                                    self.bilimsel_Araştırma_puan_3 = bilimsel_Araştırma_sayısı_3_1 * 6

                                    self.bilimsel_Araştırma_doc_oncesi.append(self.bilimsel_Araştırma_puan_3)

                                    break
                                else:
                                    print("İşleminiz Gerçekleşiyor")
                                    time.sleep(1)
                                    print("Geçersiz İşlem......")

                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")
                        except AttributeError:
                            print("Önce Proje Sayısı Girilmeli!!!")


                    elif secenek == "3":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            elif bilimsel_Araştırma == "d" or bilimsel_Araştırma == "D":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> Yüksek Lisans (eş danışmanlık) :

                                                    1.Kaç tane
                                                    2.Doktora Zamanı
                                                    3.Çıkmak İçin

                                                           """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ---------------------------------------------------------------------------------------------- (Proje sayısı)
                    if secenek == "1":
                        bilimsel_Araştırma_4 = input("Toplam kaç tane :")
                        try:
                            bilimsel_Araştırma_sayısı_4_1 = int(bilimsel_Araştırma_4)

                            continue
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")


                    elif secenek == "2":
                        self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                    "a)Doktora Sonrası \n"
                                                    "b)Doktora Öncesi :")
                        try:
                            try:
                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":

                                    self.bilimsel_Araştırma_puan_4 = bilimsel_Araştırma_sayısı_4_1 * 4

                                    self.bilimsel_Araştırma_doc_sonrası.append(self.bilimsel_Araştırma_puan_4)
                                    break


                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":

                                    self.bilimsel_Araştırma_puan_4 = bilimsel_Araştırma_sayısı_4_1 * 4

                                    self.bilimsel_Araştırma_doc_oncesi.append(self.bilimsel_Araştırma_puan_4)

                                    break
                                else:
                                    print("İşleminiz Gerçekleşiyor")
                                    time.sleep(1)
                                    print("Geçersiz İşlem......")

                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")
                        except AttributeError:
                            print("Önce Proje Sayısı Girilmeli!!!")


                    elif secenek == "3":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")


            # ------------------------------------------------------------------ toplama işlemi
            elif bilimsel_Araştırma == "p" or bilimsel_Araştırma == "P":

                bilimsel_Araştırma_docSonrası_puan = self.bilimsel_Araştırma_doc_sonrası
                bilimsel_Araştırma_toplam_puan_sonra = sum(bilimsel_Araştırma_docSonrası_puan)

                bilimsel_Araştırma_docOncesi_puan = self.bilimsel_Araştırma_doc_oncesi
                bilimsel_Araştırma_toplam_puan_once = sum(bilimsel_Araştırma_docOncesi_puan)

                if bilimsel_Araştırma_toplam_puan_sonra + bilimsel_Araştırma_toplam_puan_once > 0:
                    try:
                        if bilimsel_Araştırma_toplam_puan_sonra > 20:
                            self.doktora_sonrası.append(20)
                        elif bilimsel_Araştırma_toplam_puan_sonra < 20:
                            self.doktora_sonrası.append(bilimsel_Araştırma_toplam_puan_sonra)

                        if bilimsel_Araştırma_toplam_puan_once > 20:
                            self.doktora_oncesi.append(20)
                        elif bilimsel_Araştırma_toplam_puan_once < 20:
                            self.doktora_oncesi.append(bilimsel_Araştırma_toplam_puan_once)

                        self.doktora_sonrası_puan()
                        self.doktora_oncesi_puan()

                        soru = input("sistem yenılensın mı (E,H): ")
                        if soru == "e" or soru == "E":
                            self.bilimsel_Araştırma_liste_T_F.clear()
                            bilimsel_Araştırma_docOncesi_puan.clear()
                            bilimsel_Araştırma_docSonrası_puan.clear()
                            self.bilimsel_Araştırma_liste_T_F.append(True)
                            self.clear()
                        else:
                            self.bilimsel_Araştırma_liste_T_F.clear()
                            bilimsel_Araştırma_docOncesi_puan.clear()
                            bilimsel_Araştırma_docSonrası_puan.clear()
                            self.bilimsel_Araştırma_liste_T_F.append(True)

                            break
                    except:
                        time.sleep(1)

                elif bilimsel_Araştırma_toplam_puan_sonra + bilimsel_Araştırma_toplam_puan_once == 0:

                    try:

                        soru_2 = input(
                            "Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
                        if soru_2 == "e" or soru_2 == "E":
                            self.bilimsel_Araştırma_liste_T_F.clear()
                            print("Lütfen veri giriniz !!!!!!")
                            break
                        else:
                            if self.bilimsel_Araştırma_liste_T_F == [True]:
                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()
                                break

                    except:
                        print("hata")
                        break


            elif bilimsel_Araştırma == "q" or bilimsel_Araştırma == "Q":
                break

            else:
                print("İşleminiz Gerçekleşiyor")
                time.sleep(1)
                print("Geçersiz İşlem......")

    def Bilimsel_Toplantı_Faaliyeti(self):
        time.sleep(1)
        print("""
    ╒══════════════════════════════════════════════════════════════════════════════╕
    │                     8. Bilimsel Toplantı Faaliyeti                           │
    ╞══════════════════════════════════════════════════════════════════════════════╡
    │ a) Uluslararası bilimsel toplantılarda sunulan (poster hariç), tam metni     │
    │ veya özeti matbu veya elektronik olarak bildiri kitapçığında yayımlanmış     │
    │ çalışmalar.                                                                  │  
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ b) Ulusal bilimsel toplantılarda sunulan (poster hariç), tam metni veya      │
    │ özeti matbu veya elektronik olarak bildiri kitapçığında yayımlanmış          │
    │ çalışmalar.                                                                  │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ p) Puan Hesapla                                                              │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ q) Çıkış Yap                                                                 │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ * Bu madde kapsamında en az 5 puan almak zorunludur, en fazla 10 puan        │
    │ alınabilir. Aynıtoplantıda sunulan en fazla bir bildiri puanlanır.           │
    ╘══════════════════════════════════════════════════════════════════════════════╛
            """)
        while True:
            bilimsel_secenek = input(
                "-->Bilimsel toplantı faaliyet hesaplama :")

            # ------------------------------------------------------------------------------------(A seceneği)-------------------------------------------------------------
            if bilimsel_secenek == "a" or bilimsel_secenek == "A":
                print("""Uluslararası bilimsel toplantılarda sunulan (poster hariç), tam metni veya özeti \nmatbu veya elektronik olarak bildiri kitapçığında yayımlanmış çalışmalar. : 
                                            1. Toplam kaç kişi                                                        
                                            2. Kaç tane
                                            3. Doktora Zamanı
                                            4. Çıkmak İçin

                                                            """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    if secenek == "1":
                        self.bilimsel_basvuru_1 = input("Toplam kaç kişi:")
                        try:
                            self.bilimsel_basvuru_1_1 = int(self.bilimsel_basvuru_1)
                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")


                    elif secenek == "2":
                        self.bilimsel_makale_1 = input(
                            "--> Uluslararası bilimsel toplantılarda sunulan (poster hariç), tam metni veya özeti "
                            "matbu veya elektronik olarak bildiri kitapçığında yayımlanmış çalışmalar :")
                        try:
                            try:
                                self.bilimsel_makale_1_1 = int(self.bilimsel_makale_1)
                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                            # ------------------------------------------------------------------Zaman
                    elif secenek == "3":
                        try:
                            try:
                                self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                            "a)Doktora Sonrası \n"
                                                            "b)Doktora Öncesi :")

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.bilimsel_puan_1 = 3 / self.bilimsel_basvuru_1_1
                                    self.bilimsel_puan_2 = self.bilimsel_puan_1 * self.bilimsel_makale_1_1
                                    self.bilimsel_toplantı_doc_sonrası.append(self.bilimsel_puan_2)
                                    break


                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.bilimsel_puan_1 = 3 / self.bilimsel_basvuru_1_1
                                    self.bilimsel_puan_2 = self.bilimsel_puan_1 * self.bilimsel_makale_1_1
                                    self.bilimsel_toplantı_doc_oncesi.append(self.bilimsel_puan_2)
                                    break
                                # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa


                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Sıralamayı Bozmayın!!!")

                    elif secenek == "4":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")


            elif bilimsel_secenek == "b" or bilimsel_secenek == "B":
                print(""" Ulusal bilimsel toplantılarda sunulan (poster hariç),
                     tam metni veya özeti matbu veya elektronik olarak bildiri kitapçığında yayımlanmış çalışmalar. : 
                                                               1. Toplam kaç kişi                                                        
                                                               2. Kaç tane
                                                               3. Doktora Zamanı
                                                               4. Çıkmak İçin

                                                                               """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    if secenek == "1":
                        self.bilimsel_basvuru_2 = input("Toplam kaç kişi:")
                        try:
                            self.bilimsel_basvuru_2_1 = int(self.bilimsel_basvuru_2)
                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")


                    elif secenek == "2":
                        self.bilimsel_makale_2 = input(
                            "--> Uluslararası bilimsel toplantılarda sunulan (poster hariç), tam metni veya özeti\n "
                            "matbu veya elektronik olarak bildiri kitapçığında yayımlanmış çalışmalar :")
                        try:
                            try:
                                self.bilimsel_makale_2_1 = int(self.bilimsel_makale_2)
                            except AttributeError:
                                print("Önce Kişi Sayısı Girilmeli!!!")
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                            # ------------------------------------------------------------------Zaman
                    elif secenek == "3":
                        try:
                            try:
                                self.doktora_zamanı = input("Lüften Doktora Zamanını Seçin :\n"
                                                            "a)Doktora Sonrası \n"
                                                            "b)Doktora Öncesi :")

                                if self.doktora_zamanı == "a" or self.doktora_zamanı == "A":
                                    self.bilimsel_puan_3 = 2 / self.bilimsel_basvuru_2_1
                                    self.bilimsel_puan_4 = self.bilimsel_puan_3 * self.bilimsel_makale_2_1
                                    self.bilimsel_toplantı_doc_sonrası.append(self.bilimsel_puan_4)
                                    break


                                # -------------------------------------------------------------------------------------------------DOKTORA ZAMANI
                                elif self.doktora_zamanı == "b" or self.doktora_zamanı == "B":
                                    self.bilimsel_puan_3 = 2 / self.bilimsel_basvuru_1_1
                                    self.bilimsel_puan_4 = self.bilimsel_puan_3 * self.bilimsel_makale_1_1
                                    self.bilimsel_toplantı_doc_oncesi.append(self.bilimsel_puan_4)
                                    break
                                # -------------------------------------------------------------------------------------------------makale sayısı 2 olursa


                            except ValueError:
                                print("Sıralamayı Bozmayın!!!")

                        except AttributeError:
                            print("Sıralamayı Bozmayın!!!")

                    elif secenek == "4":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")


            elif bilimsel_secenek == "p" or bilimsel_secenek == "P":

                bilimsel_toplantı_docSonrası_alınan_puan = self.bilimsel_toplantı_doc_sonrası
                bilimsel_toplantı_doc_sonrası_toplam = sum(bilimsel_toplantı_docSonrası_alınan_puan)

                # -------------------------------------------

                bilimsel_toplantı_docOncesı_alınan_puan = self.bilimsel_toplantı_doc_oncesi
                bilimsel_toplantı_doc_oncesi_toplam = sum(bilimsel_toplantı_docOncesı_alınan_puan)

                if bilimsel_toplantı_doc_sonrası_toplam + bilimsel_toplantı_doc_oncesi_toplam >= 5:
                    try:
                        if bilimsel_toplantı_doc_sonrası_toplam > 10:
                            self.doktora_sonrası.append(10)
                        elif bilimsel_toplantı_doc_sonrası_toplam >= 5 or bilimsel_toplantı_doc_sonrası_toplam <= 10:
                            self.doktora_sonrası.append(bilimsel_toplantı_doc_sonrası_toplam)

                        if bilimsel_toplantı_doc_oncesi_toplam > 10:
                            self.doktora_oncesi.append(10)
                        elif bilimsel_toplantı_doc_oncesi_toplam >= 5 or bilimsel_toplantı_doc_oncesi_toplam <= 10:
                            self.doktora_oncesi.append(bilimsel_toplantı_doc_oncesi_toplam)

                        self.doktora_sonrası_puan()
                        self.doktora_oncesi_puan()

                        soru = input("sistem yenılensın mı (E,H): ")
                        if soru == "e" or soru == "E":
                            self.bilimsel_toplantı_T_F.clear()
                            bilimsel_toplantı_docSonrası_alınan_puan.clear()
                            bilimsel_toplantı_docOncesı_alınan_puan.clear()
                            self.bilimsel_toplantı_T_F.append(True)
                            self.clear()
                        else:
                            self.bilimsel_toplantı_T_F.clear()
                            bilimsel_toplantı_docSonrası_alınan_puan.clear()
                            bilimsel_toplantı_docOncesı_alınan_puan.clear()
                            self.bilimsel_toplantı_T_F.append(True)

                            break
                    except:
                        time.sleep(1)

                elif bilimsel_toplantı_doc_sonrası_toplam + bilimsel_toplantı_doc_oncesi_toplam < 5:

                    try:
                        soru_2 = input("Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
                        if soru_2 == "e" or soru_2 == "E":
                            self.bilimsel_toplantı_T_F.clear()
                            print("Lütfen veri giriniz...")
                            print("Bu madde kapsamında en az 5 puan almak zorunludur.")
                            self.bilimsel_toplantı_T_F.append(False)
                            break
                        else:
                            if self.bilimsel_toplantı_T_F == [True]:
                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()
                                break

                            elif self.bilimsel_toplantı_T_F == [False]:
                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()

                                break

                    except:
                        print("hata")


            elif bilimsel_secenek == "q" or bilimsel_secenek == "Q":
                break

            else:
                print("İşleminiz Gerçekleşiyor")
                time.sleep(1)
                print("Geçersiz İşlem......")

    def Eğitim_Öğretim(self):
        time.sleep(1)
        print("""
    ╒══════════════════════════════════════════════════════════════════════════════╕
    │                     9. Eğitim-Öğretim Faaliyeti                              │
    ╞══════════════════════════════════════════════════════════════════════════════╡
    │ Doktora eğitimini tamamladıktan sonra açık, uzaktan veya yüz yüze ortamlarda │
    │ verilmiş ders                                                                │  
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ a) Bir dönem yüksek lisans veya doktora dersi                                │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ b) Bir dönem önlisans veya lisans dersi                                      │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ c) Yurtiçi veya YÖK tarafından tanınan yurtdışı yükseköğretim kurumlarında   │
    │    en az 2 yıl eğitim ve öğretim faaliyetinde bulundum                       │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ p) Puan Hesapla                                                              │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ q) Çıkış Yap                                                                 │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │ * Bu madde kapsamında en az 2 puan almak zorunludur, ancak en fazla 4 puan   │ 
    │alınabilir. Yurtiçi veya YÖK tarafından tanınan yurtdışı yükseköğretim        │
    │kurumlarında en az 2 yıl öğretim elemanı olarak görev yapanlar 2 puan         │
    │almış sayılır                                                                 │
    ╘══════════════════════════════════════════════════════════════════════════════╛
            """)
        while True:
            egitim_ogretim = input(
                "-->Eğitim öğretim faaliyet hesaplama :")

            # ------------------------------------------------------------------------------------(A seceneği)-------------------------------------------------------------
            if egitim_ogretim == "a" or egitim_ogretim == "A":
                print("""--> Bir dönem yüksek lisans veya doktora dersi  :
                                            1.Kaç tane
                                            2.Çıkmak İçin
                            """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------Kaç tane
                    if secenek == "1":

                        egitim_ogretim_sayısı_1 = input("Toplam kaç tane :")
                        try:
                            egitim_ogretim_sayısı_1_1 = int(egitim_ogretim_sayısı_1)
                            self.egitim_ogretim_puan_1 = egitim_ogretim_sayısı_1_1 * 3

                            self.egitim_ogretim_doc_sonrası.append(self.egitim_ogretim_puan_1)
                            break
                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")


                    elif secenek == "2":
                        break

                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            elif egitim_ogretim == "b" or egitim_ogretim == "B":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> Bir dönem önlisans veya lisans dersi :                                
                                           1.Kaç tane
                                           2.Çıkmak İçin
                                   """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------kişi sayısı
                    if secenek == "1":
                        egitim_ogretim_sayısı_2 = input("Toplam kaç tane:")
                        try:
                            self.egitim_ogretim_sayısı_2_1 = int(egitim_ogretim_sayısı_2)
                            self.egitim_ogretim_puan_2 = self.egitim_ogretim_sayısı_2_1 * 2

                            self.egitim_ogretim_doc_sonrası.append(self.egitim_ogretim_puan_2)

                            continue

                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------ makale sayısı

                    elif secenek == "2":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")

            elif egitim_ogretim == "c" or egitim_ogretim == "c":
                print("İşleminiz Sorgunalnıyor")
                time.sleep(1)
                print("""--> Yurtiçi veya YÖK tarafından tanınan yurtdışı yükseköğretim kurumlarında en az 2 yıl eğitim ve öğretim faaliyetinde bulundum:                                
                                           1.EVET/ HAYIR
                                           2.Çıkmak İçin
                                   """)
                while True:
                    secenek = input("Lüften devam etmek icin bir seçenek seçin:")
                    # ------------------------------------------------------------------kişi sayısı
                    if secenek == "1":
                        egitim_ogretim_sayısı_3 = input("EVET ise (E) /HAYIR ise (H) basınız :")
                        try:
                            if egitim_ogretim_sayısı_3 == "e" or egitim_ogretim_sayısı_3 == "E":
                                self.egitim_ogretim_doc_sonrası.append(2)
                                break
                            else:
                                break


                        except ValueError:
                            print("Bir sayı girmelisiniz!!!")
                    # ------------------------------------------------------------------ makale sayısı

                    elif secenek == "2":
                        break
                    else:
                        print("İşleminiz Gerçekleşiyor")
                        time.sleep(1)
                        print("Geçersiz İşlem......")





            elif egitim_ogretim == "p" or egitim_ogretim == "P":

                egitim_ogretim_docSonrası_alınan_puan = self.egitim_ogretim_doc_sonrası
                egitim_ogretim_doc_sonrası_toplam = sum(egitim_ogretim_docSonrası_alınan_puan)

                # -------------------------------------------

                if egitim_ogretim_doc_sonrası_toplam >= 2:
                    try:
                        if egitim_ogretim_doc_sonrası_toplam >= 4:
                            self.doktora_sonrası.append(4)
                        elif egitim_ogretim_doc_sonrası_toplam >= 2 or egitim_ogretim_doc_sonrası_toplam < 4:
                            self.doktora_sonrası.append(egitim_ogretim_doc_sonrası_toplam)

                        self.doktora_sonrası_puan()
                        self.doktora_oncesi_puan()

                        soru = input("sistem yenılensın mı (E,H): ")
                        if soru == "e" or soru == "E":
                            self.egitim_ogretim_T_F.clear()
                            egitim_ogretim_docSonrası_alınan_puan.clear()
                            self.egitim_ogretim_T_F.append(True)
                            self.clear()
                        else:
                            self.egitim_ogretim_T_F.clear()
                            egitim_ogretim_docSonrası_alınan_puan.clear()
                            self.egitim_ogretim_T_F.append(True)

                            break
                    except:
                        time.sleep(1)

                elif egitim_ogretim_doc_sonrası_toplam < 2:

                    try:
                        soru_2 = input(
                            "Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
                        if soru_2 == "e" or soru_2 == "E":
                            self.egitim_ogretim_T_F.clear()
                            print("Lütfen veri giriniz...")
                            print("Bu madde kapsamında en az 2 puan almak zorunludur.")
                            self.egitim_ogretim_T_F.append(False)
                            break
                        else:
                            if self.egitim_ogretim_T_F == [True]:
                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()
                                break

                            elif self.egitim_ogretim_T_F == [False]:
                                self.doktora_sonrası_puan()
                                self.doktora_oncesi_puan()
                                break
                    except:
                        print("hata")
                        break

            elif egitim_ogretim == "q" or egitim_ogretim == "Q":
                break
            else:
                print("İşleminiz Gerçekleşiyor")
                time.sleep(1)
                print("Geçersiz İşlem......")




    def doktora_sonrası_puan(self):

        sayilar = self.doktora_sonrası
        self.toplam_doc_sonrası = sum(sayilar)
        print("Doktora sonrası aldığınız puan :", self.toplam_doc_sonrası)

    def doktora_oncesi_puan(self):

        sayilar = self.doktora_oncesi
        self.toplam_doc_oncesı = sum(sayilar)
        print("Doktora öncesi aldığınız puan :", self.toplam_doc_oncesı)
    def makale_toplama(self):
        ulusal_makale_sayısı = self.ulusal_makale_sayısı
        toplam_makale_sayısı = sum(ulusal_makale_sayısı)
        self.toplam_makale = toplam_makale_sayısı

    def kontrol_ıslemi(self):

        while True:
            #not direk olarak 10 işlem secılırse altakı 2 madde sorun cıkacaktır.

            if self.uluslararası_liste_T_F:
                if self.uluslararası_liste_T_F == [True]:
                    print("1.Maddesinde: Bu maddenin a veya b bentleri kapsamında en az 20 puan almak zorunluluk aşamasını gectınız.")

                elif self.uluslararası_liste_T_F == [False]:
                    print(
                        "1.Maddesinde: Bu maddenin a veya b bentleri kapsamında en az 20 puan almak zorunluluk aşamasını geçemedinizzzzzzz.")

                if self.ulusal_liste_T_F :
                    if self.ulusal_liste_T_F == [True]:
                        print("2.Maddesinde: İkisi bu maddenin a bendi kapsamında olmak üzere en az üç yayın yapmak zorunluluğunu gectiniz.")

                    elif self.ulusal_liste_T_F == [False]:

                        print(
                            "2.Maddesinde: İkisi bu maddenin a bendi kapsamında olmak üzere en az üç yayın yapmak zorunludur.")
                if self.lisans_liste_T_F :
                    if self.lisans_liste_T_F == [True]:
                        print("3.Maddesinde: Bu madde kapsamında en az 1 yayın zorunluluğu geçtiniz .")

                    elif self.lisans_liste_T_F == [False]:
                        print(
                            "3.Maddesinde: Bu madde kapsamında en az 1 yayın zorunludur.")

                if self.kitap_liste_T_F :
                    if self.kitap_liste_T_F == [True]:
                        print("4.Maddesinde: Bu aşamayı gectiniz.")

                    elif self.kitap_liste_T_F == [False]:
                        print("4.Maddesinde:veri giriniz.")

                if self.atıflar_liste_T_F :
                    if self.atıflar_liste_T_F == [True]:
                        print("5.Maddesinde: Bu madde kapsamında en az 4 puan alınma zorunluluğunu gectiniz.")

                    elif self.atıflar_liste_T_F == [False]:

                        print("5.Maddesinde: Bu madde kapsamında en az 4 puan alınması zorunludur")

                if self.lisansüstü_Tez_T_F :
                    if self.lisansüstü_Tez_T_F == [True]:
                        print("6.Maddesinde: Bu aşamayı gectiniz.")

                    elif self.lisansüstü_Tez_T_F == [False]:

                        print(
                            "6.Maddesinde: DEveri giriniz.")
                if self.bilimsel_Araştırma_liste_T_F :
                    if self.bilimsel_Araştırma_liste_T_F == [True]:
                        print("7.Maddesinde: Bu aşamayı gectiniz.")

                    elif self.bilimsel_Araştırma_liste_T_F == [False]:

                        print(
                            "7.Maddesinde: veri giriniz.")


                if self.bilimsel_toplantı_T_F :
                    if self.bilimsel_toplantı_T_F == [True]:
                        print("8.Maddesinde: Bu madde kapsamında en az 5 puan almak zorunluluğunu gectiniz.")

                    elif self.bilimsel_toplantı_T_F == [False]:

                        print(
                            "8.Maddesinde: Bu madde kapsamında en az 5 puan almak zorunludur.")

                if self.egitim_ogretim_T_F :
                    if self.egitim_ogretim_T_F == [True]:
                        print("9.Maddesinde: Bu madde kapsamında en az 2 puan almak zorunluluğunu gectiniz.")

                    elif self.egitim_ogretim_T_F == [False]:

                        print(
                            "9.Maddesinde: Bu madde kapsamında en az 2 puan almak  zorunludur.")
                try:
                    if self.toplam_doc_sonrası >0:
                        if self.toplam_doc_sonrası >= 90:
                            print("Doktora sonrası yaptığınız çalışmalardan toplam en az 90 puan aşamasını geçtiniz.")
                        elif self.toplam_doc_sonrası < 90:
                            print("Doktora sonrası yaptığınız çalışmalardan toplam en az 90 puan almanız gerekir.")
                    if self.toplam_doc_oncesı + self.toplam_doc_sonrası >= 0:
                        if self.toplam_doc_oncesı + self.toplam_doc_sonrası > 100:
                            print("Yaptığınız çalışmalardan toplam en az 100 puan aşamasını geçtiniz.")
                            break
                        elif self.toplam_doc_oncesı + self.toplam_doc_sonrası < 100:
                            print("Yaptığınız çalışmalardan toplam en az 100 puan aşamasını geçemediniz.")
                            break
                except:
                    print("Bu işlemi direk olarak seçerseniz son 2 işlem yapılmayacaktır")

                    break


            else:
                print("Veri giriniz..")
                break


print(f"""{Fore.LIGHTWHITE_EX}


╒══════════════════════════════════════════╕
│  Eğitim Bilimleri Temel Puan Hesapla     │
├──────────────────────────────────────────┤
│ 1. Uluslararası Makale                   │
│ 2. Ulusal Makale                         │
│ 3. Lisansüstü Tezlerden Üretilmiş Yayın  │
│ 4. Kitap                                 │
│ 5. Atıflar                               │
│ 6. Lisansüstü Tez Danışmanlığı           │
│ 7. Bilimsel Araştırma Projesi            │
│ 8. Bilimsel Toplantı Faaliyeti           │
│ 9. Eğitim-Öğretim Faaliyeti              │
├──────────────────────────────────────────┤
│ 10.Kontrol Aşaması                       │
├──────────────────────────────────────────┤  
│ Programdan çıkmak için 'q' ya basın      │
│                                          │
╘══════════════════════════════════════════╛
""")

egitim = EğitimOgretimFaaliyetleri()

while True:
    işlem = input("İşlem Secin:")
    print("İşleminiz Sorgunalnıyor")
    time.sleep(1)
    if işlem == "q":
        break
    elif işlem == "1":
        egitim.uluslararası_Makale()
    elif işlem == "2":
        egitim.ulusal_makale()
    elif işlem == "3":
        egitim.lisanustu_Tez()
    elif işlem == "4":
        egitim.kitap()
    elif işlem == "5":
        egitim.atıflar()
    elif işlem == "6":
        egitim.Lısansustu_Tez_Danışmanlığı()
    elif işlem == "7":
        egitim.Bilimsel_Araştırma_Projesi()
    elif işlem == "8":
        egitim.Bilimsel_Toplantı_Faaliyeti()
    elif işlem == "9":
        egitim.Eğitim_Öğretim()
    elif işlem == "10":
        egitim.kontrol_ıslemi()
    else:
        print("İşleminiz Gerçekleşiyor")
        time.sleep(1)
        print("Geçersiz İşlem......")
"""
bunlar eklenebılır projenın ılerisinde .
Kısaltmalar ve Tanımlar
SCI–Expanded: Science Citation Index-Expanded
SCI: Science Citation Index
SSCI: Social Sciences Citation Index
AHCI: Art and Humanities Index
ULAKBİM: Ulusal Akademik Ağ ve Bilgi Merkezi
AB Çerçeve Programları: AB tarafından, üye ve aday ülkelerin çeşitli alanlardaki ulusal politika ve uygulamalarının birbirine yakınlaştırılması amacıyla oluşturulan Topluluk Programlarından birisidir.
(*) Alan İndeksleri: ISI Database'e giren ilgili indeksler veya SCOPUS
Ulusal Yayınevi: En az dört yıl ulusal düzeyde düzenli faaliyet yürüten, yayınları Türkiye’deki üniversite kütüphanelerinde kataloglanan ve daha önce aynı alanda farklı yazarlara ait en az 20 kitap yayımlamış yayınevi.
Uluslararası Yayınevi: En az dört yıl uluslararası düzeyde düzenli faaliyet yürüten, yayımladığı kitaplar Yükseköğretim Kurulunca tanınan sıralama kuruluşlarınca belirlenen dünyada ilk 500'e giren üniversite kütüphanelerinde kataloglanan ve aynı alanda farklı yazarlara ait en az 20 kitap yayımlamış olan yayınevi.
Uluslararası Bilimsel Toplantı: Farklı ülkelerden bilim insanlarının bilim kurulunda bulunduğu ve sunumların bilimsel ön incelemeden geçirilerek kabul edildiği toplantı.
Ulusal Bilimsel Toplantı: Ulusal seviyede farklı kurumlardan bilim insanlarının bilim kurulunda bulunduğu ve sunumların bilimsel ön incelemeden geçirilerek kabul edildiği toplantı.
Yayımlanmış Makale: Alanında bilime katkı sağlamış olmak şartıyla özgün matbu veya elektronik ortamda yayımlanmış makale.

"""