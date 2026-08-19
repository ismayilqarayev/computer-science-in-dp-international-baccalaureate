# ============================================================================
#  PRACTICE 2 — Encapsulation (İnkapsulyasiya) və Getter/Setter
# ----------------------------------------------------------------------------
#  Bu faylda öyrənəcəyimiz mövzular:
#    1) Niyə sahələri birbaşa açıq saxlamırıq?
#    2) "_" (alt xətt) prefiksinin mənası nədir?
#    3) Getter və Setter metodları nə üçündür?
#    4) Obyekti funksiyaya ötürüb onun daxili vəziyyətini necə dəyişmək olar?
# ============================================================================

class Telebe:

    # __init__ — konstruktor, obyekt yaradılan zaman avtomatik işləyir
    def __init__(self, ad):
        # ------------------------------------------------------------
        # DİQQƏT: dəyişənin adı "ad" YOX, "_ad" kimi yazılıb —
        # önündə BİR ALT XƏTT (_) var.
        #
        # Bu, ENCAPSULATION (İnkapsulyasiya) prinsipinin Python-dakı
        # ifadə formasıdır. Java-da "private" açar sözü var və dərləyici
        # (compiler) xaricdən private sahəyə müraciəti QADAĞAN EDİR.
        # Python-da isə HƏQİQİ "private" anlayışı yoxdur — bu, sadəcə
        # PROQRAMÇILAR ARASINDA razılaşma (convention)dır:
        #     "Əvvəlində _ olan sahəyə xaricdən BİRBAŞA TOXUNMA,
        #      bunun əvəzinə mənim təqdim etdiyim getter/setter
        #      metodlarından istifadə et."
        #
        # Texniki olaraq kimsə hələ də "telebe._ad" yazıb birbaşa
        # dəyişə bilər, amma bu, "yaxşı proqramçılıq qaydalarını
        # pozmaq" sayılır və başqaları bunu görəndə "bu, səhv
        # istifadədir" deyə başa düşür.
        #
        # İnkapsulyasiyanın FAYDASI: əgər gələcəkdə "ad" sahəsinin
        # dəyişdirilməsi zamanı əlavə yoxlama (məs: boş ad qəbul
        # etməmək) lazım olarsa, bunu YALNIZ setter metodunun içində
        # ediriksə, kodun HƏR YERİNDƏ (harada bu sinif istifadə
        # olunursa olunsun) bu qayda AVTOMATİK tətbiq olunacaq.
        # ------------------------------------------------------------
        self._ad = ad

    # ------------------------------------------------------------
    # GETTER metodu — "_ad" sahəsinin CARİ DƏYƏRİNİ OXUMAQ üçündür.
    # Adının əvvəlində "get_" olması ümumi qəbul edilmiş bir
    # adlandırma qaydasıdır (Java-dakı getName() üslubuna bənzəyir).
    # Bu metod heç nəyi dəyişmir, sadəcə mövcud dəyəri "geri qaytarır".
    # ------------------------------------------------------------
    def get_ad(self):
        return self._ad

    # ------------------------------------------------------------
    # SETTER metodu — "_ad" sahəsinin DƏYƏRİNİ DƏYİŞMƏK üçündür.
    # Adının əvvəlində "set_" olması ümumi qəbul edilmiş qaydadır.
    # Hazırda burada heç bir yoxlama yoxdur (sadəcə birbaşa
    # mənimsətmə edir), amma məhz BU YERƏ gələcəkdə yoxlama əlavə
    # etmək mümkündür — məsələn:
    #     if ad.strip() == "":
    #         raise ValueError("Ad boş ola bilməz")
    # ------------------------------------------------------------
    def set_ad(self, ad):
        self._ad = ad


# --------------------------------------------------------------------------
# ad_deyis — bu funksiya bir Telebe obyekti (t) və yeni ad (yeni_ad)
# qəbul edir, sonra setter metodu vasitəsilə obyektin adını dəyişdirir.
#
# ÇOX VACİB QEYD: Python-da obyektlər funksiyalara "referens ilə"
# ötürülür — yəni "t" parametri əslində orijinal obyektin özünə
# işarə edir, onun sürəti (kopyası) DEYİL. Ona görə də bu funksiya
# daxilində edilən dəyişiklik funksiya bitdikdən SONRA da qalacaq —
# çünki eyni obyektə toxunulub.
# --------------------------------------------------------------------------
def ad_deyis(t, yeni_ad):
    t.set_ad(yeni_ad)


def main():
    # Yeni Telebe obyekti yaradılır, "Ravan" adı konstruktora ötürülür.
    # Bu, avtomatik olaraq __init__ metodunu çağırır və self._ad = "Ravan" edir.
    t1 = Telebe("Ravan")

    # Getter metodu çağırılaraq cari ad ekrana çıxarılır.
    # print() funksiyasına verilən birdən çox arqument (dəyər) aralarında
    # boşluqla ayrılaraq çap olunur.
    print("Əvvəl:", t1.get_ad())

    # ad_deyis funksiyası çağırılır. "t1" obyekti və "Ismayil" mətni
    # parametr kimi ötürülür. Funksiya daxilində setter işə düşəcək
    # və t1 obyektinin "_ad" sahəsi "Ismayil" olacaq.
    ad_deyis(t1, "Ismayil")

    # Yenilənmiş adı yenidən getter vasitəsilə oxuyub çap edirik —
    # burada "Sonra: Ismayil" görməliyik, çünki obyekt həqiqətən dəyişib.
    print("Sonra:", t1.get_ad())


if __name__ == "__main__":
    main()
