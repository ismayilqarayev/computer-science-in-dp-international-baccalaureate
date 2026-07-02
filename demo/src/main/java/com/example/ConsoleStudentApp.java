package com.example;

import java.util.Scanner;

public class ConsoleStudentApp {
    private final StudentValidator validator = new StudentValidator();

    public void run() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Graduate student data entry:");
            String gsName = readNonEmptyInput(scanner, "Enter the name of the graduate student: ");
            String gsSurname = readNonEmptyInput(scanner, "Enter the surname of the graduate student: ");
            String gsPhone = readValidPhone(scanner, "Enter the phone number of the graduate student: ");
            String gsEmail = readValidEmail(scanner, "Enter the email of the graduate student: ");
            String gsUniversity = readNonEmptyInput(scanner, "Enter the university of the graduate student: ");

            Student graduateStudent = new GraduateStudent(gsName, gsSurname, gsPhone, gsEmail, gsUniversity);
            System.out.println();
            graduateStudent.showInfo();

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

    private String readNonEmptyInput(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt);
            String input = scanner.nextLine().trim();
            if (validator.isValidInput(input)) {
                return input;
            }
            System.out.println("Invalid entry: this field cannot be empty. Please enter a valid value.");
        }
    }

    private String readValidPhone(Scanner scanner, String prompt) {
        while (true) {
            String phone = readNonEmptyInput(scanner, prompt);
            if (validator.isValidPhone(phone)) {
                return phone;
            }
            System.out.println("Invalid phone number. Use digits, spaces, dashes, and optional leading +.");
        }
    }

    private String readValidEmail(Scanner scanner, String prompt) {
        while (true) {
            String email = readNonEmptyInput(scanner, prompt);
            if (validator.isValidEmail(email)) {
                return email;
            }
            System.out.println("Invalid email format. Example: user@example.com");
        }
    }
}
