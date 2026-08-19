# ============================================================================
#  MAIN STUB — boş, "iskelet" (skeleton) sinif nümunəsi
# ----------------------------------------------------------------------------
#  Bu fayl orijinal Java kodunda da tamamilə "başlanğıc mərhələdə" idi —
#  yəni sinif sadəcə HANSI SAHƏLƏRİN OLACAĞINI planlaşdırır, amma hələ
#  heç bir metod, heç bir məntiq yazılmayıb. Bu, real layihələrdə
#  proqramçıların "əvvəlcə strukturu qurub, sonra funksionallığı əlavə
#  etmə" mərhələsinə bənzəyir.
# ============================================================================

from abc import ABC


# --------------------------------------------------------------------------
# Bu sinif ABC-dən miras alır, AMMA içində HEÇ BİR @abstractmethod yoxdur.
# Ona görə texniki olaraq bu sinif hələ "tam abstrakt" DEYİL — yəni
# istəsək ondan obyekt yarada bilərik (Python bunu qadağan etməyəcək,
# çünki qadağan yalnız @abstractmethod olan metodlar üçündür).
#
# Bu, orijinal Java kodundakı vəziyyətin EYNİ İLƏ köçürülməsidir —
# "abstract" açar sözü var idi, amma "abstract" metod yox idi.
# --------------------------------------------------------------------------
class Telebe(ABC):
    def __init__(self):
        # Bu sahələr hələ HEÇ YERDƏ istifadə olunmur — sadəcə
        # gələcəkdə bu sinifin HANSI MƏLUMATLARI SAXLAYACAĞININ
        # planını göstərir. Hamısına "None" (Java-dakı "null" ilə
        # eyni məna daşıyır — "hələ heç bir dəyər verilməyib") verilib.
        self.ad = None
        self.soyad = None
        self.telefon_nomresi = None
        self.email = None
        self.yas = None
        self.cins = None


def main():
    # Hələlik boşdur — orijinal Java kodunda da main() metodunun
    # daxilində heç bir kod yox idi
    pass


if __name__ == "__main__":
    main()
