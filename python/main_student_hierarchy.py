# ============================================================================
#  MAIN — Tam nümunə: Abstraction + Inheritance + Polymorphism
#         + Encapsulation + validasiya (bütün OOP əsasları BİR YERDƏ)
# ----------------------------------------------------------------------------
#  Bu fayl demo/Main.java-nın Python versiyasıdır və Practice 9 ilə
#  demək olar EYNİDİR — bu, kursun "final" (ən tam) nümunəsidir,
#  bütün öyrənilmiş OOP anlayışlarını bir proqramda birləşdirir:
#     - Abstraction (ABC, @abstractmethod)
#     - Encapsulation ("_" prefiksli sahələr + getter/setter)
#     - Inheritance (Telebe -> MagistrTelebe -> DoktorantTelebe)
#     - Polymorphism (melumat_goster() metodunun hər sinifdə fərqli işləməsi)
#     - Validasiya (regex ilə telefon/email formatını yoxlamaq)
# ============================================================================

import re
from abc import ABC, abstractmethod


# ══════════════════════════════════════════════════════════════════════════
#  ABSTRAKT BAZA SİNİF (Abstraction)
# ══════════════════════════════════════════════════════════════════════════
# Bu sinif birbaşa obyekt yaratmaq üçün deyil,
# digər siniflər üçün baza rolunu oynayır.
# ABC-dən miras alır və içində @abstractmethod olduğu üçün
# bu sinifdən birbaşa "Telebe(...)" yazaraq obyekt yaratmaq MÜMKÜN
# OLMAYACAQ — Python bunu XƏTA ilə əngəlləyəcək.
class Telebe(ABC):

    # ------------------------------------------------------------------
    # Encapsulation (İnkapsulyasiya)
    # Bütün sahələr "_" ilə başlayır — bu, onların sinifin "daxili detalı"
    # olduğunu, xaricdən BİRBAŞA yox, getter/setter vasitəsilə
    # dəyişdirilməli olduğunu bildirir.
    #
    # Konstruktor DÖRD parametr qəbul edir və hamısını AYRI-AYRI
    # sahələrə yazır.
    # ------------------------------------------------------------------
    def __init__(self, ad, soyad, telefon_nomresi, email):
        self._ad = ad
        self._soyad = soyad
        self._telefon_nomresi = telefon_nomresi
        self._email = email

    # ---- Getter-lər — hər sahə üçün AYRI bir "oxu" metodu ----
    def get_ad(self):
        return self._ad

    def get_soyad(self):
        return self._soyad

    def get_telefon_nomresi(self):
        return self._telefon_nomresi

    def get_email(self):
        return self._email

    # ---- Setter-lər — hər sahə üçün AYRI bir "yaz" metodu ----
    def set_ad(self, ad):
        self._ad = ad

    def set_soyad(self, soyad):
        self._soyad = soyad

    def set_telefon_nomresi(self, telefon_nomresi):
        self._telefon_nomresi = telefon_nomresi

    def set_email(self, email):
        self._email = email

    # ------------------------------------------------------------------
    # Abstrakt metod — hər alt sinif öz implementasiyasını yazmalıdır.
    # Bu, "bütün Telebe-lər melumat_goster() metoduna sahib OLMALIDIR,
    # amma HƏR BİRİ onu ÖZ ÜSULU İLƏ yazacaq" fikrini ifadə edir —
    # bu, POLYMORPHISM-in TƏMƏLİDİR.
    # ------------------------------------------------------------------
    @abstractmethod
    def melumat_goster(self):
        pass


# ══════════════════════════════════════════════════════════════════════════
#  Inheritance (İrsiyyət) — 1-Cİ SƏVİYYƏ
# ══════════════════════════════════════════════════════════════════════════
class MagistrTelebe(Telebe):

    def __init__(self, ad, soyad, telefon_nomresi, email, universitet):
        # super() ilə Telebe-nin konstruktoru çağırılır, 4 parametr ötürülür
        super().__init__(ad, soyad, telefon_nomresi, email)
        # Bu sinifə MƏXSUS əlavə sahə
        self._universitet = universitet

    # Abstrakt metodun implementasiyası (Polymorphism)
    def melumat_goster(self):
        # f-string-lər içində getter metodları çağırılır —
        # birbaşa self._ad yerinə self.get_ad() istifadə olunur,
        # bu, ENCAPSULATION prinsipinə hörmət göstərməkdir
        print(f"Ad: {self.get_ad()} {self.get_soyad()}")
        print(f"Telefon: {self.get_telefon_nomresi()}")
        print(f"Email: {self.get_email()}")
        print(f"Universitet: {self._universitet}")


# ══════════════════════════════════════════════════════════════════════════
#  Inheritance (İrsiyyət) — 2-Cİ SƏVİYYƏ
#  DoktorantTelebe -> MagistrTelebe -> Telebe ZƏNCİRİ
# ══════════════════════════════════════════════════════════════════════════
class DoktorantTelebe(MagistrTelebe):

    def __init__(self, ad, soyad, telefon_nomresi, email, universitet, tedqiqat_movzusu):
        # MagistrTelebe-nin konstruktoru çağırılır (5 parametr) —
        # o da öz növbəsində Telebe-nin konstruktorunu çağıracaq
        super().__init__(ad, soyad, telefon_nomresi, email, universitet)
        self._tedqiqat_movzusu = tedqiqat_movzusu

    # Method Overriding (Polymorphism)
    def melumat_goster(self):
        super().melumat_goster()  # MagistrTelebe-nin melumat_goster()-u ƏVVƏLCƏ işə düşür
        print(f"Tədqiqat Mövzusu: {self._tedqiqat_movzusu}")  # sonra əlavə sətir çap olunur


# ══════════════════════════════════════════════════════════════════════════
#  VALİDASİYA FUNKSİYALARI — istifadəçi girişini yoxlamaq üçün
#  Bunlar sinif DEYİL, sərbəst funksiyalardır — hər hansı bir obyektə
#  "bağlı" olmadıqları üçün sinif daxilinə YAZILMASINA EHTİYAC YOXDUR
# ══════════════════════════════════════════════════════════════════════════

def bos_olmayan_giris_oxu(mesaj):
    # Boş mətn qəbul olunmayana qədər TƏKRAR-TƏKRAR soruşur
    while True:
        deyer = input(mesaj).strip()
        if deyer:
            return deyer
        print("Yanlış giriş: bu sahə boş ola bilməz. Zəhmət olmasa düzgün dəyər daxil edin.")


def telefon_duzgundur(telefon):
    # Telefon nömrəsi: əvvəlində İSTƏYƏ BAĞLI "+" , sonra 7-20 arası
    # rəqəm/tire/boşluq simvolu (ətraflı izah üçün bax: practice9.py)
    return re.match(r"^\+?[0-9\-\s]{7,20}$", telefon) is not None


def email_duzgundur(email):
    # Email formatı: "nəsə@nəsə.nəsə" şəklində olmalıdır
    return re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", email) is not None


def duzgun_telefon_oxu(mesaj):
    while True:
        telefon = input(mesaj).strip()
        if not telefon:
            print("Yanlış giriş: telefon nömrəsi boş ola bilməz.")
            continue  # dövrün əvvəlinə qayıdır, yeni sual verir
        if telefon_duzgundur(telefon):
            return telefon
        print("Telefon nömrəsi yanlışdır. Rəqəm, boşluq, tire və ixtiyari başlanğıc + istifadə edin.")


def duzgun_email_oxu(mesaj):
    while True:
        email = input(mesaj).strip()
        if not email:
            print("Yanlış giriş: email boş ola bilməz.")
            continue
        if email_duzgundur(email):
            return email
        print("Email formatı yanlışdır. Nümunə: user@example.com")


def main():
    # ── Magistr Tələbə məlumatlarının daxil edilməsi ──────────────
    print("Magistr tələbə məlumatlarının daxil edilməsi:")
    mt_ad = bos_olmayan_giris_oxu("Magistr tələbənin adını daxil edin: ")
    mt_soyad = bos_olmayan_giris_oxu("Magistr tələbənin soyadını daxil edin: ")
    mt_telefon = duzgun_telefon_oxu("Magistr tələbənin telefon nömrəsini daxil edin: ")
    mt_email = duzgun_email_oxu("Magistr tələbənin emailini daxil edin: ")
    mt_universitet = bos_olmayan_giris_oxu("Magistr tələbənin universitetini daxil edin: ")

    # --------------------------------------------------------
    # Diqqət: "Telebe" tipli ABSTRAKT sinifdən DEYİL, konkret
    # MagistrTelebe sinifindən obyekt yaradılır — çünki Telebe
    # abstraktdır və obyekt YARADA BİLMƏZ (Python bunu qadağan edər).
    # --------------------------------------------------------
    magistr_telebe = MagistrTelebe(mt_ad, mt_soyad, mt_telefon, mt_email, mt_universitet)
    print()
    magistr_telebe.melumat_goster()

    # ── Doktorant Tələbə məlumatlarının daxil edilməsi ───────────────────
    print()
    print("Doktorant tələbə məlumatlarının daxil edilməsi:")
    dt_ad = bos_olmayan_giris_oxu("Doktorant tələbənin adını daxil edin: ")
    dt_soyad = bos_olmayan_giris_oxu("Doktorant tələbənin soyadını daxil edin: ")
    dt_telefon = duzgun_telefon_oxu("Doktorant tələbənin telefon nömrəsini daxil edin: ")
    dt_email = duzgun_email_oxu("Doktorant tələbənin emailini daxil edin: ")
    dt_universitet = bos_olmayan_giris_oxu("Doktorant tələbənin universitetini daxil edin: ")
    dt_tedqiqat_movzusu = bos_olmayan_giris_oxu("Doktorant tələbənin tədqiqat mövzusunu daxil edin: ")

    doktorant_telebe = DoktorantTelebe(dt_ad, dt_soyad, dt_telefon, dt_email, dt_universitet, dt_tedqiqat_movzusu)
    print()
    doktorant_telebe.melumat_goster()


if __name__ == "__main__":
    main()
