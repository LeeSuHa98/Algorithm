import java.util.Scanner;

public class PrimeNumberSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int M = sc.nextInt();
        int N = sc.nextInt();
        sc.close();
        
        int sum = 0;
        int min = 10001;

        for(int i = M;  i <= N; i++){
            if(getPrime(i)){
                if(sum == 0){
                    min = i;
                }
                sum += i;
            }
        }

        if(min == 10001){
            System.out.println("-1");
        }
        else{
            System.out.println(sum);
            System.out.println(min);
        }   
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
