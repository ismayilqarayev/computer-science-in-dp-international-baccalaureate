# ============================================================================
#  PRACTICE 7 — Abstraction + istifadəçi girişi ilə birlikdə
# ----------------------------------------------------------------------------
#  Bu fayl Practice 6-nın DAVAMIDIR — eyni abstrakt sinif quruluşu,
#  amma bu dəfə obyektlərin məlumatları SABİT (hardcoded) DEYİL,
#  istifadəçidən input() vasitəsilə DİNAMİK olaraq alınır.
# ============================================================================

from abc import ABC, abstractmethod


# Abstrakt baza sinif — bütün "Telebe" tiplərinin ORTAQ hissəsi bu sinifdə
class Telebe(ABC):

    def __init__(self, ad):
        self._ad = ad  # encapsulation: "_" ilə "daxili sahə" işarələnir

    def get_ad(self):
        return self._ad

    # Bu metodun gövdəsi (bədəni) YOXDUR — hər alt sinif ÖZÜ yazmalıdır.
    # Əgər alt sinif bunu yazmasa, Python obyekt yaratmağa İCAZƏ VERMƏYƏCƏK.
    @abstractmethod
    def melumat_goster(self):
        pass


# Birinci alt sinif — universitet (bakalavr/magistr) tələbəsi
class MagistrTelebe(Telebe):

    def __init__(self, ad, universitet):
        super().__init__(ad)  # ana sinifin konstruktoru işə salınır
        self._universitet = universitet

    def melumat_goster(self):
        print("Magistr Tələbə:", self.get_ad())
        print("Universitet:", self._universitet)


# İkinci alt sinif — doktorantura tələbəsi
class DoktorantTelebe(Telebe):

    def __init__(self, ad, tedqiqat_sahesi):
        super().__init__(ad)
        self._tedqiqat_sahesi = tedqiqat_sahesi

    def melumat_goster(self):
        print("Doktorant Tələbə:", self.get_ad())
        print("Tədqiqat Sahəsi:", self._tedqiqat_sahesi)


def main():
    # --------------------------------------------------------
    # Birinci obyekt — MagistrTelebe — istifadəçi girişindən yaradılır.
    #
    # Diqqət: iki dəfə input() çağırılır, ARDICIL OLARAQ.
    # Proqram birinci sualı verir, cavab gözləyir, sonra ikinci sualı verir.
    # --------------------------------------------------------
    ad = input("Magistr tələbənin adını daxil edin: ")
    universitet = input("Universiteti daxil edin: ")

    telebe = MagistrTelebe(ad, universitet)
    telebe.melumat_goster()

    print()  # ekranda boş sətir — iki nəticəni vizual olaraq ayırmaq üçün

    # --------------------------------------------------------
    # İkinci obyekt — DoktorantTelebe — yenə istifadəçi girişindən yaradılır.
    # Dəyişən adları fərqlidir (doktorant_ad, tedqiqat_sahesi), çünki
    # "ad" adı artıq yuxarıda istifadə olunub və onu YENİDƏN İSTİFADƏ
    # ETSƏYDİK, əvvəlki dəyəri ÜSTÜNDƏN YAZARDI (bu, səhv olmazdı, amma
    # kodu daha az oxunaqlı edərdi).
    # --------------------------------------------------------
    doktorant_ad = input("Doktorant tələbənin adını daxil edin: ")
    tedqiqat_sahesi = input("Tədqiqat sahəsini daxil edin: ")

    doktorant = DoktorantTelebe(doktorant_ad, tedqiqat_sahesi)
    doktorant.melumat_goster()


if __name__ == "__main__":
    main()
