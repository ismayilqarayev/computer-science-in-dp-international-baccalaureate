// ══════════════════════════════════════════════════════════════
//  PRACTICE 2 — Encapsulation (İnkapsulyasiya): getter / setter
//  (java/Java Practice Programs2.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Java-da inkapsulyasiya üçün adətən:
//   - sahə "private" edilir
//   - "getX()" adlı metod yazılır (oxumaq üçün)
//   - "setX(...)" adlı metod yazılır (dəyişmək üçün)
//
// Kotlin-də bu iş demək olar ki avtomatikdir:
//   - "var ad: String" yazdıqda Kotlin öz-özünə arxa planda
//     getter (getAd()) və setter (setAd()) yaradır.
//   - Bayt kodu (JVM bytecode) səviyyəsində Java ilə eynidir,
//     sadəcə Kotlin bunu bizim üçün gizli şəkildə yazır.

class Student(
    // "var" -> dəyər dəyişə bilər (Java-dakı private String ad + getter/setter-ə bərabər)
    // Kotlin sinif daxilində və xaricində "s.ad" yazmaqla
    // avtomatik generasiya olunan getter/setter-i işlədir
    var ad: String
)

// Bu funksiya Student obyektini qəbul edib "ad" sahəsini dəyişdirir
fun adDeyis(s: Student, yeniAd: String) {
    // Java-da: s.setAd(yeniAd);
    // Kotlin-də: birbaşa sahəyə mənimsətmə kifayətdir,
    // arxa planda Kotlin bunu setAd() çağırışına çevirir
    s.ad = yeniAd
}

fun main() {
    // Yeni Student obyekti yaradılır ("new" yazılmır)
    val s1 = Student("Ravan")

    // Java-da: s1.getAd()
    // Kotlin-də: s1.ad (avtomatik getter çağırılır)
    println("Əvvəl: ${s1.ad}")

    // Metod vasitəsilə obyektin adını dəyişdiririk
    adDeyis(s1, "Ismayil")

    println("Sonra: ${s1.ad}")
}
