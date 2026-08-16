
// Student sinfi: bir tələbə obyekti üçün sahələr və metodlar
class Student {
    private String ad;  // ad sahəsi private, birbaşa xaricdən giriş yoxdur (inkapsulyasiya)

    // Konstruktor: yeni Student obyekti yaratmaq üçün istifadə olunur
    Student(String ad) {
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
    static void adDeyis(Student s, String yeniAd) {
        s.setAd(yeniAd);  // student obyektinin ad sahəsini dəyişdiririk
    }

    public static void main(String[] args) {
        // Yeni Student obyekti yaradılır
        Student s1 = new Student("Ravan");  
        System.out.println("Əvvəl: " + s1.getAd()); // Getter vasitəsilə adı ekrana çıxarır

        // Metod vasitəsilə obyektin adını dəyişdiririk
        adDeyis(s1, "Ismayil");  
        System.out.println("Sonra: " + s1.getAd()); // Yenilənmiş ad ekrana çıxarılır
    }
}