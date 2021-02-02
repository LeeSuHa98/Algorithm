import java.util.*;

public class PrimeNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int count = 0;

        for(int i = 0; i < N; i++){
            int num = sc.nextInt();
            if(getPrime(num)){
                count++;
            }
        }

        sc.close();
        System.out.println(count);
    }

    public static boolean getPrime(int num){
        if(num < 2){
            return false;
        }
        for(int i=2; i*i<=num; i++){
            if(num % i == 0) 
                return false;
        }
        return true;
    }
}
