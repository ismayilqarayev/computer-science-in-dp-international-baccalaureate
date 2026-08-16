# ============================================================================
#  MAIN — Tam nümunə: Abstraction + Inheritance + Polymorphism
#         + Encapsulation + validasiya (bütün OOP əsasları BİR YERDƏ)
# ----------------------------------------------------------------------------
#  Bu fayl demo/Main.java-nın Python versiyasıdır və Practice 9 ilə
#  demək olar EYNİDİR — bu, kursun "final" (ən tam) nümunəsidir,
#  bütün öyrənilmiş OOP anlayışlarını bir proqramda birləşdirir:
#     - Abstraction (ABC, @abstractmethod)
#     - Encapsulation ("_" prefiksli sahələr + getter/setter)
#     - Inheritance (Student -> GraduateStudent -> PhDStudent)
#     - Polymorphism (show_info() metodunun hər sinifdə fərqli işləməsi)
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
# bu sinifdən birbaşa "Student(...)" yazaraq obyekt yaratmaq MÜMKÜN
# OLMAYACAQ — Python bunu XƏTA ilə əngəlləyəcək.
class Student(ABC):

    # ------------------------------------------------------------------
    # Encapsulation (İnkapsulyasiya)
    # Bütün sahələr "_" ilə başlayır — bu, onların sinifin "daxili detalı"
    # olduğunu, xaricdən BİRBAŞA yox, getter/setter vasitəsilə
    # dəyişdirilməli olduğunu bildirir.
    #
    # Konstruktor DÖRD parametr qəbul edir və hamısını AYRI-AYRI
    # sahələrə yazır.
    # ------------------------------------------------------------------
    def __init__(self, name, surname, phone_number, email):
        self._name = name
        self._surname = surname
        self._phone_number = phone_number
        self._email = email

    # ---- Getter-lər — hər sahə üçün AYRI bir "oxu" metodu ----
    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_phone_number(self):
        return self._phone_number

    def get_email(self):
        return self._email

    # ---- Setter-lər — hər sahə üçün AYRI bir "yaz" metodu ----
    def set_name(self, name):
        self._name = name

    def set_surname(self, surname):
        self._surname = surname

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_email(self, email):
        self._email = email

    # ------------------------------------------------------------------
    # Abstrakt metod — hər alt sinif öz implementasiyasını yazmalıdır.
    # Bu, "bütün Student-lər show_info() metoduna sahib OLMALIDIR,
    # amma HƏR BİRİ onu ÖZ ÜSULU İLƏ yazacaq" fikrini ifadə edir —
    # bu, POLYMORPHISM-in TƏMƏLİDİR.
    # ------------------------------------------------------------------
    @abstractmethod
    def show_info(self):
        pass


# ══════════════════════════════════════════════════════════════════════════
#  Inheritance (İrsiyyət) — 1-Cİ SƏVİYYƏ
# ══════════════════════════════════════════════════════════════════════════
class GraduateStudent(Student):

    def __init__(self, name, surname, phone_number, email, university):
        # super() ilə Student-in konstruktoru çağırılır, 4 parametr ötürülür
        super().__init__(name, surname, phone_number, email)
        # Bu sinifə MƏXSUS əlavə sahə
        self._university = university

    # Abstrakt metodun implementasiyası (Polymorphism)
    def show_info(self):
        # f-string-lər içində getter metodları çağırılır —
        # birbaşa self._name yerinə self.get_name() istifadə olunur,
        # bu, ENCAPSULATION prinsipinə hörmət göstərməkdir
        print(f"Name: {self.get_name()} {self.get_surname()}")
        print(f"Phone: {self.get_phone_number()}")
        print(f"Email: {self.get_email()}")
        print(f"University: {self._university}")


# ══════════════════════════════════════════════════════════════════════════
#  Inheritance (İrsiyyət) — 2-Cİ SƏVİYYƏ
#  PhDStudent -> GraduateStudent -> Student ZƏNCİRİ
# ══════════════════════════════════════════════════════════════════════════
class PhDStudent(GraduateStudent):

    def __init__(self, name, surname, phone_number, email, university, research_topic):
        # GraduateStudent-in konstruktoru çağırılır (5 parametr) —
        # o da öz növbəsində Student-in konstruktorunu çağıracaq
        super().__init__(name, surname, phone_number, email, university)
        self._research_topic = research_topic

    # Method Overriding (Polymorphism)
    def show_info(self):
        super().show_info()  # GraduateStudent-in show_info()-u ƏVVƏLCƏ işə düşür
        print(f"Research Topic: {self._research_topic}")  # sonra əlavə sətir çap olunur


# ══════════════════════════════════════════════════════════════════════════
#  VALİDASİYA FUNKSİYALARI — istifadəçi girişini yoxlamaq üçün
#  Bunlar sinif DEYİL, sərbəst funksiyalardır — hər hansı bir obyektə
#  "bağlı" olmadıqları üçün sinif daxilinə YAZILMASINA EHTİYAC YOXDUR
# ══════════════════════════════════════════════════════════════════════════

def read_non_empty_input(prompt):
    # Boş mətn qəbul olunmayana qədər TƏKRAR-TƏKRAR soruşur
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Invalid entry: this field cannot be empty. Please enter a valid value.")


def is_valid_phone(phone):
    # Telefon nömrəsi: əvvəlində İSTƏYƏ BAĞLI "+" , sonra 7-20 arası
    # rəqəm/tire/boşluq simvolu (ətraflı izah üçün bax: practice9.py)
    return re.match(r"^\+?[0-9\-\s]{7,20}$", phone) is not None


def is_valid_email(email):
    # Email formatı: "nəsə@nəsə.nəsə" şəklində olmalıdır
    return re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", email) is not None


def read_valid_phone(prompt):
    while True:
        phone = input(prompt).strip()
        if not phone:
            print("Invalid entry: phone number cannot be empty.")
            continue  # dövrün əvvəlinə qayıdır, yeni sual verir
        if is_valid_phone(phone):
            return phone
        print("Invalid phone number. Use digits, spaces, dashes, and optional leading +.")


def read_valid_email(prompt):
    while True:
        email = input(prompt).strip()
        if not email:
            print("Invalid entry: email cannot be empty.")
            continue
        if is_valid_email(email):
            return email
        print("Invalid email format. Example: user@example.com")


def main():
    # ── Graduate Student məlumatlarının daxil edilməsi ──────────────
    print("Graduate student data entry:")
    gs_name = read_non_empty_input("Enter the name of the graduate student: ")
    gs_surname = read_non_empty_input("Enter the surname of the graduate student: ")
    gs_phone = read_valid_phone("Enter the phone number of the graduate student: ")
    gs_email = read_valid_email("Enter the email of the graduate student: ")
    gs_university = read_non_empty_input("Enter the university of the graduate student: ")

    # --------------------------------------------------------
    # Diqqət: "Student" tipli ABSTRAKT sinifdən DEYİL, konkret
    # GraduateStudent sinifindən obyekt yaradılır — çünki Student
    # abstraktdır və obyekt YARADA BİLMƏZ (Python bunu qadağan edər).
    # --------------------------------------------------------
    graduate_student = GraduateStudent(gs_name, gs_surname, gs_phone, gs_email, gs_university)
    print()
    graduate_student.show_info()

    # ── PhD Student məlumatlarının daxil edilməsi ───────────────────
    print()
    print("PhD student data entry:")
    phd_name = read_non_empty_input("Enter the name of the PhD student: ")
    phd_surname = read_non_empty_input("Enter the surname of the PhD student: ")
    phd_phone = read_valid_phone("Enter the phone number of the PhD student: ")
    phd_email = read_valid_email("Enter the email of the PhD student: ")
    phd_university = read_non_empty_input("Enter the university of the PhD student: ")
    phd_research_topic = read_non_empty_input("Enter the research topic of the PhD student: ")

    phd_student = PhDStudent(phd_name, phd_surname, phd_phone, phd_email, phd_university, phd_research_topic)
    print()
    phd_student.show_info()


if __name__ == "__main__":
    main()
