import java.util.Scanner;

public class Fraction {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        sc.close();
        
        int count = 1;
        int layer = 2;

        //분자
        int numerator = 1;
        //분모
        int denominator = 1;

        while(count < N){
            count += layer;
            layer++;
        }

        layer--;

        //층이 짝수일 때
        if(layer % 2 == 0){
            numerator = layer;
            denominator = 1;
            while(count != N){
                count--;
                numerator--;
                denominator++;
            }
        }
        //층이 홀수일 때
        else if(layer % 2 == 1){
            numerator = 1;
            denominator = layer;
            while(count != N){
                count--;
                numerator++;
                denominator--;
            }
        }
        
        System.out.println(numerator + "/" + denominator);
    }
}
