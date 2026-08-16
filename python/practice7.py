# ============================================================================
#  PRACTICE 7 — Abstraction + istifadəçi girişi ilə birlikdə
# ----------------------------------------------------------------------------
#  Bu fayl Practice 6-nın DAVAMIDIR — eyni abstrakt sinif quruluşu,
#  amma bu dəfə obyektlərin məlumatları SABİT (hardcoded) DEYİL,
#  istifadəçidən input() vasitəsilə DİNAMİK olaraq alınır.
# ============================================================================

from abc import ABC, abstractmethod


# Abstrakt baza sinif — bütün "Student" tiplərinin ORTAQ hissəsi bu sinifdə
class Student(ABC):

    def __init__(self, name):
        self._name = name  # encapsulation: "_" ilə "daxili sahə" işarələnir

    def get_name(self):
        return self._name

    # Bu metodun gövdəsi (bədəni) YOXDUR — hər alt sinif ÖZÜ yazmalıdır.
    # Əgər alt sinif bunu yazmasa, Python obyekt yaratmağa İCAZƏ VERMƏYƏCƏK.
    @abstractmethod
    def show_info(self):
        pass


# Birinci alt sinif — universitet (bakalavr/magistr) tələbəsi
class GraduateStudent(Student):

    def __init__(self, name, university):
        super().__init__(name)  # ana sinifin konstruktoru işə salınır
        self._university = university

    def show_info(self):
        print("Graduate Student:", self.get_name())
        print("University:", self._university)


# İkinci alt sinif — doktorantura tələbəsi
class PhDStudent(Student):

    def __init__(self, name, research_field):
        super().__init__(name)
        self._research_field = research_field

    def show_info(self):
        print("PhD Student:", self.get_name())
        print("Research Field:", self._research_field)


def main():
    # --------------------------------------------------------
    # Birinci obyekt — GraduateStudent — istifadəçi girişindən yaradılır.
    #
    # Diqqət: iki dəfə input() çağırılır, ARDICIL OLARAQ.
    # Proqram birinci sualı verir, cavab gözləyir, sonra ikinci sualı verir.
    # --------------------------------------------------------
    name = input("Enter graduate student name: ")
    university = input("Enter university: ")

    student = GraduateStudent(name, university)
    student.show_info()

    print()  # ekranda boş sətir — iki nəticəni vizual olaraq ayırmaq üçün

    # --------------------------------------------------------
    # İkinci obyekt — PhDStudent — yenə istifadəçi girişindən yaradılır.
    # Dəyişən adları fərqlidir (phd_name, research_field), çünki
    # "name" adı artıq yuxarıda istifadə olunub və onu YENİDƏN İSTİFADƏ
    # ETSƏYDİK, əvvəlki dəyəri ÜSTÜNDƏN YAZARDI (bu, səhv olmazdı, amma
    # kodu daha az oxunaqlı edərdi).
    # --------------------------------------------------------
    phd_name = input("Enter PhD student name: ")
    research_field = input("Enter research field: ")

    phd = PhDStudent(phd_name, research_field)
    phd.show_info()


if __name__ == "__main__":
    main()
