# ============================================================================
#  PRACTICE 3 — __str__ metodu (Java-dakı toString() analoqu)
# ----------------------------------------------------------------------------
#  Bu faylda öyrənəcəyimiz mövzular:
#    1) Obyekti birbaşa print() etdikdə nə baş verir?
#    2) __str__ xüsusi (magic) metodu nədir və necə işləyir?
#    3) Sinif metodunu başqa funksiyaya ötürüb polymorphism-ə hazırlıq
# ============================================================================

class Student:

    # Konstruktor — obyekt yaradılarkən adı təyin edir
    def __init__(self, name):
        # "_name" — encapsulation üçün "daxili" sahə (bax: Practice 2-dəki izah)
        self._name = name

    # Getter — name sahəsini oxumaq üçün
    def get_name(self):
        return self._name

    # Setter — name sahəsini dəyişmək üçün
    def set_name(self, name):
        self._name = name

    # ------------------------------------------------------------
    # __str__ — Python-un DAHA BİR xüsusi (magic/dunder) metodudur.
    #
    # NORMALDA, əgər bir sinifdə __str__ metodu YAZILMASAYDI, "print(obyekt)"
    # yazdıqda ekranda bu cür bir şey görərdik:
    #     <__main__.Student object at 0x000001A2B3C4D5E6>
    # Yəni obyektin yaddaşdakı texniki ünvanı — bu, insan üçün faydasız
    # bir məlumatdır.
    #
    # __str__ metodunu yazmaqla biz Python-a deyirik:
    #     "Bu obyekt print() edilmək istəndikdə, mənim yazdığım BU
    #      METODU çağır və onun QAYTARDIĞI MƏTNİ göstər."
    #
    # Bu, DƏQİQ olaraq Java-dakı toString() metodunun etdiyi işdir —
    # Java-da da System.out.println(obyekt) çağırıldıqda avtomatik
    # olaraq obyektin toString() metodu işə düşür.
    #
    # "return" açar sözü ilə bu metod bir mətn (string) dəyəri geri qaytarır.
    # ------------------------------------------------------------
    def __str__(self):
        # "+" operatoru burada İKİ MƏTNİ (string) BİRLƏŞDİRMƏK üçün
        # istifadə olunur (Java-dakı "+" ilə string concatenation eynidir)
        return "Student name: " + self._name


# --------------------------------------------------------------------------
# rename — Student obyektini qəbul edib adını dəyişən funksiya.
# Bu funksiya İSTƏNİLƏN Student-tipli obyektlə işləyə bilər — bu,
# Polymorphism-in sadə bir formasıdır: eyni funksiya müxtəlif
# obyektlərlə (hətta Student-dən miras alan alt siniflərin obyektləri
# ilə də) işləyə bilər, çünki hamısında set_name() metodu mövcuddur.
# --------------------------------------------------------------------------
def rename(student, new_name):
    student.set_name(new_name)


def main():
    # Yeni obyekt yaradılır, "John" adı ilə
    student1 = Student("John")

    # print(student1) çağırıldıqda Python arxa planda AVTOMATİK olaraq
    # student1.__str__() metodunu çağırır və onun qaytardığı mətni çap edir.
    # Nəticədə ekranda: "Student name: John" görünəcək.
    print(student1)

    # rename funksiyası çağırılır — student1 obyektinin "_name" sahəsi
    # "Doe" olaraq dəyişdirilir (setter vasitəsilə)
    rename(student1, "Doe")

    # Yenidən print(student1) — bu dəfə __str__ yenilənmiş adı qaytaracaq:
    # "Student name: Doe"
    print(student1)


if __name__ == "__main__":
    main()
