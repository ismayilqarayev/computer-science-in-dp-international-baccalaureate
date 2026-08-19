//-------------------------------
// Telebe adlı class yaradılır
class Telebe {

    // Tələbənin adını saxlayan dəyişən
    String ad;

    // Tələbənin yaşını saxlayan dəyişən
    int yas;

    // Constructor
    // Telebe obyekti yaradılarkən avtomatik işləyir
    Telebe(String ad, int yas) {

        // this.ad -> class daxilindəki dəyişəni göstərir
        // sağdakı ad isə parametrdir
        this.ad = ad;

        // class daxilindəki yas dəyişəninə parametr kimi gələn yas verilir
        this.yas = yas;
    }
}


// Test adlı class
// Proqramın əsas işləmə hissəsi burada olacaq
class Test {

    // static metod yaradılır
    // Bu metod Telebe tipli obyekti parametr kimi qəbul edir
    static void telebeGoster(Telebe t) {

        // t -> metoda göndərilən Telebe obyektinin referensidir

        // t.ad -> obyektin ad dəyişəninə müraciət
        // t.yas -> obyektin yas dəyişəninə müraciət
        // ekrana tələbənin adı və yaşı çıxarılır
        System.out.println(t.ad + " " + t.yas);
    }

    // Proqramın başladığı əsas metod
    public static void main(String[] args) {

        // Telebe tipli obyekt yaradılır
        // new -> yaddaşda yeni obyekt yaradır
        // constructor çağırılır və "Ravan", 12 dəyərləri verilir
        Telebe telebe = new Telebe("Ravan", 12);

        // telebeGoster metodu çağırılır
        // telebe obyekti metoda parametr kimi göndərilir
        // metod daxilində bu obyekt t adı ilə istifadə olunur
        telebeGoster(telebe);
    }
}