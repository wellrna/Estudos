import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.Scanner;

public class Desafio1 {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        String[] listaDesejada = {"laranja", "banana", "uva", "abacate"};
        String[] listaEfetivada = new String[4];
        int contador = 0;
        int gorjeta = 0;

        System.out.println("Informe 4 frutas que você deseja comprar: ");

        for (int i = 0; i < listaEfetivada.length; i++) {
            listaEfetivada[i] = scan.nextLine();
        }

        for (String lista : listaDesejada) {
            for (String fruta : listaEfetivada) {
                if (lista.equalsIgnoreCase(fruta)) {
                    contador += 1;
                }
            }
        }
        System.out.println("Lista de frutas desejada => " + Arrays.toString(listaDesejada));
        System.out.println("Lista de frutas compradas => " + Arrays.toString(listaEfetivada));

        double correspondencia = ((double) contador / listaDesejada.length) * 100;

        if (correspondencia >= 50 && correspondencia < 75)  gorjeta = 3;
        else if (correspondencia >= 75 && correspondencia < 90) gorjeta = 5;
        else if (correspondencia > 90) gorjeta = 10;

        System.out.println("Correspondência de " + correspondencia + "%, gorjeta de R$ " + gorjeta);

    }
}
