// ══════════════════════════════════════════════════════════════
//  PRACTICE 7 — Abstract class + hər iki obyekt üçün istifadəçi girişi
//  (java/java Practice Programs7.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Bu fayl Practice 6-nın davamıdır — fərq budur ki, DoktorantTelebe
// məlumatları da sabit yox, istifadəçidən Scanner vasitəsilə alınır.

// NOT: Ad toqquşmasının (Telebe, MagistrTelebe, DoktorantTelebe və s.) qarşısını
// almaq üçün hər Practice faylı öz ayrıca "package"-inə yerləşdirilib.
package practice07

import java.util.Scanner

abstract class Telebe(
    val ad: String
) {
    abstract fun melumatGoster()
}

class MagistrTelebe(
    ad: String,
    private val universitet: String
) : Telebe(ad) {

    override fun melumatGoster() {
        println("Magistr tələbə: $ad")
        println("Universitet: $universitet")
    }
}

class DoktorantTelebe(
    ad: String,
    private val tedqiqatSahesi: String
) : Telebe(ad) {

    override fun melumatGoster() {
        println("Doktorant: $ad")
        println("Tədqiqat sahəsi: $tedqiqatSahesi")
    }
}

fun main() {
    // "use { }" -> Kotlin-in try-with-resources analoqu.
    // Blok bitdikdə (normal və ya xəta ilə) Scanner avtomatik bağlanır.
    Scanner(System.`in`).use { scanner ->

        // ── Magistr tələbə məlumatlarının daxil edilməsi ──────────────
        print("Magistr tələbənin adını daxil edin: ")
        val ad = scanner.nextLine()

        print("Universiteti daxil edin: ")
        val universitet = scanner.nextLine()

        val telebe: Telebe = MagistrTelebe(ad, universitet)
        telebe.melumatGoster()

        println()

        // ── Doktorant məlumatlarının daxil edilməsi ───────────────────
        print("Doktorantın adını daxil edin: ")
        val doktorantAdi = scanner.nextLine()

        print("Tədqiqat sahəsini daxil edin: ")
        val tedqiqatSahesi = scanner.nextLine()

        val doktorant: Telebe = DoktorantTelebe(doktorantAdi, tedqiqatSahesi)
        doktorant.melumatGoster()
    }
}
