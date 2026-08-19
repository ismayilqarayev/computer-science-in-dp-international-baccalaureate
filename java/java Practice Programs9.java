import java.util.Scanner;

// Abstrakt sinif (Abstraction)
// Bu sinif birbaşa obyekt yaratmaq üçün deyil,
// digər siniflər üçün baza rolunu oynayır
abstract class Telebe {

    // Encapsulation (İnkapsulyasiya)
    private String ad;
    private String soyad;
    private String telefonNomresi;
    private String email;

    // Konstruktor — sinif yaradılarkən sahələr mənimsədilir
    public Telebe(String ad, String soyad, String telefonNomresi, String email) {
        this.ad = ad;
        this.soyad = soyad;
        this.telefonNomresi = telefonNomresi;
        this.email = email;
    }

    // Getter-lər — sahə dəyərlərini oxumaq üçün
    public String getAd() {
        return ad;
    }

    public String getSoyad() {
        return soyad;
    }

    public String getTelefonNomresi() {
        return telefonNomresi;
    }

    public String getEmail() {
        return email;
    }

    // Setter-lər — sahə dəyərlərini dəyişmək üçün
    public void setAd(String ad) {
        this.ad = ad;
    }

    public void setSoyad(String soyad) {
        this.soyad = soyad;
    }

    public void setTelefonNomresi(String telefonNomresi) {
        this.telefonNomresi = telefonNomresi;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    // Abstrakt metod — hər alt sinif öz implementasiyasını yazmalıdır
    public abstract void melumatGoster();
}

// Inheritance (İrsiyyət)
// MagistrTelebe sinifi Telebe sinifindən miras alır
class MagistrTelebe extends Telebe {

    // Bu sinifə məxsus sahə — universitetin adı
    private String universitet;

    // Konstruktor — ad, soyad, telefon və email Telebe-yə,
    // universitet isə bu sinifə mənimsədilir
    public MagistrTelebe(String ad, String soyad, String telefonNomresi, String email, String universitet) {
        super(ad, soyad, telefonNomresi, email);
        this.universitet = universitet;
    }

    // Abstrakt metodun implementasiyası (Polymorphism)
    // Telebe sinifindəki melumatGoster() burada konkret şəkildə yazılır
    @Override
    public void melumatGoster() {
        System.out.println("Ad: " + getAd() + " " + getSoyad());
        System.out.println("Telefon: " + getTelefonNomresi());
        System.out.println("Email: " + getEmail());
        System.out.println("Universitet: " + universitet);
    }
}

// Inheritance (İrsiyyət)
// DoktorantTelebe sinifi MagistrTelebe sinifindən miras alır
// Beləliklə Telebe → MagistrTelebe → DoktorantTelebe zənciri yaranır
class DoktorantTelebe extends MagistrTelebe {

    // Bu sinifə məxsus sahə — tədqiqat mövzusu
    private String tedqiqatMovzusu;

    // Konstruktor — ad, soyad, telefon və email parent-ə ötürülür,
    // universitet və tedqiqatMovzusu isə bu siniflərə mənimsədilir
    public DoktorantTelebe(String ad, String soyad, String telefonNomresi, String email, String universitet, String tedqiqatMovzusu) {
        super(ad, soyad, telefonNomresi, email, universitet);
        this.tedqiqatMovzusu = tedqiqatMovzusu;
    }

    // Method Overriding (Polymorphism)
    // MagistrTelebe-dəki melumatGoster() genişləndirilir
    @Override
    public void melumatGoster() {
        super.melumatGoster();
        System.out.println("Tədqiqat mövzusu: " + tedqiqatMovzusu);
    }
}

public class Main {
    public static void main(String[] args) {

        try (Scanner scanner = new Scanner(System.in)) {

            // ── Magistr tələbə məlumatlarının daxil edilməsi ──────────────
            System.out.println("Magistr tələbə məlumatlarının daxil edilməsi:");
            String mAd = readNonEmptyInput(scanner, "Magistr tələbənin adını daxil edin: ");
            String mSoyad = readNonEmptyInput(scanner, "Magistr tələbənin soyadını daxil edin: ");
            String mTelefon = readValidPhone(scanner, "Magistr tələbənin telefon nömrəsini daxil edin: ");
            String mEmail = readValidEmail(scanner, "Magistr tələbənin emailini daxil edin: ");
            String mUniversitet = readNonEmptyInput(scanner, "Magistr tələbənin universitetini daxil edin: ");

            Telebe magistrTelebe = new MagistrTelebe(mAd, mSoyad, mTelefon, mEmail, mUniversitet);
            System.out.println();
            magistrTelebe.melumatGoster();

            // ── Doktorant məlumatlarının daxil edilməsi ───────────────────
            System.out.println();
            System.out.println("Doktorant məlumatlarının daxil edilməsi:");
            String dAd = readNonEmptyInput(scanner, "Doktorantın adını daxil edin: ");
            String dSoyad = readNonEmptyInput(scanner, "Doktorantın soyadını daxil edin: ");
            String dTelefon = readValidPhone(scanner, "Doktorantın telefon nömrəsini daxil edin: ");
            String dEmail = readValidEmail(scanner, "Doktorantın emailini daxil edin: ");
            String dUniversitet = readNonEmptyInput(scanner, "Doktorantın universitetini daxil edin: ");
            String dTedqiqatMovzusu = readNonEmptyInput(scanner, "Doktorantın tədqiqat mövzusunu daxil edin: ");

            Telebe doktorantTelebe = new DoktorantTelebe(dAd, dSoyad, dTelefon, dEmail, dUniversitet, dTedqiqatMovzusu);
            System.out.println();
            doktorantTelebe.melumatGoster();

        }
    }

    private static String readNonEmptyInput(Scanner scanner, String sual) {
        while (true) {
            System.out.print(sual);
            String giris = scanner.nextLine().trim();
            if (!giris.isEmpty()) {
                return giris;
            }
            System.out.println("Yanlış giriş: bu sahə boş ola bilməz. Zəhmət olmasa düzgün dəyər daxil edin.");
        }
    }

    private static String readValidPhone(Scanner scanner, String sual) {
        while (true) {
            System.out.print(sual);
            String telefon = scanner.nextLine().trim();
            if (telefon.isEmpty()) {
                System.out.println("Yanlış giriş: telefon nömrəsi boş ola bilməz.");
                continue;
            }
            if (isValidPhone(telefon)) {
                return telefon;
            }
            System.out.println("Yanlış telefon nömrəsi. Rəqəm, boşluq, tire və istəyə görə \"+\" işlədin.");
        }
    }

    private static String readValidEmail(Scanner scanner, String sual) {
        while (true) {
            System.out.print(sual);
            String email = scanner.nextLine().trim();
            if (email.isEmpty()) {
                System.out.println("Yanlış giriş: email boş ola bilməz.");
                continue;
            }
            if (isValidEmail(email)) {
                return email;
            }
            System.out.println("Yanlış email formatı. Nümunə: istifadeci@example.com");
        }
    }

    private static boolean isValidPhone(String telefon) {
        return telefon.matches("^\\+?[0-9\\-\\s]{7,20}$");
    }

    private static boolean isValidEmail(String email) {
        return email.matches("^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$");
    }
}
