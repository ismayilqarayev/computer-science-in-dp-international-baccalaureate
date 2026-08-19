// ══════════════════════════════════════════════════════════════
//  PRACTICE 6 — Abstract class (Abstrakt sinif)
//  (java/Java Practice Programs6.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Abstrakt sinif nədir?
//   - Birbaşa obyekti yaradıla bilməz (məs: Telebe(...) çağırmaq olmaz)
//   - Yalnız digər siniflərə "baza" (parent) rolunu oynayır
//   - İçində "abstract" funksiyalar ola bilər — bunların gövdəsi (body) yoxdur,
//     yalnız imzası (siqnaturu) var, hər alt sinif özü doldurmalıdır
//
// Qeyd: Kotlin-də "abstract class" avtomatik olaraq "open"-dır da —
// yəni ayrıca "open" yazmağa ehtiyac yoxdur, abstract sinifdən miras almaq
// həmişə mümkündür.

// NOT: Ad toqquşmasının (Telebe, MagistrTelebe, DoktorantTelebe və s.) qarşısını
// almaq üçün hər Practice faylı öz ayrıca "package"-inə yerləşdirilib.
package practice06

import java.util.Scanner

abstract class Telebe(
    val ad: String
) {
    // Bu funksiyanın gövdəsi yoxdur -> "abstract"
    // Hər alt sinif bu funksiyanı MÜTLƏQ override etməlidir
    abstract fun melumatGoster()
}

// MagistrTelebe -> Telebe-dən miras alır və melumatGoster()-i tamamlayır
class MagistrTelebe(
    ad: String,
    private val universitet: String
) : Telebe(ad) {

    override fun melumatGoster() {
        println("Magistr tələbə: $ad")
        println("Universitet: $universitet")
    }
}

// DoktorantTelebe -> Telebe-dən miras alır, öz melumatGoster()-ini yazır
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
    val scanner = Scanner(System.`in`)

    print("Tələbənin adını daxil edin: ")
    val ad = scanner.nextLine()

    print("Universiteti daxil edin: ")
    val universitet = scanner.nextLine()

    // "Telebe" tipli dəyişən MagistrTelebe obyektinə işarə edir (Polymorphism)
    val telebe: Telebe = MagistrTelebe(ad, universitet)

    telebe.melumatGoster()

    println()

    // Sabit dəyərlərlə ikinci nümunə
    val doktorant: Telebe = DoktorantTelebe("Nigar", "Süni İntellekt")

    doktorant.melumatGoster()

    scanner.close()
}
