// ══════════════════════════════════════════════════════════════
//  PRACTICE 9 — Validasiya (regex) ilə istifadəçi girişi
//  (java/java Practice Programs9.java faylının Kotlin versiyası)
// ══════════════════════════════════════════════════════════════
//
// Bu proqramda öyrənəcəyimiz əlavə mövzular:
//   - Kotlin-də regex istifadəsi (String.matches())
//   - "private fun" -> yalnız bu fayl daxilində istifadə oluna bilən köməkçi funksiyalar
//   - while(true) + return ilə "təkrar sual ver, düzgün cavab alana qədər" məntiqi

// NOT: Ad toqquşmasının (Student, GraduateStudent, PhDStudent və s.) qarşısını
// almaq üçün hər Practice faylı öz ayrıca "package"-inə yerləşdirilib.
package practice09

import java.util.Scanner

abstract class Student(
    val name: String,
    val surname: String,
    val phoneNumber: String,
    val email: String
) {
    abstract fun showInfo()
}

open class GraduateStudent(
    name: String,
    surname: String,
    phoneNumber: String,
    email: String,
    val university: String
) : Student(name, surname, phoneNumber, email) {

    override fun showInfo() {
        println("Name: $name $surname")
        println("Phone: $phoneNumber")
        println("Email: $email")
        println("University: $university")
    }
}

class PhDStudent(
    name: String,
    surname: String,
    phoneNumber: String,
    email: String,
    university: String,
    private val researchTopic: String
) : GraduateStudent(name, surname, phoneNumber, email, university) {

    override fun showInfo() {
        super.showInfo()
        println("Research Topic: $researchTopic")
    }
}

// ── Köməkçi (validasiya) funksiyaları ────────────────────────────────

// Boş olmayan mətn daxil edilənə qədər təkrar-təkrar soruşur
private fun readNonEmptyInput(scanner: Scanner, prompt: String): String {
    while (true) {
        print(prompt)
        val input = scanner.nextLine().trim()
        if (input.isNotEmpty()) {
            return input
        }
        println("Invalid entry: this field cannot be empty. Please enter a valid value.")
    }
}

// Telefon nömrəsi formatına uyğun gələnə qədər təkrar soruşur
private fun readValidPhone(scanner: Scanner, prompt: String): String {
    while (true) {
        print(prompt)
        val phone = scanner.nextLine().trim()
        if (phone.isEmpty()) {
            println("Invalid entry: phone number cannot be empty.")
            continue
        }
        if (isValidPhone(phone)) {
            return phone
        }
        println("Invalid phone number. Use digits, spaces, dashes, and optional leading +.")
    }
}

// Email formatına uyğun gələnə qədər təkrar soruşur
private fun readValidEmail(scanner: Scanner, prompt: String): String {
    while (true) {
        print(prompt)
        val email = scanner.nextLine().trim()
        if (email.isEmpty()) {
            println("Invalid entry: email cannot be empty.")
            continue
        }
        if (isValidEmail(email)) {
            return email
        }
        println("Invalid email format. Example: user@example.com")
    }
}

// Regex ilə telefon formatını yoxlayır: rəqəmlər, boşluq, tire və istəyə görə "+"
private fun isValidPhone(phone: String): Boolean {
    return phone.matches(Regex("^\\+?[0-9\\-\\s]{7,20}$"))
}

// Regex ilə sadə email formatını yoxlayır
private fun isValidEmail(email: String): Boolean {
    return email.matches(Regex("^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$"))
}

fun main() {
    Scanner(System.`in`).use { scanner ->

        // ── Graduate Student məlumatlarının daxil edilməsi ──────────────
        println("Graduate student data entry:")
        val gsName = readNonEmptyInput(scanner, "Enter the name of the graduate student: ")
        val gsSurname = readNonEmptyInput(scanner, "Enter the surname of the graduate student: ")
        val gsPhone = readValidPhone(scanner, "Enter the phone number of the graduate student: ")
        val gsEmail = readValidEmail(scanner, "Enter the email of the graduate student: ")
        val gsUniversity = readNonEmptyInput(scanner, "Enter the university of the graduate student: ")

        val graduateStudent: Student = GraduateStudent(gsName, gsSurname, gsPhone, gsEmail, gsUniversity)
        println()
        graduateStudent.showInfo()

        // ── PhD Student məlumatlarının daxil edilməsi ───────────────────
        println()
        println("PhD student data entry:")
        val phdName = readNonEmptyInput(scanner, "Enter the name of the PhD student: ")
        val phdSurname = readNonEmptyInput(scanner, "Enter the surname of the PhD student: ")
        val phdPhone = readValidPhone(scanner, "Enter the phone number of the PhD student: ")
        val phdEmail = readValidEmail(scanner, "Enter the email of the PhD student: ")
        val phdUniversity = readNonEmptyInput(scanner, "Enter the university of the PhD student: ")
        val phdResearchTopic = readNonEmptyInput(scanner, "Enter the research topic of the PhD student: ")

        val phdStudent: Student = PhDStudent(phdName, phdSurname, phdPhone, phdEmail, phdUniversity, phdResearchTopic)
        println()
        phdStudent.showInfo()
    }
}
