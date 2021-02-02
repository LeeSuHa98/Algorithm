import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class AlphaCentauri {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for(int i = 0; i < T; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            int distance = y - x;
            //double형이기 때문에 int로 자료형 변환
            int max = (int)Math.sqrt(distance);

            //max가 distance의 제곱이면
            if(max == Math.sqrt(distance)){
                sb.append(max * 2 -1).append("\n");
            }
            //max*max < distance <= max*max+max
            else if(distance <= max * max + max){
                sb.append(max * 2).append("\n");
            }
            else{
                sb.append(max * 2 + 1).append("\n");
            }
        }
        System.out.println(sb);
    }
}
