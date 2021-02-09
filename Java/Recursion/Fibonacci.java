import java.util.Scanner;

public class Fibonacci {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        sc.close();

        System.out.println(fibonacci(N));
    }

    public static int fibonacci(int n){
        if(n == 0){
            return 0;
        }
        else if(n == 1){
            return 1;
        }

        return n = fibonacci(n - 1) + fibonacci(n - 2);
    }
}
