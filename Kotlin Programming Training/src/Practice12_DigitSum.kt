// ══════════════════════════════════════════════════════════════
//  PRACTICE 12 — Ədədin rəqəmlərinin cəmi
//  (java/java Practice Programs12.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Məntiq Java ilə tamamilə eynidir:
//   - "temp % 10" -> sonuncu rəqəmi tapır
//   - "temp / 10" -> sonuncu rəqəmi ədəddən "atır"
//   - temp 0 olana qədər bu dövr edir
//
// Fərq yalnız sintaksisdədir: Kotlin-də dəyişənlərin tipi çox vaxt
// yazılmır, çünki Kotlin dəyəri özü tanıyıb tipi avtomatik təyin edir
// (buna "type inference" deyilir).

import java.util.Scanner

fun main() {
    val scanner = Scanner(System.`in`)

    print("Enter a number: ")
    val number = scanner.nextInt()

    var sum = 0
    // "var temp = number" -> Kotlin "temp"-in tipini Int kimi avtomatik təyin edir
    var temp = number

    // Java-dakı "while (temp != 0)" ilə tamamilə eyni
    while (temp != 0) {
        val digit = temp % 10
        sum += digit
        temp /= 10
    }

    println("Sum of digits of $number is: $sum")

    scanner.close()
}
