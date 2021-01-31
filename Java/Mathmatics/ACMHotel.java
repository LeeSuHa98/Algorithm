import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class ACMHotel {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int T = Integer.parseInt(st.nextToken());

        int[] arr = new int[T];
 
        for(int a = 0; a < T; a++){
            st = new StringTokenizer(br.readLine());

            int H = Integer.parseInt(st.nextToken());
		    int W = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());

            int count = 0;

            for(int i = 1; i <= W; i++){
                for(int j = 1; j <= H; j++){
                    count++;
                    if(count == N){
                        int index = j*100 + i;
                        arr[a] = index;
                       
                        break;
                    }
                }
            }
        }

        for(int i = 0; i < T; i++){
            System.err.println(arr[i]);
        }
        
    }
}
