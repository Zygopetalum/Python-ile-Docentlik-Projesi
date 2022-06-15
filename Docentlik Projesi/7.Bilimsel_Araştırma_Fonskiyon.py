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

                 #-------------------------------------bilimsel_Araştırma
                 bilimsel_Araştırma_doc_sonrası = [],
                 bilimsel_Araştırma_doc_oncesi = [],
                 bilimsel_Araştırma_liste_T_F=[],


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

        #Bilimsel Araştırma Projesi
        self.bilimsel_Araştırma_doc_sonrası = bilimsel_Araştırma_doc_sonrası
        self.bilimsel_Araştırma_doc_oncesi = bilimsel_Araştırma_doc_oncesi
        self.bilimsel_Araştırma_liste_T_F = bilimsel_Araştırma_liste_T_F



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

    def Bilimsel_Araştırma_Projesi (self):
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

                        except AttributeError :
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

                        except AttributeError :
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


                if bilimsel_Araştırma_toplam_puan_sonra +bilimsel_Araştırma_toplam_puan_once>0:
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

                        soru_2 = input("Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
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


            elif bilimsel_Araştırma =="q" or bilimsel_Araştırma =="Q" :
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
        egitim.Bilimsel_Araştırma_Projesi()

    elif işlem == "2":
        egitim.uluslararası_Makale()
    elif işlem == "10":
        egitim.kontrol_ıslemi()

    else:
        print("İşleminiz Gerçekleşiyor")
        time.sleep(1)
        print("Geçersiz İşlem......")
