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
# Analogiya: "Telebe" sinfi ev tikmək üçün olan LAYİHƏ çertyojuna bənzəyir.
# Çertyojun özü ev deyil — ondan istifadə edərək çoxlu sayda konkret ev
# (yəni konkret tələbə obyekti) tikə bilərik. Hər ev fərqli ünvanda,
# fərqli rəngdə ola bilər — eynilə hər Telebe obyektinin də fərqli
# adı və yaşı ola bilər.
# --------------------------------------------------------------------------
class Telebe:

    # ------------------------------------------------------------------
    # __init__ metodu — KONSTRUKTORdur.
    #
    # "Konstruktor" sözünün mənası: "qurucu, tikən". Bu metod məhz
    # Telebe(...) formasında yeni bir obyekt yaradılan zaman Python
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
    #   ad  — konstruktora ötürülən tələbənin adı (string/mətn tipində)
    #   yas — konstruktora ötürülən tələbənin yaşı (int/tam ədəd tipində)
    # ------------------------------------------------------------------
    def __init__(self, ad, yas):
        # self.ad = ad  --> bu sətir YENİ bir sahə (atribut) yaradır.
        # Sol tərəfdəki "self.ad" — yaradılan konkret obyektin daxilində
        # saxlanılacaq yaddaş "qutusudur". Sağ tərəfdəki "ad" isə
        # konstruktora bayaq ötürülən PARAMETRDİR.
        # Diqqət: adları eynidir (ikisi də "ad"), amma onlar TAMAM
        # FƏRQLİ ŞEYLƏRDİR — biri parametr (müvəqqəti), digəri isə
        # obyektin daimi yaddaşında saxlanan sahədir.
        self.ad = ad

        # Eyni məntiqlə "yas" parametri obyektin "yas" sahəsinə yazılır.
        # Bundan sonra bu obyekt "yaşayır" — yəni "yas" sahəsi bu obyektlə
        # birlikdə yaddaşda saxlanılır, obyekt silinənə qədər orada qalır.
        self.yas = yas


# --------------------------------------------------------------------------
# print_student — bu, sinifin DAXİLİNDƏ deyil, sinifdən KƏNARDA yazılmış
# adi bir funksiyadır (Java-dakı "static" metodla eyni məntiqi daşıyır,
# çünki heç bir konkret obyektə "bağlı" deyil, sadəcə parametr kimi
# obyekt qəbul edir).
#
# Parametr:
#   t — Telebe tipli bir obyekt (İDEAL olaraq, texniki cəhətdən Python
#       tip yoxlaması məcburi etmir, amma məntiqən belə istifadə nəzərdə
#       tutulub)
# --------------------------------------------------------------------------
def telebe_goster(t):
    # t -> funksiyaya göndərilən konkret Telebe obyektinin özüdür.
    # Bu, "referensdir" — yəni t dəyişəni obyektin özünü yox, obyektin
    # yaddaşdakı ünvanını saxlayır (Java-dakı obyekt referensləri kimi).
    #
    # t.ad -> nöqtə (.) operatoru ilə obyektin "ad" sahəsinə müraciət
    # edirik. Bu, "t obyektinin içindəki adı mənə ver" deməkdir.
    # t.yas -> eyni məntiqlə "yas" sahəsinə müraciət.
    #
    # print(a, b) — Python-un daxili funksiyasıdır, verilən bütün
    # dəyərləri ARALARINDA BOŞLUQ qoyaraq bir sətirdə ekrana çıxarır və
    # sonda avtomatik yeni sətrə keçir (\n əlavə edir).
    print(t.ad, t.yas)


# --------------------------------------------------------------------------
# main() — proqramın işə düşəcəyi əsas funksiya.
# Python-da "main" funksiyası Java-dakı kimi MƏCBURİ deyil — proqram
# faylın başından sonuna qədər sətir-sətir icra oluna bilər. Amma
# kodun oxunaqlı və təşkilatlı olması üçün bütün "əsas məntiqi"
# main() adlı funksiyanın içinə yığmaq YAXŞI PRAKTİKA sayılır.
# --------------------------------------------------------------------------
def main():
    # Yeni Telebe obyekti yaradılır.
    # "Telebe("Ravan", 12)" yazıldıqda arxa planda baş verənlər:
    #   1) Yaddaşda yeni, boş bir Telebe "qutusu" ayrılır
    #   2) Bu qutunun "self" olaraq __init__ metoduna avtomatik ötürülür
    #   3) "Ravan" -> ad parametrinə, 12 -> yas parametrinə düşür
    #   4) __init__ daxilində self.ad = "Ravan", self.yas = 12 olaraq
    #      sahələr doldurulur
    #   5) Hazır olan bu obyekt "telebe" adlı dəyişənə mənimsədilir
    telebe = Telebe("Ravan", 12)

    # telebe_goster funksiyası çağırılır, "telebe" obyekti ona parametr kimi
    # ötürülür. Funksiya daxilində bu eyni obyekt "t" adı ilə istifadə olunur
    # (dəyişənin adı fərqlidir, amma yaddaşdakı OBYEKT eynidir).
    telebe_goster(telebe)


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
