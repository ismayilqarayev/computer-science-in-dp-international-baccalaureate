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
# Bu sinif "GraduateStudent" kimi daha spesifik siniflər üçün TƏMƏL rolunu
# oynayacaq.
# --------------------------------------------------------------------------
class Student:

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Bu, "adi" (override edilə bilən, amma məcburi olmayan) bir metoddur.
    # Abstrakt deyil — Student sinifinin özündən birbaşa obyekt yaratsaq
    # belə, bu metod işləyəcək.
    def show_info(self):
        print("Student name:", self._name)


# --------------------------------------------------------------------------
# DERIVED CLASS (törəmə/alt sinif) — Student sinifindən MİRAS ALIR.
#
# Python-da miras almaq üçün sinif adının yanında mötərizə içində
# ana sinifin adı yazılır:  class GraduateStudent(Student):
#
# Bunun mənası: "GraduateStudent, Student-in BÜTÜN sahə və metodlarını
# AVTOMATİK olaraq özündə daşıyır, üstəlik özünə məxsus ƏLAVƏ sahə və
# metodlar da qura bilər."
#
# Real həyat analogiyası: "Student" ümumi "İnsan" anlayışı kimidirsə,
# "GraduateStudent" onun daha SPESİFİK bir NÖVÜDÜR — "hər GraduateStudent
# eyni zamanda bir Student-dir, amma hər Student GraduateStudent deyil".
# --------------------------------------------------------------------------
class GraduateStudent(Student):

    def __init__(self, name, university):
        # --------------------------------------------------------
        # super() — "ana sinifə" (bu halda Student-ə) müraciət etmək
        # üçün istifadə olunan xüsusi funksiyadır.
        #
        # super().__init__(name) yazdıqda, Python Student sinifinin
        # __init__ metodunu çağırır və "name" parametrini ona ötürür.
        # Bu, Student-in öz konstruktorunun etdiyi işi (yəni
        # self._name = name sətrini) BİZİM ƏVƏZİMİZƏ görür.
        #
        # NİYƏ super() İSTİFADƏ EDİRİK, NİYƏ ÖZÜMÜZ "self._name = name"
        # YAZMIRIQ?
        #   Çünki Student sinifinin __init__ metodu gələcəkdə
        #   dəyişə bilər (məsələn, əlavə yoxlama əlavə oluna bilər).
        #   Əgər biz özümüz "self._name = name" yazsaydıq, Student
        #   sinifindəki dəyişiklik BURAYA TƏSİR ETMƏZDİ. super()
        #   istifadə etməklə KOD TƏKRARLANMIR (DRY — "Don't Repeat
        #   Yourself" prinsipi) və hər iki sinif SİNXRON qalır.
        # --------------------------------------------------------
        super().__init__(name)

        # Bu sahə YALNIZ GraduateStudent sinifinə məxsusdur —
        # Student sinifində "university" deyə bir şey yoxdur
        self._university = university

    def get_university(self):
        return self._university

    def set_university(self, university):
        self._university = university

    # --------------------------------------------------------
    # METHOD OVERRIDING (metodun yenidən yazılması) —
    # Polymorphism-in bir formasıdır.
    #
    # Student sinifində artıq "show_info" adlı metod var idi.
    # Biz burada EYNİ ADLA yeni bir versiya yazırıq — bu, ana
    # sinifdəki versiyanı "ƏVƏZLƏYİR" (override edir).
    #
    # Nəticədə: GraduateStudent tipli bir obyektdə .show_info()
    # çağırıldıqda, Student-dəki DEYİL, MƏHZ BURADAKI versiya
    # icra olunacaq.
    # --------------------------------------------------------
    def show_info(self):
        # self.get_name() — ana sinifdən miras alınmış getter metodu
        # çağırılır (GraduateStudent-in özündə "get_name" YAZILMAYIB,
        # amma miras vasitəsilə ona sahibdir)
        print("Student name:", self.get_name())
        print("University:", self._university)


def main():
    name = input("Enter student name: ")
    university = input("Enter university: ")

    # GraduateStudent obyekti yaradılır.
    # Bu, arxa planda İKİ addım işə salır:
    #   1) GraduateStudent.__init__ çağırılır
    #   2) O da öz növbəsində super().__init__() ilə Student.__init__-i çağırır
    student = GraduateStudent(name, university)

    # show_info() çağırılır — burada GraduateStudent-in ÖZ versiyası
    # işləyəcək (Student-dəki deyil, çünki override edilib).
    # Bu, Polymorphism-in canlı nümunəsidir: eyni adlı metod,
    # obyektin REAL TİPİNƏ görə FƏRQLİ DAVRANIR.
    student.show_info()


if __name__ == "__main__":
    main()
