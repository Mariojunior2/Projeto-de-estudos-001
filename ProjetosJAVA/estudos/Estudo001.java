import java.util.Scanner;

public class Estudo001{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in); // O input do java mas ele precisar ser aberto e fechado
        System.err.println("Digite seu nomezinho por favor!"); // Print do JAVA
        String nome = scan.nextLine(); // O input ainda aberto identificando para ler a proxima coisa a ser escrita mas em STR claro
        System.err.println("Digite sua idade!"); // Print
        int idade = scan.nextInt(); // Aqui o input ainda está aberto e vai ler o proximo numero que for digitado

      
        System.err.printf("%s tem de idade %d", nome, idade); // Aqui esta o prin Format que coloca as variaveis fora e dentro
        // %s seria para String
        // %d seria para Int
        scan.close(); // E aqui fechamos o input
        if (idade == 10) { // if padrao
            System.err.println(", Legal!");
        } else if (idade == 18) { // elseif mas separado
            System.err.println(", Putz lhe falta emprego kk");
        } else { // else padrao
            System.err.println(", Nada legal AGORA ahahahahah!");
        }


        int[] lista = {1, 2, 3, 10, 14}; // LISTA NUMERICA
        for (int i : lista) { // PEGA CADA UM NA LISTA E COLOCA COMO SE FOSSE O i 
            System.err.println(i); // PRINT
        }

    }
}