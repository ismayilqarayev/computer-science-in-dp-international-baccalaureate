// ══════════════════════════════════════════════════════════════
//  PRACTICE 14 — Boolean məntiqi (&&, ||, müqayisə operatorları)
//  (java/SwapExample.java faylındakı "Boolean" hissəsinin Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Boolean operatorlar Java ilə Kotlin-də EYNİDİR:
//   &&  -> VƏ (hər ikisi doğru olmalıdır)
//   ||  -> VƏ YA (ən azı biri doğru olmalıdır)
//   !   -> ƏKS (inkar)
//   >, <, >=, <=, ==, != -> müqayisə operatorları

import java.util.Scanner

fun main() {
    val sc = Scanner(System.`in`)

    println("1-ci ədədi daxil edin:")
    val eded1 = sc.nextInt()

    println("2-ci ədədi daxil edin:")
    val eded2 = sc.nextInt()

    // ── Sadə müqayisə ──────────────────────────────────────────
    val boyukdur = eded1 > eded2
    if (boyukdur) {
        println("1-ci ədəd daha böyükdür")
    } else {
        println("2-ci ədəd daha böyük və ya bərabərdir")
    }

    // ── VƏ (&&) operatoru — hər iki ədəd müsbət olmalıdır ──────
    val herIkisiMusbetdir = (eded1 > 0) && (eded2 > 0)
    println("Nəticə (true/false): $herIkisiMusbetdir")

    // ── Eyni yoxlama, if/else ilə mətn şəklində nəticə ─────────
    if (eded1 > 0 && eded2 > 0) {
        println("True: hər iki ədəd müsbətdir")
    } else {
        println("False: ən azı bir ədəd mənfi və ya sıfırdır")
    }

    sc.close()
}
