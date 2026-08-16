// Base class  
class Student {

    private String name;

    public Student(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void showInfo() {
        System.out.println("Student name: " + name);
    }
}

// Derived class
class GraduateStudent extends Student {

    private String university;

    public GraduateStudent(String name, String university) {
        super(name); // parent constructor
        this.university = university;
    }

    public String getUniversity() {
        return university;
    }

    public void setUniversity(String university) {
        this.university = university;
    }

    @Override
    public void showInfo() {
        System.out.println("Student name: " + getName());
        System.out.println("University: " + university);
    }
}

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter student name: ");
        String name = scanner.nextLine();

        System.out.print("Enter university: ");
        String university = scanner.nextLine();

        GraduateStudent student = new GraduateStudent(name, university);

        student.showInfo();

        scanner.close();
    }
}