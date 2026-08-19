// ══════════════════════════════════════════════════════════════
//  PRACTICE 3 — toString() metodunun override edilməsi
//  (java/Java Practice Programs3.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// NOT: Ad toqquşmasının (Telebe, adiDeyis və s.) qarşısını almaq üçün
// hər Practice faylı öz ayrıca "package"-inə yerləşdirilib.
package practice03

// Java-da hər obyektin defolt bir toString() metodu var (Object sinifindən gəlir),
// amma bu, oxunaqlı deyil (məs: Telebe@1b6d3586).
// Ona görə "@Override public String toString()" yazıb öz formatımızı veririk.
//
// Kotlin-də də eyni məntiq var, sadəcə "@Override" əvəzinə "override" açar sözü işlədilir.

class Telebe(
    var ad: String
) {
    // Kotlin-də hər funksiyanın əvvəlinə "fun" yazılır (Java-da yoxdur)
    // "override" -> bu funksiya ana sinifdəki (Any/Object) funksiyanı əvəz edir
    override fun toString(): String {
        return "Tələbənin adı: $ad"
    }
}

// Telebe obyektini qəbul edib adını dəyişən funksiya
fun adiDeyis(telebe: Telebe, yeniAd: String) {
    telebe.ad = yeniAd
}

fun main() {
    // Yeni obyekt yaradılır
    val telebe1 = Telebe("Cavid")

    // println(telebe1) çağırıldıqda Kotlin avtomatik olaraq
    // telebe1.toString() metodunu işə salır
    println(telebe1)

    // Adı dəyişirik
    adiDeyis(telebe1, "Elvin")

    // Yenilənmiş obyekti çap edirik
    println(telebe1)
}
