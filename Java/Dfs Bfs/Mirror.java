import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Mirror {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    public static int row;
    public static int col;

    static int[] xArr = {0, 1, 0, -1};
    static int[] yArr = {-1, 0, 1, 0};

    public static int mirror[][];
    public static boolean visit[][];

    public static void main(String[] args) throws IOException{
        StringTokenizer st = new StringTokenizer(br.readLine());

        row = Integer.parseInt(st.nextToken());
        col = Integer.parseInt(st.nextToken());

        mirror = new int[100][100];
        visit = new boolean[100][100];

        for(int i = 0; i < row; i++){
            st = new StringTokenizer(br.readLine());
            String temp = st.nextToken();
            
            for(int j = 0; j < col; j++){
                mirror[i][j] = temp.charAt(j) - '0';
            }
        }

        //0,0에서 시작
        bfs(0, 0);
        System.out.println(mirror[row - 1][col - 1]);
    }

    public static void bfs(int x, int y){
        // 시작좌표 (x,y)
        // bfs는 Queue 사용
        // x 값 저장소 xQueue, y 값 저장소 yQueue
        Queue<Integer> xQueue = new LinkedList<Integer>();
        Queue<Integer> yQueue = new LinkedList<Integer>();

        // x,y 값 각각 Queue에 add
        xQueue.add(x);
        yQueue.add(y);

        // xQueue, yQueue 가 모두 빌 때 까지 반복
        while(!xQueue.isEmpty() && !yQueue.isEmpty()){
            // xQueue, yQueue 값 빼기 (FIFO)
            x = xQueue.poll();
            y = yQueue.poll();

            // 방문한 x,y는 true 로 변경
            visit[x][y] = true;

            // 동서남북 4번 확인
            for(int i = 0; i < 4; i++){
                int xCheck = x + xArr[i];
                int yCheck = y + yArr[i];

                if(xCheck >= 0 && yCheck >= 0 & xCheck < row && yCheck < col){
                    if(mirror[xCheck][yCheck] == 1 && visit[xCheck][yCheck] == false){
                        xQueue.add(xCheck);
                        yQueue.add(yCheck);

                        visit[xCheck][yCheck] = true;
                        mirror[xCheck][yCheck] = mirror[x][y] +1;
                    }
                }
            }
        }
    }
}
