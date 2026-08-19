//

/////////////////////////////////////////////////////////////////
//IBprogramming dili Java'da OOP (Object-Oriented Programming) //
/////////////////////////////////////////////////////////////////
//B2.1.1 Variables //  Data types and user input


package com.example;

import java.util.Scanner;


public class Telebe {
    public String ad;
    public int yas;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Telebe telebe = new Telebe();

        System.out.println("Adınızı daxil edin: ");
        telebe.ad = sc.nextLine();

        //-------------------------------------------
        System.out.println("Yaşınızı daxil edin: ");
        telebe.yas = sc.nextInt();

        //------------------------------------------
        System.out.println("Ad: " + telebe.ad + " Yaş: " + telebe.yas);
        sc.close();
    }
}

//---------------------------------------------------


package com.example;

/import java.util.Scanner;

class Telebe {
    public String ad;
    public int yas;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Telebe telebe = new Telebe();

        System.out.println("Adı daxil edin:");
        telebe.ad = sc.nextLine();

        System.out.println("Yaşı daxil edin:");
        telebe.yas = sc.nextInt();
        telebe.yas++;

        System.out.println("Ad: " + telebe.ad);
        System.out.println("Yaş: " + telebe.yas);

        sc.close();
    }
}

//------------------------------
//double and float

package com.example;

import java.util.Scanner;

class Mehsul {
    public String ad;
    public double qiymet;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Mehsul mehsul = new Mehsul();

        // Məhsulun adını daxil edirik
        System.out.println("Məhsulun adını daxil edin:");
        mehsul.ad = sc.nextLine();

        // Məhsulun qiymətini daxil edirik (double tipində)
        System.out.println("Məhsulun qiymətini daxil edin:");
        mehsul.qiymet = sc.nextDouble();

        // Endirim faizini daxil edirik
        System.out.println("Endirim faizini daxil edin:");
        double endirimFaizi = sc.nextDouble();

        // Endirimdən sonrakı qiyməti hesablayırıq
        double sonQiymet = mehsul.qiymet - (mehsul.qiymet * endirimFaizi / 100);

        // Nəticəni çap edirik
        System.out.println("Məhsul: " + mehsul.ad);
        System.out.println("Əsas Qiymət: " + mehsul.qiymet);
        System.out.println("Endirim: " + endirimFaizi + "%");
        System.out.println("Son Qiymət: " + sonQiymet);

        sc.close();
    }
}


package com.example;

import java.util.Scanner;

class Mehsul {
    public String ad;
    public double qiymet;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Mehsul mehsul = new Mehsul();

        // Məhsulun adını daxil edirik
        System.out.println("Məhsulun adını daxil edin:");
        mehsul.ad = sc.nextLine();

        // Məhsulun qiymətini daxil edirik (double tipində)
        System.out.println("Məhsulun qiymətini daxil edin:");
        mehsul.qiymet = sc.nextDouble();

        // Endirim faizini daxil edirik
        System.out.println("Endirim faizini daxil edin:");
        double endirimFaizi = sc.nextDouble();

        // Endirimdən sonrakı qiyməti hesablayırıq
        double sonQiymet = mehsul.qiymet - (mehsul.qiymet * endirimFaizi / 100);

        // Nəticəni çap edirik
        System.out.println("Məhsul: " + mehsul.ad);
        System.out.println("Əsas Qiymət: " + mehsul.qiymet);
        System.out.println("Endirim: " + endirimFaizi + "%");
        System.out.println("Son Qiymət: " + sonQiymet);

        sc.close();
    }
}


//--------------------------------------
//Boolean-------------------------------------------------
package com.example;

import java.util.Scanner;

class Main {
    boolean eded1 =
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("1-ci ədədi daxil edin:");
        int eded1 = sc.nextInt();

        System.out.println("2-ci ədədi daxil edin:");
        int eded2 = sc.nextInt();

        boolean netice = eded1 > eded2;

        if (netice) {
            System.out.println("1-ci ədəd daha böyükdür");
        } else {
            System.out.println("2-ci ədəd daha böyük və ya bərabərdir");
        }

        sc.close();
    }
}

//--------------------------------------

package com.example;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("1-ci ədədi daxil edin:");
        int eded1 = sc.nextInt();

        System.out.println("2-ci ədədi daxil edin:");
        int eded2 = sc.nextInt();

        boolean netice = (eded1 > 0) && (eded2 > 0);

        System.out.println("Nəticə (true/false): " + netice);

        sc.close();
    }
}


//------------------------------

package com.example;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        int eded1;
        int eded2;

        Scanner sc = new Scanner(System.in);

        System.out.println("1-ci ədədi daxil edin:");
        eded1 = sc.nextInt();

        System.out.println("2-ci ədədi daxil edin:");
        eded2 = sc.nextInt();

        if (eded1 > 0 && eded2 > 0) {
            System.out.println("True: hər iki ədəd müsbətdir");
        } else {
            System.out.println("False: ən azı bir ədəd mənfi və ya sıfırdır");
        }

        sc.close();
    }
}

// Assignments --------------------------------------

public class SwapExample {
    public static void main(String[] args) {
        int a = 5;
        int b = 7;

        System.out.println("Əvvəl: a = " + a + ", b = " + b);

        // Müvəqqəti dəyişənlə dəyişmə
        int temp = a;
        a = b;
        b = temp;

        System.out.println("Sonra: a = " + a + ", b = " + b);
    }
}

package com.example;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
       int eded1 = 5;
       int eded2 = 7;

       System.out.println("Əvvəl: a = " + eded1 + ", b = " + eded2);

       int temp = eded1;
       eded1 = eded2;
       eded2 = temp;
    }
}

package com.example;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // İstifadəçidən ədədləri daxil etməsini istəyirik
        System.out.println("1-ci ədədi daxil edin:");
        int eded1 = sc.nextInt();

        System.out.println("2-ci ədədi daxil edin:");
        int eded2 = sc.nextInt();

        System.out.println("Əvvəl: a = " + eded1 + ", b = " + eded2);

        // Dəyərləri dəyişmək (swap)
        int temp = eded1;
        eded1 = eded2;
        eded2 = temp;

        // İnkremet əməliyyatı (hər birini 1 vahid artırırıq)
        eded1++;
        eded2++;

        System.out.println("Sonra (swap + increment): a = " + eded1 + ", b = " + eded2);

        sc.close();
    }
}


// Düzgün olmayan swap nümunəsi
package com.example;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
       int seh1 = 5;
       int seh2 = 7;

       System.out.println("Əvvəl: a = " + seh1 + ", b = " + seh2);


       seh1 = seh2;
       seh2 = seh1;
       System.out.println("Sonra: a = " + seh1 + ", b = " + seh2);
    }
}

