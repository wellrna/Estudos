package NovoProjeto;

import java.sql.SQLOutput;
import java.time.LocalDateTime;
import java.time.LocalDate;
import java.time.format.TextStyle;
import java.util.Locale;
import java.util.Random;

public class OlaMundo {

    public static void main(String[] args) {
        System.out.println("Ola Mundo");

        // Olá, {nome}, hoje é {dia-da-semana}. Bom Dia

        String nome = "Wellington";
        System.out.println(nome);
        System.out.println(nome.toUpperCase());
        System.out.println(nome.toLowerCase());
        System.out.println(nome.length());

        String nomeOutro = "Wellington";
        String nomeOutro1 = "wellington";
        System.out.println(nome.equals(nomeOutro));
        System.out.println(nome.equals(nomeOutro1));
        System.out.println(nome.equalsIgnoreCase(nomeOutro1));

        // ISO 8601 - formato da data
        LocalDate hoje = LocalDate.now();
        Locale brasil = new Locale("pt", "BR");
        // Locale brasil = new Locale("pt", "BR");
        System.out.println(hoje.getDayOfWeek().getDisplayName(TextStyle.FULL,brasil));
        String diaDaSemana = hoje.getDayOfWeek().getDisplayName(TextStyle.FULL,brasil);
        String saudacao;
        LocalDateTime agora = LocalDateTime.now();
        if (agora.getHour() >=0 && agora.getHour() < 12) {
            saudacao = "bom dia";
        } else if (agora.getHour() >=12 && agora.getHour() < 18) {
            saudacao = "boa tarde";
        } else if (agora.getHour() >=18 && agora.getHour() < 24) {
            saudacao = "boa noite";
        } else {
            saudacao = "Ola";
        }

        System.out.printf("Olá, %s. Hoje é %s, %s.%n", nome, diaDaSemana, saudacao.toUpperCase());
        System.out.printf("Ola, %s. Hoje e %s, %s.%n", nome, diaDaSemana, saudacao.toUpperCase());

        // exibir numeros de 1 a 10
        for(int i = 1; i <= 10; i++){
            for(int j = 1; j <= 10; j++){
                System.out.println(j + "*" + i + " = " +j * i);
            }
        }

        // Numeros Randomicos

        Random gerador = new Random(); // gerador é o nome que escolhi para a  varíável de geração

        // Gerar número inteiro aleatório

        int numeroInteiroAleatorio_0_a_10 = gerador.nextInt(10);
        System.out.println("Número inteiro aleatório de 0 até 10: " + numeroInteiroAleatorio_0_a_10);

        int numeroInteiroAleatorio_0_a_100 = gerador.nextInt(100);
        System.out.println("Número inteiro aleatório de 0 até 100: " + numeroInteiroAleatorio_0_a_100);

        // Gerar número reais aleatórios

        double numeroRealAleatorio_0_a_1 = gerador.nextDouble();
        System.out.println("Número real aleatório de 0 até 1: " + numeroRealAleatorio_0_a_1);

        double numeroRealAleatorio_0_a_10 = gerador.nextDouble() * 10;
        System.out.println("Número real aleatório de 0 até 10: " + numeroRealAleatorio_0_a_10);

        double numeroRealAleatorio_0_a_100 = gerador.nextDouble() * 100;
        System.out.println("Número real aleatório de 0 até 100: " + numeroRealAleatorio_0_a_100);

        // Array Java não permite misturar tipos de dados, ou só numeros int ou só numeros float ou só strings

        int[] numerosI = new int[10];
        double[] numerosR = new double[10];
        for(int i = 0; i <= 9; i++){
            numerosI[i] = gerador.nextInt(100);
            numerosR[i] = gerador.nextDouble() * 100;
        }
        for(int i = 0; i < numerosI.length; i++){
            System.out.println(numerosI[i]);
        }
        for(int i = 0; i < numerosR.length; i++){
            System.out.println(numerosR[i]);
        }

        int maiorI = numerosI[0];
        int menorI = numerosI[0];
        int mediaI = 0;
        double maiorR = numerosR[0];
        double menorR = numerosR[0];
        double mediaR = 0;

        for (int i=0; i < numerosI.length; i++) {
            if (numerosI[i] > maiorI) {
                maiorI = numerosI[i];
            }
            if (numerosI[i] < menorI) {
                menorI = numerosI[i];
            }
                mediaI += numerosI[i];
            if (numerosR[i] > maiorR) {
                maiorR = numerosR[i];
            }
            if (numerosI[i] < menorR) {
                menorR = numerosR[i];
            }
                mediaR += numerosR[i];
        }
        System.out.println("Maior Int: "+maiorI);
        System.out.println("Menor Int: "+menorI);
        System.out.println("Soma Int: "+mediaI);
        System.out.println("Média Int: "+mediaI/numerosI.length);
        System.out.println("Qtde de itens no Array Int: "+numerosI.length);
        System.out.println("Maior Real: "+maiorR);
        System.out.println("Menor Real: "+menorR);
        System.out.println("Soma Real: "+mediaR);
        System.out.println("Média Real: "+mediaR/numerosR.length);
        System.out.println("Qtde de itens no Array Real: "+numerosR.length);

        String nomeN = "Wellington na aula de Java";
        saudacao(nomeN);

        int resultadoSoma = soma(2, 3);
        System.out.println("Resultado função soma: "+resultadoSoma);
    }

    public static void saudacao(String nomeNaFuncao) {
        System.out.println("Hello, "+ nomeNaFuncao);
    }
    public static int soma(int a, int b) {
        return (a+b);
    }
}
