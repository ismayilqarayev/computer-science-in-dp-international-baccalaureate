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
// NOT: Digər Practice fayllarında da "Telebe" adlı sinif olduğu üçün
// ad toqquşmasının (redeclaration) qarşısını almaq məqsədilə hər fayl
// öz ayrıca "package"-inə yerləşdirilib.
package practice02

// Kotlin-də bu iş demək olar ki avtomatikdir:
//   - "var ad: String" yazdıqda Kotlin öz-özünə arxa planda
//     getter (getAd()) və setter (setAd()) yaradır.
//   - Bayt kodu (JVM bytecode) səviyyəsində Java ilə eynidir,
//     sadəcə Kotlin bunu bizim üçün gizli şəkildə yazır.

class Telebe(
    // "var" -> dəyər dəyişə bilər (Java-dakı private String ad + getter/setter-ə bərabər)
    // Kotlin sinif daxilində və xaricində "t.ad" yazmaqla
    // avtomatik generasiya olunan getter/setter-i işlədir
    var ad: String
)

// Bu funksiya Telebe obyektini qəbul edib "ad" sahəsini dəyişdirir
fun adDeyis(t: Telebe, yeniAd: String) {
    // Java-da: t.setAd(yeniAd);
    // Kotlin-də: birbaşa sahəyə mənimsətmə kifayətdir,
    // arxa planda Kotlin bunu setAd() çağırışına çevirir
    t.ad = yeniAd
}

fun main() {
    // Yeni Telebe obyekti yaradılır ("new" yazılmır)
    val telebe1 = Telebe("Ravan")

    // Java-da: telebe1.getAd()
    // Kotlin-də: telebe1.ad (avtomatik getter çağırılır)
    println("Əvvəl: ${telebe1.ad}")

    // Metod vasitəsilə obyektin adını dəyişdiririk
    adDeyis(telebe1, "Ismayil")

    println("Sonra: ${telebe1.ad}")
}
