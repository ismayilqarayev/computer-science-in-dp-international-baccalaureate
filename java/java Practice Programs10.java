


//-------------------------------------------------------------------------------------------

//Abstract class Student

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// ══════════════════════════════════════════════
//  ABSTRAKT BAZ SİNİF — Şəxs
// ══════════════════════════════════════════════
abstract class Sexs {
    private String ad;
    private String soyad;
    private int yas;

    public Sexs(String ad, String soyad, int yas) {
        this.ad = ad;
        this.soyad = soyad;
        this.yas = yas;
    }

    public String getAd() {
         return ad; 
        }
        
    public String getSoyad() {
         return soyad; 
        }

    public int getYas() {
         return yas;
        }

    public abstract void melumatlariGoster();
}

// ══════════════════════════════════════════════
//  KURS SİNİFİ
// ══════════════════════════════════════════════
class Kurs {
    private String kursAdi;
    private int kreditSaati;
    private String muellim;

    public Kurs(String kursAdi, int kreditSaati, String muellim) {
        this.kursAdi = kursAdi;
        this.kreditSaati = kreditSaati;
        this.muellim = muellim;
    }

    public String getKursAdi() { return kursAdi; }
    public int getKreditSaati() { return kreditSaati; }
    public String getMuellim() { return muellim; }

    public void kursInfosu() {
        System.out.println("  Kurs     : " + kursAdi);
        System.out.println("  Kredit   : " + kreditSaati);
        System.out.println("  Müəllim  : " + muellim);
    }
}

// ══════════════════════════════════════════════
//  İMTAHAN SİNİFİ
// ══════════════════════════════════════════════
class Imtahan {
    private String fenn;
    private double bal;
    private String tarix;

    public Imtahan(String fenn, double bal, String tarix) {
        this.fenn = fenn;
        this.bal = bal;
        this.tarix = tarix;
    }

    public double getBal() { return bal; }

    public void imtahanInfosu() {
        System.out.println("  Fənn   : " + fenn);
        System.out.println("  Bal    : " + bal);
        System.out.println("  Tarix  : " + tarix);
    }
}

// ══════════════════════════════════════════════
//  DİPLOM SİNİFİ
// ══════════════════════════════════════════════
class Diplom {
    private String ixtisas;
    private String tarix;
    private double ortalama;

    public Diplom(String ixtisas, String tarix, double ortalama) {
        this.ixtisas = ixtisas;
        this.tarix = tarix;
        this.ortalama = ortalama;
    }

    public void diplomInfosu() {
        System.out.println("  İxtisas  : " + ixtisas);
        System.out.println("  Tarix    : " + tarix);
        System.out.println("  Ortalama : " + ortalama);
    }
}

// ══════════════════════════════════════════════
//  TƏLƏBƏ — Şəxs-dən miras alır
// ══════════════════════════════════════════════
class Telebe extends Sexs {
    private String fakulte;
    private int kurs;
    private List<Imtahan> imtahanlar;
    private List<Kurs> kursList;

    public Telebe(String ad, String soyad, int yas,
                  String fakulte, int kurs) {
        super(ad, soyad, yas);
        this.fakulte = fakulte;
        this.kurs = kurs;
        this.imtahanlar = new ArrayList<>();
        this.kursList = new ArrayList<>();
    }

    public void imtahanElave(Imtahan imtahan) {
        imtahanlar.add(imtahan);
    }

    public void kursElave(Kurs k) {
        kursList.add(k);
    }

    public double ortalamaHesabla() {
        if (imtahanlar.isEmpty()) return 0;
        double cem = 0;
        for (Imtahan i : imtahanlar) cem += i.getBal();
        return cem / imtahanlar.size();
    }

    public String getFakulte() { return fakulte; }
    public int getKurs() { return kurs; }

    @Override
    public void melumatlariGoster() {
        System.out.println("Ad / Soyad : " + getAd() + " " + getSoyad());
        System.out.println("Yaş        : " + getYas());
        System.out.println("Fakültə    : " + fakulte);
        System.out.println("Kurs       : " + kurs);
        System.out.println("Ortalama   : " + ortalamaHesabla());

        if (!kursList.isEmpty()) {
            System.out.println("--- Kurslar ---");
            for (Kurs k : kursList) k.kursInfosu();
        }

        if (!imtahanlar.isEmpty()) {
            System.out.println("--- İmtahanlar ---");
            for (Imtahan i : imtahanlar) i.imtahanInfosu();
        }
    }
}

// ══════════════════════════════════════════════
//  MAGİSTR — Tələbə-dən miras alır
// ══════════════════════════════════════════════
class Magistr extends Telebe {
    private String teqiqatMovzusu;
    private String elmiRehber;

    public Magistr(String ad, String soyad, int yas,
                   String fakulte, int kurs,
                   String teqiqatMovzusu, String elmiRehber) {
        super(ad, soyad, yas, fakulte, kurs);
        this.teqiqatMovzusu = teqiqatMovzusu;
        this.elmiRehber = elmiRehber;
    }

    @Override
    public void melumatlariGoster() {
        super.melumatlariGoster();
        System.out.println("Tədqiqat   : " + teqiqatMovzusu);
        System.out.println("Elmi rəhbər: " + elmiRehber);
    }
}

// ══════════════════════════════════════════════
//  DOKTORANT — Magistr-dən miras alır
// ══════════════════════════════════════════════
class Doktorant extends Magistr {
    private String dissertasiyaMovzusu;
    private int neşrSayi;
    private Diplom diplom;

    public Doktorant(String ad, String soyad, int yas,
                     String fakulte, int kurs,
                     String teqiqatMovzusu, String elmiRehber,
                     String dissertasiyaMovzusu, int neşrSayi) {
        super(ad, soyad, yas, fakulte, kurs, teqiqatMovzusu, elmiRehber);
        this.dissertasiyaMovzusu = dissertasiyaMovzusu;
        this.neşrSayi = neşrSayi;
    }

    public void diplomTəyin(Diplom diplom) {
        this.diplom = diplom;
    }

    @Override
    public void melumatlariGoster() {
        super.melumatlariGoster();
        System.out.println("Dissertasiya: " + dissertasiyaMovzusu);
        System.out.println("Nəşr sayı   : " + neşrSayi);
        if (diplom != null) {
            System.out.println("--- Diplom ---");
            diplom.diplomInfosu();
        }
    }
}

// ══════════════════════════════════════════════
//  MÜƏLLİM — Şəxs-dən miras alır
// ══════════════════════════════════════════════
class Muellim extends Sexs {
    private String fakulte;
    private String fenn;
    private int tedrisTecurbesi;

    public Muellim(String ad, String soyad, int yas,
                   String fakulte, String fenn, int tedrisTecurbesi) {
        super(ad, soyad, yas);
        this.fakulte = fakulte;
        this.fenn = fenn;
        this.tedrisTecurbesi = tedrisTecurbesi;
    }

    public String getFakulte() { return fakulte; }
    public String getFenn() { return fenn; }

    @Override
    public void melumatlariGoster() {
        System.out.println("Ad / Soyad   : " + getAd() + " " + getSoyad());
        System.out.println("Yaş          : " + getYas());
        System.out.println("Fakültə      : " + fakulte);
        System.out.println("Fənn         : " + fenn);
        System.out.println("Təcrübə (il) : " + tedrisTecurbesi);
    }
}

// ══════════════════════════════════════════════
//  PROFESSOR — Müəllim-dən miras alır
// ══════════════════════════════════════════════
class Professor extends Muellim {
    private String elmiDerece;
    private int neşrSayi;

    public Professor(String ad, String soyad, int yas,
                     String fakulte, String fenn, int tedrisTecurbesi,
                     String elmiDerece, int neşrSayi) {
        super(ad, soyad, yas, fakulte, fenn, tedrisTecurbesi);
        this.elmiDerece = elmiDerece;
        this.neşrSayi = neşrSayi;
    }

    @Override
    public void melumatlariGoster() {
        super.melumatlariGoster();
        System.out.println("Elmi dərəcə  : " + elmiDerece);
        System.out.println("Nəşr sayı    : " + neşrSayi);
    }
}

// ══════════════════════════════════════════════
//  REKTOR — Professor-dan miras alır
// ══════════════════════════════════════════════
class Rektor extends Professor {
    private String universitet;
    private int idareetmeTecurbesi;

    public Rektor(String ad, String soyad, int yas,
                  String fakulte, String fenn, int tedrisTecurbesi,
                  String elmiDerece, int neşrSayi,
                  String universitet, int idareetmeTecurbesi) {
        super(ad, soyad, yas, fakulte, fenn, tedrisTecurbesi,
              elmiDerece, neşrSayi);
        this.universitet = universitet;
        this.idareetmeTecurbesi = idareetmeTecurbesi;
    }

    @Override
    public void melumatlariGoster() {
        super.melumatlariGoster();
        System.out.println("Universitet      : " + universitet);
        System.out.println("İdarəetmə (il)   : " + idareetmeTecurbesi);
    }
}

// ══════════════════════════════════════════════
//  MAIN
// ══════════════════════════════════════════════
public class Main {
    public static void main(String[] args) {

        try (Scanner scanner = new Scanner(System.in)) {

            // ── TƏLƏBƏ ──────────────────────────────────────────
            System.out.println("\n========== TƏLƏBƏ ==========");
            System.out.print("Ad: ");           String tAd = scanner.nextLine();
            System.out.print("Soyad: ");        String tSoyad = scanner.nextLine();
            System.out.print("Yaş: ");          int tYas = Integer.parseInt(scanner.nextLine());
            System.out.print("Fakültə: ");      String tFakulte = scanner.nextLine();
            System.out.print("Kurs (1-4): ");   int tKurs = Integer.parseInt(scanner.nextLine());

            Telebe telebe = new Telebe(tAd, tSoyad, tYas, tFakulte, tKurs);

            System.out.print("Kurs adı: ");     String kAd = scanner.nextLine();
            System.out.print("Kredit saatı: "); int kKredit = Integer.parseInt(scanner.nextLine());
            System.out.print("Müəllim: ");      String kMuellim = scanner.nextLine();
            telebe.kursElave(new Kurs(kAd, kKredit, kMuellim));

            System.out.print("İmtahan fənni: "); String iFenn = scanner.nextLine();
            System.out.print("Bal: ");           double iBal = Double.parseDouble(scanner.nextLine());
            System.out.print("Tarix: ");         String iTarix = scanner.nextLine();
            telebe.imtahanElave(new Imtahan(iFenn, iBal, iTarix));

            System.out.println("\n--- Tələbə məlumatları ---");
            telebe.melumatlariGoster();

            // ── MAGİSTR ─────────────────────────────────────────
            System.out.println("\n========== MAGİSTR ==========");
            System.out.print("Ad: ");              String mAd = scanner.nextLine();
            System.out.print("Soyad: ");           String mSoyad = scanner.nextLine();
            System.out.print("Yaş: ");             int mYas = Integer.parseInt(scanner.nextLine());
            System.out.print("Fakültə: ");         String mFakulte = scanner.nextLine();
            System.out.print("Kurs: ");            int mKurs = Integer.parseInt(scanner.nextLine());
            System.out.print("Tədqiqat mövzusu: ");String mMovzu = scanner.nextLine();
            System.out.print("Elmi rəhbər: ");     String mRehber = scanner.nextLine();

            Magistr magistr = new Magistr(mAd, mSoyad, mYas,
                    mFakulte, mKurs, mMovzu, mRehber);

            System.out.println("\n--- Magistr məlumatları ---");
            magistr.melumatlariGoster();

            // ── DOKTORANT ────────────────────────────────────────
            System.out.println("\n========== DOKTORANT ==========");
            System.out.print("Ad: ");               String dAd = scanner.nextLine();
            System.out.print("Soyad: ");            String dSoyad = scanner.nextLine();
            System.out.print("Yaş: ");              int dYas = Integer.parseInt(scanner.nextLine());
            System.out.print("Fakültə: ");          String dFakulte = scanner.nextLine();
            System.out.print("Kurs: ");             int dKurs = Integer.parseInt(scanner.nextLine());
            System.out.print("Tədqiqat mövzusu: "); String dMovzu = scanner.nextLine();
            System.out.print("Elmi rəhbər: ");      String dRehber = scanner.nextLine();
            System.out.print("Dissertasiya: ");     String dDiss = scanner.nextLine();
            System.out.print("Nəşr sayı: ");        int dNesr = Integer.parseInt(scanner.nextLine());

            Doktorant doktorant = new Doktorant(dAd, dSoyad, dYas,
                    dFakulte, dKurs, dMovzu, dRehber, dDiss, dNesr);

            System.out.print("Diplom ixtisası: ");  String dipIxt = scanner.nextLine();
            System.out.print("Diplom tarixi: ");    String dipTarix = scanner.nextLine();
            System.out.print("Diplom ortalama: ");  double dipOrt = Double.parseDouble(scanner.nextLine());
            doktorant.diplomTəyin(new Diplom(dipIxt, dipTarix, dipOrt));

            System.out.println("\n--- Doktorant məlumatları ---");
            doktorant.melumatlariGoster();

            // ── MÜƏLLİM ─────────────────────────────────────────
            System.out.println("\n========== MÜƏLLİM ==========");
            System.out.print("Ad: ");           String muAd = scanner.nextLine();
            System.out.print("Soyad: ");        String muSoyad = scanner.nextLine();
            System.out.print("Yaş: ");          int muYas = Integer.parseInt(scanner.nextLine());
            System.out.print("Fakültə: ");      String muFakulte = scanner.nextLine();
            System.out.print("Fənn: ");         String muFenn = scanner.nextLine();
            System.out.print("Təcrübə (il): "); int muTec = Integer.parseInt(scanner.nextLine());

            Muellim muellim = new Muellim(muAd, muSoyad, muYas,
                    muFakulte, muFenn, muTec);

            System.out.println("\n--- Müəllim məlumatları ---");
            muellim.melumatlariGoster();

            // ── PROFESSOR ────────────────────────────────────────
            System.out.println("\n========== PROFESSOR ==========");
            System.out.print("Ad: ");           String prAd = scanner.nextLine();
            System.out.print("Soyad: ");        String prSoyad = scanner.nextLine();
            System.out.print("Yaş: ");          int prYas = Integer.parseInt(scanner.nextLine());
            System.out.print("Fakültə: ");      String prFakulte = scanner.nextLine();
            System.out.print("Fənn: ");         String prFenn = scanner.nextLine();
            System.out.print("Təcrübə (il): "); int prTec = Integer.parseInt(scanner.nextLine());
            System.out.print("Elmi dərəcə: ");  String prDerece = scanner.nextLine();
            System.out.print("Nəşr sayı: ");    int prNesr = Integer.parseInt(scanner.nextLine());

            Professor professor = new Professor(prAd, prSoyad, prYas,
                    prFakulte, prFenn, prTec, prDerece, prNesr);

            System.out.println("\n--- Professor məlumatları ---");
            professor.melumatlariGoster();

            // ── REKTOR ───────────────────────────────────────────
            System.out.println("\n========== REKTOR ==========");
            System.out.print("Ad: ");               String rAd = scanner.nextLine();
            System.out.print("Soyad: ");            String rSoyad = scanner.nextLine();
            System.out.print("Yaş: ");              int rYas = Integer.parseInt(scanner.nextLine());
            System.out.print("Fakültə: ");          String rFakulte = scanner.nextLine();
            System.out.print("Fənn: ");             String rFenn = scanner.nextLine();
            System.out.print("Təcrübə (il): ");     int rTec = Integer.parseInt(scanner.nextLine());
            System.out.print("Elmi dərəcə: ");      String rDerece = scanner.nextLine();
            System.out.print("Nəşr sayı: ");        int rNesr = Integer.parseInt(scanner.nextLine());
            System.out.print("Universitet: ");      String rUniver = scanner.nextLine();
            System.out.print("İdarəetmə (il): ");   int rIdaree = Integer.parseInt(scanner.nextLine());

            Rektor rektor = new Rektor(rAd, rSoyad, rYas,
                    rFakulte, rFenn, rTec, rDerece, rNesr, rUniver, rIdaree);

            System.out.println("\n--- Rektor məlumatları ---");
            rektor.melumatlariGoster();
        }
    }
}