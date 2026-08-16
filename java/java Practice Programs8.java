// Abstract class Student
// Bu sinif bir tələbənin ümumi xüsusiyyətlərini və davranışlarını təyin edir
// Abstract olduğu üçün birbaşa obyekt yaradıla bilməz
// Bu sinifdən törədilmiş siniflər öz spesifik xüsusiyyətlərini əlavə edə və showInfo metodunu implementasiya edə bilərlər
// Bu, polymorphism və inheritance konseptlərini nümayiş etdirir
// Student sinfi tələbənin adını saxlayır və showInfo metodunu abstrakt olaraq təyin edir
// GraduateStudent sinfi Student sinifindən törədilir və universitet məlumatını əlavə edir
// PhDStudent sinfi GraduateStudent sinifindən törədilir və tədqiqat
// yeni daha spesifik məlumat əlavə edir (tədqiqat mövzusu)
// yeni versiya yazdım daha aydın olsun deyə

import java.util.Scanner;

// Abstrakt sinif (Abstraction)
// Bu sinif birbaşa obyekt yaratmaq üçün deyil,
// digər siniflər üçün baza rolunu oynayır
abstract class Student {

    // Encapsulation (İnkapsulyasiya)
    // name dəyişəni private-dir — yalnız bu sinif daxilində əlçatandır
    private String name;

    // Konstruktor — sinif yaradılarkən name dəyəri mənimsədilir
    public Student(String name) {
        this.name = name;
    }

    // Getter — name dəyərini oxumaq üçün
    public String getName() { 
        return name; 
    }

    // Setter — name dəyərini dəyişmək üçün
    public void setName(String name) {
         this.name = name;
        }

    // Abstrakt metod — hər alt sinif öz implementasiyasını yazmalıdır
    public abstract void showInfo();
}

// Inheritance (İrsiyyət)
// GraduateStudent sinifi Student sinifindən miras alır
class GraduateStudent extends Student {

    // Bu sinifə məxsus sahə — universitetin adı
    private String university;

    // Konstruktor — name Student-ə, university isə bu sinifə mənimsədilir
    public GraduateStudent(String name, String university) {
        super(name); // Student sinifinin konstruktorunu çağırır
        this.university = university;
    }

    // Abstrakt metodun implementasiyası (Polymorphism)
    // Student sinifindəki showInfo() burada konkret şəkildə yazılır
    @Override
    public void showInfo() {
        // name-ə birbaşa yox, getter vasitəsilə müraciət edilir (Encapsulation)
        System.out.println("Name: " + getName());
        System.out.println("University: " + university);
    }
}

// Inheritance (İrsiyyət)
// PhDStudent sinifi GraduateStudent sinifindən miras alır
// Beləliklə Student → GraduateStudent → PhDStudent zənciri yaranır
class PhDStudent extends GraduateStudent {

    // Bu sinifə məxsus sahə — tədqiqat mövzusu
    private String researchTopic;

    // Konstruktor — name və university parent-ə ötürülür,
    // researchTopic isə bu sinifə mənimsədilir
    public PhDStudent(String name, String university, String researchTopic) {
        super(name, university); // GraduateStudent konstruktorunu çağırır
        this.researchTopic = researchTopic;
    }

    // Method Overriding (Polymorphism)
    // GraduateStudent-dəki showInfo() genişləndirilir
    @Override
    public void showInfo() {
        super.showInfo(); // Parent metodunu çağırır (name + university çap olunur)
        System.out.println("Research Topic: " + researchTopic); // əlavə məlumat
    }
}

public class Main {
    public static void main(String[] args) {

        // try-with-resources — Scanner avtomatik bağlanır, manual close lazım deyil
        try (Scanner scanner = new Scanner(System.in)) {

            // ── Graduate Student məlumatlarının daxil edilməsi ──────────────
            System.out.print("Enter the name of the graduate student: ");
            String gsName = scanner.nextLine();

            System.out.print("Enter the university of the graduate student: ");
            String gsUniversity = scanner.nextLine();

            // Polymorphism — Student tipli referensiya GraduateStudent obyektinə işarə edir
            Student graduateStudent = new GraduateStudent(gsName, gsUniversity);

            // showInfo() çağırılır — hansı sinifin metodu olduğu runtime-da müəyyən olunur
            graduateStudent.showInfo();

            // ── PhD Student məlumatlarının daxil edilməsi ───────────────────
            System.out.print("Enter the name of the PhD student: ");
            String phdName = scanner.nextLine();

            System.out.print("Enter the university of the PhD student: ");
            String phdUniversity = scanner.nextLine();

            System.out.print("Enter the research topic of the PhD student: ");
            String phdResearchTopic = scanner.nextLine();

            // Polymorphism — Student tipli referensiya PhDStudent obyektinə işarə edir
            Student phdStudent = new PhDStudent(phdName, phdUniversity, phdResearchTopic);

            // showInfo() çağırılır — PhDStudent-in override edilmiş metodu işləyir
            phdStudent.showInfo();

        } // try bloku bitdikdə Scanner avtomatik bağlanır
    }
}