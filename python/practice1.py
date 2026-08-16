# ============================================================================
#  PRACTICE 1 — Ən sadə sinif (class) nümunəsi
# ----------------------------------------------------------------------------
#  Bu faylda öyrənəcəyimiz mövzular:
#    1) Sinif (class) nədir və niyə istifadə olunur?
#    2) Konstruktor (__init__) nə üçündür?
#    3) "self" sözü nəyi bildirir?
#    4) Obyekt (instance) necə yaradılır?
#    5) Adi funksiya vasitəsilə obyektlə necə işləmək olar?
# ============================================================================


# --------------------------------------------------------------------------
# "class" açar sözü ilə yeni bir sinif təsvir edirik.
# Sinif — real həyatdakı bir "şeyin" (bizim halda: TƏLƏBƏNİN) hansı
# məlumatları (sahələri) və hansı davranışları (metodları) olacağını
# əvvəlcədən planlaşdıran bir "qəlib" və ya "çertyoj"dur.
#
# Analogiya: "Student" sinfi ev tikmək üçün olan LAYİHƏ çertyojuna bənzəyir.
# Çertyojun özü ev deyil — ondan istifadə edərək çoxlu sayda konkret ev
# (yəni konkret tələbə obyekti) tikə bilərik. Hər ev fərqli ünvanda,
# fərqli rəngdə ola bilər — eynilə hər Student obyektinin də fərqli
# adı və yaşı ola bilər.
# --------------------------------------------------------------------------
class Student:

    # ------------------------------------------------------------------
    # __init__ metodu — KONSTRUKTORdur.
    #
    # "Konstruktor" sözünün mənası: "qurucu, tikən". Bu metod məhz
    # Student(...) formasında yeni bir obyekt yaradılan zaman Python
    # tərəfindən AVTOMATİK olaraq, bir dəfə çağırılır. Bizim onu əl ilə
    # çağırmağımıza ehtiyac yoxdur.
    #
    # Adının əvvəlində və sonunda iki alt xətt (__) olması Python-da
    # bunun "xüsusi" (magic/dunder — "double underscore") bir metod
    # olduğunu bildirir. Python-un daxilində onlarla belə xüsusi metod var,
    # __init__ onlardan ən çox istifadə olunanıdır.
    #
    # Parametrlər:
    #   self — yaradılmaqda olan KONKRET obyektin özüdür. Java-da buna
    #          "this" deyilir. Fərq ondadır ki, Java-da "this" gizlidir,
    #          Python-da isə "self" HƏR metodun BİRİNCİ parametri kimi
    #          açıq şəkildə yazılmalıdır (adı məcburi "self" olmasa da,
    #          ümumi qəbul edilmiş razılaşmadır).
    #   name — konstruktora ötürülən tələbənin adı (string/mətn tipində)
    #   age  — konstruktora ötürülən tələbənin yaşı (int/tam ədəd tipində)
    # ------------------------------------------------------------------
    def __init__(self, name, age):
        # self.name = name  --> bu sətir YENİ bir sahə (atribut) yaradır.
        # Sol tərəfdəki "self.name" — yaradılan konkret obyektin daxilində
        # saxlanılacaq yaddaş "qutusudur". Sağ tərəfdəki "name" isə
        # konstruktora bayaq ötürülən PARAMETRDİR.
        # Diqqət: adları eynidir (ikisi də "name"), amma onlar TAMAM
        # FƏRQLİ ŞEYLƏRDİR — biri parametr (müvəqqəti), digəri isə
        # obyektin daimi yaddaşında saxlanan sahədir.
        self.name = name

        # Eyni məntiqlə "age" parametri obyektin "age" sahəsinə yazılır.
        # Bundan sonra bu obyekt "yaşayır" — yəni "age" sahəsi bu obyektlə
        # birlikdə yaddaşda saxlanılır, obyekt silinənə qədər orada qalır.
        self.age = age


# --------------------------------------------------------------------------
# print_student — bu, sinifin DAXİLİNDƏ deyil, sinifdən KƏNARDA yazılmış
# adi bir funksiyadır (Java-dakı "static" metodla eyni məntiqi daşıyır,
# çünki heç bir konkret obyektə "bağlı" deyil, sadəcə parametr kimi
# obyekt qəbul edir).
#
# Parametr:
#   s — Student tipli bir obyekt (İDEAL olaraq, texniki cəhətdən Python
#       tip yoxlaması məcburi etmir, amma məntiqən belə istifadə nəzərdə
#       tutulub)
# --------------------------------------------------------------------------
def print_student(s):
    # s -> funksiyaya göndərilən konkret Student obyektinin özüdür.
    # Bu, "referensdir" — yəni s dəyişəni obyektin özünü yox, obyektin
    # yaddaşdakı ünvanını saxlayır (Java-dakı obyekt referensləri kimi).
    #
    # s.name -> nöqtə (.) operatoru ilə obyektin "name" sahəsinə müraciət
    # edirik. Bu, "s obyektinin içindəki name-i mənə ver" deməkdir.
    # s.age  -> eyni məntiqlə "age" sahəsinə müraciət.
    #
    # print(a, b) — Python-un daxili funksiyasıdır, verilən bütün
    # dəyərləri ARALARINDA BOŞLUQ qoyaraq bir sətirdə ekrana çıxarır və
    # sonda avtomatik yeni sətrə keçir (\n əlavə edir).
    print(s.name, s.age)


# --------------------------------------------------------------------------
# main() — proqramın işə düşəcəyi əsas funksiya.
# Python-da "main" funksiyası Java-dakı kimi MƏCBURİ deyil — proqram
# faylın başından sonuna qədər sətir-sətir icra oluna bilər. Amma
# kodun oxunaqlı və təşkilatlı olması üçün bütün "əsas məntiqi"
# main() adlı funksiyanın içinə yığmaq YAXŞI PRAKTİKA sayılır.
# --------------------------------------------------------------------------
def main():
    # Yeni Student obyekti yaradılır.
    # "Student("Ravan", 12)" yazıldıqda arxa planda baş verənlər:
    #   1) Yaddaşda yeni, boş bir Student "qutusu" ayrılır
    #   2) Bu qutunun "self" olaraq __init__ metoduna avtomatik ötürülür
    #   3) "Ravan" -> name parametrinə, 12 -> age parametrinə düşür
    #   4) __init__ daxilində self.name = "Ravan", self.age = 12 olaraq
    #      sahələr doldurulur
    #   5) Hazır olan bu obyekt "st" adlı dəyişənə mənimsədilir
    st = Student("Ravan", 12)

    # print_student funksiyası çağırılır, "st" obyekti ona parametr kimi
    # ötürülür. Funksiya daxilində bu eyni obyekt "s" adı ilə istifadə olunur
    # (dəyişənin adı fərqlidir, amma yaddaşdakı OBYEKT eynidir).
    print_student(st)


# --------------------------------------------------------------------------
# Bu şərt Python-un standart "giriş nöqtəsi" yoxlamasıdır.
#
# "__name__" — Python-un hər fayla avtomatik verdiyi xüsusi dəyişəndir.
#   - Əgər bu fayl BİRBAŞA işə salınırsa (məsələn: "python practice1.py"),
#     __name__ dəyişəninin dəyəri "__main__" olur.
#   - Əgər bu fayl başqa bir fayldan "import practice1" kimi
#     idxal edilirsə, __name__ dəyişəni "practice1" (faylın adı) olur.
#
# Bu yoxlama olmasaydı, kimsə bu faylı başqa yerdən import etdikdə
# main() funksiyası istəmədən avtomatik işə düşərdi. Bu şərt sayəsində
# main() YALNIZ fayl birbaşa işə salındıqda çağırılır.
# --------------------------------------------------------------------------
if __name__ == "__main__":
    main()
