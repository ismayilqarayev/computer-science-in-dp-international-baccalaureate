// ══════════════════════════════════════════════════════════════
//  PRACTICE 5 — İrsiyyət (Inheritance): open class və override
//  (java/Java Practice Programs5.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// ÇOX VACİB FƏRQ:
// Java-da hər sinifdən defolt olaraq miras almaq (extends) mümkündür,
// yalnız "final" yazsaq qadağan olunur.
//
// Kotlin-də isə TAM ƏKSİNƏDİR: hər sinif defolt olaraq "final"-dır,
// yəni ondan miras almaq (heir yaratmaq) olmaz!
// Əgər bir sinifdən miras alınmasını istəyiriksə, mütləq "open" yazmalıyıq.
// Bu, Kotlin-in "təhlükəsiz dizayn" fəlsəfəsindən irəli gəlir —
// təsadüfən səhv yerdə miras almağın qarşısını alır.

import java.util.Scanner

// "open" -> bu sinifdən miras almaq mümkündür
open class Student(
    var name: String
) {
    // "open" -> bu funksiya alt sinifdə override edilə bilər
    // Əgər "open" yazmasaq, alt sinif bu funksiyanı override edə bilməz (xəta verər)
    open fun showInfo() {
        println("Student name: $name")
    }
}

// ": Student(name)" -> Java-dakı "extends Student" + "super(name)" birləşməsidir
// Kotlin-də ana sinifin constructor-u birbaşa burada çağırılır
class GraduateStudent(
    name: String,
    var university: String
) : Student(name) {

    // "override" -> ana sinifdəki showInfo() funksiyasını əvəz edirik
    override fun showInfo() {
        println("Student name: $name")
        println("University: $university")
    }
}

fun main() {
    val scanner = Scanner(System.`in`)

    print("Enter student name: ")
    val name = scanner.nextLine()

    print("Enter university: ")
    val university = scanner.nextLine()

    val student = GraduateStudent(name, university)

    student.showInfo()

    // Kotlin-də Scanner-i manual bağlamaq üçün close() çağırıla bilər,
    // amma "use { }" blokundan istifadə etmək daha yaxşı praktikadır
    scanner.close()
}
