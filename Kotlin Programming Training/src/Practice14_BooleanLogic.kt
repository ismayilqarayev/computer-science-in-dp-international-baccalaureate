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

    println("Enter number 1:")
    val number1 = sc.nextInt()

    println("Enter number 2:")
    val number2 = sc.nextInt()

    // ── Sadə müqayisə ──────────────────────────────────────────
    val isBigger = number1 > number2
    if (isBigger) {
        println("Number 1 is bigger")
    } else {
        println("Number 2 is bigger or equal")
    }

    // ── VƏ (&&) operatoru — hər iki ədəd müsbət olmalıdır ──────
    val bothPositiveExpr = (number1 > 0) && (number2 > 0)
    println("Result (true/false): $bothPositiveExpr")

    // ── Eyni yoxlama, if/else ilə mətn şəklində nəticə ─────────
    if (number1 > 0 && number2 > 0) {
        println("True: both numbers are positive")
    } else {
        println("False: at least one number is negative or zero")
    }

    sc.close()
}
