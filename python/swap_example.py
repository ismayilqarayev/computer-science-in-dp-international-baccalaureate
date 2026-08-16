# ============================================================================
#  SWAP EXAMPLE — orijinal Java faylındakı BİR NEÇƏ AYRI, kiçik
#  nümunənin (Student, Product, boolean, swap) hamısının Python-a
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
#  çağırıla bilər (məsələn: product_example()).
# ============================================================================


def student_example():
    # --------------------------------------------------------
    # Funksiya DAXİLİNDƏ LOKAL (yerli) sinif təyin olunur —
    # bu, YALNIZ bu funksiya işlədikdə mövcud olan, funksiyadan
    # KƏNARDAN GÖRÜNMƏYƏN bir sinifdir. Bu üsul burada sadəcə
    # "hər nümunənin tam MÜSTƏQİL olması" üçün istifadə olunub
    # (adətən sinifləri faylın ən yuxarısında yazmaq daha
    # ümumi PRAKTİKADIR).
    # --------------------------------------------------------
    class Student:
        def __init__(self):
            self.name = None  # hələ dəyər verilməyib (Java-dakı null kimi)
            self.age = None

    student = Student()

    print("Enter your name: ")
    student.name = input()

    print("Enter your age: ")
    # int(...) ilə mətn tam ədədə çevrilir
    student.age = int(input())

    print(f"Name: {student.name} Age: {student.age}")


def student_increment_example():
    class Student:
        def __init__(self):
            self.name = None
            self.age = None

    st = Student()

    print("Enter name:")
    st.name = input()

    print("Enter age:")
    st.age = int(input())

    # st.age += 1 — Java-dakı "st.age++" ilə EYNİ NƏTİCƏNİ verir:
    # yaşı BİR VAHİD artırır. Python-da "++" operatoru YOXDUR,
    # ona görə "+= 1" istifadə olunur.
    st.age += 1

    print("Name:", st.name)
    print("Age:", st.age)


def product_example():
    class Product:
        def __init__(self):
            self.name = None
            self.price = None

    pr = Product()

    print("Enter product name:")
    pr.name = input()

    print("Enter product price:")
    # float(...) — VERGÜLLÜ (kəsr hissəli) ədədə çevirir (Java-dakı
    # "double" tipinə bənzəyir). Məsələn "19.99" -> 19.99
    pr.price = float(input())

    print("Enter discount percentage:")
    discount = float(input())

    # ------------------------------------------------------------
    # Endirimdən sonrakı son qiymət hesablanır:
    #   son_qiymət = qiymət - (qiymət * endirim_faizi / 100)
    #
    # Misal: qiymət=100, endirim=20 olsa:
    #   100 - (100 * 20 / 100) = 100 - 20 = 80
    # ------------------------------------------------------------
    final_price = pr.price - (pr.price * discount / 100)

    print("Product:", pr.name)
    print("Original Price:", pr.price)
    print(f"Discount: {discount}%")
    print("Final Price:", final_price)


def mehsul_example():
    # Yuxarıdakı product_example ilə TAM EYNİ məntiq, sadəcə
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


def bigger_number_example():
    # Sadə müqayisə nümunəsi — iki ədəddən hansının BÖYÜK olduğunu tapır
    print("Enter number 1:")
    number_1 = int(input())

    print("Enter number 2:")
    number_2 = int(input())

    # ------------------------------------------------------------
    # ">" MÜQAYİSƏ OPERATORU — iki ədədi müqayisə edir və
    # NƏTİCƏ OLARAQ BOOLEAN (True və ya False) qaytarır.
    # "result" dəyişəni burada BİR ƏDƏD YOX, BİR BOOLEAN dəyər saxlayır.
    # ------------------------------------------------------------
    result = number_1 > number_2

    # if/else — "result" DƏYƏRİ True olarsa birinci blok,
    # False olarsa ikinci (else) blok icra olunur
    if result:
        print("Number 1 is bigger")
    else:
        print("Number 2 is bigger or equal")


def both_positive_and_example():
    # --------------------------------------------------------
    # "and" MƏNTİQİ OPERATORU — HƏR İKİ ŞƏRT DOĞRU olduqda
    # (yəni hər ikisi True olduqda) True qaytarır, əks halda False.
    #
    # Java-dakı "&&" operatoru ilə eynidir.
    # --------------------------------------------------------
    print("Enter number 1:")
    number_1 = int(input())

    print("Enter number 2:")
    number_2 = int(input())

    result = (number_1 > 0) and (number_2 > 0)

    print("Result (true/false):", result)


def both_positive_if_example():
    # Eyni məntiq, amma bu dəfə nəticə ARA DƏYİŞƏNDƏ SAXLANMIR,
    # birbaşa if-in ŞƏRTİ kimi istifadə olunur
    print("Enter number 1:")
    number_1 = int(input())

    print("Enter number 2:")
    number_2 = int(input())

    if number_1 > 0 and number_2 > 0:
        print("True: both numbers are positive")
    else:
        print("False: at least one number is negative or zero")


def swap_example():
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


def swap_no_input_example():
    # Yuxarıdakının GİRİŞSİZ, sadəcə sabit dəyərlərlə variantı
    number_1 = 5
    number_2 = 7

    print(f"Əvvəl: a = {number_1}, b = {number_2}")

    number_1, number_2 = number_2, number_1


def swap_and_increment_example():
    # SWAP əməliyyatından SONRA hər iki dəyəri 1 vahid artıran nümunə
    print("Enter number 1:")
    number_1 = int(input())

    print("Enter number 2:")
    number_2 = int(input())

    print(f"Əvvəl: a = {number_1}, b = {number_2}")

    # Dəyərləri dəyişmək (swap)
    number_1, number_2 = number_2, number_1

    # İnkrement əməliyyatı (hər birini 1 vahid artırırıq).
    # "+=" — "x = x + 1"-in QISA YAZILIŞIDIR
    number_1 += 1
    number_2 += 1

    print(f"Sonra (swap + increment): a = {number_1}, b = {number_2}")


def incorrect_swap_example():
    # ------------------------------------------------------------
    # DİQQƏT: bu, BİLƏRƏKDƏN TƏHRİF EDİLMİŞ (SƏHV) bir SWAP
    # nümunəsidir — orijinal Java kodunda olan xəta EYNİ İLƏ
    # saxlanılıb ki, tələbələr NİYƏ SƏHV olduğunu görüb müzakirə
    # edə bilsinlər (bu, YAXŞI bir dərs materialı nümunəsidir —
    # səhvlərdən öyrənmək).
    #
    # SƏHVİN SƏBƏBİ:
    #   "number_1 = number_2" sətri işlədikdə number_1-in KÖHNƏ
    #   (orijinal) dəyəri (5) HƏMİŞƏLİK İTİR — çünki heç bir yerdə
    #   saxlanılmayıb. İndi HƏM number_1, HƏM DƏ number_2 EYNİ
    #   DƏYƏRƏ (7) SAHİBDİR.
    #
    #   Sonra "number_2 = number_1" sətri işlədikdə, artıq DƏYİŞMİŞ
    #   olan number_1-i (7) yenidən number_2-yə YAZIR — nəticədə
    #   HEÇ NƏ DƏYİŞMİR, hər iki dəyişən 7 olaraq QALIR.
    #
    #   DÜZGÜN nəticə "a=7, b=5" olmalı idi, amma bu SƏHV kodda
    #   "a=7, b=7" alınır.
    # ------------------------------------------------------------
    number_1 = 5
    number_2 = 7

    print(f"Əvvəl: a = {number_1}, b = {number_2}")

    number_1 = number_2   # number_1 = 7 olur, amma orijinal 5 dəyəri HƏMİŞƏLİK İTİR
    number_2 = number_1   # number_2 = 7 (artıq dəyişmiş number_1) olur — SWAP ALINMADI
    print(f"Sonra: a = {number_1}, b = {number_2}")


# ----------------------------------------------------------------------------
# Fayl BİRBAŞA işə salındıqda YALNIZ əsas "swap_example" nümunəsi göstərilir.
# Digər funksiyaları sınamaq üçün onları burada ÇAĞIRMAQ KİFAYƏTDİR,
# məsələn: product_example() və ya bigger_number_example()
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    swap_example()
