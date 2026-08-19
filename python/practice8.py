# ============================================================================
#  PRACTICE 8 — 3 səviyyəli irsiyyət zənciri
# ----------------------------------------------------------------------------
#  Mövzu: Telebe -> MagistrTelebe -> DoktorantTelebe
#  (hər sinif ÖZÜNDƏN ƏVVƏLKİNDƏN miras alır — bu, "ÇOX SƏVİYYƏLİ
#  İRSİYYƏT" (multi-level inheritance) adlanır)
#
#  Fərq Practice 6/7-dən: orada DoktorantTelebe BİRBAŞA Telebe-dən miras
#  alırdı (iki sinif QARDAŞ idi). Burada isə DoktorantTelebe, MagistrTelebe-
#  dən miras alır — yəni DoktorantTelebe "MagistrTelebe-nin bir NÖVÜDÜR",
#  o da öz növbəsində "Telebe-nin bir NÖVÜDÜR".
# ============================================================================

from abc import ABC, abstractmethod

# Bu sinif bir tələbənin ÜMUMİ xüsusiyyətlərini və davranışlarını təyin edir.
# Abstract olduğu üçün BİRBAŞA obyekt yaradıla bilməz.
# Bu sinifdən törədilmiş siniflər öz spesifik xüsusiyyətlərini əlavə edə
# və melumat_goster metodunu implementasiya edə bilərlər.
# Bu, Polymorphism və Inheritance konseptlərini nümayiş etdirir.


# Abstrakt sinif (Abstraction)
# Bu sinif birbaşa obyekt yaratmaq üçün deyil,
# digər siniflər üçün BAZA rolunu oynayır
class Telebe(ABC):

    # Encapsulation (İnkapsulyasiya)
    # _ad dəyişəni "daxili" sahədir — birbaşa xaricdən dəyişdirilməməlidir,
    # bunun üçün aşağıdakı getter/setter metodları var
    def __init__(self, ad):
        self._ad = ad

    # Getter — ad dəyərini oxumaq üçün
    def get_ad(self):
        return self._ad

    # Setter — ad dəyərini dəyişmək üçün
    def set_ad(self, ad):
        self._ad = ad

    # Abstrakt metod — hər alt sinif öz implementasiyasını yazmalıdır
    @abstractmethod
    def melumat_goster(self):
        pass


# --------------------------------------------------------------------------
# Inheritance (İrsiyyət) — 1-Cİ SƏVİYYƏ
# MagistrTelebe sinifi Telebe sinifindən miras alır
# --------------------------------------------------------------------------
class MagistrTelebe(Telebe):

    # Bu sinifə məxsus ƏLAVƏ sahə — universitetin adı
    def __init__(self, ad, universitet):
        super().__init__(ad)  # Telebe sinifinin konstruktorunu çağırır
        self._universitet = universitet

    # Abstrakt metodun implementasiyası (Polymorphism)
    def melumat_goster(self):
        # ad-a birbaşa YOX, getter vasitəsilə müraciət edilir (Encapsulation)
        print("Ad:", self.get_ad())
        print("Universitet:", self._universitet)


# --------------------------------------------------------------------------
# Inheritance (İrsiyyət) — 2-Cİ SƏVİYYƏ
# DoktorantTelebe sinifi Telebe-dən YOX, birbaşa MagistrTelebe sinifindən
# miras alır.
#
# Beləliklə Telebe -> MagistrTelebe -> DoktorantTelebe ZƏNCİRİ yaranır —
# yəni DoktorantTelebe həm MagistrTelebe-nin, həm də (DOLAYI YOLLA,
# MagistrTelebe vasitəsilə) Telebe-nin BÜTÜN sahə və metodlarına
# sahibdir. Bu, "ƏCDAD-NƏVƏ" münasibətinə bənzəyir: DoktorantTelebe
# MagistrTelebe-nin "övladı", Telebe-nin isə "nəvəsidir".
# --------------------------------------------------------------------------
class DoktorantTelebe(MagistrTelebe):

    # Bu sinifə məxsus əlavə sahə — tədqiqat mövzusu
    def __init__(self, ad, universitet, tedqiqat_movzusu):
        # --------------------------------------------------------
        # super().__init__(ad, universitet) burada MagistrTelebe-nin
        # konstruktorunu çağırır.
        #
        # MagistrTelebe-nin konstruktoru İSƏ öz növbəsində
        # super().__init__(ad) ilə Telebe-nin konstruktorunu çağırır.
        #
        # Beləliklə bir DoktorantTelebe yaradıldıqda ARDICIL OLARAQ:
        #   DoktorantTelebe.__init__ -> MagistrTelebe.__init__ -> Telebe.__init__
        # ZƏNCİRVARİ ÇAĞIRIŞ baş verir, hər addımda öz sahəsi qurulur.
        # --------------------------------------------------------
        super().__init__(ad, universitet)
        self._tedqiqat_movzusu = tedqiqat_movzusu

    # --------------------------------------------------------
    # Method Overriding (Polymorphism)
    # MagistrTelebe-dəki melumat_goster() metodu burada GENİŞLƏNDİRİLİR
    # (tamam ƏVƏZLƏNMİR — köhnə versiya da içəridə İSTİFADƏ OLUNUR).
    # --------------------------------------------------------
    def melumat_goster(self):
        # Əvvəlcə ana sinifin (MagistrTelebe) melumat_goster() metodu çağırılır —
        # bu, "Ad" və "Universitet" sətirlərini çap edir.
        # Diqqət: bu, öz növbəsində Telebe-nin getter-lərindən istifadə edir,
        # amma Telebe-nin ÖZ melumat_goster()-i YOXDUR (o abstraktdır),
        # ona görə burada MagistrTelebe-nin versiyası işə düşür.
        super().melumat_goster()

        # Sonra BU sinifə (DoktorantTelebe-yə) məxsus əlavə məlumat çap olunur
        print("Tədqiqat Mövzusu:", self._tedqiqat_movzusu)  # əlavə məlumat


def main():
    # ── Magistr Tələbə məlumatlarının daxil edilməsi ──────────────
    mt_ad = input("Magistr tələbənin adını daxil edin: ")
    mt_universitet = input("Magistr tələbənin universitetini daxil edin: ")

    # Polymorphism — "magistr_telebe" dəyişəni konseptual olaraq
    # HƏM MagistrTelebe, HƏM DƏ Telebe sayıla bilər (çünki miras var)
    magistr_telebe = MagistrTelebe(mt_ad, mt_universitet)

    # melumat_goster() çağırılır — hansı sinifin metodu işə düşdüyü
    # obyektin REAL TİPİNƏ (runtime-da müəyyən olunan tip) görə seçilir
    magistr_telebe.melumat_goster()

    # ── Doktorant Tələbə məlumatlarının daxil edilməsi ───────────────────
    dt_ad = input("Doktorant tələbənin adını daxil edin: ")
    dt_universitet = input("Doktorant tələbənin universitetini daxil edin: ")
    dt_tedqiqat_movzusu = input("Doktorant tələbənin tədqiqat mövzusunu daxil edin: ")

    # Polymorphism — DoktorantTelebe obyekti yaradılır.
    # Bu obyekt EYNİ ZAMANDA MagistrTelebe VƏ Telebe sayıla bilər
    # (çünki irsiyyət zənciri var: DoktorantTelebe -> MagistrTelebe -> Telebe)
    doktorant_telebe = DoktorantTelebe(dt_ad, dt_universitet, dt_tedqiqat_movzusu)

    # melumat_goster() çağırılır — bu dəfə DoktorantTelebe-nin OVERRIDE EDİLMİŞ
    # (həm də daxilində MagistrTelebe-nin metodunu ÇAĞIRAN) versiyası işləyir
    doktorant_telebe.melumat_goster()


if __name__ == "__main__":
    main()
