# ============================================================================
#  DATA — tamamilə boş sinif nümunəsi
# ----------------------------------------------------------------------------
#  Bu, mümkün olan ƏN SADƏ sinif təsviridir — heç bir sahəsi,
#  heç bir metodu yoxdur.
# ============================================================================

# "class Data:" yazıb dərhal sətri bitirsək, Python "bu sinifin
# GÖVDƏSİ (bədəni) haradadır?" deyə xəta verər — Java-dakı kimi
# boş {} mötərizə YAZMAQ Python-da mümkün deyil, çünki Python bloklarını
# mötərizə ilə yox, GİRİNTİ (indentation) ilə müəyyən edir.
#
# Ona görə boş bir blok yaratmaq üçün "pass" açar sözündən istifadə
# olunur. "pass" hərfi mənada "keç, heç nə etmə" deməkdir — sadəcə
# Python-a "bura BOŞ QALSIN, bu, SƏHV DEYİL" mesajını verir.
class Data:
    pass
