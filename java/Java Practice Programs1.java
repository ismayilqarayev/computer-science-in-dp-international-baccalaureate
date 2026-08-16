//-------------------------------
// Student adlı class yaradılır
class Student {

    // Tələbənin adını saxlayan dəyişən
    String name;

    // Tələbənin yaşını saxlayan dəyişən
    int age;

    // Constructor
    // Student obyekti yaradılarkən avtomatik işləyir
    Student(String name, int age) {

        // this.name -> class daxilindəki dəyişəni göstərir
        // sağdakı name isə parametrdir
        this.name = name;

        // class daxilindəki age dəyişəninə parametr kimi gələn age verilir
        this.age = age;
    }
}


// Test adlı class
// Proqramın əsas işləmə hissəsi burada olacaq
class Test {

    // static metod yaradılır
    // Bu metod Student tipli obyekti parametr kimi qəbul edir
    static void printStudent(Student s) {

        // s -> metoda göndərilən Student obyektinin referensidir

        // s.name -> obyektin name dəyişəninə müraciət
        // s.age -> obyektin age dəyişəninə müraciət
        // ekrana tələbənin adı və yaşı çıxarılır
        System.out.println(s.name + " " + s.age);
    }

    // Proqramın başladığı əsas metod
    public static void main(String[] args) {

        // Student tipli obyekt yaradılır
        // new -> yaddaşda yeni obyekt yaradır
        // constructor çağırılır və "Ravan", 12 dəyərləri verilir
        Student st = new Student("Ravan", 12);

        // printStudent metodu çağırılır
        // st obyekti metoda parametr kimi göndərilir
        // metod daxilində bu obyekt s adı ilə istifadə olunur
        printStudent(st);
    }
}