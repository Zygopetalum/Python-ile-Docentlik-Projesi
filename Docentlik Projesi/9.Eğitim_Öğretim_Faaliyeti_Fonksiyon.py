import time
import colorama
import pyautogui
from colorama import Fore, Back, Style
import os
import keyboard

colorama.init(autoreset=True)
from texttable import Texttable


class EğitimOgretimFaaliyetleri():
    def __init__(self,
                 # ---------------------------------- uluslararası
                 uluslararsıa=20, uluslararsıb=15,
                 uluslararsıc=5, uluslararası_liste_T_F=[],

                 # -------------------------------------------- ulusal
                 ulusala=8, ulusalb=4,
                 ulusal_makale_sayısı=[], ulusal_liste_T_F=[],
                 toplam_makale=0, ulusal_makale_1_1=0,

                 # -------------------------------------- lisasüstü
                 makale_list=[],
                 lisans_liste_T_F=[],
                 lisans_doc_sonrası=[],
                 lisans_doc_oncesi=[],

                 # --------------------------------------- kitap

                 kitap_liste_T_F=[],

                 # -----------------------------------------Atıflar
                 atıflar_doc_sonrası=[],
                 atıflar_doc_oncesi=[],

                 #-----------------------------egitim ogretim
                 egitim_ogretim_doc_sonrası=[],
                 egitim_ogretim_T_F=[],



                 # -------------------------------------- global
                 makale_sayısı=0, basvuran_kısı=0,
                 doktora_sonrası=[], doktora_oncesi=[]

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
        self.toplam_makale = toplam_makale
        self.ulusal_liste_T_F = ulusal_liste_T_F
        self.ulusal_makale_1_1 = ulusal_makale_1_1

        # lisasüstü
        self.makale_list = makale_list
        self.lisans_liste_T_F = lisans_liste_T_F
        self.lisans_doc_sonrası = lisans_doc_sonrası
        self.lisans_doc_oncesi = lisans_doc_oncesi

        # kitap
        self.kitap_liste_T_F = kitap_liste_T_F

        # Atıflar
        self.atıflar_doc_sonrası = atıflar_doc_sonrası
        self.atıflar_doc_oncesi = atıflar_doc_oncesi


        #Eğitim Öğretim Faaliyet
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

    def Eğitim_Öğretim (self):
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
                            if egitim_ogretim_sayısı_3 =="e" or egitim_ogretim_sayısı_3 =="E":
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

                elif egitim_ogretim_doc_sonrası_toplam <2:

                    try:
                        soru_2 = input("Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
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

            elif egitim_ogretim =="q" or egitim_ogretim =="Q" :
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

    def makale_toplama(self):
        ulusal_makale_sayısı = self.ulusal_makale_sayısı
        toplam_makale_sayısı = sum(ulusal_makale_sayısı)
        self.toplam_makale = toplam_makale_sayısı

        # bu fonskıyon ayarlanacak

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
        egitim.Eğitim_Öğretim()

    else:
        print("İşleminiz Gerçekleşiyor")
        time.sleep(1)
        print("Geçersiz İşlem......")
