abstract class Telebe {

    private String ad;

    public Telebe(String ad) {
        this.ad = ad;
    }

    public String getAd() {
        return ad;
    }

    public abstract void melumatGoster();
}

class MagistrTelebe extends Telebe {

    private String universitet;

    public MagistrTelebe(String ad, String universitet) {
        super(ad);
        this.universitet = universitet;
    }

    @Override
    public void melumatGoster() {
        System.out.println("Magistr tələbə: " + getAd());
        System.out.println("Universitet: " + universitet);
    }
}

class DoktorantTelebe extends Telebe {

    private String tedqiqatSahesi;

    public DoktorantTelebe(String ad, String tedqiqatSahesi) {
        super(ad);
        this.tedqiqatSahesi = tedqiqatSahesi;
    }

    @Override
    public void melumatGoster() {
        System.out.println("Doktorant: " + getAd());
        System.out.println("Tədqiqat sahəsi: " + tedqiqatSahesi);
    }
}

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Magistr tələbənin adını daxil edin: ");
        String ad = scanner.nextLine();

        System.out.print("Universiteti daxil edin: ");
        String universitet = scanner.nextLine();

        Telebe telebe = new MagistrTelebe(ad, universitet);

        telebe.melumatGoster();

        System.out.println();

        System.out.print("Doktorantın adını daxil edin: ");
        String doktorantAdi = scanner.nextLine();

        System.out.print("Tədqiqat sahəsini daxil edin: ");
        String tedqiqatSahesi = scanner.nextLine();

        Telebe doktorant = new DoktorantTelebe(doktorantAdi, tedqiqatSahesi);

        doktorant.melumatGoster();

        scanner.close();
    }
}