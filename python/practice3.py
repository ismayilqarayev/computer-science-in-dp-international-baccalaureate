# ============================================================================
#  PRACTICE 3 — __str__ metodu (Java-dakı toString() analoqu)
# ----------------------------------------------------------------------------
#  Bu faylda öyrənəcəyimiz mövzular:
#    1) Obyekti birbaşa print() etdikdə nə baş verir?
#    2) __str__ xüsusi (magic) metodu nədir və necə işləyir?
#    3) Sinif metodunu başqa funksiyaya ötürüb polymorphism-ə hazırlıq
# ============================================================================

class Telebe:

    # Konstruktor — obyekt yaradılarkən adı təyin edir
    def __init__(self, ad):
        # "_ad" — encapsulation üçün "daxili" sahə (bax: Practice 2-dəki izah)
        self._ad = ad

    # Getter — ad sahəsini oxumaq üçün
    def get_ad(self):
        return self._ad

    # Setter — ad sahəsini dəyişmək üçün
    def set_ad(self, ad):
        self._ad = ad

    # ------------------------------------------------------------
    # __str__ — Python-un DAHA BİR xüsusi (magic/dunder) metodudur.
    #
    # NORMALDA, əgər bir sinifdə __str__ metodu YAZILMASAYDI, "print(obyekt)"
    # yazdıqda ekranda bu cür bir şey görərdik:
    #     <__main__.Telebe object at 0x000001A2B3C4D5E6>
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
        return "Tələbənin adı: " + self._ad


# --------------------------------------------------------------------------
# adi_deyis — Telebe obyektini qəbul edib adını dəyişən funksiya.
# Bu funksiya İSTƏNİLƏN Telebe-tipli obyektlə işləyə bilər — bu,
# Polymorphism-in sadə bir formasıdır: eyni funksiya müxtəlif
# obyektlərlə (hətta Telebe-dən miras alan alt siniflərin obyektləri
# ilə də) işləyə bilər, çünki hamısında set_ad() metodu mövcuddur.
# --------------------------------------------------------------------------
def adi_deyis(telebe, yeni_ad):
    telebe.set_ad(yeni_ad)


def main():
    # Yeni obyekt yaradılır, "John" adı ilə
    telebe1 = Telebe("John")

    # print(telebe1) çağırıldıqda Python arxa planda AVTOMATİK olaraq
    # telebe1.__str__() metodunu çağırır və onun qaytardığı mətni çap edir.
    # Nəticədə ekranda: "Tələbənin adı: John" görünəcək.
    print(telebe1)

    # adi_deyis funksiyası çağırılır — telebe1 obyektinin "_ad" sahəsi
    # "Doe" olaraq dəyişdirilir (setter vasitəsilə)
    adi_deyis(telebe1, "Doe")

    # Yenidən print(telebe1) — bu dəfə __str__ yenilənmiş adı qaytaracaq:
    # "Tələbənin adı: Doe"
    print(telebe1)


if __name__ == "__main__":
    main()
