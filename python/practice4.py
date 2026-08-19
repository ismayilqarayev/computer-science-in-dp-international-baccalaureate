# ============================================================================
#  PRACTICE 4 — İstifadəçi girişi (input) ilə işləmək
# ----------------------------------------------------------------------------
#  Bu faylda öyrənəcəyimiz mövzular:
#    1) input() funksiyası ilə klaviaturadan mətn oxumaq
#    2) __str__ ilə obyekti oxunaqlı formada çap etmək
#    3) Dinamik (istifadəçi tərəfindən daxil edilən) məlumatla
#       obyekt yaratmaq
# ============================================================================

class Telebe:

    def __init__(self, ad):
        self._ad = ad

    def get_ad(self):
        return self._ad

    def set_ad(self, ad):
        self._ad = ad

    # Bu dəfə __str__ sadəcə adın özünü qaytarır (əlavə "Tələbənin adı:"
    # mətni yoxdur — Practice 3-dəkindən fərqli olaraq)
    def __str__(self):
        return self._ad


# Obyektin adını dəyişən köməkçi funksiya
def adi_deyis(telebe, yeni_ad):
    telebe.set_ad(yeni_ad)


def main():
    # ------------------------------------------------------------
    # input(prompt) — Python-un DAXİLİ (built-in) funksiyasıdır.
    #
    # İşləmə prinsipi:
    #   1) Mötərizə içindəki mətn ("Tələbənin adını daxil edin: ")
    #      ekrana çıxarılır, İSTİFADƏÇİDƏN GİRİŞ GÖZLƏNİLİR
    #      (proqram burada DAYANIR)
    #   2) İstifadəçi klaviaturadan nəsə yazıb Enter düyməsini basır
    #   3) Yazılan mətn (Enter-ə qədər olan hissə) FUNKSİYANIN NƏTİCƏSİ
    #      kimi geri qaytarılır və "telebe_adi" dəyişəninə yazılır
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
    telebe_adi = input("Tələbənin adını daxil edin: ")

    # Daxil edilən adla yeni Telebe obyekti yaradılır
    telebe = Telebe(telebe_adi)

    # print("Cari ad:", telebe) — burada iki dəyər verilib:
    # sabit mətn "Cari ad:" və "telebe" obyekti.
    # print() bunları BOŞLUQLA ayıraraq çap edir, "telebe" hissəsi
    # üçün avtomatik olaraq __str__ metodu çağırılır.
    print("Cari ad:", telebe)

    # Yeni ad üçün təkrar giriş alınır
    yeni_ad = input("Tələbənin yeni adını daxil edin: ")

    # adi_deyis funksiyası vasitəsilə obyektin adı yenilənir.
    # Diqqət: "telebe" dəyişəni HƏMİN OBYEKTƏ işarə etməyə davam edir,
    # sadəcə onun DAXİLİNDƏKİ "_ad" sahəsi dəyişib.
    adi_deyis(telebe, yeni_ad)

    # Yenilənmiş adla obyekt yenidən çap olunur
    print("Yeni ad:", telebe)


if __name__ == "__main__":
    main()
