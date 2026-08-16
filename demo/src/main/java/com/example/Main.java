package com.example;

import java.util.Scanner;

// Abstrakt sinif (Abstraction)
// Bu sinif birbaşa obyekt yaratmaq üçün deyil,
// digər siniflər üçün baza rolunu oynayır
abstract class Student {

    // Encapsulation (İnkapsulyasiya)
    private String name;
    private String surname;
    private String phoneNumber;
    private String email;

    // Konstruktor — sinif yaradılarkən sahələr mənimsədilir
    public Student(String name, String surname, String phoneNumber, String email) {
        this.name = name;
        this.surname = surname;
        this.phoneNumber = phoneNumber;
        this.email = email;
    }

    // Getter-lər — sahə dəyərlərini oxumaq üçün
    public String getName() {
        return name;
    }

    public String getSurname() {
        return surname;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public String getEmail() {
        return email;
    }

    // Setter-lər — sahə dəyərlərini dəyişmək üçün
    public void setName(String name) {
        this.name = name;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    // Abstrakt metod — hər alt sinif öz implementasiyasını yazmalıdır
    public abstract void showInfo();
}

// Inheritance (İrsiyyət)
// GraduateStudent sinifi Student sinifindən miras alır
class GraduateStudent extends Student {

    // Bu sinifə məxsus sahə — universitetin adı
    private String university;

    // Konstruktor — name, surname, phone və email Student-ə,
    // university isə bu sinifə mənimsədilir
    public GraduateStudent(String name, String surname, String phoneNumber, String email, String university) {
        super(name, surname, phoneNumber, email);
        this.university = university;
    }

    // Abstrakt metodun implementasiyası (Polymorphism)
    // Student sinifindəki showInfo() burada konkret şəkildə yazılır
    @Override
    public void showInfo() {
        System.out.println("Name: " + getName() + " " + getSurname());
        System.out.println("Phone: " + getPhoneNumber());
        System.out.println("Email: " + getEmail());
        System.out.println("University: " + university);
    }
}

// Inheritance (İrsiyyət)
// PhDStudent sinifi GraduateStudent sinifindən miras alır
// Beləliklə Student → GraduateStudent → PhDStudent zənciri yaranır
class PhDStudent extends GraduateStudent {

    // Bu sinifə məxsus sahə — tədqiqat mövzusu
    private String researchTopic;

    // Konstruktor — name, surname, phone və email parent-ə ötürülür,
    // university və researchTopic isə bu siniflərə mənimsədilir
    public PhDStudent(String name, String surname, String phoneNumber, String email, String university, String researchTopic) {
        super(name, surname, phoneNumber, email, university);
        this.researchTopic = researchTopic;
    }

    // Method Overriding (Polymorphism)
    // GraduateStudent-dəki showInfo() genişləndirilir
    @Override
    public void showInfo() {
        super.showInfo();
        System.out.println("Research Topic: " + researchTopic);
    }
}

public class Main {
    public static void main(String[] args) {

        try (Scanner scanner = new Scanner(System.in)) {

            // ── Graduate Student məlumatlarının daxil edilməsi ──────────────
            System.out.println("Graduate student data entry:");
            String gsName = readNonEmptyInput(scanner, "Enter the name of the graduate student: ");
            String gsSurname = readNonEmptyInput(scanner, "Enter the surname of the graduate student: ");
            String gsPhone = readValidPhone(scanner, "Enter the phone number of the graduate student: ");
            String gsEmail = readValidEmail(scanner, "Enter the email of the graduate student: ");
            String gsUniversity = readNonEmptyInput(scanner, "Enter the university of the graduate student: ");

            Student graduateStudent = new GraduateStudent(gsName, gsSurname, gsPhone, gsEmail, gsUniversity);
            System.out.println();
            graduateStudent.showInfo();

            // ── PhD Student məlumatlarının daxil edilməsi ───────────────────
            System.out.println();
            System.out.println("PhD student data entry:");
            String phdName = readNonEmptyInput(scanner, "Enter the name of the PhD student: ");
            String phdSurname = readNonEmptyInput(scanner, "Enter the surname of the PhD student: ");
            String phdPhone = readValidPhone(scanner, "Enter the phone number of the PhD student: ");
            String phdEmail = readValidEmail(scanner, "Enter the email of the PhD student: ");
            String phdUniversity = readNonEmptyInput(scanner, "Enter the university of the PhD student: ");
            String phdResearchTopic = readNonEmptyInput(scanner, "Enter the research topic of the PhD student: ");

            Student phdStudent = new PhDStudent(phdName, phdSurname, phdPhone, phdEmail, phdUniversity, phdResearchTopic);
            System.out.println();
            phdStudent.showInfo();

        }
    }

    private static String readNonEmptyInput(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt);
            String input = scanner.nextLine().trim();
            if (!input.isEmpty()) {
                return input;
            }
            System.out.println("Invalid entry: this field cannot be empty. Please enter a valid value.");
        }
    }

    private static String readValidPhone(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt);
            String phone = scanner.nextLine().trim();
            if (phone.isEmpty()) {
                System.out.println("Invalid entry: phone number cannot be empty.");
                continue;
            }
            if (isValidPhone(phone)) {
                return phone;
            }
            System.out.println("Invalid phone number. Use digits, spaces, dashes, and optional leading +.");
        }
    }

    private static String readValidEmail(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt);
            String email = scanner.nextLine().trim();
            if (email.isEmpty()) {
                System.out.println("Invalid entry: email cannot be empty.");
                continue;
            }
            if (isValidEmail(email)) {
                return email;
            }
            System.out.println("Invalid email format. Example: user@example.com");
        }
    }

    private static boolean isValidPhone(String phone) {
        return phone.matches("^\\+?[0-9\\-\\s]{7,20}$");
    }

    private static boolean isValidEmail(String email) {
        return email.matches("^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$");
    }
}
