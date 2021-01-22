import java.util.Scanner;

public class Change {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = 1000 - N;

        int num = 0;
        int[] coin = {500, 100, 50, 10, 5, 1};

        for(int i = 0; i < coin.length; i++){
            if( K / coin[i] > 0){
                num += K / coin[i];
                K = K % coin[i];
            }
        }

        System.out.println(num);
    }
}
