# ============================================================================
#  PRACTICE 12 — Ədədin rəqəmlərinin cəmi
# ----------------------------------------------------------------------------
#  Bu faylda öyrənəcəyimiz mövzular:
#    1) while dövrü ilə təkrarlanan hesablama
#    2) Modulo (%) operatoru — bölmədən qalanı tapmaq
#    3) Tam bölmə (//) operatoru — bölməni tam ədədə yuvarlaqlaşdırmaq
#    4) f-string ilə mətn daxilində dəyişən dəyərləri göstərmək
# ============================================================================

def main():
    # ------------------------------------------------------------
    # input() HƏMİŞƏ mətn (str) qaytarır, hətta istifadəçi rəqəm
    # yazsa belə. Ona görə int(...) funksiyası ilə həmin mətni
    # TAM ƏDƏDƏ (integer) çeviririk.
    #
    # Bu, Java-dakı bu sətrə bərabərdir:
    #     int number = scanner.nextInt();
    #
    # Əgər istifadəçi rəqəm əvəzinə hərf yazsa, int(...) xəta
    # (ValueError) verəcək — bu proqramda əlavə yoxlama yoxdur,
    # ona görə düzgün rəqəm daxil edilməlidir.
    # ------------------------------------------------------------
    number = int(input("Enter a number: "))

    total = 0  # rəqəmlərin CƏMİNİ saxlayacaq dəyişən, əvvəlcə 0-dan başlayır
    temp = number  # "number"-in bir KOPYASI — orijinal dəyəri pozmamaq üçün.
    #                Əgər birbaşa "number" ilə işləsəydik, dövr bitəndə
    #                "number" dəyişəni artıq 0 olardı və son çap edilən
    #                mesajda orijinal rəqəmi göstərə bilməzdik.

    # ------------------------------------------------------------
    # while temp != 0: — "temp SIFIRA BƏRABƏR OLMADIĞI MÜDDƏTCƏ"
    # dövrün daxilindəki kod TƏKRAR-TƏKRAR icra olunur.
    #
    # Məsələn, number = 123 olarsa:
    #   1-ci dövr: temp = 123
    #   2-ci dövr: temp = 12
    #   3-cü dövr: temp = 1
    #   4-cü dövr: temp = 0  -> şərt yalan olur, dövr DAYANIR
    # ------------------------------------------------------------
    while temp != 0:
        # ---- % (MODULO) operatoru ----
        # temp % 10 — temp ədədinin 10-a bölünməsindən QALAN hissəni verir.
        # Onluq say sistemində bir ədədi 10-a böləndə qalan HƏMİŞƏ
        # onun ƏN SONUNCU (ən sağdakı) rəqəmi olur.
        # Misal: 123 % 10 = 3  (çünki 123 = 12*10 + 3)
        digit = temp % 10

        # Tapılan son rəqəm ümumi cəmə əlavə olunur.
        # "total += digit" — "total = total + digit"-in QISA YAZILIŞIDIR
        total += digit

        # ---- // (TAM BÖLMƏ) operatoru ----
        # temp // 10 — temp-i 10-a bölüb, NƏTİCƏNİN KƏSR HİSSƏSİNİ ATARAQ
        # (yəni Java-dakı int/int bölməsi kimi) tam ədəd qaytarır.
        # Misal: 123 // 10 = 12  (0.3 hissəsi atılır)
        # Bu, sanki ədədin ən sonuncu rəqəmini "SİLİR".
        temp //= 10
        # Beləliklə hər dövrdə temp-in ən sağındakı rəqəm "qopardılıb"
        # cəmə əlavə olunur, temp isə get-gedə kiçilir, sonda 0 olur.

    # ------------------------------------------------------------
    # f-string (formatted string) — mətnin əvvəlində "f" hərfi qoyulur
    # və mötərizələr {} içində dəyişənləri BİRBAŞA mətnin İÇİNƏ yerləşdirmək
    # mümkün olur.
    #
    # Bu, Java-dakı bu sətrə bərabərdir:
    #     System.out.println("Sum of digits of " + number + " is: " + total);
    # ------------------------------------------------------------
    print(f"Sum of digits of {number} is: {total}")


if __name__ == "__main__":
    main()
