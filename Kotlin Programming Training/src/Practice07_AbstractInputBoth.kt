// ══════════════════════════════════════════════════════════════
//  PRACTICE 7 — Abstract class + hər iki obyekt üçün istifadəçi girişi
//  (java/java Practice Programs7.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Bu fayl Practice 6-nın davamıdır — fərq budur ki, PhDStudent məlumatları
// da sabit yox, istifadəçidən Scanner vasitəsilə alınır.

import java.util.Scanner

abstract class Student(
    val name: String
) {
    abstract fun showInfo()
}

class GraduateStudent(
    name: String,
    private val university: String
) : Student(name) {

    override fun showInfo() {
        println("Graduate Student: $name")
        println("University: $university")
    }
}

class PhDStudent(
    name: String,
    private val researchField: String
) : Student(name) {

    override fun showInfo() {
        println("PhD Student: $name")
        println("Research Field: $researchField")
    }
}

fun main() {
    // "use { }" -> Kotlin-in try-with-resources analoqu.
    // Blok bitdikdə (normal və ya xəta ilə) Scanner avtomatik bağlanır.
    Scanner(System.`in`).use { scanner ->

        // ── Graduate Student məlumatlarının daxil edilməsi ──────────────
        print("Enter graduate student name: ")
        val name = scanner.nextLine()

        print("Enter university: ")
        val university = scanner.nextLine()

        val student: Student = GraduateStudent(name, university)
        student.showInfo()

        println()

        // ── PhD Student məlumatlarının daxil edilməsi ───────────────────
        print("Enter PhD student name: ")
        val phdName = scanner.nextLine()

        print("Enter research field: ")
        val researchField = scanner.nextLine()

        val phd: Student = PhDStudent(phdName, researchField)
        phd.showInfo()
    }
}
