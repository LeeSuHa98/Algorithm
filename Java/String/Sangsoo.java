import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Sangsoo {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int numA = Integer.parseInt(st.nextToken());
        int numB = Integer.parseInt(st.nextToken());

        int A = backwards(numA);
        int B = backwards(numB);

        if(A > B){
            System.out.println(A);
        }
        else{
            System.out.println(B);
        }
    }
    public static int backwards(int num){
        int result = 0;

        while(num != 0){
            result = result*10 + num%10;
            num /= 10;
        }

        return result;
    }
}
