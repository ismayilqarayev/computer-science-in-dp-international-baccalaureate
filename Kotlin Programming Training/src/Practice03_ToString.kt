// ══════════════════════════════════════════════════════════════
//  PRACTICE 3 — toString() metodunun override edilməsi
//  (java/Java Practice Programs3.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Java-da hər obyektin defolt bir toString() metodu var (Object sinifindən gəlir),
// amma bu, oxunaqlı deyil (məs: Student@1b6d3586).
// Ona görə "@Override public String toString()" yazıb öz formatımızı veririk.
//
// Kotlin-də də eyni məntiq var, sadəcə "@Override" əvəzinə "override" açar sözü işlədilir.

class Student(
    var name: String
) {
    // Kotlin-də hər funksiyanın əvvəlinə "fun" yazılır (Java-da yoxdur)
    // "override" -> bu funksiya ana sinifdəki (Any/Object) funksiyanı əvəz edir
    override fun toString(): String {
        return "Student name: $name"
    }
}

// Student obyektini qəbul edib adını dəyişən funksiya
fun rename(student: Student, newName: String) {
    student.name = newName
}

fun main() {
    // Yeni obyekt yaradılır
    val student1 = Student("John")

    // println(student1) çağırıldıqda Kotlin avtomatik olaraq
    // student1.toString() metodunu işə salır
    println(student1)

    // Adı dəyişirik
    rename(student1, "Doe")

    // Yenilənmiş obyekti çap edirik
    println(student1)
}
