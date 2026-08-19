// ══════════════════════════════════════════════════════════════
//  PRACTICE 8 — Çox səviyyəli irsiyyət (Multi-level inheritance)
//  (java/java Practice Programs8.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Zəncir: Telebe → MagistrTelebe → DoktorantTelebe
// Yəni DoktorantTelebe həm Telebe-nin, həm də MagistrTelebe-nin
// bütün funksionallığını miras alır.
//
// Burada 4 əsas OOP prinsipini görürük:
//   1) Abstraction  — Telebe abstrakt sinifdir, birbaşa obyekt yaradıla bilməz
//   2) Encapsulation — sahələr private/val, xaricdən yalnız funksiyalarla əlaqə
//   3) Inheritance   — MagistrTelebe və DoktorantTelebe miras alır
//   4) Polymorphism  — eyni melumatGoster() çağırışı, fərqli nəticələr verir

// NOT: Ad toqquşmasının (Telebe, MagistrTelebe, DoktorantTelebe və s.) qarşısını
// almaq üçün hər Practice faylı öz ayrıca "package"-inə yerləşdirilib.
package practice08

import java.util.Scanner

// Abstrakt sinif — baza rolunu oynayır
abstract class Telebe(
    // Kotlin-də constructor parametri "val" olduqda avtomatik
    // getter yaranır və digər siniflər ona müraciət edə bilir.
    // Java-dakı "private String name + getName()" ekvivalenti budur.
    val ad: String
) {
    abstract fun melumatGoster()
}

// Inheritance: MagistrTelebe Telebe-dən miras alır
open class MagistrTelebe(
    ad: String,
    val universitet: String
) : Telebe(ad) {

    override fun melumatGoster() {
        println("Ad: $ad")
        println("Universitet: $universitet")
    }
}

// Inheritance: DoktorantTelebe MagistrTelebe-dən miras alır
// (Telebe → MagistrTelebe → DoktorantTelebe zənciri)
class DoktorantTelebe(
    ad: String,
    universitet: String,
    private val tedqiqatMovzusu: String
) : MagistrTelebe(ad, universitet) {

    // Method Overriding (Polymorphism)
    // MagistrTelebe-dəki melumatGoster()-i genişləndiririk
    override fun melumatGoster() {
        // "super.melumatGoster()" -> ana sinifin funksiyasını çağırır
        // (Java ilə eyni sintaksis)
        super.melumatGoster()
        println("Tədqiqat mövzusu: $tedqiqatMovzusu")
    }
}

fun main() {
    Scanner(System.`in`).use { scanner ->

        // ── Magistr tələbə məlumatlarının daxil edilməsi ──────────────
        print("Magistr tələbənin adını daxil edin: ")
        val mAd = scanner.nextLine()

        print("Magistr tələbənin universitetini daxil edin: ")
        val mUniversitet = scanner.nextLine()

        // Polymorphism — Telebe tipli dəyişən MagistrTelebe obyektinə işarə edir
        val magistrTelebe: Telebe = MagistrTelebe(mAd, mUniversitet)

        // melumatGoster() çağırılır — hansı sinifin metodu olduğu runtime-da müəyyən olunur
        magistrTelebe.melumatGoster()

        println()

        // ── Doktorant məlumatlarının daxil edilməsi ───────────────────
        print("Doktorantın adını daxil edin: ")
        val dAd = scanner.nextLine()

        print("Doktorantın universitetini daxil edin: ")
        val dUniversitet = scanner.nextLine()

        print("Doktorantın tədqiqat mövzusunu daxil edin: ")
        val dTedqiqatMovzusu = scanner.nextLine()

        // Polymorphism — Telebe tipli dəyişən DoktorantTelebe obyektinə işarə edir
        val doktorantTelebe: Telebe = DoktorantTelebe(dAd, dUniversitet, dTedqiqatMovzusu)

        // melumatGoster() çağırılır — DoktorantTelebe-nin override edilmiş metodu işləyir
        doktorantTelebe.melumatGoster()

    } // "use" bloku bitdikdə Scanner avtomatik bağlanır
}
