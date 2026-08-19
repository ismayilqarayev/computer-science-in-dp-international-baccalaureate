// ══════════════════════════════════════════════════════════════
//  PRACTICE 12 — Ədədin rəqəmlərinin cəmi
//  (java/java Practice Programs12.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Məntiq Java ilə tamamilə eynidir:
//   - "muveqqeti % 10" -> sonuncu rəqəmi tapır
//   - "muveqqeti / 10" -> sonuncu rəqəmi ədəddən "atır"
//   - muveqqeti 0 olana qədər bu dövr edir
//
// Fərq yalnız sintaksisdədir: Kotlin-də dəyişənlərin tipi çox vaxt
// yazılmır, çünki Kotlin dəyəri özü tanıyıb tipi avtomatik təyin edir
// (buna "type inference" deyilir).

import java.util.Scanner

fun main() {
    val scanner = Scanner(System.`in`)

    print("Bir ədəd daxil edin: ")
    val eded = scanner.nextInt()

    var cem = 0
    // "var muveqqeti = eded" -> Kotlin "muveqqeti"-nin tipini Int kimi avtomatik təyin edir
    var muveqqeti = eded

    // Java-dakı "while (temp != 0)" ilə tamamilə eyni
    while (muveqqeti != 0) {
        val reqem = muveqqeti % 10
        cem += reqem
        muveqqeti /= 10
    }

    println("$eded ədədinin rəqəmlərinin cəmi: $cem")

    scanner.close()
}
