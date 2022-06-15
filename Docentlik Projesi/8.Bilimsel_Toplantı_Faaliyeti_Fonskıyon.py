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

                 #--------------------------------
                 bilimsel_toplantı_doc_sonrası=[],
                 bilimsel_toplantı_doc_oncesi = [],
                 bilimsel_toplantı_T_F=[],


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

        #bilimsel_toplantı
        self.bilimsel_toplantı_doc_sonrası =bilimsel_toplantı_doc_sonrası
        self.bilimsel_toplantı_doc_oncesi =bilimsel_toplantı_doc_oncesi
        self.bilimsel_toplantı_T_F = bilimsel_toplantı_T_F


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

    def Bilimsel_Toplantı_Faaliyeti (self):
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


            elif bilimsel_secenek =="q" or bilimsel_secenek =="Q" :
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
        egitim.Bilimsel_Toplantı_Faaliyeti()

    else:
        print("İşleminiz Gerçekleşiyor")
        time.sleep(1)
        print("Geçersiz İşlem......")
