// ══════════════════════════════════════════════════════════════
//  PRACTICE 9 — Validasiya (regex) ilə istifadəçi girişi
//  (java/java Practice Programs9.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Bu proqramda öyrənəcəyimiz əlavə mövzular:
//   - Kotlin-də regex istifadəsi (String.matches())
//   - "private fun" -> yalnız bu fayl daxilində istifadə oluna bilən köməkçi funksiyalar
//   - while(true) + return ilə "təkrar sual ver, düzgün cavab alana qədər" məntiqi

// NOT: Ad toqquşmasının (Telebe, MagistrTelebe, DoktorantTelebe və s.) qarşısını
// almaq üçün hər Practice faylı öz ayrıca "package"-inə yerləşdirilib.
package practice09

import java.util.Scanner

abstract class Telebe(
    val ad: String,
    val soyad: String,
    val telefon: String,
    val email: String
) {
    abstract fun melumatGoster()
}

open class MagistrTelebe(
    ad: String,
    soyad: String,
    telefon: String,
    email: String,
    val universitet: String
) : Telebe(ad, soyad, telefon, email) {

    override fun melumatGoster() {
        println("Ad: $ad $soyad")
        println("Telefon: $telefon")
        println("Email: $email")
        println("Universitet: $universitet")
    }
}

class DoktorantTelebe(
    ad: String,
    soyad: String,
    telefon: String,
    email: String,
    universitet: String,
    private val tedqiqatMovzusu: String
) : MagistrTelebe(ad, soyad, telefon, email, universitet) {

    override fun melumatGoster() {
        super.melumatGoster()
        println("Tədqiqat mövzusu: $tedqiqatMovzusu")
    }
}

// ── Köməkçi (validasiya) funksiyaları ────────────────────────────────

// Boş olmayan mətn daxil edilənə qədər təkrar-təkrar soruşur
private fun boşOlmayanGiriş(scanner: Scanner, sual: String): String {
    while (true) {
        print(sual)
        val giris = scanner.nextLine().trim()
        if (giris.isNotEmpty()) {
            return giris
        }
        println("Yanlış giriş: bu sahə boş ola bilməz. Zəhmət olmasa düzgün dəyər daxil edin.")
    }
}

// Telefon nömrəsi formatına uyğun gələnə qədər təkrar soruşur
private fun duzgunTelefonGiriş(scanner: Scanner, sual: String): String {
    while (true) {
        print(sual)
        val telefon = scanner.nextLine().trim()
        if (telefon.isEmpty()) {
            println("Yanlış giriş: telefon nömrəsi boş ola bilməz.")
            continue
        }
        if (telefonDuzgundur(telefon)) {
            return telefon
        }
        println("Yanlış telefon nömrəsi. Rəqəm, boşluq, tire və istəyə görə \"+\" işlədin.")
    }
}

// Email formatına uyğun gələnə qədər təkrar soruşur
private fun duzgunEmailGiriş(scanner: Scanner, sual: String): String {
    while (true) {
        print(sual)
        val email = scanner.nextLine().trim()
        if (email.isEmpty()) {
            println("Yanlış giriş: email boş ola bilməz.")
            continue
        }
        if (emailDuzgundur(email)) {
            return email
        }
        println("Yanlış email formatı. Nümunə: istifadeci@example.com")
    }
}

// Regex ilə telefon formatını yoxlayır: rəqəmlər, boşluq, tire və istəyə görə "+"
private fun telefonDuzgundur(telefon: String): Boolean {
    return telefon.matches(Regex("^\\+?[0-9\\-\\s]{7,20}$"))
}

// Regex ilə sadə email formatını yoxlayır
private fun emailDuzgundur(email: String): Boolean {
    return email.matches(Regex("^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$"))
}

fun main() {
    Scanner(System.`in`).use { scanner ->

        // ── Magistr tələbə məlumatlarının daxil edilməsi ──────────────
        println("Magistr tələbə məlumatlarının daxil edilməsi:")
        val mAd = boşOlmayanGiriş(scanner, "Magistr tələbənin adını daxil edin: ")
        val mSoyad = boşOlmayanGiriş(scanner, "Magistr tələbənin soyadını daxil edin: ")
        val mTelefon = duzgunTelefonGiriş(scanner, "Magistr tələbənin telefon nömrəsini daxil edin: ")
        val mEmail = duzgunEmailGiriş(scanner, "Magistr tələbənin emailini daxil edin: ")
        val mUniversitet = boşOlmayanGiriş(scanner, "Magistr tələbənin universitetini daxil edin: ")

        val magistrTelebe: Telebe = MagistrTelebe(mAd, mSoyad, mTelefon, mEmail, mUniversitet)
        println()
        magistrTelebe.melumatGoster()

        // ── Doktorant məlumatlarının daxil edilməsi ───────────────────
        println()
        println("Doktorant məlumatlarının daxil edilməsi:")
        val dAd = boşOlmayanGiriş(scanner, "Doktorantın adını daxil edin: ")
        val dSoyad = boşOlmayanGiriş(scanner, "Doktorantın soyadını daxil edin: ")
        val dTelefon = duzgunTelefonGiriş(scanner, "Doktorantın telefon nömrəsini daxil edin: ")
        val dEmail = duzgunEmailGiriş(scanner, "Doktorantın emailini daxil edin: ")
        val dUniversitet = boşOlmayanGiriş(scanner, "Doktorantın universitetini daxil edin: ")
        val dTedqiqatMovzusu = boşOlmayanGiriş(scanner, "Doktorantın tədqiqat mövzusunu daxil edin: ")

        val doktorantTelebe: Telebe = DoktorantTelebe(dAd, dSoyad, dTelefon, dEmail, dUniversitet, dTedqiqatMovzusu)
        println()
        doktorantTelebe.melumatGoster()
    }
}
