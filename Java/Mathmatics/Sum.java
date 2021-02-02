import java.math.BigInteger;
import java.util.*;

public class Sum {
    public static void main(String[] args) throws IllegalStateException{
        Scanner sc = new Scanner(System.in);
        
        BigInteger a = sc.nextBigInteger();
        BigInteger b = sc.nextBigInteger();

        sc.close();
        System.out.println(a.add(b));
    }
}
