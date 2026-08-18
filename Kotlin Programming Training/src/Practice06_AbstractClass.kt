// ══════════════════════════════════════════════════════════════
//  PRACTICE 6 — Abstract class (Abstrakt sinif)
//  (java/Java Practice Programs6.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Abstrakt sinif nədir?
//   - Birbaşa obyekti yaradıla bilməz (məs: Student(...) çağırmaq olmaz)
//   - Yalnız digər siniflərə "baza" (parent) rolunu oynayır
//   - İçində "abstract" funksiyalar ola bilər — bunların gövdəsi (body) yoxdur,
//     yalnız imzası (siqnaturu) var, hər alt sinif özü doldurmalıdır
//
// Qeyd: Kotlin-də "abstract class" avtomatik olaraq "open"-dır da —
// yəni ayrıca "open" yazmağa ehtiyac yoxdur, abstract sinifdən miras almaq
// həmişə mümkündür.

// NOT: Ad toqquşmasının (Student, GraduateStudent, PhDStudent və s.) qarşısını
// almaq üçün hər Practice faylı öz ayrıca "package"-inə yerləşdirilib.
package practice06

import java.util.Scanner

abstract class Student(
    val name: String
) {
    // Bu funksiyanın gövdəsi yoxdur -> "abstract"
    // Hər alt sinif bu funksiyanı MÜTLƏQ override etməlidir
    abstract fun showInfo()
}

// GraduateStudent -> Student-dən miras alır və showInfo()-nu tamamlayır
class GraduateStudent(
    name: String,
    private val university: String
) : Student(name) {

    override fun showInfo() {
        println("Graduate Student: $name")
        println("University: $university")
    }
}

// PhDStudent -> Student-dən miras alır, öz showInfo()-sunu yazır
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
    val scanner = Scanner(System.`in`)

    print("Enter student name: ")
    val name = scanner.nextLine()

    print("Enter university: ")
    val university = scanner.nextLine()

    // "Student" tipli dəyişən GraduateStudent obyektinə işarə edir (Polymorphism)
    val student: Student = GraduateStudent(name, university)

    student.showInfo()

    println()

    // Sabit dəyərlərlə ikinci nümunə
    val phd: Student = PhDStudent("Nigar", "Artificial Intelligence")

    phd.showInfo()

    scanner.close()
}
