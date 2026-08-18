// ══════════════════════════════════════════════════════════════
//  PRACTICE 15 — İki dəyişənin yerini dəyişmək (Swap)
//  (java/SwapExample.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Ən klassik swap üsulu — müvəqqəti (temp) dəyişəndən istifadə etmək.
// Kotlin-də bu, Java ilə demək olar ki eynidir.
//
// DİQQƏT: Java-dakı faylda YANLIŞ bir nümunə də var idi:
//     number_1 = number_2;
//     number_2 = number_1;   // <-- SƏHV! Artıq number_1 dəyişdiyi üçün
//                             //     number_2 köhnə number_1-i yox, YENİ
//                             //     (yəni number_2-nin öz köhnə) dəyərini alır
// Bu, tipik başlanğıc səhvidir və aşağıda düzgün üsulla müqayisəli göstərilib.

import java.util.Scanner

fun main() {
    // ── 1) Sabit dəyərlərlə düzgün swap ──────────────────────────
    var a = 5
    var b = 7

    println("Əvvəl: a = $a, b = $b")

    // Müvəqqəti dəyişənlə dəyişmə (düzgün üsul)
    val temp = a
    a = b
    b = temp

    println("Sonra: a = $a, b = $b")

    println()

    // ── 2) İstifadəçidən alınan ədədlərlə swap + increment ──────
    val sc = Scanner(System.`in`)

    println("Enter number 1:")
    var number1 = sc.nextInt()

    println("Enter number 2:")
    var number2 = sc.nextInt()

    println("Əvvəl: a = $number1, b = $number2")

    // Dəyərləri dəyişmək (swap)
    val temp2 = number1
    number1 = number2
    number2 = temp2

    // İnkremet əməliyyatı (hər birini 1 vahid artırırıq)
    number1++
    number2++

    println("Sonra (swap + increment): a = $number1, b = $number2")

    sc.close()

    println()

    // ── 3) SƏHV swap nümunəsi — niyə işləmir? ────────────────────
    var wrong1 = 5
    var wrong2 = 7

    println("Əvvəl (səhv nümunə): a = $wrong1, b = $wrong2")

    // Bu üsul YANLIŞDIR, çünki temp dəyişəni istifadə olunmur:
    wrong1 = wrong2          // wrong1 indi 7-yə bərabər oldu, köhnə 5 itdi
    wrong2 = wrong1          // wrong2 artıq YENİ wrong1-i (7-ni) alır, nəticədə hər ikisi 7 olur

    println("Sonra (səhv nümunə): a = $wrong1, b = $wrong2")
    println("Diqqət et -> hər ikisi eyni dəyərə düşdü, bu SƏHVdir!")
}
