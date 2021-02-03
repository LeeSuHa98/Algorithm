import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class GoldBach {
    public static boolean[] prime = new boolean[100001];
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        getPrime();

        while( T --> 0 ){
            int n = Integer.parseInt(br.readLine());
            int first = n / 2;
            int second = n / 2;

            while(true){
                if(!prime[first] && !prime[second]){
                    sb.append(first).append(" ").append(second);
                    break;
                }
                first--;
                second++;
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

    public static void getPrime(){
        prime[0] = prime[1] = true;

        for(int i = 2; i < Math.sqrt(prime.length); i++){
            if(prime[i])
                continue;
            for(int j = i*i; j < prime.length; j += i){
                prime[j] = true;
            }
        }
    }
}
