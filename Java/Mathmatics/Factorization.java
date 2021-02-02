import java.io.*;

public class Factorization {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        for(int i = 2; i <= N; i++){
            while(N%i == 0){
                N /= i;
                sb.append(i).append("\n");
            }
        }

        System.out.println(sb);
    }
}
