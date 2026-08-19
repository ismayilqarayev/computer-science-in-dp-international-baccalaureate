// Base class
class Telebe {

    private String ad;

    public Telebe(String ad) {
        this.ad = ad;
    }

    public String getAd() {
        return ad;
    }

    public void setAd(String ad) {
        this.ad = ad;
    }

    public void melumatGoster() {
        System.out.println("Tələbənin adı: " + ad);
    }
}

// Derived class
class MagistrTelebe extends Telebe {

    private String universitet;

    public MagistrTelebe(String ad, String universitet) {
        super(ad); // parent constructor
        this.universitet = universitet;
    }

    public String getUniversitet() {
        return universitet;
    }

    public void setUniversitet(String universitet) {
        this.universitet = universitet;
    }

    @Override
    public void melumatGoster() {
        System.out.println("Tələbənin adı: " + getAd());
        System.out.println("Universitet: " + universitet);
    }
}

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Tələbənin adını daxil edin: ");
        String ad = scanner.nextLine();

        System.out.print("Universiteti daxil edin: ");
        String universitet = scanner.nextLine();

        MagistrTelebe telebe = new MagistrTelebe(ad, universitet);

        telebe.melumatGoster();

        scanner.close();
    }
}