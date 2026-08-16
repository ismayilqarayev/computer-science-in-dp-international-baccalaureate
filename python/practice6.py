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
# Abtract class Student
#
# NİYƏ ABSTRAKT SİNİF LAZIMDIR?
# Təsəvvür edin ki, "Tələbə" anlayışı özlüyündə "natamam"dır — real
# həyatda sırf "Tələbə" deyə bir şey yoxdur, HƏR tələbə ya bakalavr,
# ya magistr, ya da doktoranturadadır (konkret bir NÖVDÜR).
# "Student" sinfini abstrakt etməklə biz deyirik:
#     "Bu sinifin özündən BİRBAŞA obyekt yaratmaq MƏNTİQSİZDİR,
#      YALNIZ ondan miras alan KONKRET siniflər (GraduateStudent,
#      PhDStudent) obyekt yarada bilər."
#
# ABC-dən miras almaqla (class Student(ABC):) sinif "abstrakt" statusu
# qazanır.
# --------------------------------------------------------------------------
class Student(ABC):

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    # --------------------------------------------------------
    # @abstractmethod — bu, DEKORATORDUR (metodun üstündə "@" ilə yazılır).
    #
    # Dekoratorun mənası: "aşağıdakı metodu XÜSUSİ QAYDA ilə işlət".
    # @abstractmethod bu metodu "MƏCBURİ OVERRIDE OLUNMALI" elan edir.
    #
    # NƏTİCƏ:
    #   - Əgər GraduateStudent (və ya hər hansı digər alt sinif)
    #     show_info() metodunu ÖZÜ YAZMASA, Python ondan obyekt
    #     yaratmağa İCAZƏ VERMƏYƏCƏK və xəta buraxacaq:
    #         TypeError: Can't instantiate abstract class ... with
    #         abstract method show_info
    #
    # "pass" — bu metodun burada heç bir real kodu (gövdəsi) yoxdur,
    # sadəcə onun "İMZASINI" (adını və parametrlərini) göstərir.
    # "pass" Python-da "heç nə etmə, sadəcə bura boş qalmasın deyə
    # yazılıb" mənasını verən açar sözdür.
    # --------------------------------------------------------
    @abstractmethod
    def show_info(self):
        pass


# --------------------------------------------------------------------------
# Student-dən miras alan BİRİNCİ konkret (real obyekt yaradıla bilən) sinif
# --------------------------------------------------------------------------
class GraduateStudent(Student):

    def __init__(self, name, university):
        super().__init__(name)  # ana sinifin konstruktoru çağırılır
        self._university = university

    # Abstrakt metodun KONKRET İMPLEMENTASİYASI.
    # Məhz bu metod yazıldığı üçün GraduateStudent sinifindən artıq
    # obyekt yaratmaq mümkündür (bütün abstrakt metodlar "doldurulub").
    def show_info(self):
        print("Graduate Student:", self.get_name())
        print("University:", self._university)


# --------------------------------------------------------------------------
# Student-dən miras alan İKİNCİ konkret sinif.
# Diqqət: GraduateStudent-dən deyil, birbaşa Student-dən miras alır —
# yəni bu iki sinif (GraduateStudent və PhDStudent) BİR-BİRİNƏ QOHUM
# DEYİL, hər ikisi sadəcə eyni "ata"nın (Student) övladlarıdır.
# --------------------------------------------------------------------------
class PhDStudent(Student):

    def __init__(self, name, research_field):
        super().__init__(name)
        self._research_field = research_field

    def show_info(self):
        print("PhD Student:", self.get_name())
        print("Research Field:", self._research_field)


def main():
    name = input("Enter student name: ")
    university = input("Enter university: ")

    # ------------------------------------------------------------
    # Diqqət: "student" dəyişəni GraduateStudent TİPLİ bir obyektə
    # işarə edir, amma KONSEPTUAL olaraq o eyni zamanda "bir Student"
    # da sayılır (çünki GraduateStudent, Student-dən miras alıb).
    #
    # Bu, POLYMORPHISM-in başqa bir təzahürüdür: "bir GraduateStudent,
    # istənilən yerdə Student kimi də istifadə oluna bilər".
    # ------------------------------------------------------------
    student = GraduateStudent(name, university)
    student.show_info()

    print()  # ekranda boş bir sətir — vizual ayırma üçün

    # İkinci alt sinifdən obyekt yaradılır — bu dəfə dəyərlər
    # istifadəçidən yox, birbaşa kodun içində SABİT (hardcoded)
    # olaraq verilib
    phd = PhDStudent("Nigar", "Artificial Intelligence")
    phd.show_info()


if __name__ == "__main__":
    main()
