
// Telebe sinfi: bir tələbə obyekti üçün sahələr və metodlar
class Telebe {
    private String ad;  // ad sahəsi private, birbaşa xaricdən giriş yoxdur (inkapsulyasiya)

    // Konstruktor: yeni Telebe obyekti yaratmaq üçün istifadə olunur
    Telebe(String ad) {
        this.ad = ad;  // sahəni konstruktor parametri ilə doldururuq
    }

    // Getter metodu: ad sahəsini oxumaq üçün
    public String getAd(){
        return ad;
    }

    // Setter metodu: ad sahəsini dəyişmək üçün
    public void setAd(String ad){
        this.ad = ad;
    }
}

public class Main {
    // Metod obyekt qəbul edir və obyektin ad sahəsini dəyişdirir
    static void adDeyis(Telebe t, String yeniAd) {
        t.setAd(yeniAd);  // telebe obyektinin ad sahəsini dəyişdiririk
    }

    public static void main(String[] args) {
        // Yeni Telebe obyekti yaradılır
        Telebe telebe1 = new Telebe("Ravan");
        System.out.println("Əvvəl: " + telebe1.getAd()); // Getter vasitəsilə adı ekrana çıxarır

        // Metod vasitəsilə obyektin adını dəyişdiririk
        adDeyis(telebe1, "Ismayil");
        System.out.println("Sonra: " + telebe1.getAd()); // Yenilənmiş ad ekrana çıxarılır
    }
}