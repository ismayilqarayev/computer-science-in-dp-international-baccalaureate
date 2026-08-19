# ============================================================================
#  PRACTICE 9 — Validasiya (input yoxlaması) ilə tam nümunə
# ----------------------------------------------------------------------------
#  Bu, ən əvvəlki nümunələrin (abstraction + inheritance + polymorphism +
#  encapsulation) HAMISINI BİR YERƏ toplayan, üstəlik istifadəçi
#  girişini YOXLAYAN (validasiya edən) TAM bir proqramdır.
#
#  Yeni mövzular:
#    1) re modulu (regular expressions / requlyar ifadələr) nədir?
#    2) while dövrü ilə "düzgün giriş alınana qədər soruş" məntiqi
#    3) strip() ilə boşluqları təmizləmək
#    4) continue açar sözü ilə dövrün əvvəlinə qayıtmaq
# ============================================================================

import re  # re — Python-un STANDART kitabxanasında olan, requlyar
#            ifadələrlə (mətn şablonları ilə) işləmək üçün modul
from abc import ABC, abstractmethod


# Abstrakt sinif (Abstraction)
# Bu sinif birbaşa obyekt yaratmaq üçün deyil,
# digər siniflər üçün baza rolunu oynayır
class Telebe(ABC):

    # Encapsulation (İnkapsulyasiya) — 4 "daxili" sahə
    def __init__(self, ad, soyad, telefon_nomresi, email):
        self._ad = ad
        self._soyad = soyad
        self._telefon_nomresi = telefon_nomresi
        self._email = email

    # ---- Getter-lər — sahə dəyərlərini oxumaq üçün ----
    def get_ad(self):
        return self._ad

    def get_soyad(self):
        return self._soyad

    def get_telefon_nomresi(self):
        return self._telefon_nomresi

    def get_email(self):
        return self._email

    # ---- Setter-lər — sahə dəyərlərini dəyişmək üçün ----
    def set_ad(self, ad):
        self._ad = ad

    def set_soyad(self, soyad):
        self._soyad = soyad

    def set_telefon_nomresi(self, telefon_nomresi):
        self._telefon_nomresi = telefon_nomresi

    def set_email(self, email):
        self._email = email

    # Abstrakt metod — hər alt sinif öz implementasiyasını yazmalıdır
    @abstractmethod
    def melumat_goster(self):
        pass


# Inheritance (İrsiyyət)
# MagistrTelebe sinifi Telebe sinifindən miras alır
class MagistrTelebe(Telebe):

    # Bu sinifə məxsus əlavə sahə — universitetin adı
    def __init__(self, ad, soyad, telefon_nomresi, email, universitet):
        super().__init__(ad, soyad, telefon_nomresi, email)
        self._universitet = universitet

    # Abstrakt metodun implementasiyası (Polymorphism)
    def melumat_goster(self):
        print(f"Ad: {self.get_ad()} {self.get_soyad()}")
        print(f"Telefon: {self.get_telefon_nomresi()}")
        print(f"Email: {self.get_email()}")
        print(f"Universitet: {self._universitet}")


# Inheritance (İrsiyyət) — 2-ci səviyyə
# DoktorantTelebe sinifi MagistrTelebe sinifindən miras alır.
# Beləliklə Telebe -> MagistrTelebe -> DoktorantTelebe zənciri yaranır
class DoktorantTelebe(MagistrTelebe):

    # Bu sinifə məxsus əlavə sahə — tədqiqat mövzusu
    def __init__(self, ad, soyad, telefon_nomresi, email, universitet, tedqiqat_movzusu):
        super().__init__(ad, soyad, telefon_nomresi, email, universitet)
        self._tedqiqat_movzusu = tedqiqat_movzusu

    # Method Overriding (Polymorphism)
    def melumat_goster(self):
        super().melumat_goster()  # ana sinifin BÜTÜN məlumatını əvvəlcə çap edir
        print(f"Tədqiqat Mövzusu: {self._tedqiqat_movzusu}")


# ============================================================================
#  KÖMƏKÇİ (helper) FUNKSİYALAR — validasiya ilə giriş almaq üçün
#  Bu funksiyalar sinif deyil, sadəcə YENİDƏN İSTİFADƏ oluna bilən
#  "alət" funksiyalarıdır. Kod TƏKRARLANMASIN deyə ayrıca yazılıblar.
# ============================================================================

def bos_olmayan_giris_oxu(mesaj):
    # --------------------------------------------------------
    # Bu funksiya istifadəçidən BOŞ OLMAYAN mətn alana qədər
    # sual verməyə DAVAM EDİR — yəni "sonsuz dövr, düzgün cavab
    # alınanda özü DAYANIR" məntiqi.
    # --------------------------------------------------------
    while True:  # "True" HƏMİŞƏ doğrudur, ona görə bu, SONSUZ dövrdür —
        #          dövrdən yalnız "return" ilə çıxmaq olar
        deyer = input(mesaj).strip()
        # .strip() — mətnin ƏVVƏLİNDƏKİ və SONUNDAKI boşluq/tab/yeni-sətir
        # simvollarını təmizləyir. Məsələn "  Ali  " -> "Ali" olur.
        # Bu, istifadəçinin təsadüfən əlavə boşluq yazmasının qarşısını alır.

        if deyer:  # BOŞ MƏTN Python-da "yalan" (falsy) sayılır,
            #        yəni "if deyer:" əslində "if deyer != '':" ilə eynidir
            return deyer  # düzgün dəyər tapıldı, funksiyadan bu dəyərlə çıxırıq

        # Əgər buraya çatdıqsa, deməli "deyer" boş idi —
        # xəbərdarlıq mesajı çap olunur və dövr TƏKRAR BAŞLAYIR
        # (yeni sual veriləcək)
        print("Yanlış giriş: bu sahə boş ola bilməz. Zəhmət olmasa düzgün dəyər daxil edin.")


def telefon_duzgundur(telefon):
    # --------------------------------------------------------
    # re.match(pattern, text) — "text" mətninin ƏVVƏLİNDƏN başlayaraq
    # "pattern" şablonuna uyğun gəlib-gəlmədiyini yoxlayır.
    # Uyğun gəlirsə bir "Match" obyekti, gəlmirsə "None" qaytarır.
    #
    # Şablon izahı: r"^\+?[0-9\-\s]{7,20}$"
    #   r"..."      -> "raw string" — mətn daxilindəki \ işarələrinin
    #                  Python tərəfindən xüsusi məna daşımamasını təmin edir
    #   ^           -> mətnin BAŞLANĞICI
    #   \+?         -> ixtiyari (?) olaraq BİR "+" işarəsi ola bilər
    #   [0-9\-\s]   -> BU SİNİFDƏKİ simvollardan biri: rəqəm (0-9),
    #                  tire (-) və ya boşluq (\s)
    #   {7,20}      -> yuxarıdakı simvol sinfindən 7 İLƏ 20 ARASI say
    #   $           -> mətnin SONU
    #
    # Yəni: "istəyə bağlı + işarəsi ilə başlayan, sonra 7-20 arası
    # rəqəm/tire/boşluqdan ibarət mətn" formatını yoxlayır.
    #
    # "is not None" — əgər uyğunluq tapılıbsa (None deyilsə) True,
    # tapılmayıbsa (None-dursa) False qaytarır.
    # --------------------------------------------------------
    return re.match(r"^\+?[0-9\-\s]{7,20}$", telefon) is not None


def email_duzgundur(email):
    # --------------------------------------------------------
    # Şablon izahı: r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    #   ^[^\s@]+    -> mətnin əvvəlində, BOŞLUQ VƏ "@" OLMAYAN,
    #                  ən azı 1 simvoldan ibarət hissə (istifadəçi adı)
    #   @           -> tam olaraq BİR "@" işarəsi
    #   [^\s@]+     -> domen adı hissəsi (yenə boşluq/@ olmadan)
    #   \.          -> NÖQTƏ işarəsi (\. yazılıb, çünki tək "." regex-də
    #                  "İSTƏNİLƏN SİMVOL" mənasını verir, biz isə
    #                  HƏQİQİ nöqtəni axtarırıq)
    #   [^\s@]+$    -> domen uzantısı (com, az, org və s.), mətnin SONU
    #
    # Misal uyğunluq: "user@example.com" -> DÜZGÜN
    # Misal uyğunsuzluq: "user@@example" -> SƏHV (iki @ var, nöqtə yoxdur)
    # --------------------------------------------------------
    return re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", email) is not None


def duzgun_telefon_oxu(mesaj):
    # Düzgün formatda telefon nömrəsi daxil edilənə qədər TƏKRAR SORĞU EDİR
    while True:
        telefon = input(mesaj).strip()

        if not telefon:  # "not telefon" -> telefon boşdursa True
            print("Yanlış giriş: telefon nömrəsi boş ola bilməz.")
            # ------------------------------------------------
            # continue — dövrün QALAN HİSSƏSİNİ ATLAYIR və birbaşa
            # "while True:" sətrinə QAYIDIR, yəni YENİ sual verir.
            # Bu, "return" DEYİL — funksiyadan çıxmır, sadəcə
            # bu dövr addımını erkən bitirir.
            # ------------------------------------------------
            continue

        if telefon_duzgundur(telefon):
            return telefon  # format düzgündür, funksiyadan çıxırıq

        # Buraya çatdıqsa: telefon boş DEYİL, amma format YANLIŞDIR
        print("Telefon nömrəsi yanlışdır. Rəqəm, boşluq, tire və ixtiyari başlanğıc + istifadə edin.")


def duzgun_email_oxu(mesaj):
    # Eyni məntiq, email üçün
    while True:
        email = input(mesaj).strip()
        if not email:
            print("Yanlış giriş: email boş ola bilməz.")
            continue
        if email_duzgundur(email):
            return email
        print("Email formatı yanlışdır. Nümunə: user@example.com")


def main():
    # ── Magistr Tələbə məlumatlarının daxil edilməsi ──────────────
    print("Magistr tələbə məlumatlarının daxil edilməsi:")
    mt_ad = bos_olmayan_giris_oxu("Magistr tələbənin adını daxil edin: ")
    mt_soyad = bos_olmayan_giris_oxu("Magistr tələbənin soyadını daxil edin: ")
    mt_telefon = duzgun_telefon_oxu("Magistr tələbənin telefon nömrəsini daxil edin: ")
    mt_email = duzgun_email_oxu("Magistr tələbənin emailini daxil edin: ")
    mt_universitet = bos_olmayan_giris_oxu("Magistr tələbənin universitetini daxil edin: ")

    magistr_telebe = MagistrTelebe(mt_ad, mt_soyad, mt_telefon, mt_email, mt_universitet)
    print()
    magistr_telebe.melumat_goster()

    # ── Doktorant Tələbə məlumatlarının daxil edilməsi ───────────────────
    print()
    print("Doktorant tələbə məlumatlarının daxil edilməsi:")
    dt_ad = bos_olmayan_giris_oxu("Doktorant tələbənin adını daxil edin: ")
    dt_soyad = bos_olmayan_giris_oxu("Doktorant tələbənin soyadını daxil edin: ")
    dt_telefon = duzgun_telefon_oxu("Doktorant tələbənin telefon nömrəsini daxil edin: ")
    dt_email = duzgun_email_oxu("Doktorant tələbənin emailini daxil edin: ")
    dt_universitet = bos_olmayan_giris_oxu("Doktorant tələbənin universitetini daxil edin: ")
    dt_tedqiqat_movzusu = bos_olmayan_giris_oxu("Doktorant tələbənin tədqiqat mövzusunu daxil edin: ")

    doktorant_telebe = DoktorantTelebe(dt_ad, dt_soyad, dt_telefon, dt_email, dt_universitet, dt_tedqiqat_movzusu)
    print()
    doktorant_telebe.melumat_goster()


if __name__ == "__main__":
    main()
