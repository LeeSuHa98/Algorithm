import java.util.*;

public class ForthPoint {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int A = sc.nextInt();
        int b = sc.nextInt();
        int B = sc.nextInt();
        int c = sc.nextInt();
        int C = sc.nextInt();

        sc.close();
        
        int x, y;

        if(a == b){
            x = c;
        }
        else if(a == c){
            x = b;
        }
        else{
            x = a;
        }

        if(A == B){
            y = C;
        }
        else if(A == C){
            y = B;
        }
        else{
            y = A;
        }

        System.out.println(x + " " + y);
    }
}
