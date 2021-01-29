import java.util.Scanner;

public class BreakevenPoint {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A, B, C = 0;

        A = sc.nextInt();
        B = sc.nextInt();
        C = sc.nextInt();

        sc.close();

        if(B >= C){
            System.out.println("-1");
        }
        else{
            System.out.println(A / ( C - B) + 1);
        }
    }
}
