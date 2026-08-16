# ============================================================================
#  PRACTICE 4 — İstifadəçi girişi (input) ilə işləmək
# ----------------------------------------------------------------------------
#  Bu faylda öyrənəcəyimiz mövzular:
#    1) input() funksiyası ilə klaviaturadan mətn oxumaq
#    2) __str__ ilə obyekti oxunaqlı formada çap etmək
#    3) Dinamik (istifadəçi tərəfindən daxil edilən) məlumatla
#       obyekt yaratmaq
# ============================================================================

class Student:

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Bu dəfə __str__ sadəcə adın özünü qaytarır (əlavə "Student name:"
    # mətni yoxdur — Practice 3-dəkindən fərqli olaraq)
    def __str__(self):
        return self._name


# Obyektin adını dəyişən köməkçi funksiya
def rename(student, new_name):
    student.set_name(new_name)


def main():
    # ------------------------------------------------------------
    # input(prompt) — Python-un DAXİLİ (built-in) funksiyasıdır.
    #
    # İşləmə prinsipi:
    #   1) Mötərizə içindəki mətn ("Enter the name of the student: ")
    #      ekrana çıxarılır, İSTİFADƏÇİDƏN GİRİŞ GÖZLƏNİLİR
    #      (proqram burada DAYANIR)
    #   2) İstifadəçi klaviaturadan nəsə yazıb Enter düyməsini basır
    #   3) Yazılan mətn (Enter-ə qədər olan hissə) FUNKSİYANIN NƏTİCƏSİ
    #      kimi geri qaytarılır və "student_name" dəyişəninə yazılır
    #
    # Bu, Java-dakı bu iki sətrə DƏQİQ bərabərdir:
    #     Scanner scanner = new Scanner(System.in);
    #     String studentName = scanner.nextLine();
    #
    # input() HƏMİŞƏ mətn (str) tipində dəyər qaytarır — əgər rəqəm
    # daxil edilsə belə, Python onu "avtomatik" ədədə çevirmir,
    # bunun üçün ayrıca int(...) və ya float(...) çağırmaq lazımdır
    # (bunu digər fayllarda görəcəyik).
    # ------------------------------------------------------------
    student_name = input("Enter the name of the student: ")

    # Daxil edilən adla yeni Student obyekti yaradılır
    student = Student(student_name)

    # print("Current name:", student) — burada iki dəyər verilib:
    # sabit mətn "Current name:" və "student" obyekti.
    # print() bunları BOŞLUQLA ayıraraq çap edir, "student" hissəsi
    # üçün avtomatik olaraq __str__ metodu çağırılır.
    print("Current name:", student)

    # Yeni ad üçün təkrar giriş alınır
    new_name = input("Enter the new name of the student: ")

    # rename funksiyası vasitəsilə obyektin adı yenilənir.
    # Diqqət: "student" dəyişəni HƏMİN OBYEKTƏ işarə etməyə davam edir,
    # sadəcə onun DAXİLİNDƏKİ "_name" sahəsi dəyişib.
    rename(student, new_name)

    # Yenilənmiş adla obyekt yenidən çap olunur
    print("New name:", student)


if __name__ == "__main__":
    main()
