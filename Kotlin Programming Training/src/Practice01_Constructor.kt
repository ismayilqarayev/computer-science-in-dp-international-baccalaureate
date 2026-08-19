// ══════════════════════════════════════════════════════════════
//  PRACTICE 1 — Sadə sinif (class) və constructor
//  (java/Java Practice Programs1.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Bu nümunədə öyrənəcəyimiz mövzular:
//   1) Kotlin-də class necə yaradılır
//   2) "primary constructor" nədir və Java-dakı constructor-dan fərqi
//   3) Obyekt (instance) necə yaradılır
//   4) Funksiyaya obyekt parametr kimi necə ötürülür
//
// Java-da constructor ayrıca bir metod kimi yazılır:
//      Telebe(String ad, int yas) { this.ad = ad; this.yas = yas; }
// Kotlin-də isə constructor birbaşa class başlığının içində yazılır —
// bu, "primary constructor" adlanır və çox vaxt ayrıca kod yazmağa ehtiyac qalmır.

// NOT: Bu faylın öz "package" bloku var. Səbəbi: bu layihədə hər Practice
// faylında "Telebe" adlı bənzər siniflər var, əgər hamısı eyni (default) paketdə
// olsaydı, Kotlin "Redeclaration: class Telebe" xətası verərdi. Hər fayla ayrıca
// paket adı verməklə bu siniflər bir-birindən təcrid olunur.
package practice01

// "class Telebe(...)" -> mötərizə içindəki hər parametr avtomatik olaraq
// sinifin bir sahəsinə (property) çevrilir. Java-da bunun üçün
// həm dəyişən elan etmək, həm constructor yazmaq, həm də this.x = x etmək lazımdır.
class Telebe(
    // "val" -> bu sahə yalnız oxuna bilər (Java-dakı "final" sahəyə bənzəyir)
    // Əgər sahəni sonradan dəyişmək istəsəydik "var" yazardıq
    val ad: String,
    val yas: Int
)

// Kotlin-də "main funksiyası" hər zaman class-dan kənarda, sərbəst (top-level)
// funksiya kimi yazıla bilər. Java-da isə mütləq bir sinifin içində olmalıdır.

// Bu funksiya Telebe tipli obyekt qəbul edir və məlumatlarını ekrana çıxarır
fun telebeGoster(t: Telebe) {
    // t.ad və t.yas -> obyektin sahələrinə birbaşa müraciət
    // Kotlin-də ayrıca getter yazmağa ehtiyac yoxdur, val/var avtomatik yaradır
    println("${t.ad} ${t.yas}")
}

fun main() {
    // "new" açar sözü Kotlin-də İSTİFADƏ OLUNMUR!
    // Java: Telebe t = new Telebe("Ravan", 12);
    // Kotlin: sadəcə sinifin adını çağırmaq kifayətdir
    val telebe = Telebe("Ravan", 12)

    // Obyekti funksiyaya ötürürük
    telebeGoster(telebe)
}
