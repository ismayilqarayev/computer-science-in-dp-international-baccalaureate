import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.InputMismatchException;

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

    static List<Telebe> telebeler = new ArrayList<>();
    static Scanner scanner = new Scanner(System.in);

    // tələbə əlavə etmək
    public static void telebeElaveEt(){
        System.out.print("Tələbə adı daxil edin: ");
        String ad = scanner.nextLine();

        telebeler.add(new Telebe(ad));
        System.out.println("Tələbə əlavə edildi.");
    }

    // tələbələri göstərmək
    public static void telebeleriGoster(){

        if(telebeler.isEmpty()){
            System.out.println("Tələbə yoxdur.");
            return;
        }

        for(int i = 0; i < telebeler.size(); i++){
            System.out.println(i + " - " + telebeler.get(i));
        }
    }

    // ad dəyişmək
    public static void adDeyis(){
        telebeleriGoster();

        System.out.print("İndeks daxil edin: ");
        int indeks = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Yeni ad daxil edin: ");
        String yeniAd = scanner.nextLine();

        telebeler.get(indeks).setAd(yeniAd);
        System.out.println("Ad dəyişdirildi.");
    }

    // tələbə silmək
    public static void telebeSil(){
        telebeleriGoster();

        System.out.print("Silinəcək indeks: ");
        int indeks = scanner.nextInt();
        scanner.nextLine();

        telebeler.remove(indeks);
        System.out.println("Tələbə silindi.");
    }

    public static void main(String[] args) {

        while(true){

            System.out.println("\n1 - Tələbə əlavə et");
            System.out.println("2 - Tələbələri göstər");
            System.out.println("3 - Ad dəyiş");
            System.out.println("4 - Tələbə sil");
            System.out.println("0 - Çıxış");

            System.out.print("Seçim: ");
            int secim = scanner.nextInt();
            scanner.nextLine();

            switch(secim){

                case 1:
                    telebeElaveEt();
                    break;

                case 2:
                    telebeleriGoster();
                    break;

                case 3:
                    adDeyis();
                    break;

                case 4:
                    telebeSil();
                    break;

                case 0:
                    System.out.println("Proqram bitdi.");
                    return;

                default:
                    System.out.println("Yanlış seçim.");
            }
        }
    }
}