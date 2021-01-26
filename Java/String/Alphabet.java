import java.util.Scanner;

public class Alphabet {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String N = sc.next();
        
        for(char c = 'a'; c <= 'z'; c++){
            System.out.println(N.indexOf(c)+ "");
        }

        sc.close();
    }
}
