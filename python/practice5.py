# ============================================================================
#  PRACTICE 5 — Inheritance (İrsiyyət) və Method Overriding
# ----------------------------------------------------------------------------
#  Bu faylda öyrənəcəyimiz mövzular:
#    1) Bir sinif başqa bir sinifdən necə "miras alır"?
#    2) super() nə üçündür, necə işləyir?
#    3) Method Overriding (metodun yenidən yazılması) nədir?
#    4) Bir alt sinif obyekti ilə çağırılan metodun HANSI VERSİYASININ
#       işə düşəcəyi necə müəyyən olunur?
# ============================================================================

# --------------------------------------------------------------------------
# BASE CLASS (baza/ana sinif) — bütün "ortaq" xüsusiyyətlər burada olur.
# Bu sinif "MagistrTelebe" kimi daha spesifik siniflər üçün TƏMƏL rolunu
# oynayacaq.
# --------------------------------------------------------------------------
class Telebe:

    def __init__(self, ad):
        self._ad = ad

    def get_ad(self):
        return self._ad

    def set_ad(self, ad):
        self._ad = ad

    # Bu, "adi" (override edilə bilən, amma məcburi olmayan) bir metoddur.
    # Abstrakt deyil — Telebe sinifinin özündən birbaşa obyekt yaratsaq
    # belə, bu metod işləyəcək.
    def melumat_goster(self):
        print("Tələbənin adı:", self._ad)


# --------------------------------------------------------------------------
# DERIVED CLASS (törəmə/alt sinif) — Telebe sinifindən MİRAS ALIR.
#
# Python-da miras almaq üçün sinif adının yanında mötərizə içində
# ana sinifin adı yazılır:  class MagistrTelebe(Telebe):
#
# Bunun mənası: "MagistrTelebe, Telebe-nin BÜTÜN sahə və metodlarını
# AVTOMATİK olaraq özündə daşıyır, üstəlik özünə məxsus ƏLAVƏ sahə və
# metodlar da qura bilər."
#
# Real həyat analogiyası: "Telebe" ümumi "İnsan" anlayışı kimidirsə,
# "MagistrTelebe" onun daha SPESİFİK bir NÖVÜDÜR — "hər MagistrTelebe
# eyni zamanda bir Telebe-dir, amma hər Telebe MagistrTelebe deyil".
# --------------------------------------------------------------------------
class MagistrTelebe(Telebe):

    def __init__(self, ad, universitet):
        # --------------------------------------------------------
        # super() — "ana sinifə" (bu halda Telebe-yə) müraciət etmək
        # üçün istifadə olunan xüsusi funksiyadır.
        #
        # super().__init__(ad) yazdıqda, Python Telebe sinifinin
        # __init__ metodunu çağırır və "ad" parametrini ona ötürür.
        # Bu, Telebe-nin öz konstruktorunun etdiyi işi (yəni
        # self._ad = ad sətrini) BİZİM ƏVƏZİMİZƏ görür.
        #
        # NİYƏ super() İSTİFADƏ EDİRİK, NİYƏ ÖZÜMÜZ "self._ad = ad"
        # YAZMIRIQ?
        #   Çünki Telebe sinifinin __init__ metodu gələcəkdə
        #   dəyişə bilər (məsələn, əlavə yoxlama əlavə oluna bilər).
        #   Əgər biz özümüz "self._ad = ad" yazsaydıq, Telebe
        #   sinifindəki dəyişiklik BURAYA TƏSİR ETMƏZDİ. super()
        #   istifadə etməklə KOD TƏKRARLANMIR (DRY — "Don't Repeat
        #   Yourself" prinsipi) və hər iki sinif SİNXRON qalır.
        # --------------------------------------------------------
        super().__init__(ad)

        # Bu sahə YALNIZ MagistrTelebe sinifinə məxsusdur —
        # Telebe sinifində "universitet" deyə bir şey yoxdur
        self._universitet = universitet

    def get_universitet(self):
        return self._universitet

    def set_universitet(self, universitet):
        self._universitet = universitet

    # --------------------------------------------------------
    # METHOD OVERRIDING (metodun yenidən yazılması) —
    # Polymorphism-in bir formasıdır.
    #
    # Telebe sinifində artıq "melumat_goster" adlı metod var idi.
    # Biz burada EYNİ ADLA yeni bir versiya yazırıq — bu, ana
    # sinifdəki versiyanı "ƏVƏZLƏYİR" (override edir).
    #
    # Nəticədə: MagistrTelebe tipli bir obyektdə .melumat_goster()
    # çağırıldıqda, Telebe-dəki DEYİL, MƏHZ BURADAKI versiya
    # icra olunacaq.
    # --------------------------------------------------------
    def melumat_goster(self):
        # self.get_ad() — ana sinifdən miras alınmış getter metodu
        # çağırılır (MagistrTelebe-nin özündə "get_ad" YAZILMAYIB,
        # amma miras vasitəsilə ona sahibdir)
        print("Tələbənin adı:", self.get_ad())
        print("Universitet:", self._universitet)


def main():
    ad = input("Tələbənin adını daxil edin: ")
    universitet = input("Universiteti daxil edin: ")

    # MagistrTelebe obyekti yaradılır.
    # Bu, arxa planda İKİ addım işə salır:
    #   1) MagistrTelebe.__init__ çağırılır
    #   2) O da öz növbəsində super().__init__() ilə Telebe.__init__-i çağırır
    telebe = MagistrTelebe(ad, universitet)

    # melumat_goster() çağırılır — burada MagistrTelebe-nin ÖZ versiyası
    # işləyəcək (Telebe-dəki deyil, çünki override edilib).
    # Bu, Polymorphism-in canlı nümunəsidir: eyni adlı metod,
    # obyektin REAL TİPİNƏ görə FƏRQLİ DAVRANIR.
    telebe.melumat_goster()


if __name__ == "__main__":
    main()
