import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class ApartmentNumbering {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    static int N;
    //단지 내 집의 수
    static int number;

    static int[] xArr = {0, 1, 0, -1};
    static int[] yArr = {-1, 0, 1, 0};

    static int apart[][] = new int[25][25];
    static boolean visit[][] = new boolean[25][25];

    //총 단지 수
    static ArrayList array = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        apart = new int[N][N];
        visit = new boolean[N][N];

        //단지 입력
        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            String temp = st.nextToken();

            for(int j = 0; j < N; j++){
                apart[i][j] = temp.charAt(j) - '0';
            }
        }

        //인접 단지 찾기 
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(apart[i][j] == 1 && visit[i][j] == false){
                    number = 1;
                    dfs(i,j);
                    array.add(number);
                }
            }
        }

        //단지 오름차순 정렬
        Collections.sort(array);

        //총 단지 개수
        System.out.println(array.size());

        //각각 단지 내 총 단지 개수 출력
        for(int i = 0; i < array.size(); i++){
            System.out.println(array.get(i)); 
        }
    }
    
    static int dfs(int x, int y){
        visit[x][y] = true;

        for(int i = 0; i < 4; i++){
            int xCheck = x + xArr[i];
            int yCheck = y + yArr[i];

            if(xCheck >= 0 && yCheck >= 0 & xCheck < N && yCheck < N){
                if(apart[xCheck][yCheck] == 1 && visit[xCheck][yCheck] == false){
                    dfs(xCheck, yCheck);
                    number++;
                }
            }
        }
        return number;
    }
}
