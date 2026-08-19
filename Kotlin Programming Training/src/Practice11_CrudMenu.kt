// ══════════════════════════════════════════════════════════════
//  PRACTICE 11 — Siyahı (List) ilə CRUD menyusu
//  (java/java Practice Programs11.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Bu proqram istifadəçiyə menyu göstərir və seçimə görə:
//   1) Tələbə əlavə edir      (Create)
//   2) Tələbələri göstərir    (Read)
//   3) Tələbənin adını dəyişir (Update)
//   4) Tələbəni silir         (Delete)
//   0) Proqramdan çıxır
//
// Java-dakı ArrayList<Telebe> əvəzinə Kotlin-də MutableList<Telebe> işlədilir.
// "mutableListOf<Telebe>()" -> boş, dəyişdirilə bilən siyahı yaradır.

// NOT: Ad toqquşmasının (Telebe və s.) qarşısını almaq üçün hər Practice
// faylı öz ayrıca "package"-inə yerləşdirilib.
package practice11

import java.util.Scanner

class Telebe(
    var ad: String
) {
    override fun toString(): String = ad
}

// Kotlin-də top-level (sinifdən kənar) dəyişənlər birbaşa yazıla bilər —
// Java-da bunun üçün "static" açar sözü ilə sinif daxilində yazmaq lazımdır
val telebeler = mutableListOf<Telebe>()
val scanner = Scanner(System.`in`)

// tələbə əlavə etmək
fun telebeElaveEt() {
    print("Tələbə adı daxil edin: ")
    val ad = scanner.nextLine()

    telebeler.add(Telebe(ad))
    println("Tələbə əlavə edildi.")
}

// tələbələri göstərmək
fun telebeleriGoster() {
    if (telebeler.isEmpty()) {
        println("Tələbə yoxdur.")
        return
    }

    // Kotlin-də "withIndex()" ilə həm indeksi, həm dəyəri birlikdə ala bilirik —
    // Java-dakı klassik "for(int i=0; i<size; i++)" dövrünə ehtiyac qalmır
    for ((indeks, telebe) in telebeler.withIndex()) {
        println("$indeks - $telebe")
    }
}

// ad dəyişmək
fun adDeyis() {
    telebeleriGoster()

    print("İndeks daxil edin: ")
    // Java-da: scanner.nextInt(); scanner.nextLine();  (iki addım)
    // Kotlin-də Scanner sinfi eynidir, ona görə yenə iki addım lazımdır,
    // çünki nextInt() sətir sonundakı "enter"-i (\n) oxumur
    val indeks = scanner.nextInt()
    scanner.nextLine()

    print("Yeni ad daxil edin: ")
    val yeniAd = scanner.nextLine()

    telebeler[indeks].ad = yeniAd
    println("Ad dəyişdirildi.")
}

// tələbə silmək
fun telebeSil() {
    telebeleriGoster()

    print("Silinəcək indeks: ")
    val indeks = scanner.nextInt()
    scanner.nextLine()

    telebeler.removeAt(indeks)
    println("Tələbə silindi.")
}

fun main() {
    while (true) {
        println("\n1 - Tələbə əlavə et")
        println("2 - Tələbələri göstər")
        println("3 - Ad dəyiş")
        println("4 - Tələbə sil")
        println("0 - Çıxış")

        print("Seçim: ")
        val secim = scanner.nextInt()
        scanner.nextLine()

        // Kotlin-də "switch" yoxdur, onun yerinə daha güclü "when" istifadə olunur.
        // Java-dakı hər "case" sətri Kotlin-də bir "->" sətrinə uyğun gəlir,
        // "break" yazmağa ehtiyac yoxdur — Kotlin-də avtomatik "fall-through" olmur.
        when (secim) {
            1 -> telebeElaveEt()
            2 -> telebeleriGoster()
            3 -> adDeyis()
            4 -> telebeSil()
            0 -> {
                println("Proqram bitdi.")
                return
            }
            else -> println("Yanlış seçim.")
        }
    }
}
