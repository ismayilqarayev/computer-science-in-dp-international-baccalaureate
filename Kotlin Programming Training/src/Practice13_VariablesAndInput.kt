// ══════════════════════════════════════════════════════════════
//  PRACTICE 13 — Dəyişənlər (Variables) və data type-lar
//  (java/SwapExample.java faylındakı "Variables / Data types" hissəsinin
//   Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Bu faylda B2.1.1 mövzusu üzrə IB Java nümunələrini Kotlin-ə çeviririk:
// String, Int, Double tipli sahələr və Scanner ilə istifadəçi girişi.
//
// ƏSAS FƏRQ (Java vs Kotlin dəyişən elanı):
//   Java:   String ad;          int yas;        double qiymet;
//   Kotlin: var ad: String      var yas: Int     var qiymet: Double
//   Kotlin-də ƏVVƏLCƏ dəyişənin adı, SONRA ":" işarəsi, SONRA tipi yazılır.

// NOT: Ad toqquşmasının (Telebe, Mehsul və s.) qarşısını almaq üçün hər
// Practice faylı öz ayrıca "package"-inə yerləşdirilib.
package practice13

import java.util.Scanner

class Telebe {
    // Sinif daxilində "var" ilə boş sahələr elan edilir,
    // sonra obyekt yaradıldıqdan sonra dəyər mənimsədilir
    var ad: String = ""
    var yas: Int = 0
}

class Mehsul {
    var ad: String = ""
    var qiymet: Double = 0.0
}

fun main() {
    val sc = Scanner(System.`in`)

    // ── 1) Sadə String və Int dəyişənlər ─────────────────────────
    val telebe = Telebe()

    println("Adınızı daxil edin: ")
    telebe.ad = sc.nextLine()

    println("Yaşınızı daxil edin: ")
    // Java-da: sc.nextInt()
    // Kotlin-də Scanner eyni cür işləyir
    telebe.yas = sc.nextInt()
    sc.nextLine() // sətir sonundakı "enter"-i təmizləyirik (buffer problemi olmasın deyə)

    println("Ad: ${telebe.ad}, Yaş: ${telebe.yas}")

    // Yaşı 1 vahid artırırıq (increment)
    telebe.yas++
    println("Gələn ilki yaş: ${telebe.yas}")

    // ── 2) Double tipli dəyişən — endirim hesablama nümunəsi ─────
    val mehsul = Mehsul()

    println("Məhsulun adını daxil edin: ")
    mehsul.ad = sc.nextLine()

    println("Məhsulun qiymətini daxil edin: ")
    // Java-da: sc.nextDouble()
    mehsul.qiymet = sc.nextDouble()

    println("Endirim faizini daxil edin: ")
    val endirimFaizi = sc.nextDouble()

    // Endirimdən sonrakı qiyməti hesablayırıq
    val sonQiymet = mehsul.qiymet - (mehsul.qiymet * endirimFaizi / 100)

    println("Məhsul: ${mehsul.ad}")
    println("Əsas qiymət: ${mehsul.qiymet}")
    println("Endirim: $endirimFaizi%")
    println("Son qiymət: $sonQiymet")

    sc.close()
}
