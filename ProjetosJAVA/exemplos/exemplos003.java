import java.util.Scanner;

public class exemplos003 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.err.println(" Me diga um valor! ");
        int v1 = scan.nextInt();
        System.err.println(" Me diga outro valor! ");
        int v2 = scan.nextInt();
        System.err.printf(" %d + %d = %d \n", v1, v2, v1 + v2);
        System.err.printf(" %d - %d = %d \n", v1, v2, v1 + v2);
        System.err.printf(" %d x %d = %d \n", v1, v2, v1 * v2);
        System.err.printf(" %d / %d = %d \n", v1, v2, v1 / v2);
        System.out.print("Raiz de " +  v1 + " = " + Math.sqrt(v1) + "\n");
        if ( v1 != v2) {
            System.out.print("Raiz de " + v2 + " = " + Math.sqrt(v2) + "\n");
        }

        System.out.print("A Tabuada do: " + v1 + "\n");
        for (int i = 0; i <= 10; i++) {
            System.out.print(" " + v1 + " x " + i + " = " + v1 * i + "\n");
        }

        if (v1 != v2) {
            System.out.print("A Tabuada do " + v2 + "\n");
            for (int i = 0; i <= 10; i++) {
                System.out.print(" " + v2 + " x " + i + " = " + v2 * i + "\n");
            }
        }


        scan.close();
    }
}
