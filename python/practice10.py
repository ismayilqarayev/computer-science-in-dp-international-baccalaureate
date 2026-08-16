# ============================================================================
#  PRACTICE 10 — Böyük universitet sistemi nümunəsi
# ----------------------------------------------------------------------------
#  Bu, kursun ƏN BÖYÜK və ƏN MÜRƏKKƏB nümunəsidir. İki fərqli OOP
#  əlaqə növünü BİR ARADA göstərir:
#
#  1) INHERITANCE (İrsiyyət) — "is-a" (BİR NÖVDÜR) əlaqəsi:
#     Sexs (abstrakt)
#       ├── Telebe -> Magistr -> Doktorant
#       └── Muellim -> Professor -> Rektor
#     Məsələn: "Rektor BİR Professordur, Professor BİR Müəllimdir,
#     Müəllim isə BİR Şəxsdir" — bu, ARDICIL ZƏNCİRVARİ irsiyyətdir.
#
#  2) COMPOSITION (Tərkib) — "has-a" (SAHİBDİR) əlaqəsi:
#     Telebe   — İÇİNDƏ bir çox Kurs VƏ Imtahan obyekti SAXLAYIR
#     Doktorant — İÇİNDƏ bir Diplom obyekti SAXLAYIR
#     Məsələn: "Telebe-nin BİR Kursu VAR" — bu, irsiyyət DEYİL,
#     sadəcə bir sinifin daxilində BAŞQA sinifin obyektini SAXLAMASIDIR.
#
#  FƏRQ: irsiyyətdə alt sinif ana sinifin BÜTÜN sahə/metodlarına
#  AVTOMATİK sahib olur. Composition-da isə YALNIZ "mən bu obyekti
#  öz daxilimdə SAXLAYIRAM" əlaqəsi var, heç bir metod avtomatik
#  MİRAS ALINMIR.
# ============================================================================

from abc import ABC, abstractmethod


# ══════════════════════════════════════════════════════════════════════════
#  ABSTRAKT BAZ SİNİF — Şəxs
#  Bütün insan tiplərinin (tələbə, müəllim və onların BÜTÜN alt növlərinin)
#  ORTAQ xüsusiyyətlərini (ad, soyad, yaş) özündə CƏMLƏYİR.
#  Bu sinifdən BİRBAŞA obyekt yaratmaq mümkün deyil (abstraktdır).
# ══════════════════════════════════════════════════════════════════════════
class Sexs(ABC):
    def __init__(self, ad, soyad, yas):
        # "_" prefiksi — Encapsulation. Bu sahələr YALNIZ aşağıdakı
        # getter metodları VASİTƏSİLƏ oxunmalıdır, birbaşa deyil.
        self._ad = ad
        self._soyad = soyad
        self._yas = yas

    # Hər sahə üçün AYRI bir getter — yalnız OXUMAQ üçün (setter YOXDUR,
    # çünki bu nümunədə ad/soyad/yaş dəyişdirilmək NƏZƏRDƏ TUTULMAYIB)
    def get_ad(self):
        return self._ad

    def get_soyad(self):
        return self._soyad

    def get_yas(self):
        return self._yas

    # --------------------------------------------------------------
    # Abstrakt metod — Sexs-dən miras alan HƏR bir sinif
    # (Telebe, Muellim VƏ onların BÜTÜN alt sinifləri — Magistr,
    # Doktorant, Professor, Rektor) bunu MÜTLƏQ ÖZ ÜSULU İLƏ
    # implementasiya etməlidir. Bu, bütün bu siniflərin "eyni
    # ADLA amma FƏRQLİ MƏZMUNLA" işləyən bir metoda sahib olmasını
    # TƏMİN edir — Polymorphism-in TƏMƏLİ budur.
    # --------------------------------------------------------------
    @abstractmethod
    def melumatlari_goster(self):
        pass


# ══════════════════════════════════════════════════════════════════════════
#  KURS SİNİFİ (Composition üçün köməkçi sinif)
#  Sexs-dən MİRAS ALMIR — TAMAMILƏ MÜSTƏQİL, sərbəst bir sinifdir.
#  Telebe obyektləri bu sinifin obyektlərini "ÖZÜNDƏ SAXLAYIR"
#  (composition əlaqəsi: "Telebe-nin Kursu VAR", "Telebe BİR Kurs
#  DEYİL" — bu vacib fərqdir).
# ══════════════════════════════════════════════════════════════════════════
class Kurs:
    def __init__(self, kurs_adi, kredit_saati, muellim):
        self._kurs_adi = kurs_adi
        self._kredit_saati = kredit_saati
        self._muellim = muellim  # burada sadəcə müəllimin ADI (mətn) saxlanılır,
        #                          Muellim OBYEKTİ deyil — sadələşdirmə üçün

    def get_kurs_adi(self):
        return self._kurs_adi

    def get_kredit_saati(self):
        return self._kredit_saati

    def get_muellim(self):
        return self._muellim

    # Kursun məlumatlarını çap edən adi (abstrakt OLMAYAN) metod.
    # İki boşluqla başlaması SADƏCƏ VİZUAL FORMATLAŞDIRMA üçündür —
    # "Kurs" başlığının ALTINDA "girintili" görünsün deyə.
    def kurs_infosu(self):
        print("  Kurs     :", self._kurs_adi)
        print("  Kredit   :", self._kredit_saati)
        print("  Müəllim  :", self._muellim)


# ══════════════════════════════════════════════════════════════════════════
#  İMTAHAN SİNİFİ (Composition üçün köməkçi sinif)
#  Telebe obyektləri bir NEÇƏ Imtahan obyektini ÖZÜNDƏ saxlaya bilər —
#  hər tələbənin BİRDƏN ÇOX imtahanı ola bilər deməkdir.
# ══════════════════════════════════════════════════════════════════════════
class Imtahan:
    def __init__(self, fenn, bal, tarix):
        self._fenn = fenn
        self._bal = bal
        self._tarix = tarix

    # Yalnız "bal" ÜÇÜN getter var (fenn və tarix üçün YOXDUR, çünki
    # bu nümunədə YALNIZ bal ortalama hesablamaq üçün lazımdır —
    # kodda İSTİFADƏ EDİLMƏYƏN getter YAZILMAYIB)
    def get_bal(self):
        return self._bal

    def imtahan_infosu(self):
        print("  Fənn   :", self._fenn)
        print("  Bal    :", self._bal)
        print("  Tarix  :", self._tarix)


# ══════════════════════════════════════════════════════════════════════════
#  DİPLOM SİNİFİ (Composition üçün köməkçi sinif)
#  Yalnız Doktorant sinifində istifadə olunur (1-ə-1 əlaqə —
#  hər doktorantın YALNIZ BİR diplomu ola bilər)
# ══════════════════════════════════════════════════════════════════════════
class Diplom:
    def __init__(self, ixtisas, tarix, ortalama):
        self._ixtisas = ixtisas
        self._tarix = tarix
        self._ortalama = ortalama

    def diplom_infosu(self):
        print("  İxtisas  :", self._ixtisas)
        print("  Tarix    :", self._tarix)
        print("  Ortalama :", self._ortalama)


# ══════════════════════════════════════════════════════════════════════════
#  TƏLƏBƏ — Şəxs-dən miras alır (1-Cİ SƏVİYYƏ irsiyyət)
#  Sexs-in (ad, soyad, yaş) sahələrinə ƏLAVƏ olaraq fakültə, kurs
#  nömrəsi, imtahanlar siyahısı VƏ kurslar siyahısını saxlayır.
# ══════════════════════════════════════════════════════════════════════════
class Telebe(Sexs):
    def __init__(self, ad, soyad, yas, fakulte, kurs):
        # ------------------------------------------------------------
        # super().__init__(ad, soyad, yas) — ANA SİNİFİN (Sexs) konstruktoru
        # çağırılır. Bu, self._ad, self._soyad, self._yas sahələrini
        # BİZİM ƏVƏZİMİZƏ QURUR. Telebe sinifi bu üç sahəni ÖZÜ İKİNCİ
        # DƏFƏ YAZMIR — bu, kodun TƏKRARLANMAMASI üçündür.
        # ------------------------------------------------------------
        super().__init__(ad, soyad, yas)
        self._fakulte = fakulte
        self._kurs = kurs
        # ------------------------------------------------------------
        # Boş siyahılar — COMPOSITION əlaqəsinin BAŞLANĞICI.
        # Hazırda bu tələbənin HEÇ BİR imtahanı/kursu YOXDUR, amma
        # aşağıdakı imtahan_elave() və kurs_elave() metodları vasitəsilə
        # SONRADAN doldurula bilər.
        # ------------------------------------------------------------
        self._imtahanlar = []
        self._kurs_list = []

    # --------------------------------------------------------------
    # COMPOSITION: Telebe obyektinin DAXİLİNƏ YENİ BİR Imtahan obyekti
    # "QOŞULUR" (append edilir). Diqqət: bu, İRSİYYƏT DEYİL — Telebe
    # Imtahan-dan MİRAS ALMIR, sadəcə onu ÖZ SİYAHISINDA SAXLAYIR.
    # --------------------------------------------------------------
    def imtahan_elave(self, imtahan):
        self._imtahanlar.append(imtahan)

    # COMPOSITION: eyni məntiqlə, YENİ BİR Kurs obyekti "QOŞULUR"
    def kurs_elave(self, k):
        self._kurs_list.append(k)

    # --------------------------------------------------------------
    # Bütün imtahan ballarının ORTA QİYMƏTİNİ hesablayır.
    # --------------------------------------------------------------
    def ortalama_hesabla(self):
        if not self._imtahanlar:  # siyahı BOŞDURSA (heç imtahan yoxdursa)
            return 0  # sıfıra bölmə XƏTASININ QARŞISINI ALMAQ üçün erkən çıxış

        # ------------------------------------------------------------
        # sum(i.get_bal() for i in self._imtahanlar)
        #
        # Bu, "GENERATOR İFADƏSİDİR" — Python-un çox güclü, qısa yazılış
        # üsuludur. Sətri belə OXUMAQ olar:
        #     "self._imtahanlar siyahısındakı HƏR BİR 'i' üçün,
        #      onun get_bal() dəyərini götür, SONRA hamısını CƏMLƏ"
        #
        # Bu, Java-dakı bu koda BƏRABƏRDİR:
        #     double cem = 0;
        #     for (Imtahan i : imtahanlar) {
        #         cem += i.getBal();
        #     }
        #
        # Python-da bunu BİR SƏTİRDƏ yazmaq mümkündür, çünki sum()
        # funksiyası verilən "generator"un HƏR ELEMENTİNİ ötürüb CƏMLƏYİR.
        # ------------------------------------------------------------
        cem = sum(i.get_bal() for i in self._imtahanlar)

        # len(...) — siyahının NEÇƏ ELEMENTDƏN İBARƏT olduğunu qaytarır
        # (Java-dakı .size() metoduna bənzəyir)
        return cem / len(self._imtahanlar)

    def get_fakulte(self):
        return self._fakulte

    def get_kurs(self):
        return self._kurs

    # --------------------------------------------------------------
    # Abstrakt melumatlari_goster() metodunun Telebe ÜÇÜN KONKRET versiyası.
    # Bu metod HƏM Sexs-dən miras aldığı getter-ləri (get_ad, get_soyad,
    # get_yas), HƏM DƏ öz composition SİYAHILARINI (kurslar, imtahanlar)
    # bir yerdə İSTİFADƏ EDİR.
    # --------------------------------------------------------------
    def melumatlari_goster(self):
        print("Ad / Soyad :", self.get_ad(), self.get_soyad())
        print("Yaş        :", self.get_yas())
        print("Fakültə    :", self._fakulte)
        print("Kurs       :", self._kurs)
        print("Ortalama   :", self.ortalama_hesabla())

        # Yalnız siyahı BOŞ OLMADIQDA əlavə başlıq VƏ elementləri çap edir —
        # bu, "boş --- Kurslar --- başlığı görünməsin" deyə edilir
        if self._kurs_list:
            print("--- Kurslar ---")
            for k in self._kurs_list:
                k.kurs_infosu()  # hər Kurs obyektinin ÖZ metodu çağırılır

        if self._imtahanlar:
            print("--- İmtahanlar ---")
            for i in self._imtahanlar:
                i.imtahan_infosu()


# ══════════════════════════════════════════════════════════════════════════
#  MAGİSTR — Tələbə-dən miras alır (2-Cİ SƏVİYYƏ irsiyyət)
#  Telebe-nin BÜTÜN xüsusiyyətlərinə (ki, o da Sexs-dən irsiyyət alıb —
#  yəni Magistr DOLAYI YOLLA Sexs-in DƏ bütün sahələrinə sahibdir)
#  ƏLAVƏ olaraq tədqiqat mövzusu VƏ elmi rəhbər sahələrini əlavə edir.
# ══════════════════════════════════════════════════════════════════════════
class Magistr(Telebe):
    def __init__(self, ad, soyad, yas, fakulte, kurs, teqiqat_movzusu, elmi_rehber):
        # Telebe-nin konstruktoru çağırılır — O DA ÖZ NÖVBƏSİNDƏ Sexs-i çağırır.
        # Beləliklə BİR Magistr yaradıldıqda ZƏNCİRVARİ ÇAĞIRIŞ baş verir:
        #     Magistr.__init__ -> Telebe.__init__ -> Sexs.__init__
        super().__init__(ad, soyad, yas, fakulte, kurs)
        self._teqiqat_movzusu = teqiqat_movzusu
        self._elmi_rehber = elmi_rehber

    # --------------------------------------------------------------
    # Method Overriding: Telebe-nin melumatlari_goster()-i ƏVVƏLCƏ
    # çağırılır (bu, Ad/Soyad/Yaş/Fakültə/Kurs/Ortalama/Kurslar/
    # İmtahanlar hissəsini çap edir), SONRA Magistr-ə MƏXSUS əlavə
    # sətrlər çap olunur. Bu üsul "GENİŞLƏNDİRMƏ" (extension) adlanır —
    # köhnə davranış TAMAM ATILMIR, sadəcə ÜSTÜNƏ ƏLAVƏ EDİLİR.
    # --------------------------------------------------------------
    def melumatlari_goster(self):
        super().melumatlari_goster()
        print("Tədqiqat   :", self._teqiqat_movzusu)
        print("Elmi rəhbər:", self._elmi_rehber)


# ══════════════════════════════════════════════════════════════════════════
#  DOKTORANT — Magistr-dən miras alır (3-CÜ SƏVİYYƏ irsiyyət)
#  TAM ZƏNCİR: Sexs -> Telebe -> Magistr -> Doktorant
#  Doktorant HƏM DƏ bir Diplom obyektini ÖZÜNDƏ saxlaya bilər (composition)
# ══════════════════════════════════════════════════════════════════════════
class Doktorant(Magistr):
    def __init__(self, ad, soyad, yas, fakulte, kurs, teqiqat_movzusu, elmi_rehber,
                 dissertasiya_movzusu, nesr_sayi):
        # Magistr-in konstruktoru çağırılır (7 parametr) — O DA ZƏNCİRİ DAVAM ETDİRİR
        super().__init__(ad, soyad, yas, fakulte, kurs, teqiqat_movzusu, elmi_rehber)
        self._dissertasiya_movzusu = dissertasiya_movzusu
        self._nesr_sayi = nesr_sayi
        # Diplom HƏLƏ TƏYİN OLUNMAYIB, ona görə None (Java-dakı "null"
        # ilə EYNİ MƏNANI daşıyır: "burada hələ heç bir dəyər YOXDUR")
        self._diplom = None

    # --------------------------------------------------------------
    # COMPOSITION: Doktoranta BİR Diplom obyekti "BAĞLANIR".
    # Diqqət: bu, KONSTRUKTORDA DEYİL, AYRI BİR METODLA edilir —
    # çünki diplom TƏLƏBƏ QƏBUL EDİLDİKDƏ DEYİL, DAHA SONRA
    # (təhsili bitirdikdə) verilir — bu, PROQRAMIN MƏNTİQİNƏ UYĞUNDUR.
    # --------------------------------------------------------------
    def diplom_teyin(self, diplom):
        self._diplom = diplom

    def melumatlari_goster(self):
        # Zəncirvari çağırış: Doktorant -> Magistr -> Telebe ->
        # (Sexs-in getter-ləri) — bu TƏK sətir HƏQİQƏTDƏ ÜÇ FƏRQLİ
        # SİNİFDƏKİ məlumatları BİR ARADA çap edir
        super().melumatlari_goster()
        print("Dissertasiya:", self._dissertasiya_movzusu)
        print("Nəşr sayı   :", self._nesr_sayi)

        # Diplom YALNIZ təyin OLUNUBSA çap olunur (None YOXLAMASI —
        # "is not None" YAZMAQ "if self._diplom:" yazmaqdan DAHA
        # AYDINDIR, çünki niyyətimiz "None DEYİLMİ" YOXLAMAQDIR)
        if self._diplom is not None:
            print("--- Diplom ---")
            self._diplom.diplom_infosu()


# ══════════════════════════════════════════════════════════════════════════
#  MÜƏLLİM — Şəxs-dən miras alır (1-Cİ SƏVİYYƏ irsiyyət,
#  Telebe-dən TAMAM AYRI, PARALEL bir BUDAQ — Muellim VƏ Telebe
#  BİR-BİRİNƏ QOHUM DEYİL, hər ikisi sadəcə eyni "ATANIN" (Sexs)
#  övladlarıdır)
# ══════════════════════════════════════════════════════════════════════════
class Muellim(Sexs):
    def __init__(self, ad, soyad, yas, fakulte, fenn, tedris_tecurbesi):
        super().__init__(ad, soyad, yas)
        self._fakulte = fakulte
        self._fenn = fenn
        self._tedris_tecurbesi = tedris_tecurbesi

    def get_fakulte(self):
        return self._fakulte

    def get_fenn(self):
        return self._fenn

    def melumatlari_goster(self):
        print("Ad / Soyad   :", self.get_ad(), self.get_soyad())
        print("Yaş          :", self.get_yas())
        print("Fakültə      :", self._fakulte)
        print("Fənn         :", self._fenn)
        print("Təcrübə (il) :", self._tedris_tecurbesi)


# ══════════════════════════════════════════════════════════════════════════
#  PROFESSOR — Müəllim-dən miras alır (2-Cİ SƏVİYYƏ)
# ══════════════════════════════════════════════════════════════════════════
class Professor(Muellim):
    def __init__(self, ad, soyad, yas, fakulte, fenn, tedris_tecurbesi, elmi_derece, nesr_sayi):
        super().__init__(ad, soyad, yas, fakulte, fenn, tedris_tecurbesi)
        self._elmi_derece = elmi_derece
        self._nesr_sayi = nesr_sayi

    def melumatlari_goster(self):
        super().melumatlari_goster()
        print("Elmi dərəcə  :", self._elmi_derece)
        print("Nəşr sayı    :", self._nesr_sayi)


# ══════════════════════════════════════════════════════════════════════════
#  REKTOR — Professor-dan miras alır (3-CÜ SƏVİYYƏ)
#  TAM ZƏNCİR: Sexs -> Muellim -> Professor -> Rektor
#  (Telebe budağı ilə Muellim budağı TAMAM PARALELDİR — ikisi
#  arasında HEÇ BİR birbaşa əlaqə YOXDUR, YALNIZ ORTAQ ƏCDADLARI
#  Sexs-dir)
# ══════════════════════════════════════════════════════════════════════════
class Rektor(Professor):
    def __init__(self, ad, soyad, yas, fakulte, fenn, tedris_tecurbesi,
                 elmi_derece, nesr_sayi, universitet, idareetme_tecurbesi):
        super().__init__(ad, soyad, yas, fakulte, fenn, tedris_tecurbesi,
                          elmi_derece, nesr_sayi)
        self._universitet = universitet
        self._idareetme_tecurbesi = idareetme_tecurbesi

    def melumatlari_goster(self):
        # Zəncirvari çağırış: Rektor -> Professor -> Muellim ->
        # (Sexs-in getter-ləri)
        super().melumatlari_goster()
        print("Universitet      :", self._universitet)
        print("İdarəetmə (il)   :", self._idareetme_tecurbesi)


# ══════════════════════════════════════════════════════════════════════════
#  MAIN — bütün sinifləri SINAQDAN KEÇİRƏN əsas funksiya.
#  Hər bölmə istifadəçidən MÜVAFİQ məlumatları alır, UYĞUN obyekti
#  yaradır və melumatlari_goster() ilə nəticəni çap edir.
#
#  Struktur olaraq bu funksiya YEDDİ (7) OXŞAR BLOKDAN İBARƏTDİR —
#  hər blok "sual soruş -> obyekt yarat -> göstər" ardıcıllığını
#  təkrarlayır, sadəcə HANSI SİNİFDƏN İSTİFADƏ EDİLDİYİ FƏRQLƏNİR.
# ══════════════════════════════════════════════════════════════════════════
def main():
    # ── TƏLƏBƏ ──────────────────────────────────────────
    print("\n========== TƏLƏBƏ ==========")
    # "\n" — mətn daxilində YENİ SƏTRƏ keçid simvoludur, başlıqdan
    # ƏVVƏL boş sətir buraxmaq üçün istifadə olunur
    t_ad = input("Ad: ")
    t_soyad = input("Soyad: ")
    t_yas = int(input("Yaş: "))  # mətn -> tam ədəd çevrilməsi
    t_fakulte = input("Fakültə: ")
    t_kurs = int(input("Kurs (1-4): "))

    # Telebe obyekti yaradılır — bu, arxa planda Telebe.__init__ ->
    # Sexs.__init__ zəncirini işə salır
    telebe = Telebe(t_ad, t_soyad, t_yas, t_fakulte, t_kurs)

    # Telebe-yə BİR Kurs obyekti "ƏLAVƏ" edilir (composition) —
    # əvvəlcə Kurs(...) ilə YENİ obyekt yaradılır, sonra bu obyekt
    # kurs_elave() metoduna ötürülüb Telebe-nin daxili siyahısına yığılır
    k_ad = input("Kurs adı: ")
    k_kredit = int(input("Kredit saatı: "))
    k_muellim = input("Müəllim: ")
    telebe.kurs_elave(Kurs(k_ad, k_kredit, k_muellim))

    # Telebe-yə BİR Imtahan obyekti "ƏLAVƏ" edilir (composition) — eyni məntiq
    i_fenn = input("İmtahan fənni: ")
    i_bal = float(input("Bal: "))  # bal kəsr ədəd ola bilər (məs: 87.5)
    i_tarix = input("Tarix: ")
    telebe.imtahan_elave(Imtahan(i_fenn, i_bal, i_tarix))

    print("\n--- Tələbə məlumatları ---")
    telebe.melumatlari_goster()

    # ── MAGİSTR ─────────────────────────────────────────
    print("\n========== MAGİSTR ==========")
    m_ad = input("Ad: ")
    m_soyad = input("Soyad: ")
    m_yas = int(input("Yaş: "))
    m_fakulte = input("Fakültə: ")
    m_kurs = int(input("Kurs: "))
    m_movzu = input("Tədqiqat mövzusu: ")
    m_rehber = input("Elmi rəhbər: ")

    magistr = Magistr(m_ad, m_soyad, m_yas, m_fakulte, m_kurs, m_movzu, m_rehber)

    print("\n--- Magistr məlumatları ---")
    magistr.melumatlari_goster()

    # ── DOKTORANT ────────────────────────────────────────
    print("\n========== DOKTORANT ==========")
    d_ad = input("Ad: ")
    d_soyad = input("Soyad: ")
    d_yas = int(input("Yaş: "))
    d_fakulte = input("Fakültə: ")
    d_kurs = int(input("Kurs: "))
    d_movzu = input("Tədqiqat mövzusu: ")
    d_rehber = input("Elmi rəhbər: ")
    d_diss = input("Dissertasiya: ")
    d_nesr = int(input("Nəşr sayı: "))

    doktorant = Doktorant(d_ad, d_soyad, d_yas, d_fakulte, d_kurs, d_movzu, d_rehber, d_diss, d_nesr)

    # Doktoranta BİR Diplom obyekti TƏYİN EDİLİR (composition) —
    # yalnız DOKTORANT üçün əlavə edilir, digər siniflər üçün yoxdur
    dip_ixt = input("Diplom ixtisası: ")
    dip_tarix = input("Diplom tarixi: ")
    dip_ort = float(input("Diplom ortalama: "))
    doktorant.diplom_teyin(Diplom(dip_ixt, dip_tarix, dip_ort))

    print("\n--- Doktorant məlumatları ---")
    doktorant.melumatlari_goster()

    # ── MÜƏLLİM ─────────────────────────────────────────
    print("\n========== MÜƏLLİM ==========")
    mu_ad = input("Ad: ")
    mu_soyad = input("Soyad: ")
    mu_yas = int(input("Yaş: "))
    mu_fakulte = input("Fakültə: ")
    mu_fenn = input("Fənn: ")
    mu_tec = int(input("Təcrübə (il): "))

    muellim = Muellim(mu_ad, mu_soyad, mu_yas, mu_fakulte, mu_fenn, mu_tec)

    print("\n--- Müəllim məlumatları ---")
    muellim.melumatlari_goster()

    # ── PROFESSOR ────────────────────────────────────────
    print("\n========== PROFESSOR ==========")
    pr_ad = input("Ad: ")
    pr_soyad = input("Soyad: ")
    pr_yas = int(input("Yaş: "))
    pr_fakulte = input("Fakültə: ")
    pr_fenn = input("Fənn: ")
    pr_tec = int(input("Təcrübə (il): "))
    pr_derece = input("Elmi dərəcə: ")
    pr_nesr = int(input("Nəşr sayı: "))

    professor = Professor(pr_ad, pr_soyad, pr_yas, pr_fakulte, pr_fenn, pr_tec, pr_derece, pr_nesr)

    print("\n--- Professor məlumatları ---")
    professor.melumatlari_goster()

    # ── REKTOR ───────────────────────────────────────────
    print("\n========== REKTOR ==========")
    r_ad = input("Ad: ")
    r_soyad = input("Soyad: ")
    r_yas = int(input("Yaş: "))
    r_fakulte = input("Fakültə: ")
    r_fenn = input("Fənn: ")
    r_tec = int(input("Təcrübə (il): "))
    r_derece = input("Elmi dərəcə: ")
    r_nesr = int(input("Nəşr sayı: "))
    r_univer = input("Universitet: ")
    r_idaree = int(input("İdarəetmə (il): "))

    # Ən uzun konstruktor çağırışı — 10 parametr, çünki Rektor
    # ZƏNCİRİN ƏN SONUNDADIR və BÜTÜN əcdadlarının sahələrini daşıyır
    rektor = Rektor(r_ad, r_soyad, r_yas, r_fakulte, r_fenn, r_tec, r_derece, r_nesr, r_univer, r_idaree)

    print("\n--- Rektor məlumatları ---")
    rektor.melumatlari_goster()


if __name__ == "__main__":
    main()
