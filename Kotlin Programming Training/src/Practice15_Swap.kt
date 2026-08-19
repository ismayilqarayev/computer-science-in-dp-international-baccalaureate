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

    println("1-ci ədədi daxil edin:")
    var eded1 = sc.nextInt()

    println("2-ci ədədi daxil edin:")
    var eded2 = sc.nextInt()

    println("Əvvəl: a = $eded1, b = $eded2")

    // Dəyərləri dəyişmək (swap)
    val temp2 = eded1
    eded1 = eded2
    eded2 = temp2

    // İnkremet əməliyyatı (hər birini 1 vahid artırırıq)
    eded1++
    eded2++

    println("Sonra (swap + increment): a = $eded1, b = $eded2")

    sc.close()

    println()

    // ── 3) SƏHV swap nümunəsi — niyə işləmir? ────────────────────
    var seh1 = 5
    var seh2 = 7

    println("Əvvəl (səhv nümunə): a = $seh1, b = $seh2")

    // Bu üsul YANLIŞDIR, çünki temp dəyişəni istifadə olunmur:
    seh1 = seh2          // seh1 indi 7-yə bərabər oldu, köhnə 5 itdi
    seh2 = seh1          // seh2 artıq YENİ seh1-i (7-ni) alır, nəticədə hər ikisi 7 olur

    println("Sonra (səhv nümunə): a = $seh1, b = $seh2")
    println("Diqqət et -> hər ikisi eyni dəyərə düşdü, bu SƏHVdir!")
}
