// Abstract class Telebe
// Bu sinif bir tələbənin ümumi xüsusiyyətlərini və davranışlarını təyin edir
// Abstract olduğu üçün birbaşa obyekt yaradıla bilməz
// Bu sinifdən törədilmiş siniflər öz spesifik xüsusiyyətlərini əlavə edə və melumatGoster metodunu implementasiya edə bilərlər
// Bu, polymorphism və inheritance konseptlərini nümayiş etdirir
// Telebe sinfi tələbənin adını saxlayır və melumatGoster metodunu abstrakt olaraq təyin edir
// MagistrTelebe sinfi Telebe sinifindən törədilir və universitet məlumatını əlavə edir
// DoktorantTelebe sinfi MagistrTelebe sinifindən törədilir və tədqiqat
// yeni daha spesifik məlumat əlavə edir (tədqiqat mövzusu)
// yeni versiya yazdım daha aydın olsun deyə

import java.util.Scanner;

// Abstrakt sinif (Abstraction)
// Bu sinif birbaşa obyekt yaratmaq üçün deyil,
// digər siniflər üçün baza rolunu oynayır
abstract class Telebe {

    // Encapsulation (İnkapsulyasiya)
    // ad dəyişəni private-dir — yalnız bu sinif daxilində əlçatandır
    private String ad;

    // Konstruktor — sinif yaradılarkən ad dəyəri mənimsədilir
    public Telebe(String ad) {
        this.ad = ad;
    }

    // Getter — ad dəyərini oxumaq üçün
    public String getAd() {
        return ad;
    }

    // Setter — ad dəyərini dəyişmək üçün
    public void setAd(String ad) {
         this.ad = ad;
        }

    // Abstrakt metod — hər alt sinif öz implementasiyasını yazmalıdır
    public abstract void melumatGoster();
}

// Inheritance (İrsiyyət)
// MagistrTelebe sinifi Telebe sinifindən miras alır
class MagistrTelebe extends Telebe {

    // Bu sinifə məxsus sahə — universitetin adı
    private String universitet;

    // Konstruktor — ad Telebe-yə, universitet isə bu sinifə mənimsədilir
    public MagistrTelebe(String ad, String universitet) {
        super(ad); // Telebe sinifinin konstruktorunu çağırır
        this.universitet = universitet;
    }

    // Abstrakt metodun implementasiyası (Polymorphism)
    // Telebe sinifindəki melumatGoster() burada konkret şəkildə yazılır
    @Override
    public void melumatGoster() {
        // ad-a birbaşa yox, getter vasitəsilə müraciət edilir (Encapsulation)
        System.out.println("Ad: " + getAd());
        System.out.println("Universitet: " + universitet);
    }
}

// Inheritance (İrsiyyət)
// DoktorantTelebe sinifi MagistrTelebe sinifindən miras alır
// Beləliklə Telebe → MagistrTelebe → DoktorantTelebe zənciri yaranır
class DoktorantTelebe extends MagistrTelebe {

    // Bu sinifə məxsus sahə — tədqiqat mövzusu
    private String tedqiqatMovzusu;

    // Konstruktor — ad və universitet parent-ə ötürülür,
    // tedqiqatMovzusu isə bu sinifə mənimsədilir
    public DoktorantTelebe(String ad, String universitet, String tedqiqatMovzusu) {
        super(ad, universitet); // MagistrTelebe konstruktorunu çağırır
        this.tedqiqatMovzusu = tedqiqatMovzusu;
    }

    // Method Overriding (Polymorphism)
    // MagistrTelebe-dəki melumatGoster() genişləndirilir
    @Override
    public void melumatGoster() {
        super.melumatGoster(); // Parent metodunu çağırır (ad + universitet çap olunur)
        System.out.println("Tədqiqat mövzusu: " + tedqiqatMovzusu); // əlavə məlumat
    }
}

public class Main {
    public static void main(String[] args) {

        // try-with-resources — Scanner avtomatik bağlanır, manual close lazım deyil
        try (Scanner scanner = new Scanner(System.in)) {

            // ── Magistr tələbə məlumatlarının daxil edilməsi ──────────────
            System.out.print("Magistr tələbənin adını daxil edin: ");
            String mAd = scanner.nextLine();

            System.out.print("Magistr tələbənin universitetini daxil edin: ");
            String mUniversitet = scanner.nextLine();

            // Polymorphism — Telebe tipli referensiya MagistrTelebe obyektinə işarə edir
            Telebe magistrTelebe = new MagistrTelebe(mAd, mUniversitet);

            // melumatGoster() çağırılır — hansı sinifin metodu olduğu runtime-da müəyyən olunur
            magistrTelebe.melumatGoster();

            // ── Doktorant məlumatlarının daxil edilməsi ───────────────────
            System.out.print("Doktorantın adını daxil edin: ");
            String dAd = scanner.nextLine();

            System.out.print("Doktorantın universitetini daxil edin: ");
            String dUniversitet = scanner.nextLine();

            System.out.print("Doktorantın tədqiqat mövzusunu daxil edin: ");
            String dTedqiqatMovzusu = scanner.nextLine();

            // Polymorphism — Telebe tipli referensiya DoktorantTelebe obyektinə işarə edir
            Telebe doktorantTelebe = new DoktorantTelebe(dAd, dUniversitet, dTedqiqatMovzusu);

            // melumatGoster() çağırılır — DoktorantTelebe-nin override edilmiş metodu işləyir
            doktorantTelebe.melumatGoster();

        } // try bloku bitdikdə Scanner avtomatik bağlanır
    }
}