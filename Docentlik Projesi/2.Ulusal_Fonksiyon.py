import time
import colorama
from colorama import Fore, Back, Style
import os
colorama.init(autoreset=True)


class EğitimOgretimFaaliyetleri():

    def __init__(self,
                 # ---------------------------------- uluslararası
                 uluslararsıa=20,uluslararsıb=15,
                 uluslararsıc=5, uluslararası_liste_T_F=[],
                 #-------------------------------------------- ulusal
                 ulusala=8, ulusalb=4,
                 ulusal_makale_sayısı=[],ulusal_liste_T_F=[False],
                 toplam_makale=0, ulusal_makale_1_1=0,
                 ulusal_doc_sonrası = [],
                 ulusal_doc_oncesi =[],

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
        self.ulusal_doc_sonrası = ulusal_doc_sonrası
        self.ulusal_doc_oncesi = ulusal_doc_oncesi
        self.ulusal_makale_sayısı = ulusal_makale_sayısı
        self.toplam_makale =  toplam_makale
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
                        soru_2 = input("Bu tuşa veri girmeden mi bastınız (Evet ise 'E',Hayır ise 'H' tuşuna basınız):")
                        if soru_2 == "e" or soru_2 == "E":
                            self.ulusal_liste_T_F.clear()
                            print("İkisi bu maddenin a bendi kapsamında olmak üzere en az üç yayın yapmak zorunludur.")
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


            elif ulusal_secenek =="q" or ulusal_secenek =="Q" :
                break
            else:
                print("İşleminiz Gerçekleşiyor")
                time.sleep(1)
                print("Geçersiz İşlem......")
            if self.ulusal_makale_1_1 < 2:
                print("Aşamadaki zorunluluk sağlanmadığı için sonlandırılıyor....")
                time.sleep(1)
                break

#-------------------------------------------------------------------------------------------------------
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

#bu fonskıyon ayarlanacak

    def kontrol_ıslemi(self):
        while True:
            if self.ulusal_liste_T_F:
                if self.ulusal_liste_T_F == [True]:
                    print(
                        "İkisi bu maddenin a bendi kapsamında olmak üzere en az üç yayın yapmak zorunluluğunu gectiniz.")
                    if self.uluslararası_liste_T_F == [True]:
                        print(
                            "Bu maddenin a veya b bentleri kapsamında en az 20 puan almak zorunluluk aşamasını gectınız.")
                        break
                    elif self.uluslararası_liste_T_F == [False]:
                        print(
                            "Bu maddenin a veya b bentleri kapsamında en az 20 puan almak zorunluluk aşamasını geçemedinizzzzzzz.")
                        break


                elif self.ulusal_liste_T_F == [False]:
                    print(
                        "İkisi bu maddenin a bendi kapsamında olmak üzere en az üç yayın yapmak zorunluluğunu gecemedınız.")

                break

            else:
                print("hatalı")
                break





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
        egitim.ulusal_makale()

    elif işlem == "2":
        egitim.uluslararası_Makale()
    elif işlem == "10":
        egitim.kontrol_ıslemi()

    else:
        print("İşleminiz Gerçekleşiyor")
        time.sleep(1)
        print("Geçersiz İşlem......")