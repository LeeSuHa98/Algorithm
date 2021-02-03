import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BertPrime {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while(true){
            int n = Integer.parseInt(br.readLine());
            int count = 0;

            if(n == 0){
                break;
            }
            for(int i = n + 1; i <= 2*n; i++){
                if(getPrime(i)){
                    count++;
                }
            }

            sb.append(count).append("\n");
        }

        System.out.println(sb);
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
