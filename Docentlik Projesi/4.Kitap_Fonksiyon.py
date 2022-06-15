import os
import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)



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
                 toplam_lisans_puan=[],
                 lisans_liste_T_F=[],

                 #--------------------------------------- kitap

                 kitap_liste_T_F=[],
                 kitap_doc_sonrası=[],
                 kitap_doc_oncesi=[],


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
        self.toplam_lisans_puan = toplam_lisans_puan
        self.lisans_liste_T_F = lisans_liste_T_F

        #kitap
        self.kitap_liste_T_F = kitap_liste_T_F
        self.kitap_doc_sonrası = kitap_doc_sonrası
        self.kitap_doc_oncesi = kitap_doc_oncesi

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

            secenek_kitap = input("-->Adayın hazırladığı lisansüstü tezlerinden üretilmemiş ve başvurulan\ndoçentlik bilim alanı ile ilgili olmak kaydıyla:")

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
                    #-------------------------------------------------------------------------(makale sayısı)
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
                    elif secenek == "3" :
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
#------------------------------------------------------------------------------------(C seceneği)-------------------------------------------------------------

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
                    elif secenek == "2" :
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
                    elif secenek == "3" :
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
                    if secenek =="1":
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

                    elif secenek == "3" :
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
# ------------------------------------------------------------------------------------(Puan Hesapla)-------------------------------------------------------------
            elif secenek_kitap == "p" or secenek_kitap == "P":

                kitap_docSonrası_alınan_puan = self.kitap_doc_sonrası
                kitap_doc_sonrası_toplam = sum(kitap_docSonrası_alınan_puan)

                # -------------------------------------------

                kitap_docOncesı_alınan_puan = self.kitap_doc_oncesi
                kitap_doc_oncesi_toplam = sum(kitap_docOncesı_alınan_puan)


                if kitap_doc_sonrası_toplam + kitap_doc_oncesi_toplam >0:
                    try:
                        if kitap_doc_oncesi_toplam + kitap_doc_sonrası_toplam >0:

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
                        soru_2 = input("Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
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

            elif secenek_kitap =="q" or secenek_kitap =="Q" :
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
        pass
    elif işlem == "4":
        egitim.kitap()
    elif işlem == "5":
        pass
    elif işlem == "6":
        pass
    elif işlem == "7":
        pass
    elif işlem == "8":
        pass
    elif işlem == "9":
        pass
    elif işlem == "10":
        egitim.kontrol_ıslemi()
    else:
        print("İşleminiz Gerçekleşiyor")
        time.sleep(1)
        print("Geçersiz İşlem......")