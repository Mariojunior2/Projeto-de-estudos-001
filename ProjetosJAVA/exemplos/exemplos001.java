public class exemplos001 {
    public static void main(String[] args) {
        // VALORES! 
        String name = "Joao"; // string seria para palavras ou textos
        int valor = 15; // seria o int para um valor inteiro
        valor = 20; // aqui acontece uma transformacao do valor 15 para 20
        // caso nao queria que o valor mude tem que colocar final
        final int casaV = 15;
        // casaV = 20;  Aqui daria erro


        // Resumidamente seria assim

        int myNum = 5; // para valores inteiros
        float myNumq = 14.55f; // para valores quebrados sempre coloque o f para o java identificar
        char myLetter = 'M'; // para um unico charactere
        boolean myVouF = true; // para um valor verdadeiro ou falso
        String name2 = "Mario"; // para palavras ou frases e etc...

        // para juntar frases

        String nome = "John";
        System.out.println("Hello " + nome);


        // para variables de str

        String firstName = "John ";
        String lastName = "Doe";
        String fullName = firstName + lastName;
        System.out.println(fullName);


        // para somar 

        int x = 5;
        int y = 6;
        System.out.println(x + y); 


        // outra forma

        int a = 5, b = 6, c = 50;
        System.out.println(a + b + c);
    }
}
