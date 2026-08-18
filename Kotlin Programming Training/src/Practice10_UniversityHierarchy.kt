// ══════════════════════════════════════════════════════════════
//  PRACTICE 10 — Çoxsəviyyəli irsiyyət: Universitet iyerarxiyası
//  (java/java Practice Programs10.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Bu, Main.kt-dəki eyni proqramdır — bura "Practice10" adı ilə əlavə
// olunub ki, digər Practice fayllarıyla eyni nömrələmə ardıcıllığı
// (01-15) qorunsun. Məzmun Main.kt ilə eynidir.
//
// NOT: Main.kt-də "Sexs", "Telebe", "Muellim" və s. eyni adlı siniflər
// artıq var. Ad toqquşmasının (redeclaration) qarşısını almaq üçün
// bu fayl öz ayrıca "package"-inə yerləşdirilib.
package practice10

import java.util.Scanner

// ══════════════════════════════════════════════
//  ABSTRAKT BAZ SİNİF — Şəxs
// ══════════════════════════════════════════════
abstract class Sexs(
    val ad: String,
    val soyad: String,
    val yas: Int
) {
    abstract fun melumatlariGoster()
}

// ══════════════════════════════════════════════
//  KURS SİNİFİ
// ══════════════════════════════════════════════
class Kurs(
    val kursAdi: String,
    val kreditSaati: Int,
    val muellim: String
) {
    fun kursInfosu() {
        println("  Kurs     : $kursAdi")
        println("  Kredit   : $kreditSaati")
        println("  Müəllim  : $muellim")
    }
}

// ══════════════════════════════════════════════
//  İMTAHAN SİNİFİ
// ══════════════════════════════════════════════
class Imtahan(
    private val fenn: String,
    val bal: Double,
    private val tarix: String
) {
    fun imtahanInfosu() {
        println("  Fənn   : $fenn")
        println("  Bal    : $bal")
        println("  Tarix  : $tarix")
    }
}

// ══════════════════════════════════════════════
//  DİPLOM SİNİFİ
// ══════════════════════════════════════════════
class Diplom(
    private val ixtisas: String,
    private val tarix: String,
    private val ortalama: Double
) {
    fun diplomInfosu() {
        println("  İxtisas  : $ixtisas")
        println("  Tarix    : $tarix")
        println("  Ortalama : $ortalama")
    }
}

// ══════════════════════════════════════════════
//  TƏLƏBƏ — Şəxs-dən miras alır
// ══════════════════════════════════════════════
open class Telebe(
    ad: String,
    soyad: String,
    yas: Int,
    val fakulte: String,
    val kurs: Int
) : Sexs(ad, soyad, yas) {

    private val imtahanlar = mutableListOf<Imtahan>()
    private val kursList = mutableListOf<Kurs>()

    fun imtahanElave(imtahan: Imtahan) {
        imtahanlar.add(imtahan)
    }

    fun kursElave(k: Kurs) {
        kursList.add(k)
    }

    fun ortalamaHesabla(): Double {
        if (imtahanlar.isEmpty()) return 0.0
        var cem = 0.0
        for (i in imtahanlar) cem += i.bal
        return cem / imtahanlar.size
    }

    override fun melumatlariGoster() {
        println("Ad / Soyad : $ad $soyad")
        println("Yaş        : $yas")
        println("Fakültə    : $fakulte")
        println("Kurs       : $kurs")
        println("Ortalama   : ${ortalamaHesabla()}")

        if (kursList.isNotEmpty()) {
            println("--- Kurslar ---")
            for (k in kursList) k.kursInfosu()
        }

        if (imtahanlar.isNotEmpty()) {
            println("--- İmtahanlar ---")
            for (i in imtahanlar) i.imtahanInfosu()
        }
    }
}

// ══════════════════════════════════════════════
//  MAGİSTR — Tələbə-dən miras alır
// ══════════════════════════════════════════════
open class Magistr(
    ad: String,
    soyad: String,
    yas: Int,
    fakulte: String,
    kurs: Int,
    private val teqiqatMovzusu: String,
    private val elmiRehber: String
) : Telebe(ad, soyad, yas, fakulte, kurs) {

    override fun melumatlariGoster() {
        super.melumatlariGoster()
        println("Tədqiqat   : $teqiqatMovzusu")
        println("Elmi rəhbər: $elmiRehber")
    }
}

// ══════════════════════════════════════════════
//  DOKTORANT — Magistr-dən miras alır
// ══════════════════════════════════════════════
class Doktorant(
    ad: String,
    soyad: String,
    yas: Int,
    fakulte: String,
    kurs: Int,
    teqiqatMovzusu: String,
    elmiRehber: String,
    private val dissertasiyaMovzusu: String,
    private val nesrSayi: Int
) : Magistr(ad, soyad, yas, fakulte, kurs, teqiqatMovzusu, elmiRehber) {

    private var diplom: Diplom? = null

    fun diplomTeyin(diplom: Diplom) {
        this.diplom = diplom
    }

    override fun melumatlariGoster() {
        super.melumatlariGoster()
        println("Dissertasiya: $dissertasiyaMovzusu")
        println("Nəşr sayı   : $nesrSayi")
        // Kotlin-in "safe call" (?.) və "let" birləşməsi:
        // diplom yalnız null OLMADIQDA {} bloku icra olunur —
        // Java-dakı "if (diplom != null) { ... }" quruluşunun qısa forması
        diplom?.let {
            println("--- Diplom ---")
            it.diplomInfosu()
        }
    }
}

// ══════════════════════════════════════════════
//  MÜƏLLİM — Şəxs-dən miras alır
// ══════════════════════════════════════════════
open class Muellim(
    ad: String,
    soyad: String,
    yas: Int,
    val fakulte: String,
    val fenn: String,
    private val tedrisTecrubesi: Int
) : Sexs(ad, soyad, yas) {

    override fun melumatlariGoster() {
        println("Ad / Soyad   : $ad $soyad")
        println("Yaş          : $yas")
        println("Fakültə      : $fakulte")
        println("Fənn         : $fenn")
        println("Təcrübə (il) : $tedrisTecrubesi")
    }
}

// ══════════════════════════════════════════════
//  PROFESSOR — Müəllim-dən miras alır
// ══════════════════════════════════════════════
open class Professor(
    ad: String,
    soyad: String,
    yas: Int,
    fakulte: String,
    fenn: String,
    tedrisTecrubesi: Int,
    private val elmiDerece: String,
    private val nesrSayi: Int
) : Muellim(ad, soyad, yas, fakulte, fenn, tedrisTecrubesi) {

    override fun melumatlariGoster() {
        super.melumatlariGoster()
        println("Elmi dərəcə  : $elmiDerece")
        println("Nəşr sayı    : $nesrSayi")
    }
}

// ══════════════════════════════════════════════
//  REKTOR — Professor-dan miras alır
// ══════════════════════════════════════════════
class Rektor(
    ad: String,
    soyad: String,
    yas: Int,
    fakulte: String,
    fenn: String,
    tedrisTecrubesi: Int,
    elmiDerece: String,
    nesrSayi: Int,
    private val universitet: String,
    private val idareetmeTecrubesi: Int
) : Professor(ad, soyad, yas, fakulte, fenn, tedrisTecrubesi, elmiDerece, nesrSayi) {

    override fun melumatlariGoster() {
        super.melumatlariGoster()
        println("Universitet      : $universitet")
        println("İdarəetmə (il)   : $idareetmeTecrubesi")
    }
}

// ══════════════════════════════════════════════
//  MAIN
// ══════════════════════════════════════════════
fun main() {
    Scanner(System.`in`).use { scanner ->

        // ── TƏLƏBƏ ──────────────────────────────────────────
        println("\n========== TƏLƏBƏ ==========")
        print("Ad: ");           val tAd = scanner.nextLine()
        print("Soyad: ");        val tSoyad = scanner.nextLine()
        print("Yaş: ");          val tYas = scanner.nextLine().toInt()
        print("Fakültə: ");      val tFakulte = scanner.nextLine()
        print("Kurs (1-4): ");   val tKurs = scanner.nextLine().toInt()

        val telebe = Telebe(tAd, tSoyad, tYas, tFakulte, tKurs)

        print("Kurs adı: ");     val kAd = scanner.nextLine()
        print("Kredit saatı: "); val kKredit = scanner.nextLine().toInt()
        print("Müəllim: ");      val kMuellim = scanner.nextLine()
        telebe.kursElave(Kurs(kAd, kKredit, kMuellim))

        print("İmtahan fənni: "); val iFenn = scanner.nextLine()
        print("Bal: ");           val iBal = scanner.nextLine().toDouble()
        print("Tarix: ");         val iTarix = scanner.nextLine()
        telebe.imtahanElave(Imtahan(iFenn, iBal, iTarix))

        println("\n--- Tələbə məlumatları ---")
        telebe.melumatlariGoster()

        // ── MAGİSTR ─────────────────────────────────────────
        println("\n========== MAGİSTR ==========")
        print("Ad: ");               val mAd = scanner.nextLine()
        print("Soyad: ");            val mSoyad = scanner.nextLine()
        print("Yaş: ");              val mYas = scanner.nextLine().toInt()
        print("Fakültə: ");          val mFakulte = scanner.nextLine()
        print("Kurs: ");             val mKurs = scanner.nextLine().toInt()
        print("Tədqiqat mövzusu: "); val mMovzu = scanner.nextLine()
        print("Elmi rəhbər: ");      val mRehber = scanner.nextLine()

        val magistr = Magistr(mAd, mSoyad, mYas, mFakulte, mKurs, mMovzu, mRehber)

        println("\n--- Magistr məlumatları ---")
        magistr.melumatlariGoster()

        // ── DOKTORANT ────────────────────────────────────────
        println("\n========== DOKTORANT ==========")
        print("Ad: ");               val dAd = scanner.nextLine()
        print("Soyad: ");            val dSoyad = scanner.nextLine()
        print("Yaş: ");              val dYas = scanner.nextLine().toInt()
        print("Fakültə: ");          val dFakulte = scanner.nextLine()
        print("Kurs: ");             val dKurs = scanner.nextLine().toInt()
        print("Tədqiqat mövzusu: "); val dMovzu = scanner.nextLine()
        print("Elmi rəhbər: ");      val dRehber = scanner.nextLine()
        print("Dissertasiya: ");     val dDiss = scanner.nextLine()
        print("Nəşr sayı: ");        val dNesr = scanner.nextLine().toInt()

        val doktorant = Doktorant(dAd, dSoyad, dYas, dFakulte, dKurs, dMovzu, dRehber, dDiss, dNesr)

        print("Diplom ixtisası: ");  val dipIxt = scanner.nextLine()
        print("Diplom tarixi: ");    val dipTarix = scanner.nextLine()
        print("Diplom ortalama: ");  val dipOrt = scanner.nextLine().toDouble()
        doktorant.diplomTeyin(Diplom(dipIxt, dipTarix, dipOrt))

        println("\n--- Doktorant məlumatları ---")
        doktorant.melumatlariGoster()

        // ── MÜƏLLİM ─────────────────────────────────────────
        println("\n========== MÜƏLLİM ==========")
        print("Ad: ");           val muAd = scanner.nextLine()
        print("Soyad: ");        val muSoyad = scanner.nextLine()
        print("Yaş: ");          val muYas = scanner.nextLine().toInt()
        print("Fakültə: ");      val muFakulte = scanner.nextLine()
        print("Fənn: ");         val muFenn = scanner.nextLine()
        print("Təcrübə (il): "); val muTec = scanner.nextLine().toInt()

        val muellim = Muellim(muAd, muSoyad, muYas, muFakulte, muFenn, muTec)

        println("\n--- Müəllim məlumatları ---")
        muellim.melumatlariGoster()

        // ── PROFESSOR ────────────────────────────────────────
        println("\n========== PROFESSOR ==========")
        print("Ad: ");           val prAd = scanner.nextLine()
        print("Soyad: ");        val prSoyad = scanner.nextLine()
        print("Yaş: ");          val prYas = scanner.nextLine().toInt()
        print("Fakültə: ");      val prFakulte = scanner.nextLine()
        print("Fənn: ");         val prFenn = scanner.nextLine()
        print("Təcrübə (il): "); val prTec = scanner.nextLine().toInt()
        print("Elmi dərəcə: ");  val prDerece = scanner.nextLine()
        print("Nəşr sayı: ");    val prNesr = scanner.nextLine().toInt()

        val professor = Professor(prAd, prSoyad, prYas, prFakulte, prFenn, prTec, prDerece, prNesr)

        println("\n--- Professor məlumatları ---")
        professor.melumatlariGoster()

        // ── REKTOR ───────────────────────────────────────────
        println("\n========== REKTOR ==========")
        print("Ad: ");             val rAd = scanner.nextLine()
        print("Soyad: ");          val rSoyad = scanner.nextLine()
        print("Yaş: ");            val rYas = scanner.nextLine().toInt()
        print("Fakültə: ");        val rFakulte = scanner.nextLine()
        print("Fənn: ");           val rFenn = scanner.nextLine()
        print("Təcrübə (il): ");   val rTec = scanner.nextLine().toInt()
        print("Elmi dərəcə: ");    val rDerece = scanner.nextLine()
        print("Nəşr sayı: ");      val rNesr = scanner.nextLine().toInt()
        print("Universitet: ");    val rUniver = scanner.nextLine()
        print("İdarəetmə (il): "); val rIdaree = scanner.nextLine().toInt()

        val rektor = Rektor(rAd, rSoyad, rYas, rFakulte, rFenn, rTec, rDerece, rNesr, rUniver, rIdaree)

        println("\n--- Rektor məlumatları ---")
        rektor.melumatlariGoster()
    }
}
