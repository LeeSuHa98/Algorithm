import java.util.Scanner;

public class Sum {

	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        String temp = sc.next();
        int sum = 0;

        for(int i = 0; i < N; i++){
            int a = temp.charAt(i) - '0';
            sum = sum + a;
        }

        System.out.println(sum);
        
        sc.close();
    }
}
