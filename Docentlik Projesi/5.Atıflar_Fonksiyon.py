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

                 #-----------------------------------------Atıflar
                 atıflar_doc_sonrası =[],
                 atıflar_doc_oncesi=[],
                 atıflar_liste_T_F=[],

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

        #Atıflar
        self.atıflar_doc_sonrası = atıflar_doc_sonrası
        self.atıflar_doc_oncesi = atıflar_doc_oncesi
        self.atıflar_liste_T_F = atıflar_liste_T_F

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

                        self.atıflar_1 = input("--> SCI, SCI-Expanded, SSCI ve AHCI tarafından taranan dergilerde; uluslararası yayınevleritarafından\nyayımlanmış kitaplarda yayımlanan ve adayın yazar olarak yer almadığı yayınlardan her birinde\nmetin içindeki atıf sayısına bakılmaksızın adayın atıf yapılan eser sayısı: ")

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
                        #-----------------------------------------------------------------
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
                elif atıflar_doc_sonrası_toplam + atıflar_doc_oncesi_toplam  < 4:
                    try:
                        soru_2 = input("Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
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
            elif atıflar =="q" or atıflar =="Q" :
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
        egitim.atıflar()


    elif işlem == "2":
        egitim.uluslararası_Makale()
    elif işlem == "10":
        egitim.kontrol_ıslemi()

    else:
        print("İşleminiz Gerçekleşiyor")
        time.sleep(1)
        print("Geçersiz İşlem......")
