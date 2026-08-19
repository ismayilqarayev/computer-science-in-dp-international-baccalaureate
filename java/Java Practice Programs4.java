class Telebe {

    private String ad;

    public Telebe(String ad){
        this.ad = ad;
    }

    public String getAd(){
        return ad;
    }

    public void setAd(String ad){
        this.ad = ad;
    }

    @Override
    public String toString(){
        return ad;
    }
}

public class Main {
    public static void adiDeyis(Telebe telebe, String yeniAd){
        telebe.setAd(yeniAd);
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Tələbənin adını daxil edin: ");
        String telebeAdi = scanner.nextLine();

        Telebe telebe = new Telebe(telebeAdi);
        System.out.println("Hazırkı ad: " + telebe);

        System.out.print("Tələbənin yeni adını daxil edin: ");
        String yeniAd = scanner.nextLine();

        adiDeyis(telebe, yeniAd);
        System.out.println("Yeni ad: " + telebe);
    }
}