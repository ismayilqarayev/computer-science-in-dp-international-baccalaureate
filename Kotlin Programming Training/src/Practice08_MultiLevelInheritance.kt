// ══════════════════════════════════════════════════════════════
//  PRACTICE 8 — Çox səviyyəli irsiyyət (Multi-level inheritance)
//  (java/java Practice Programs8.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Zəncir: Student → GraduateStudent → PhDStudent
// Yəni PhDStudent həm Student-in, həm də GraduateStudent-in
// bütün funksionallığını miras alır.
//
// Burada 4 əsas OOP prinsipini görürük:
//   1) Abstraction  — Student abstrakt sinifdir, birbaşa obyekt yaradıla bilməz
//   2) Encapsulation — sahələr private/val, xaricdən yalnız funksiyalarla əlaqə
//   3) Inheritance   — GraduateStudent və PhDStudent miras alır
//   4) Polymorphism  — eyni showInfo() çağırışı, fərqli nəticələr verir

// NOT: Ad toqquşmasının (Student, GraduateStudent, PhDStudent və s.) qarşısını
// almaq üçün hər Practice faylı öz ayrıca "package"-inə yerləşdirilib.
package practice08

import java.util.Scanner

// Abstrakt sinif — baza rolunu oynayır
abstract class Student(
    // Kotlin-də constructor parametri "val" olduqda avtomatik
    // getter yaranır və digər siniflər ona müraciət edə bilir.
    // Java-dakı "private String name + getName()" ekvivalenti budur.
    val name: String
) {
    abstract fun showInfo()
}

// Inheritance: GraduateStudent Student-dən miras alır
open class GraduateStudent(
    name: String,
    val university: String
) : Student(name) {

    override fun showInfo() {
        println("Name: $name")
        println("University: $university")
    }
}

// Inheritance: PhDStudent GraduateStudent-dən miras alır
// (Student → GraduateStudent → PhDStudent zənciri)
class PhDStudent(
    name: String,
    university: String,
    private val researchTopic: String
) : GraduateStudent(name, university) {

    // Method Overriding (Polymorphism)
    // GraduateStudent-dəki showInfo()-nu genişləndiririk
    override fun showInfo() {
        // "super.showInfo()" -> ana sinifin funksiyasını çağırır
        // (Java ilə eyni sintaksis)
        super.showInfo()
        println("Research Topic: $researchTopic")
    }
}

fun main() {
    Scanner(System.`in`).use { scanner ->

        // ── Graduate Student məlumatlarının daxil edilməsi ──────────────
        print("Enter the name of the graduate student: ")
        val gsName = scanner.nextLine()

        print("Enter the university of the graduate student: ")
        val gsUniversity = scanner.nextLine()

        // Polymorphism — Student tipli dəyişən GraduateStudent obyektinə işarə edir
        val graduateStudent: Student = GraduateStudent(gsName, gsUniversity)

        // showInfo() çağırılır — hansı sinifin metodu olduğu runtime-da müəyyən olunur
        graduateStudent.showInfo()

        println()

        // ── PhD Student məlumatlarının daxil edilməsi ───────────────────
        print("Enter the name of the PhD student: ")
        val phdName = scanner.nextLine()

        print("Enter the university of the PhD student: ")
        val phdUniversity = scanner.nextLine()

        print("Enter the research topic of the PhD student: ")
        val phdResearchTopic = scanner.nextLine()

        // Polymorphism — Student tipli dəyişən PhDStudent obyektinə işarə edir
        val phdStudent: Student = PhDStudent(phdName, phdUniversity, phdResearchTopic)

        // showInfo() çağırılır — PhDStudent-in override edilmiş metodu işləyir
        phdStudent.showInfo()

    } // "use" bloku bitdikdə Scanner avtomatik bağlanır
}
