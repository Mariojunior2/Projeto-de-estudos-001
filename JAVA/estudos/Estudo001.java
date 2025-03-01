import java.util.Scanner;

public class Estudo001{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.err.println("Digite seu nomezinho por favor!");
        String nome = scan.nextLine();
        System.err.println("Digite sua idade!");
        int idade = scan.nextInt();

      
        System.err.printf("%s tem de idade %d ", nome, idade);
        scan.close();
        if (idade == 10) {
            System.err.println(", Legal!");
        } else {
            System.err.println(", Nada legal AGORA ahahahahah!");
        }


        int[] lista = {1, 2, 3, 10, 14}; // LISTA NUMERICA
        for (int i : lista) { // PEGA CADA UM NA LISTA E COLOCA COMO SE FOSSE O i 
            System.err.println(i); // PRINT
        }

    }
}