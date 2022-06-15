import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
from texttable import Texttable


class EğitimOgretimFaaliyetleri():
    def __init__(self,
                 # ---------------------------------- uluslararası
                 uluslararsıa=20,uluslararsıb=15,
                 uluslararsıc=5, uluslararası_liste_T_F=[],

                 #-------------------------------------------- ulusal
                 ulusala = 8, ulusalb = 4,
                 ulusal_makale_sayısı = [],ulusal_liste_T_F = [],
                 toplam_makale = 0, ulusal_makale_1_1 = 0,

                 # -------------------------------------- lisasüstü
                 makale_list = [],
                 lisans_liste_T_F = [],
                 lisans_doc_sonrası = [],
                 lisans_doc_oncesi = [],
                 # -------------------------------------- global
                 makale_sayısı = 0, basvuran_kısı = 0,
                 doktora_sonrası = [], doktora_oncesi = []

                 ):

        # uluslararası bolum
        self.uluslararsıa = uluslararsıa
        self.uluslararsıb = uluslararsıb
        self.uluslararsıc = uluslararsıc
        self.uluslararası_liste_T_F = uluslararası_liste_T_F


        # ulusal bolum
        self.ulusala = ulusala
        self.ulusalb = ulusalb
        self.ulusal_makale_sayısı = ulusal_makale_sayısı
        self.toplam_makale =  toplam_makale
        self.ulusal_liste_T_F = ulusal_liste_T_F
        self.ulusal_makale_1_1 = ulusal_makale_1_1

        # lisasüstü
        self.makale_list = makale_list
        self.lisans_liste_T_F = lisans_liste_T_F
        self.lisans_doc_sonrası = lisans_doc_sonrası
        self.lisans_doc_oncesi = lisans_doc_oncesi

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
                    elif secenek == "3" :
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
                                #-------------------------------------------------------------------------------------------------makale sayısı 2 olursa


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
                                self.lisans_makale_2_1= int(self.lisans_makale_2)

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
                    secenek =input("Lüften devam etmek icin bir seçenek seçin:")
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
                                lisansustu_makale_sayısı.clear() # burada duruma gore degerlendırebılır ıstenırse yenı
                                                                #kayıt veya ustune ekleme yapılır tercıh duruma gore
                                self.lisans_liste_T_F(True)                           # ilerde yapılacak gelıstırmelerde goz onune alınacaktır.
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
                        soru_2 = input("Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
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

            elif secenek_lisans =="q" or secenek_lisans =="Q" :
                break
            else:
                print("İşleminiz Gerçekleşiyor")
                time.sleep(1)
                print("Geçersiz İşlem......")

    def doktora_sonrası_puan(self):

        sayilar = self.doktora_sonrası
        toplam = sum(sayilar)
        print("Doktora sonrası aldığınız puan :", toplam)

    def doktora_oncesi_puan(self):

        sayilar = self.doktora_oncesi
        toplam = sum(sayilar)
        print("Doktora öncesi aldığınız puan :", toplam)



print(f"""{Fore.LIGHTWHITE_EX} 
 ------------------------------------------
|                                          |
|                                          |
| işlemler;                                |
|                                          |
| 1.Eğitim Bilimleri Temel Puan Hesapla    |
| 2.Aşamaların Son Hali                    |
| 10.Kontrol Aşaması                       |  
| Programdan çıkmak için 'q' ya basın      |
|                                          |
 ------------------------------------------""")

egitim = EğitimOgretimFaaliyetleri()

while True:
    işlem = input("İşlem Secin:")
    print("İşleminiz Sorgunalnıyor")
    time.sleep(1)
    if işlem == "q":
        break
    elif işlem == "1":
        egitim.lisanustu_Tez()

    elif işlem == "2":
        egitim.uluslararası_Makale()
    elif işlem == "10":
        egitim.kontrol_ıslemi()

    else:
        print("İşleminiz Gerçekleşiyor")
        time.sleep(1)
        print("Geçersiz İşlem......")

