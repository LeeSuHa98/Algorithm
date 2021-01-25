import java.io.*;
import java.util.*;

public class Tomato {
    static int[][] tomatoBox;

    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    static int N, M;

    static class Node {
        int x;
        int y;
        int num;

        public Node(int x, int y, int num){
            this.x = x;
            this.y = y;
            this.num = num;
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        tomatoBox = new int[M][N];

        for(int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++){
                tomatoBox[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        bfs();
    }    

    static void bfs(){
        Queue<Node> que = new LinkedList<Node>();
        int num = 0;

        //토마토가 있는 위치 찾아서 que에 넣기
        for(int i = 0; i < M; i++){
            for(int j = 0; j < N; j++){
                //1이면 토마토가 있는거
                if(tomatoBox[i][j] == 1){
                    que.offer(new Node(i, j, 0));
                }
            }
        }

        while (!que.isEmpty()) {
            Node node = que.poll();
            num = node.num;

            for(int i = 0; i < 4; i++){
                int xCheck = node.x + dx[i];
                int yCheck = node.y + dy[i];

                if(xCheck >= 0 && yCheck >= 0 && xCheck < M && yCheck < N){
                    //0이면 토마토 익힘
                    if(tomatoBox[xCheck][yCheck] == 0){
                        tomatoBox[xCheck][yCheck] = 1;

                        que.add(new Node(xCheck, yCheck, num+1));
                    }
                }
            }
        }
        if(checkTomato()){
            System.out.println(num);
        }
        //토마토가 모두 익지 못했다
        else{
            System.out.println(-1);
        }
    }

    //토마토가 모두 익었는지 확인
    static boolean checkTomato() {
        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                if(tomatoBox[i][j] == 0)
                    return false;
            }
        }
 
        return true;
    }
}
