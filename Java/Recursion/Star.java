import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Star {
    static char[][] arr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        arr = new char[N][N];

        putStar(0, 0, N, false);

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                sb.append(arr[i][j]);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
    public static void putStar(int x, int y, int N, boolean blank){
        // blank일 때 공백 출력
        if(blank){
            for(int i = x; i < x + N; i++){
                for(int j = y; j < y + N; j++){
                    arr[i][j] = ' ';
                }
            }
            return;
        }

        //더이상 쪼갤 것이 없는 경우
        if(N == 1){
            arr[x][y] = '*';
            return;
        }

        int size = N / 3;
        int count = 0;

        for(int i = x; i < x + N; i += size){
            for(int j = y; j < y + N; j += size){
                count++;
                if(count == 5){
                    putStar(i, j, size, true);
                }
                else{
                    putStar(i, j, size, false);
                }
            }
        }
    }
}
