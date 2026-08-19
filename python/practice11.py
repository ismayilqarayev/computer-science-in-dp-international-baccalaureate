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

class Telebe:

    def __init__(self, ad):
        self._ad = ad

    def get_ad(self):
        return self._ad

    def set_ad(self, ad):
        self._ad = ad

    # print(telebe) çağırıldıqda ekrana adın özü çıxacaq
    def __str__(self):
        return self._ad


# ----------------------------------------------------------------------
# Bütün tələbələri saxlayan QLOBAL siyahı (Java-dakı ArrayList<Student> analoqu).
#
# "Qlobal" olması o deməkdir ki, bu dəyişən HƏR HANSI FUNKSİYANIN
# DAXİLİNDƏ YOX, faylın ƏN ÜST SƏVİYYƏSİNDƏ (indentasiyasız) təyin
# olunub, ona görə də faylın İÇİNDƏKİ BÜTÜN funksiyalar (telebe_elave_et,
# telebeleri_goster, adi_deyis, telebe_sil) bu siyahıya BİRBAŞA
# müraciət edə bilir.
#
# list — Python-un ən çox istifadə olunan "kolleksiya" tipidir.
# İçində istənilən sayda element saxlaya bilər, ölçüsü AVTOMATİK
# BÖYÜYÜR/KİÇİLİR (Java-dakı sabit ölçülü array-dən fərqli olaraq,
# Java-dakı ArrayList-ə bənzəyir).
# "[]" — boş siyahı yaratmağın ən sadə yoludur.
# ----------------------------------------------------------------------
telebeler = []


# ---- tələbə əlavə etmək (CREATE) ----
def telebe_elave_et():
    ad = input("Tələbə adı daxil edin: ")
    # .append(...) — siyahının SONUNA yeni bir element ƏLAVƏ EDİR.
    # Burada yeni bir Telebe obyekti yaradılır və birbaşa siyahıya qoyulur.
    telebeler.append(Telebe(ad))
    print("Tələbə əlavə edildi.")


# ---- tələbələri göstərmək (READ) ----
def telebeleri_goster():
    # "not telebeler" — əgər siyahı BOŞDURSA True qaytarır
    # (boş siyahı Python-da "yalan"/falsy sayılır, eynilə boş mətn kimi)
    if not telebeler:
        print("Tələbə yoxdur.")
        return  # funksiyadan erkən çıxırıq, aşağıdakı kod işləmir

    # --------------------------------------------------------
    # enumerate(telebeler) — siyahının HƏR ELEMENTİNİ, onun İNDEKSİ
    # İLƏ BİRLİKDƏ qaytaran xüsusi funksiyadır.
    #
    # Adi "for telebe in telebeler:" yazsaydıq, YALNIZ obyektləri
    # görərdik, indeksləri BİLMƏZDİK. enumerate() bizə hər ikisini
    # eyni anda verir:
    #     (0, birinci_tələbə), (1, ikinci_tələbə), (2, üçüncü_tələbə)...
    #
    # "for i, telebe in enumerate(telebeler):" yazdıqda Python
    # avtomatik olaraq HƏR CÜTÜ İKİ AYRI DƏYİŞƏNƏ (i və telebe)
    # "AÇIR" (unpacking).
    # --------------------------------------------------------
    for i, telebe in enumerate(telebeler):
        # f-string ilə indeks və tələbənin adı (telebe-nin __str__
        # metodu vasitəsilə) bir sətirdə çap olunur
        print(f"{i} - {telebe}")


# ---- ad dəyişmək (UPDATE) ----
def adi_deyis():
    telebeleri_goster()  # istifadəçiyə hansı indekslərin mövcud olduğunu göstərir

    # int(input(...)) — mətn kimi daxil edilən indeksi TAM ƏDƏDƏ çevirir
    indeks = int(input("İndeks daxil edin: "))
    yeni_ad = input("Yeni ad daxil edin: ")

    # --------------------------------------------------------
    # telebeler[indeks] — siyahıdan İNDEKSƏ GÖRƏ element seçmək.
    # Python-da (Java kimi) indekslər 0-dan başlayır: ilk element
    # telebeler[0], ikinci telebeler[1] və s.
    #
    # DİQQƏT: əgər istifadəçi mövcud olmayan bir indeks (məsələn,
    # siyahıda 3 element varkən 5) daxil etsə, bu sətir XƏTA
    # (IndexError) verəcək — bu proqramda bu HAL üçün əlavə yoxlama
    # YAZILMAYIB (orijinal Java kodunda da yox idi).
    # --------------------------------------------------------
    telebeler[indeks].set_ad(yeni_ad)
    print("Ad dəyişdirildi.")


# ---- tələbə silmək (DELETE) ----
def telebe_sil():
    telebeleri_goster()

    indeks = int(input("Silinəcək indeks: "))

    # --------------------------------------------------------
    # del — Python-un AÇAR SÖZÜDÜR (funksiya deyil), verilən
    # indeksdəki elementi siyahıdan TAMAMILƏ SİLİR.
    # Silindikdən sonra siyahının ölçüsü 1 vahid AZALIR və
    # silinən elementdən sonrakı bütün elementlərin indeksi
    # BİR VAHİD AŞAĞI SÜRÜŞÜR (avtomatik).
    # --------------------------------------------------------
    del telebeler[indeks]
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

        secim = int(input("Seçim: "))

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
        if secim == 1:
            telebe_elave_et()
        elif secim == 2:
            telebeleri_goster()
        elif secim == 3:
            adi_deyis()
        elif secim == 4:
            telebe_sil()
        elif secim == 0:
            print("Proqram bitdi.")
            return  # main() funksiyasından çıxır, deməli proqram da BİTİR
        else:
            # Yuxarıdakı HEÇ BİR şərtə uyğun gəlməyən HƏR HANSI dəyər üçün
            print("Yanlış seçim.")


if __name__ == "__main__":
    main()
