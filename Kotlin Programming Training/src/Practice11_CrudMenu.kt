// ══════════════════════════════════════════════════════════════
//  PRACTICE 11 — Siyahı (List) ilə CRUD menyusu
//  (java/java Practice Programs11.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Bu proqram istifadəçiyə menyu göstərir və seçimə görə:
//   1) Tələbə əlavə edir      (Create)
//   2) Tələbələri göstərir    (Read)
//   3) Tələbənin adını dəyişir (Update)
//   4) Tələbəni silir         (Delete)
//   0) Proqramdan çıxır
//
// Java-dakı ArrayList<Student> əvəzinə Kotlin-də MutableList<Student> işlədilir.
// "mutableListOf<Student>()" -> boş, dəyişdirilə bilən siyahı yaradır.

// NOT: Ad toqquşmasının (Student və s.) qarşısını almaq üçün hər Practice
// faylı öz ayrıca "package"-inə yerləşdirilib.
package practice11

import java.util.Scanner

class Student(
    var name: String
) {
    override fun toString(): String = name
}

// Kotlin-də top-level (sinifdən kənar) dəyişənlər birbaşa yazıla bilər —
// Java-da bunun üçün "static" açar sözü ilə sinif daxilində yazmaq lazımdır
val students = mutableListOf<Student>()
val scanner = Scanner(System.`in`)

// tələbə əlavə etmək
fun addStudent() {
    print("Tələbə adı daxil edin: ")
    val name = scanner.nextLine()

    students.add(Student(name))
    println("Tələbə əlavə edildi.")
}

// tələbələri göstərmək
fun showStudents() {
    if (students.isEmpty()) {
        println("Tələbə yoxdur.")
        return
    }

    // Kotlin-də "withIndex()" ilə həm indeksi, həm dəyəri birlikdə ala bilirik —
    // Java-dakı klassik "for(int i=0; i<size; i++)" dövrünə ehtiyac qalmır
    for ((index, student) in students.withIndex()) {
        println("$index - $student")
    }
}

// ad dəyişmək
fun renameStudent() {
    showStudents()

    print("İndeks daxil edin: ")
    // Java-da: scanner.nextInt(); scanner.nextLine();  (iki addım)
    // Kotlin-də Scanner sinfi eynidir, ona görə yenə iki addım lazımdır,
    // çünki nextInt() sətir sonundakı "enter"-i (\n) oxumur
    val index = scanner.nextInt()
    scanner.nextLine()

    print("Yeni ad daxil edin: ")
    val newName = scanner.nextLine()

    students[index].name = newName
    println("Ad dəyişdirildi.")
}

// tələbə silmək
fun removeStudent() {
    showStudents()

    print("Silinəcək indeks: ")
    val index = scanner.nextInt()
    scanner.nextLine()

    students.removeAt(index)
    println("Tələbə silindi.")
}

fun main() {
    while (true) {
        println("\n1 - Tələbə əlavə et")
        println("2 - Tələbələri göstər")
        println("3 - Ad dəyiş")
        println("4 - Tələbə sil")
        println("0 - Çıxış")

        print("Seçim: ")
        val choice = scanner.nextInt()
        scanner.nextLine()

        // Kotlin-də "switch" yoxdur, onun yerinə daha güclü "when" istifadə olunur.
        // Java-dakı hər "case" sətri Kotlin-də bir "->" sətrinə uyğun gəlir,
        // "break" yazmağa ehtiyac yoxdur — Kotlin-də avtomatik "fall-through" olmur.
        when (choice) {
            1 -> addStudent()
            2 -> showStudents()
            3 -> renameStudent()
            4 -> removeStudent()
            0 -> {
                println("Proqram bitdi.")
                return
            }
            else -> println("Yanlış seçim.")
        }
    }
}
