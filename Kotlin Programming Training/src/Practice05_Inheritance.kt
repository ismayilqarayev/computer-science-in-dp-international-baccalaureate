// ══════════════════════════════════════════════════════════════
//  PRACTICE 5 — İrsiyyət (Inheritance): open class və override
//  (java/Java Practice Programs5.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// ÇOX VACİB FƏRQ:
// Java-da hər sinifdən defolt olaraq miras almaq (extends) mümkündür,
// yalnız "final" yazsaq qadağan olunur.
//
// Kotlin-də isə TAM ƏKSİNƏDİR: hər sinif defolt olaraq "final"-dır,
// yəni ondan miras almaq (heir yaratmaq) olmaz!
// Əgər bir sinifdən miras alınmasını istəyiriksə, mütləq "open" yazmalıyıq.
// Bu, Kotlin-in "təhlükəsiz dizayn" fəlsəfəsindən irəli gəlir —
// təsadüfən səhv yerdə miras almağın qarşısını alır.

// NOT: Ad toqquşmasının (Telebe, MagistrTelebe və s.) qarşısını almaq üçün
// hər Practice faylı öz ayrıca "package"-inə yerləşdirilib.
package practice05

import java.util.Scanner

// "open" -> bu sinifdən miras almaq mümkündür
open class Telebe(
    var ad: String
) {
    // "open" -> bu funksiya alt sinifdə override edilə bilər
    // Əgər "open" yazmasaq, alt sinif bu funksiyanı override edə bilməz (xəta verər)
    open fun melumatGoster() {
        println("Tələbənin adı: $ad")
    }
}

// ": Telebe(ad)" -> Java-dakı "extends Telebe" + "super(ad)" birləşməsidir
// Kotlin-də ana sinifin constructor-u birbaşa burada çağırılır
class MagistrTelebe(
    ad: String,
    var universitet: String
) : Telebe(ad) {

    // "override" -> ana sinifdəki melumatGoster() funksiyasını əvəz edirik
    override fun melumatGoster() {
        println("Tələbənin adı: $ad")
        println("Universitet: $universitet")
    }
}

fun main() {
    val scanner = Scanner(System.`in`)

    print("Tələbənin adını daxil edin: ")
    val ad = scanner.nextLine()

    print("Universiteti daxil edin: ")
    val universitet = scanner.nextLine()

    val telebe = MagistrTelebe(ad, universitet)

    telebe.melumatGoster()

    // Kotlin-də Scanner-i manual bağlamaq üçün close() çağırıla bilər,
    // amma "use { }" blokundan istifadə etmək daha yaxşı praktikadır
    scanner.close()
}
