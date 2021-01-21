import java.util.Scanner;
import java.util.Arrays;

public class ATM {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] array = new int[N];

        for(int i = 0; i < array.length; i++){
            array[i] = sc.nextInt();
        }
    
        Arrays.sort(array);

        int pre = 0;
        int sum = 0;
        for (int i = 0; i < array.length; i++) {
            pre += array[i];
            sum += pre;
        }

        System.out.println(sum);
    }
}
