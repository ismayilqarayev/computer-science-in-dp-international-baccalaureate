# ============================================================================
#  SWAP EXAMPLE — orijinal Java faylındakı BİR NEÇƏ AYRI, kiçik
#  nümunənin (Tələbə, Məhsul, boolean, swap) hamısının Python-a
#  çevrilmiş, hər biri AYRI FUNKSİYA kimi tərtib edilmiş versiyası
# ----------------------------------------------------------------------------
#  Qeyd: orijinal Java faylı əslində bir neçə fərqli "mini-proqramın"
#  ÜST-ÜSTƏ KÖÇÜRÜLMƏSİ idi (hər biri öz "class Main"-i ilə, hətta
#  bəziləri Java baxımından KOMPİLYASİYA OLUNMURDU — dərs zamanı
#  addım-addım göstərilən nümunələr toplusu idi).
#
#  Python-da eyni fayl daxilində BİR NEÇƏ "class Main" ola bilməz və
#  ümumiyyətlə bu qədər ayrı nümunəni bir yerə yığmaq səliqəsiz
#  olardı, ona görə HƏR NÜMUNƏ ayrıca funksiya şəklində təşkil olunub.
#  Faylı işə saldıqda yalnız ən aşağıdakı __main__ blokunda çağırılan
#  funksiya icra olunur, QALANLARI isə funksiya adı ilə AYRICA
#  çağırıla bilər (məsələn: mehsul_numunesi()).
# ============================================================================


def telebe_numunesi():
    # --------------------------------------------------------
    # Funksiya DAXİLİNDƏ LOKAL (yerli) sinif təyin olunur —
    # bu, YALNIZ bu funksiya işlədikdə mövcud olan, funksiyadan
    # KƏNARDAN GÖRÜNMƏYƏN bir sinifdir. Bu üsul burada sadəcə
    # "hər nümunənin tam MÜSTƏQİL olması" üçün istifadə olunub
    # (adətən sinifləri faylın ən yuxarısında yazmaq daha
    # ümumi PRAKTİKADIR).
    # --------------------------------------------------------
    class Telebe:
        def __init__(self):
            self.ad = None  # hələ dəyər verilməyib (Java-dakı null kimi)
            self.yas = None

    telebe = Telebe()

    print("Adınızı daxil edin: ")
    telebe.ad = input()

    print("Yaşınızı daxil edin: ")
    # int(...) ilə mətn tam ədədə çevrilir
    telebe.yas = int(input())

    print(f"Ad: {telebe.ad} Yaş: {telebe.yas}")


def telebe_artirma_numunesi():
    class Telebe:
        def __init__(self):
            self.ad = None
            self.yas = None

    t = Telebe()

    print("Ad daxil edin:")
    t.ad = input()

    print("Yaş daxil edin:")
    t.yas = int(input())

    # t.yas += 1 — Java-dakı "t.age++" ilə EYNİ NƏTİCƏNİ verir:
    # yaşı BİR VAHİD artırır. Python-da "++" operatoru YOXDUR,
    # ona görə "+= 1" istifadə olunur.
    t.yas += 1

    print("Ad:", t.ad)
    print("Yaş:", t.yas)


def mehsul_numunesi_ing():
    class Mehsul:
        def __init__(self):
            self.ad = None
            self.qiymet = None

    m = Mehsul()

    print("Enter product name:")
    m.ad = input()

    print("Enter product price:")
    # float(...) — VERGÜLLÜ (kəsr hissəli) ədədə çevirir (Java-dakı
    # "double" tipinə bənzəyir). Məsələn "19.99" -> 19.99
    m.qiymet = float(input())

    print("Enter discount percentage:")
    endirim = float(input())

    # ------------------------------------------------------------
    # Endirimdən sonrakı son qiymət hesablanır:
    #   son_qiymət = qiymət - (qiymət * endirim_faizi / 100)
    #
    # Misal: qiymət=100, endirim=20 olsa:
    #   100 - (100 * 20 / 100) = 100 - 20 = 80
    # ------------------------------------------------------------
    son_qiymet = m.qiymet - (m.qiymet * endirim / 100)

    print("Product:", m.ad)
    print("Original Price:", m.qiymet)
    print(f"Discount: {endirim}%")
    print("Final Price:", son_qiymet)


def mehsul_numunesi():
    # Yuxarıdakı mehsul_numunesi_ing ilə TAM EYNİ məntiq, sadəcə
    # dəyişən adları Azərbaycan dilində yazılıb (orijinal Java
    # faylındakı kimi) — bu, eyni məsələnin iki DİLDƏ yazılmış
    # versiyasını müqayisə etmək üçün faydalıdır
    class Mehsul:
        def __init__(self):
            self.ad = None
            self.qiymet = None

    mehsul = Mehsul()

    print("Məhsulun adını daxil edin:")
    mehsul.ad = input()

    print("Məhsulun qiymətini daxil edin:")
    mehsul.qiymet = float(input())

    print("Endirim faizini daxil edin:")
    endirim_faizi = float(input())

    son_qiymet = mehsul.qiymet - (mehsul.qiymet * endirim_faizi / 100)

    print("Məhsul:", mehsul.ad)
    print("Əsas Qiymət:", mehsul.qiymet)
    print(f"Endirim: {endirim_faizi}%")
    print("Son Qiymət:", son_qiymet)


def boyuk_eded_numunesi():
    # Sadə müqayisə nümunəsi — iki ədəddən hansının BÖYÜK olduğunu tapır
    print("1-ci ədədi daxil edin:")
    eded_1 = int(input())

    print("2-ci ədədi daxil edin:")
    eded_2 = int(input())

    # ------------------------------------------------------------
    # ">" MÜQAYİSƏ OPERATORU — iki ədədi müqayisə edir və
    # NƏTİCƏ OLARAQ BOOLEAN (True və ya False) qaytarır.
    # "neticə" dəyişəni burada BİR ƏDƏD YOX, BİR BOOLEAN dəyər saxlayır.
    # ------------------------------------------------------------
    neticə = eded_1 > eded_2

    # if/else — "neticə" DƏYƏRİ True olarsa birinci blok,
    # False olarsa ikinci (else) blok icra olunur
    if neticə:
        print("1-ci ədəd daha böyükdür")
    else:
        print("2-ci ədəd böyük və ya bərabərdir")


def her_ikisi_musbet_and_numunesi():
    # --------------------------------------------------------
    # "and" MƏNTİQİ OPERATORU — HƏR İKİ ŞƏRT DOĞRU olduqda
    # (yəni hər ikisi True olduqda) True qaytarır, əks halda False.
    #
    # Java-dakı "&&" operatoru ilə eynidir.
    # --------------------------------------------------------
    print("1-ci ədədi daxil edin:")
    eded_1 = int(input())

    print("2-ci ədədi daxil edin:")
    eded_2 = int(input())

    neticə = (eded_1 > 0) and (eded_2 > 0)

    print("Nəticə (true/false):", neticə)


def her_ikisi_musbet_if_numunesi():
    # Eyni məntiq, amma bu dəfə nəticə ARA DƏYİŞƏNDƏ SAXLANMIR,
    # birbaşa if-in ŞƏRTİ kimi istifadə olunur
    print("1-ci ədədi daxil edin:")
    eded_1 = int(input())

    print("2-ci ədədi daxil edin:")
    eded_2 = int(input())

    if eded_1 > 0 and eded_2 > 0:
        print("Doğru: hər iki ədəd müsbətdir")
    else:
        print("Yanlış: ən azı bir ədəd mənfi və ya sıfırdır")


def swap_numunesi():
    # Klassik "SWAP" (iki dəyişənin qiymətlərini BİR-BİRİ İLƏ DƏYİŞMƏK) nümunəsi
    a = 5
    b = 7

    print(f"Əvvəl: a = {a}, b = {b}")

    # ------------------------------------------------------------
    # Java-da bunun üçün ÜÇÜNCÜ (müvəqqəti/temp) bir dəyişən LAZIMDIR,
    # çünki əvvəlcə "a"-nı "b"-yə yazsaq, "a"-nın KÖHNƏ dəyəri İTİR:
    #     int temp = a;
    #     a = b;
    #     b = temp;
    #
    # Python-da isə "TUPLE UNPACKING" (dəst açma) adlanan bir üsulla
    # bunu BİR SƏTİRDƏ etmək mümkündür:
    #     a, b = b, a
    #
    # Bu sətirdə NƏ BAŞ VERİR:
    #   1) ƏVVƏLCƏ sağ tərəf HESABLANIR: (b, a) — yəni (7, 5) adlı
    #      bir DƏST (tuple) YARADILIR, İKİ KÖHNƏ DƏYƏR DE BU DƏSTDƏ
    #      "DONDURULUR"
    #   2) SONRA bu dəst SOL TƏRƏFƏ "AÇILIR" (paylanır):
    #      birinci element (7) a-ya, ikinci element (5) b-yə yazılır
    #
    # Beləliklə HEÇ BİR müvəqqəti dəyişənə EHTİYAC QALMIR — Python-un
    # bu xüsusiyyəti kodun daha qısa yazılmasına imkan verir.
    # ------------------------------------------------------------
    a, b = b, a

    print(f"Sonra: a = {a}, b = {b}")


def girissiz_swap_numunesi():
    # Yuxarıdakının GİRİŞSİZ, sadəcə sabit dəyərlərlə variantı
    eded_1 = 5
    eded_2 = 7

    print(f"Əvvəl: a = {eded_1}, b = {eded_2}")

    eded_1, eded_2 = eded_2, eded_1


def swap_ve_artirma_numunesi():
    # SWAP əməliyyatından SONRA hər iki dəyəri 1 vahid artıran nümunə
    print("1-ci ədədi daxil edin:")
    eded_1 = int(input())

    print("2-ci ədədi daxil edin:")
    eded_2 = int(input())

    print(f"Əvvəl: a = {eded_1}, b = {eded_2}")

    # Dəyərləri dəyişmək (swap)
    eded_1, eded_2 = eded_2, eded_1

    # İnkrement əməliyyatı (hər birini 1 vahid artırırıq).
    # "+=" — "x = x + 1"-in QISA YAZILIŞIDIR
    eded_1 += 1
    eded_2 += 1

    print(f"Sonra (swap + artırma): a = {eded_1}, b = {eded_2}")


def yanlis_swap_numunesi():
    # ------------------------------------------------------------
    # DİQQƏT: bu, BİLƏRƏKDƏN TƏHRİF EDİLMİŞ (SƏHV) bir SWAP
    # nümunəsidir — orijinal Java kodunda olan xəta EYNİ İLƏ
    # saxlanılıb ki, tələbələr NİYƏ SƏHV olduğunu görüb müzakirə
    # edə bilsinlər (bu, YAXŞI bir dərs materialı nümunəsidir —
    # səhvlərdən öyrənmək).
    #
    # SƏHVİN SƏBƏBİ:
    #   "eded_1 = eded_2" sətri işlədikdə eded_1-in KÖHNƏ
    #   (orijinal) dəyəri (5) HƏMİŞƏLİK İTİR — çünki heç bir yerdə
    #   saxlanılmayıb. İndi HƏM eded_1, HƏM DƏ eded_2 EYNİ
    #   DƏYƏRƏ (7) SAHİBDİR.
    #
    #   Sonra "eded_2 = eded_1" sətri işlədikdə, artıq DƏYİŞMİŞ
    #   olan eded_1-i (7) yenidən eded_2-yə YAZIR — nəticədə
    #   HEÇ NƏ DƏYİŞMİR, hər iki dəyişən 7 olaraq QALIR.
    #
    #   DÜZGÜN nəticə "a=7, b=5" olmalı idi, amma bu SƏHV kodda
    #   "a=7, b=7" alınır.
    # ------------------------------------------------------------
    eded_1 = 5
    eded_2 = 7

    print(f"Əvvəl: a = {eded_1}, b = {eded_2}")

    eded_1 = eded_2   # eded_1 = 7 olur, amma orijinal 5 dəyəri HƏMİŞƏLİK İTİR
    eded_2 = eded_1   # eded_2 = 7 (artıq dəyişmiş eded_1) olur — SWAP ALINMADI
    print(f"Sonra: a = {eded_1}, b = {eded_2}")


# ----------------------------------------------------------------------------
# Fayl BİRBAŞA işə salındıqda YALNIZ əsas "swap_numunesi" nümunəsi göstərilir.
# Digər funksiyaları sınamaq üçün onları burada ÇAĞIRMAQ KİFAYƏTDİR,
# məsələn: mehsul_numunesi() və ya boyuk_eded_numunesi()
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    swap_numunesi()
