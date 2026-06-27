// Student sinfi - tələbə obyektini təsvir edir
class Student {

    // Sahə (encapsulation üçün private)
    private String name;

    // Konstruktor - obyekt yaradılarkən adı təyin edir
    public Student(String name){
        this.name = name;
    }

    // Getter - name sahəsini oxumaq üçün
    public String getName(){
        return name;
    }

    // Setter - name sahəsini dəyişmək üçün
    public void setName(String name){
        this.name = name;
    }

    // toString metodu - obyekti çap etmək üçün rahat üsul
    @Override
    public String toString() {
        return "Student name: " + name;
    }
}

public class Main {

    // Student obyektini qəbul edib adını dəyişən metod
    public static void rename(Student student, String newName) {
        student.setName(newName);
    }

    public static void main(String[] args) {

        // Yeni obyekt yaradılır
        Student student1 = new Student("John");

        // Obyekti çap edirik
        System.out.println(student1);

        // Adı dəyişirik
        rename(student1, "Doe");

        // Yenilənmiş obyekti çap edirik
        System.out.println(student1);
    }
}