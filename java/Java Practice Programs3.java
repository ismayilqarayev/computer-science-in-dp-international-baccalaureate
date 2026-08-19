// Telebe sinfi - tələbə obyektini təsvir edir
class Telebe {

    // Sahə (encapsulation üçün private)
    private String ad;

    // Konstruktor - obyekt yaradılarkən adı təyin edir
    public Telebe(String ad){
        this.ad = ad;
    }

    // Getter - ad sahəsini oxumaq üçün
    public String getAd(){
        return ad;
    }

    // Setter - ad sahəsini dəyişmək üçün
    public void setAd(String ad){
        this.ad = ad;
    }

    // toString metodu - obyekti çap etmək üçün rahat üsul
    @Override
    public String toString() {
        return "Tələbənin adı: " + ad;
    }
}

public class Main {

    // Telebe obyektini qəbul edib adını dəyişən metod
    public static void adiDeyis(Telebe telebe, String yeniAd) {
        telebe.setAd(yeniAd);
    }

    public static void main(String[] args) {

        // Yeni obyekt yaradılır
        Telebe telebe1 = new Telebe("Cavid");

        // Obyekti çap edirik
        System.out.println(telebe1);

        // Adı dəyişirik
        adiDeyis(telebe1, "Elvin");

        // Yenilənmiş obyekti çap edirik
        System.out.println(telebe1);
    }
}