import java.util.Scanner;

public class FindPrimeNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int M = sc.nextInt();
        int N = sc.nextInt();

        for(int i = M; i <= N; i++){
            if(getPrime(i)){
                System.out.println(i);
            }
        }

        sc.close();
    }

    public static boolean getPrime(int num){
        if(num < 2){
            return false;
        }
        for(int i=2; i*i<=num; i++){
            if(num % i == 0) return false;
        }
        return true;
    }
}
