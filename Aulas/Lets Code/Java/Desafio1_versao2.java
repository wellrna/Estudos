Desafio 1 + Sugestão
```java
import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.Scanner;

public class Desafio2 {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00##");
        DecimalFormat df2 = new DecimalFormat("0.##");

        String[] listaDesejada = {"laranja", "banana", "uva", "abacate" };
        String[] listaEfetivada = new String[4];
        int contador = 0;
        double gorjeta = 0.0;
        double preco = 0;

        System.out.println("Frutas no estoque: laranja, banana, uva, abacate, maca, melao, ameixa, morango e limao.");
        System.out.println("Informe as quatro frutas escolhidas para compra: ");

        for (int i = 0; i < listaEfetivada.length; i++) {
            listaEfetivada[i] = scan.nextLine();
            if (listaEfetivada[i].equalsIgnoreCase("abacate")) preco += 2;
            else if (listaEfetivada[i].equalsIgnoreCase("uva")) preco += 7.7;
            else if (listaEfetivada[i].equalsIgnoreCase("banana")) preco += 2.2;
            else if (listaEfetivada[i].equalsIgnoreCase("laranja")) preco += 3.3;
            else if (listaEfetivada[i].equalsIgnoreCase("maca")) preco += 4;
            else if (listaEfetivada[i].equalsIgnoreCase("limao")) preco += 1.5;
            else if (listaEfetivada[i].equalsIgnoreCase("ameixa")) preco += 6.2;
            else if (listaEfetivada[i].equalsIgnoreCase("morango")) preco += 5.2;
            else if (listaEfetivada[i].equalsIgnoreCase("melao")) preco += 2.7;
        }

        for (String lista : listaDesejada) {
            for (String fruta : listaEfetivada) {
                if (lista.equalsIgnoreCase(fruta)) {
                    contador += 1;
                }
            }
        }

        double correspondencia = ((double) contador / listaDesejada.length) * 100;
        if (correspondencia >= 50 && correspondencia < 75) gorjeta = 3;
        else if (correspondencia >= 75 && correspondencia < 90) gorjeta = 5;
        else if (correspondencia > 90) gorjeta = 10;

        System.out.println("Lista de frutas desejada => " + Arrays.toString(listaDesejada));
        System.out.println("Lista de frutas compradas => " + Arrays.toString(listaEfetivada));
        System.out.println("Correspondência de " + df2.format(correspondencia) + "%, gorjeta de R$ " + df.format(gorjeta));
        System.out.println("Valor total de sua compra (incluindo a gorjeta): R$" + df.format(preco + gorjeta));

    }
}

========================================= Novas Sugestões

public class Desafio2 {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00##");
        DecimalFormat df2 = new DecimalFormat("0.##");

        String[] listaDesejada = {"laranja", "banana", "uva", "abacate" };
        String[] nomeFrutasEstoque = {"abacate", "uva", "banana", "laranja", "maca", "limao", "ameixa", "morango", "melao", "pera"};
        Double[] precoFrutasEstoque = {2.0, 7.7, 2.2, 3.3, 4.9, 1.5, 6.2, 5.2, 2.7, 1.2};
       
        int contador = 0; double gorjeta = 0.0; double preco = 0;

        System.out.println("A feira tem as seguintes frutas no estoque: " + Arrays.toString(nomeFrutasEstoque));
        System.out.println("Quantas frutas deseja comprar? ");
        int quantidadeFrutas = scan.nextInt();       
        String[] listaCompras = new String[(quantidadeFrutas + 1)];        
        System.out.println("Informe quais frutas deseja comprar: ");

        for (int i = 0; i < listaCompras.length; i++){
            listaCompras[i] = scan.nextLine();
            for (int j = 0; j < nomeFrutasEstoque.length; j++) {                    
                if  (listaCompras[i].equalsIgnoreCase(nomeFrutasEstoque[j])) preco += precoFrutasEstoque[j];                        
            }
        }        

        for (String lista : listaDesejada) {
            for (String fruta : listaCompras) {
                if (lista.equalsIgnoreCase(fruta)) contador += 1;                
            }
        }

        double correspondencia = ((double) contador / listaDesejada.length) * 100;
        if (correspondencia >= 50 && correspondencia < 75) gorjeta = 3;
        else if (correspondencia >= 75 && correspondencia < 90) gorjeta = 5;
        else if (correspondencia > 90) gorjeta = 10;       
    
        System.out.println("Valor total de sua compra (incluindo a gorjeta): R$" + df.format(preco + gorjeta));
    }
}