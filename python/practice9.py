# ============================================================================
#  PRACTICE 9 — Validasiya (input yoxlaması) ilə tam nümunə
# ----------------------------------------------------------------------------
#  Bu, ən əvvəlki nümunələrin (abstraction + inheritance + polymorphism +
#  encapsulation) HAMISINI BİR YERƏ toplayan, üstəlik istifadəçi
#  girişini YOXLAYAN (validasiya edən) TAM bir proqramdır.
#
#  Yeni mövzular:
#    1) re modulu (regular expressions / requlyar ifadələr) nədir?
#    2) while dövrü ilə "düzgün giriş alınana qədər soruş" məntiqi
#    3) strip() ilə boşluqları təmizləmək
#    4) continue açar sözü ilə dövrün əvvəlinə qayıtmaq
# ============================================================================

import re  # re — Python-un STANDART kitabxanasında olan, requlyar
#            ifadələrlə (mətn şablonları ilə) işləmək üçün modul
from abc import ABC, abstractmethod


# Abstrakt sinif (Abstraction)
# Bu sinif birbaşa obyekt yaratmaq üçün deyil,
# digər siniflər üçün baza rolunu oynayır
class Student(ABC):

    # Encapsulation (İnkapsulyasiya) — 4 "daxili" sahə
    def __init__(self, name, surname, phone_number, email):
        self._name = name
        self._surname = surname
        self._phone_number = phone_number
        self._email = email

    # ---- Getter-lər — sahə dəyərlərini oxumaq üçün ----
    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_phone_number(self):
        return self._phone_number

    def get_email(self):
        return self._email

    # ---- Setter-lər — sahə dəyərlərini dəyişmək üçün ----
    def set_name(self, name):
        self._name = name

    def set_surname(self, surname):
        self._surname = surname

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_email(self, email):
        self._email = email

    # Abstrakt metod — hər alt sinif öz implementasiyasını yazmalıdır
    @abstractmethod
    def show_info(self):
        pass


# Inheritance (İrsiyyət)
# GraduateStudent sinifi Student sinifindən miras alır
class GraduateStudent(Student):

    # Bu sinifə məxsus əlavə sahə — universitetin adı
    def __init__(self, name, surname, phone_number, email, university):
        super().__init__(name, surname, phone_number, email)
        self._university = university

    # Abstrakt metodun implementasiyası (Polymorphism)
    def show_info(self):
        print(f"Name: {self.get_name()} {self.get_surname()}")
        print(f"Phone: {self.get_phone_number()}")
        print(f"Email: {self.get_email()}")
        print(f"University: {self._university}")


# Inheritance (İrsiyyət) — 2-ci səviyyə
# PhDStudent sinifi GraduateStudent sinifindən miras alır.
# Beləliklə Student -> GraduateStudent -> PhDStudent zənciri yaranır
class PhDStudent(GraduateStudent):

    # Bu sinifə məxsus əlavə sahə — tədqiqat mövzusu
    def __init__(self, name, surname, phone_number, email, university, research_topic):
        super().__init__(name, surname, phone_number, email, university)
        self._research_topic = research_topic

    # Method Overriding (Polymorphism)
    def show_info(self):
        super().show_info()  # ana sinifin BÜTÜN məlumatını əvvəlcə çap edir
        print(f"Research Topic: {self._research_topic}")


# ============================================================================
#  KÖMƏKÇİ (helper) FUNKSİYALAR — validasiya ilə giriş almaq üçün
#  Bu funksiyalar sinif deyil, sadəcə YENİDƏN İSTİFADƏ oluna bilən
#  "alət" funksiyalarıdır. Kod TƏKRARLANMASIN deyə ayrıca yazılıblar.
# ============================================================================

def read_non_empty_input(prompt):
    # --------------------------------------------------------
    # Bu funksiya istifadəçidən BOŞ OLMAYAN mətn alana qədər
    # sual verməyə DAVAM EDİR — yəni "sonsuz dövr, düzgün cavab
    # alınanda özü DAYANIR" məntiqi.
    # --------------------------------------------------------
    while True:  # "True" HƏMİŞƏ doğrudur, ona görə bu, SONSUZ dövrdür —
        #          dövrdən yalnız "return" ilə çıxmaq olar
        value = input(prompt).strip()
        # .strip() — mətnin ƏVVƏLİNDƏKİ və SONUNDAKI boşluq/tab/yeni-sətir
        # simvollarını təmizləyir. Məsələn "  Ali  " -> "Ali" olur.
        # Bu, istifadəçinin təsadüfən əlavə boşluq yazmasının qarşısını alır.

        if value:  # BOŞ MƏTN Python-da "yalan" (falsy) sayılır,
            #        yəni "if value:" əslində "if value != '':" ilə eynidir
            return value  # düzgün dəyər tapıldı, funksiyadan bu dəyərlə çıxırıq

        # Əgər buraya çatdıqsa, deməli "value" boş idi —
        # xəbərdarlıq mesajı çap olunur və dövr TƏKRAR BAŞLAYIR
        # (yeni sual veriləcək)
        print("Invalid entry: this field cannot be empty. Please enter a valid value.")


def is_valid_phone(phone):
    # --------------------------------------------------------
    # re.match(pattern, text) — "text" mətninin ƏVVƏLİNDƏN başlayaraq
    # "pattern" şablonuna uyğun gəlib-gəlmədiyini yoxlayır.
    # Uyğun gəlirsə bir "Match" obyekti, gəlmirsə "None" qaytarır.
    #
    # Şablon izahı: r"^\+?[0-9\-\s]{7,20}$"
    #   r"..."      -> "raw string" — mətn daxilindəki \ işarələrinin
    #                  Python tərəfindən xüsusi məna daşımamasını təmin edir
    #   ^           -> mətnin BAŞLANĞICI
    #   \+?         -> ixtiyari (?) olaraq BİR "+" işarəsi ola bilər
    #   [0-9\-\s]   -> BU SİNİFDƏKİ simvollardan biri: rəqəm (0-9),
    #                  tire (-) və ya boşluq (\s)
    #   {7,20}      -> yuxarıdakı simvol sinfindən 7 İLƏ 20 ARASI say
    #   $           -> mətnin SONU
    #
    # Yəni: "istəyə bağlı + işarəsi ilə başlayan, sonra 7-20 arası
    # rəqəm/tire/boşluqdan ibarət mətn" formatını yoxlayır.
    #
    # "is not None" — əgər uyğunluq tapılıbsa (None deyilsə) True,
    # tapılmayıbsa (None-dursa) False qaytarır.
    # --------------------------------------------------------
    return re.match(r"^\+?[0-9\-\s]{7,20}$", phone) is not None


def is_valid_email(email):
    # --------------------------------------------------------
    # Şablon izahı: r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    #   ^[^\s@]+    -> mətnin əvvəlində, BOŞLUQ VƏ "@" OLMAYAN,
    #                  ən azı 1 simvoldan ibarət hissə (istifadəçi adı)
    #   @           -> tam olaraq BİR "@" işarəsi
    #   [^\s@]+     -> domen adı hissəsi (yenə boşluq/@ olmadan)
    #   \.          -> NÖQTƏ işarəsi (\. yazılıb, çünki tək "." regex-də
    #                  "İSTƏNİLƏN SİMVOL" mənasını verir, biz isə
    #                  HƏQİQİ nöqtəni axtarırıq)
    #   [^\s@]+$    -> domen uzantısı (com, az, org və s.), mətnin SONU
    #
    # Misal uyğunluq: "user@example.com" -> DÜZGÜN
    # Misal uyğunsuzluq: "user@@example" -> SƏHV (iki @ var, nöqtə yoxdur)
    # --------------------------------------------------------
    return re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", email) is not None


def read_valid_phone(prompt):
    # Düzgün formatda telefon nömrəsi daxil edilənə qədər TƏKRAR SORĞU EDİR
    while True:
        phone = input(prompt).strip()

        if not phone:  # "not phone" -> phone boşdursa True
            print("Invalid entry: phone number cannot be empty.")
            # ------------------------------------------------
            # continue — dövrün QALAN HİSSƏSİNİ ATLAYIR və birbaşa
            # "while True:" sətrinə QAYIDIR, yəni YENİ sual verir.
            # Bu, "return" DEYİL — funksiyadan çıxmır, sadəcə
            # bu dövr addımını erkən bitirir.
            # ------------------------------------------------
            continue

        if is_valid_phone(phone):
            return phone  # format düzgündür, funksiyadan çıxırıq

        # Buraya çatdıqsa: phone boş DEYİL, amma format YANLIŞDIR
        print("Invalid phone number. Use digits, spaces, dashes, and optional leading +.")


def read_valid_email(prompt):
    # Eyni məntiq, email üçün
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
