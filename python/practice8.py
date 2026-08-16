# ============================================================================
#  PRACTICE 8 — 3 səviyyəli irsiyyət zənciri
# ----------------------------------------------------------------------------
#  Mövzu: Student -> GraduateStudent -> PhDStudent
#  (hər sinif ÖZÜNDƏN ƏVVƏLKİNDƏN miras alır — bu, "ÇOX SƏVİYYƏLİ
#  İRSİYYƏT" (multi-level inheritance) adlanır)
#
#  Fərq Practice 6/7-dən: orada PhDStudent BİRBAŞA Student-dən miras
#  alırdı (iki sinif QARDAŞ idi). Burada isə PhDStudent, GraduateStudent-
#  dən miras alır — yəni PhDStudent "GraduateStudent-in bir NÖVÜDÜR",
#  o da öz növbəsində "Student-in bir NÖVÜDÜR".
# ============================================================================

from abc import ABC, abstractmethod

# Bu sinif bir tələbənin ÜMUMİ xüsusiyyətlərini və davranışlarını təyin edir.
# Abstract olduğu üçün BİRBAŞA obyekt yaradıla bilməz.
# Bu sinifdən törədilmiş siniflər öz spesifik xüsusiyyətlərini əlavə edə
# və show_info metodunu implementasiya edə bilərlər.
# Bu, Polymorphism və Inheritance konseptlərini nümayiş etdirir.


# Abstrakt sinif (Abstraction)
# Bu sinif birbaşa obyekt yaratmaq üçün deyil,
# digər siniflər üçün BAZA rolunu oynayır
class Student(ABC):

    # Encapsulation (İnkapsulyasiya)
    # _name dəyişəni "daxili" sahədir — birbaşa xaricdən dəyişdirilməməlidir,
    # bunun üçün aşağıdakı getter/setter metodları var
    def __init__(self, name):
        self._name = name

    # Getter — name dəyərini oxumaq üçün
    def get_name(self):
        return self._name

    # Setter — name dəyərini dəyişmək üçün
    def set_name(self, name):
        self._name = name

    # Abstrakt metod — hər alt sinif öz implementasiyasını yazmalıdır
    @abstractmethod
    def show_info(self):
        pass


# --------------------------------------------------------------------------
# Inheritance (İrsiyyət) — 1-Cİ SƏVİYYƏ
# GraduateStudent sinifi Student sinifindən miras alır
# --------------------------------------------------------------------------
class GraduateStudent(Student):

    # Bu sinifə məxsus ƏLAVƏ sahə — universitetin adı
    def __init__(self, name, university):
        super().__init__(name)  # Student sinifinin konstruktorunu çağırır
        self._university = university

    # Abstrakt metodun implementasiyası (Polymorphism)
    def show_info(self):
        # name-ə birbaşa YOX, getter vasitəsilə müraciət edilir (Encapsulation)
        print("Name:", self.get_name())
        print("University:", self._university)


# --------------------------------------------------------------------------
# Inheritance (İrsiyyət) — 2-Cİ SƏVİYYƏ
# PhDStudent sinifi Student-dən YOX, birbaşa GraduateStudent sinifindən
# miras alır.
#
# Beləliklə Student -> GraduateStudent -> PhDStudent ZƏNCİRİ yaranır —
# yəni PhDStudent həm GraduateStudent-in, həm də (DOLAYI YOLLA,
# GraduateStudent vasitəsilə) Student-in BÜTÜN sahə və metodlarına
# sahibdir. Bu, "ƏCDAD-NƏVƏ" münasibətinə bənzəyir: PhDStudent
# GraduateStudent-in "övladı", Student-in isə "nəvəsidir".
# --------------------------------------------------------------------------
class PhDStudent(GraduateStudent):

    # Bu sinifə məxsus əlavə sahə — tədqiqat mövzusu
    def __init__(self, name, university, research_topic):
        # --------------------------------------------------------
        # super().__init__(name, university) burada GraduateStudent-in
        # konstruktorunu çağırır.
        #
        # GraduateStudent-in konstruktoru İSƏ öz növbəsində
        # super().__init__(name) ilə Student-in konstruktorunu çağırır.
        #
        # Beləliklə bir PhDStudent yaradıldıqda ARDICIL OLARAQ:
        #   PhDStudent.__init__ -> GraduateStudent.__init__ -> Student.__init__
        # ZƏNCİRVARİ ÇAĞIRIŞ baş verir, hər addımda öz sahəsi qurulur.
        # --------------------------------------------------------
        super().__init__(name, university)
        self._research_topic = research_topic

    # --------------------------------------------------------
    # Method Overriding (Polymorphism)
    # GraduateStudent-dəki show_info() metodu burada GENİŞLƏNDİRİLİR
    # (tamam ƏVƏZLƏNMİR — köhnə versiya da içəridə İSTİFADƏ OLUNUR).
    # --------------------------------------------------------
    def show_info(self):
        # Əvvəlcə ana sinifin (GraduateStudent) show_info() metodu çağırılır —
        # bu, "Name" və "University" sətirlərini çap edir.
        # Diqqət: bu, öz növbəsində Student-in getter-lərindən istifadə edir,
        # amma Student-in ÖZ show_info()-u YOXDUR (o abstraktdır),
        # ona görə burada GraduateStudent-in versiyası işə düşür.
        super().show_info()

        # Sonra BU sinifə (PhDStudent-ə) məxsus əlavə məlumat çap olunur
        print("Research Topic:", self._research_topic)  # əlavə məlumat


def main():
    # ── Graduate Student məlumatlarının daxil edilməsi ──────────────
    gs_name = input("Enter the name of the graduate student: ")
    gs_university = input("Enter the university of the graduate student: ")

    # Polymorphism — "graduate_student" dəyişəni konseptual olaraq
    # HƏM GraduateStudent, HƏM DƏ Student sayıla bilər (çünki miras var)
    graduate_student = GraduateStudent(gs_name, gs_university)

    # show_info() çağırılır — hansı sinifin metodu işə düşdüyü
    # obyektin REAL TİPİNƏ (runtime-da müəyyən olunan tip) görə seçilir
    graduate_student.show_info()

    # ── PhD Student məlumatlarının daxil edilməsi ───────────────────
    phd_name = input("Enter the name of the PhD student: ")
    phd_university = input("Enter the university of the PhD student: ")
    phd_research_topic = input("Enter the research topic of the PhD student: ")

    # Polymorphism — PhDStudent obyekti yaradılır.
    # Bu obyekt EYNİ ZAMANDA GraduateStudent VƏ Student sayıla bilər
    # (çünki irsiyyət zənciri var: PhDStudent -> GraduateStudent -> Student)
    phd_student = PhDStudent(phd_name, phd_university, phd_research_topic)

    # show_info() çağırılır — bu dəfə PhDStudent-in OVERRIDE EDİLMİŞ
    # (həm də daxilində GraduateStudent-in metodunu ÇAĞIRAN) versiyası işləyir
    phd_student.show_info()


if __name__ == "__main__":
    main()
