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
                 uluslarası_doc_sonrası=[0],
                 uluslarası_doc_oncesi=[0],

                 # -------------------------------------------- ulusal
                 ulusala=8, ulusalb=4,
                 ulusal_makale_sayısı=[], ulusal_liste_T_F=[],
                 toplam_makale=0, ulusal_makale_1_1=0,

                 # -------------------------------------- global
                 makale_sayısı=0, basvuran_kısı=0,
                 doktora_sonrası=[], doktora_oncesi=[]

                 ):

        # uluslararası bolum
        self.uluslararsıa = uluslararsıa
        self.uluslararsıb = uluslararsıb
        self.uluslararsıc = uluslararsıc
        self.uluslararası_liste_T_F = uluslararası_liste_T_F
        self.uluslarası_doc_sonrası = uluslarası_doc_sonrası
        self.uluslarası_doc_oncesi = uluslarası_doc_oncesi

        # ulusal bolum
        self.ulusala = ulusala
        self.ulusalb = ulusalb
        self.ulusal_makale_sayısı = ulusal_makale_sayısı
        self.toplam_makale = toplam_makale
        self.ulusal_liste_T_F = ulusal_liste_T_F
        self.ulusal_makale_1_1 = ulusal_makale_1_1

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

    def kontrol_ıslemi(self):

        while True:

            if self.uluslararası_liste_T_F:
                if self.uluslararası_liste_T_F == [True]:
                    print("Bu maddenin a veya b bentleri kapsamında en az 20 puan almak zorunluluk aşamasını gectınız.")
                    self.uluslararası_liste_T_F.clear()
                    break
                elif self.uluslararası_liste_T_F == [False]:
                    self.uluslararası_liste_T_F.clear()
                    print(
                        "Bu maddenin a veya b bentleri kapsamında en az 20 puan almak zorunluluk aşamasını geçemedinizzzzzzz.")
                    break

            else:
                print("hatalı")
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
        pass
    elif işlem == "3":
        pass
    elif işlem == "4":
        pass
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







