# ============================================================================
#  PRACTICE 11 — CRUD (Create, Read, Update, Delete) menyu proqramı
# ----------------------------------------------------------------------------
#  Bu faylda öyrənəcəyimiz mövzular:
#    1) Siyahı (list) — birdən çox obyekti saxlamaq
#    2) Qlobal dəyişən (global variable) nədir?
#    3) while True + if/elif ilə sonsuz menyu necə yaradılır?
#    4) enumerate() ilə siyahını indekslə birlikdə gəzmək
#    5) del açar sözü ilə siyahıdan element silmək
# ============================================================================

class Student:

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # print(student) çağırıldıqda ekrana adın özü çıxacaq
    def __str__(self):
        return self._name


# ----------------------------------------------------------------------
# Bütün tələbələri saxlayan QLOBAL siyahı (Java-dakı ArrayList<Student> analoqu).
#
# "Qlobal" olması o deməkdir ki, bu dəyişən HƏR HANSI FUNKSİYANIN
# DAXİLİNDƏ YOX, faylın ƏN ÜST SƏVİYYƏSİNDƏ (indentasiyasız) təyin
# olunub, ona görə də faylın İÇİNDƏKİ BÜTÜN funksiyalar (add_student,
# show_students, rename_student, remove_student) bu siyahıya BİRBAŞA
# müraciət edə bilir.
#
# list — Python-un ən çox istifadə olunan "kolleksiya" tipidir.
# İçində istənilən sayda element saxlaya bilər, ölçüsü AVTOMATİK
# BÖYÜYÜR/KİÇİLİR (Java-dakı sabit ölçülü array-dən fərqli olaraq,
# Java-dakı ArrayList-ə bənzəyir).
# "[]" — boş siyahı yaratmağın ən sadə yoludur.
# ----------------------------------------------------------------------
students = []


# ---- tələbə əlavə etmək (CREATE) ----
def add_student():
    name = input("Tələbə adı daxil edin: ")
    # .append(...) — siyahının SONUNA yeni bir element ƏLAVƏ EDİR.
    # Burada yeni bir Student obyekti yaradılır və birbaşa siyahıya qoyulur.
    students.append(Student(name))
    print("Tələbə əlavə edildi.")


# ---- tələbələri göstərmək (READ) ----
def show_students():
    # "not students" — əgər siyahı BOŞDURSA True qaytarır
    # (boş siyahı Python-da "yalan"/falsy sayılır, eynilə boş mətn kimi)
    if not students:
        print("Tələbə yoxdur.")
        return  # funksiyadan erkən çıxırıq, aşağıdakı kod işləmir

    # --------------------------------------------------------
    # enumerate(students) — siyahının HƏR ELEMENTİNİ, onun İNDEKSİ
    # İLƏ BİRLİKDƏ qaytaran xüsusi funksiyadır.
    #
    # Adi "for student in students:" yazsaydıq, YALNIZ obyektləri
    # görərdik, indeksləri BİLMƏZDİK. enumerate() bizə hər ikisini
    # eyni anda verir:
    #     (0, birinci_tələbə), (1, ikinci_tələbə), (2, üçüncü_tələbə)...
    #
    # "for i, student in enumerate(students):" yazdıqda Python
    # avtomatik olaraq HƏR CÜTÜ İKİ AYRI DƏYİŞƏNƏ (i və student)
    # "AÇIR" (unpacking).
    # --------------------------------------------------------
    for i, student in enumerate(students):
        # f-string ilə indeks və tələbənin adı (student-in __str__
        # metodu vasitəsilə) bir sətirdə çap olunur
        print(f"{i} - {student}")


# ---- ad dəyişmək (UPDATE) ----
def rename_student():
    show_students()  # istifadəçiyə hansı indekslərin mövcud olduğunu göstərir

    # int(input(...)) — mətn kimi daxil edilən indeksi TAM ƏDƏDƏ çevirir
    index = int(input("İndeks daxil edin: "))
    new_name = input("Yeni ad daxil edin: ")

    # --------------------------------------------------------
    # students[index] — siyahıdan İNDEKSƏ GÖRƏ element seçmək.
    # Python-da (Java kimi) indekslər 0-dan başlayır: ilk element
    # students[0], ikinci students[1] və s.
    #
    # DİQQƏT: əgər istifadəçi mövcud olmayan bir indeks (məsələn,
    # siyahıda 3 element varkən 5) daxil etsə, bu sətir XƏTA
    # (IndexError) verəcək — bu proqramda bu HAL üçün əlavə yoxlama
    # YAZILMAYIB (orijinal Java kodunda da yox idi).
    # --------------------------------------------------------
    students[index].set_name(new_name)
    print("Ad dəyişdirildi.")


# ---- tələbə silmək (DELETE) ----
def remove_student():
    show_students()

    index = int(input("Silinəcək indeks: "))

    # --------------------------------------------------------
    # del — Python-un AÇAR SÖZÜDÜR (funksiya deyil), verilən
    # indeksdəki elementi siyahıdan TAMAMILƏ SİLİR.
    # Silindikdən sonra siyahının ölçüsü 1 vahid AZALIR və
    # silinən elementdən sonrakı bütün elementlərin indeksi
    # BİR VAHİD AŞAĞI SÜRÜŞÜR (avtomatik).
    # --------------------------------------------------------
    del students[index]
    print("Tələbə silindi.")


def main():
    # --------------------------------------------------------
    # while True: — şərti HƏMİŞƏ doğru olan SONSUZ dövr.
    # Bu, bir "menyu" proqramı üçün TİPİK BİR ÜSULDUR:
    # istifadəçi "0" seçənə qədər menyunu TƏKRAR-TƏKRAR göstər.
    #
    # Dövrdən çıxmaq üçün İÇƏRİDƏ "return" istifadə olunur
    # (istifadəçi "0" seçdikdə) — "break" də istifadə oluna bilərdi,
    # amma "return" burada həm dövrü, həm də funksiyanı bitirir.
    # --------------------------------------------------------
    while True:
        print("\n1 - Tələbə əlavə et")
        print("2 - Tələbələri göstər")
        print("3 - Ad dəyiş")
        print("4 - Tələbə sil")
        print("0 - Çıxış")

        choice = int(input("Seçim: "))

        # --------------------------------------------------------
        # Java-dakı switch/case-in Python-dakı ƏN YAYĞIN analoqu
        # if/elif ZƏNCİRİDİR (Python 3.10+ versiyalarında "match/case"
        # sintaksisi də var, amma if/elif HƏR Python versiyasında işləyir
        # və başlanğıc səviyyə üçün daha aydındır).
        #
        # Python YUXARIDAN AŞAĞI, HANSI ŞƏRT İLK DOĞRU ÇIXARSA,
        # ONUN bloku icra olunur, QALANLARI YOXLANMIR (Java-dakı
        # "break" olmadan switch-in "fall-through" davranışı Python-da
        # YOXDUR — hər elif AYRI-AYRI yoxlanılır).
        # --------------------------------------------------------
        if choice == 1:
            add_student()
        elif choice == 2:
            show_students()
        elif choice == 3:
            rename_student()
        elif choice == 4:
            remove_student()
        elif choice == 0:
            print("Proqram bitdi.")
            return  # main() funksiyasından çıxır, deməli proqram da BİTİR
        else:
            # Yuxarıdakı HEÇ BİR şərtə uyğun gəlməyən HƏR HANSI dəyər üçün
            print("Yanlış seçim.")


if __name__ == "__main__":
    main()
