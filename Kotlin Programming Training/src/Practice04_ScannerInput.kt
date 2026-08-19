// ══════════════════════════════════════════════════════════════
//  PRACTICE 4 — İstifadəçidən məlumat almaq (Scanner)
//  (java/Java Practice Programs4.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Kotlin JVM üzərində işlədiyi üçün Java-nın java.util.Scanner
// sinifini birbaşa istifadə edə bilərik (import edərək).
// Fərq yalnız sintaksisdədir, işləmə məntiqi eynidir.
//
// Qeyd: Kotlin-də "System.in" yazmaq mümkün deyil, çünki "in" Kotlin-də
// açar sözdür (məs: "for (x in list)"). Ona görə geriyə tərs apostrof (`)
// içində yazılır: System.`in`

// NOT: Ad toqquşmasının (Telebe, adiDeyis və s.) qarşısını almaq üçün
// hər Practice faylı öz ayrıca "package"-inə yerləşdirilib.
package practice04

import java.util.Scanner

class Telebe(
    var ad: String
) {
    override fun toString(): String = ad
}

fun adiDeyis(telebe: Telebe, yeniAd: String) {
    telebe.ad = yeniAd
}

fun main() {
    val scanner = Scanner(System.`in`)

    print("Tələbənin adını daxil edin: ")
    // Java: scanner.nextLine()  ->  Kotlin-də də eyni cür işlədilir
    val telebeAdi = scanner.nextLine()

    val telebe = Telebe(telebeAdi)
    println("Hazırkı ad: $telebe")

    print("Tələbənin yeni adını daxil edin: ")
    val yeniAd = scanner.nextLine()

    adiDeyis(telebe, yeniAd)
    println("Yeni ad: $telebe")

    // Kotlin-də Scanner-i "use { }" bloku ilə istifadə etsək,
    // blok bitdikdə avtomatik bağlanır (Java-dakı try-with-resources kimi).
    // Burada sadəlik üçün manual şəkildə saxladıq, amma daha "kotlin-vari" yol budur:
    //
    // Scanner(System.`in`).use { sc ->
    //     ... bütün oxuma əməliyyatları burada ...
    // }
}
