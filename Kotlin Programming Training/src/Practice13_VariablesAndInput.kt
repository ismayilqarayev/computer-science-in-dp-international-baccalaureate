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
//   Java:   String name;        int age;        double price;
//   Kotlin: var name: String    var age: Int    var price: Double
//   Kotlin-də ƏVVƏLCƏ dəyişənin adı, SONRA ":" işarəsi, SONRA tipi yazılır.

import java.util.Scanner

class Student {
    // Sinif daxilində "var" ilə boş sahələr elan edilir,
    // sonra obyekt yaradıldıqdan sonra dəyər mənimsədilir
    var name: String = ""
    var age: Int = 0
}

class Product {
    var name: String = ""
    var price: Double = 0.0
}

fun main() {
    val sc = Scanner(System.`in`)

    // ── 1) Sadə String və Int dəyişənlər ─────────────────────────
    val student = Student()

    println("Enter your name: ")
    student.name = sc.nextLine()

    println("Enter your age: ")
    // Java-da: sc.nextInt()
    // Kotlin-də Scanner eyni cür işləyir
    student.age = sc.nextInt()
    sc.nextLine() // sətir sonundakı "enter"-i təmizləyirik (buffer problemi olmasın deyə)

    println("Name: ${student.name} Age: ${student.age}")

    // Yaşı 1 vahid artırırıq (increment)
    student.age++
    println("Next year age: ${student.age}")

    // ── 2) Double tipli dəyişən — endirim hesablama nümunəsi ─────
    val product = Product()

    println("Enter product name: ")
    product.name = sc.nextLine()

    println("Enter product price: ")
    // Java-da: sc.nextDouble()
    product.price = sc.nextDouble()

    println("Enter discount percentage: ")
    val discount = sc.nextDouble()

    // Endirimdən sonrakı qiyməti hesablayırıq
    val finalPrice = product.price - (product.price * discount / 100)

    println("Product: ${product.name}")
    println("Original Price: ${product.price}")
    println("Discount: $discount%")
    println("Final Price: $finalPrice")

    sc.close()
}
