# ============================================================================
#  PRACTICE 6 — Abstraction (Abstraksiya) — abstrakt sinif
# ----------------------------------------------------------------------------
#  Bu faylda öyrənəcəyimiz mövzular:
#    1) Abstrakt sinif nədir, niyə lazımdır?
#    2) ABC (Abstract Base Class) modulu necə istifadə olunur?
#    3) @abstractmethod dekoratoru nə edir?
#    4) Niyə abstrakt sinifdən BİRBAŞA obyekt yarada bilmirik?
# ============================================================================

# Python-da Java-dakı "abstract" açar sözü YOXDUR.
# Onun əvəzinə standart kitabxanadakı "abc" (Abstract Base Classes)
# modulundan istifadə olunur. Bu modul bizə iki alət verir:
#   ABC            -> sinifin "abstrakt" olması üçün ondan miras alınır
#   abstractmethod -> hansı metodun MƏCBURİ override olunacağını bildirən dekorator
from abc import ABC, abstractmethod


# --------------------------------------------------------------------------
# Abstrakt sinif Telebe
#
# NİYƏ ABSTRAKT SİNİF LAZIMDIR?
# Təsəvvür edin ki, "Tələbə" anlayışı özlüyündə "natamam"dır — real
# həyatda sırf "Tələbə" deyə bir şey yoxdur, HƏR tələbə ya bakalavr,
# ya magistr, ya da doktoranturadadır (konkret bir NÖVDÜR).
# "Telebe" sinfini abstrakt etməklə biz deyirik:
#     "Bu sinifin özündən BİRBAŞA obyekt yaratmaq MƏNTİQSİZDİR,
#      YALNIZ ondan miras alan KONKRET siniflər (MagistrTelebe,
#      DoktorantTelebe) obyekt yarada bilər."
#
# ABC-dən miras almaqla (class Telebe(ABC):) sinif "abstrakt" statusu
# qazanır.
# --------------------------------------------------------------------------
class Telebe(ABC):

    def __init__(self, ad):
        self._ad = ad

    def get_ad(self):
        return self._ad

    # --------------------------------------------------------
    # @abstractmethod — bu, DEKORATORDUR (metodun üstündə "@" ilə yazılır).
    #
    # Dekoratorun mənası: "aşağıdakı metodu XÜSUSİ QAYDA ilə işlət".
    # @abstractmethod bu metodu "MƏCBURİ OVERRIDE OLUNMALI" elan edir.
    #
    # NƏTİCƏ:
    #   - Əgər MagistrTelebe (və ya hər hansı digər alt sinif)
    #     melumat_goster() metodunu ÖZÜ YAZMASA, Python ondan obyekt
    #     yaratmağa İCAZƏ VERMƏYƏCƏK və xəta buraxacaq:
    #         TypeError: Can't instantiate abstract class ... with
    #         abstract method melumat_goster
    #
    # "pass" — bu metodun burada heç bir real kodu (gövdəsi) yoxdur,
    # sadəcə onun "İMZASINI" (adını və parametrlərini) göstərir.
    # "pass" Python-da "heç nə etmə, sadəcə bura boş qalmasın deyə
    # yazılıb" mənasını verən açar sözdür.
    # --------------------------------------------------------
    @abstractmethod
    def melumat_goster(self):
        pass


# --------------------------------------------------------------------------
# Telebe-dən miras alan BİRİNCİ konkret (real obyekt yaradıla bilən) sinif
# --------------------------------------------------------------------------
class MagistrTelebe(Telebe):

    def __init__(self, ad, universitet):
        super().__init__(ad)  # ana sinifin konstruktoru çağırılır
        self._universitet = universitet

    # Abstrakt metodun KONKRET İMPLEMENTASİYASI.
    # Məhz bu metod yazıldığı üçün MagistrTelebe sinifindən artıq
    # obyekt yaratmaq mümkündür (bütün abstrakt metodlar "doldurulub").
    def melumat_goster(self):
        print("Magistr Tələbə:", self.get_ad())
        print("Universitet:", self._universitet)


# --------------------------------------------------------------------------
# Telebe-dən miras alan İKİNCİ konkret sinif.
# Diqqət: MagistrTelebe-dən deyil, birbaşa Telebe-dən miras alır —
# yəni bu iki sinif (MagistrTelebe və DoktorantTelebe) BİR-BİRİNƏ QOHUM
# DEYİL, hər ikisi sadəcə eyni "ata"nın (Telebe) övladlarıdır.
# --------------------------------------------------------------------------
class DoktorantTelebe(Telebe):

    def __init__(self, ad, tedqiqat_sahesi):
        super().__init__(ad)
        self._tedqiqat_sahesi = tedqiqat_sahesi

    def melumat_goster(self):
        print("Doktorant Tələbə:", self.get_ad())
        print("Tədqiqat Sahəsi:", self._tedqiqat_sahesi)


def main():
    ad = input("Tələbənin adını daxil edin: ")
    universitet = input("Universiteti daxil edin: ")

    # ------------------------------------------------------------
    # Diqqət: "telebe" dəyişəni MagistrTelebe TİPLİ bir obyektə
    # işarə edir, amma KONSEPTUAL olaraq o eyni zamanda "bir Telebe"
    # da sayılır (çünki MagistrTelebe, Telebe-dən miras alıb).
    #
    # Bu, POLYMORPHISM-in başqa bir təzahürüdür: "bir MagistrTelebe,
    # istənilən yerdə Telebe kimi də istifadə oluna bilər".
    # ------------------------------------------------------------
    telebe = MagistrTelebe(ad, universitet)
    telebe.melumat_goster()

    print()  # ekranda boş bir sətir — vizual ayırma üçün

    # İkinci alt sinifdən obyekt yaradılır — bu dəfə dəyərlər
    # istifadəçidən yox, birbaşa kodun içində SABİT (hardcoded)
    # olaraq verilib
    doktorant = DoktorantTelebe("Nigar", "Süni İntellekt")
    doktorant.melumat_goster()


if __name__ == "__main__":
    main()
