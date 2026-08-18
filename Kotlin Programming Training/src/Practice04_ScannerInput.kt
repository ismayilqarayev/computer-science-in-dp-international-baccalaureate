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

import java.util.Scanner

class Student(
    var name: String
) {
    override fun toString(): String = name
}

fun rename(student: Student, newName: String) {
    student.name = newName
}

fun main() {
    val scanner = Scanner(System.`in`)

    print("Enter the name of the student: ")
    // Java: scanner.nextLine()  ->  Kotlin-də də eyni cür işlədilir
    val studentName = scanner.nextLine()

    val student = Student(studentName)
    println("Current name: $student")

    print("Enter the new name of the student: ")
    val newName = scanner.nextLine()

    rename(student, newName)
    println("New name: $student")

    // Kotlin-də Scanner-i "use { }" bloku ilə istifadə etsək,
    // blok bitdikdə avtomatik bağlanır (Java-dakı try-with-resources kimi).
    // Burada sadəlik üçün manual şəkildə saxladıq, amma daha "kotlin-vari" yol budur:
    //
    // Scanner(System.`in`).use { sc ->
    //     ... bütün oxuma əməliyyatları burada ...
    // }
}
