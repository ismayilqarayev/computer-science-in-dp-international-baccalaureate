import java.util.Scanner;

public class App {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Bir ədəd daxil edin: ");
        int eded = scanner.nextInt();
        int cem = 0;
        int muveqqeti = eded;

        while (muveqqeti != 0) {
            int reqem = muveqqeti % 10;
            cem += reqem;
            muveqqeti /= 10;
        }

        System.out.println(eded + " ədədinin rəqəmlərinin cəmi: " + cem);
        scanner.close();
    }
}
