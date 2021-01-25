import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class virus {
    public static boolean[] visit;
    public static int[][] check;
    
    public static int count = 0;
    
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        //컴퓨터 수
        int N = sc.nextInt();
        //연결된 컴퓨터 수
        int K = sc.nextInt();

        check = new int[N+1][N+1];
        visit = new boolean[N+1];

        //컴퓨터간 연결
        for(int i = 1; i < K+1; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();

            check[a][b] = 1;
            check[b][a] = 1;
        }

        bfs(1);

        System.out.println(count);

        sc.close();
    }
    public static void bfs(int vertex){
        Queue<Integer> que = new LinkedList<Integer>();

        //값 리턴하기 위해 add 대신 offer 사용
        que.offer(vertex);
        visit[vertex] = true;

        while(!que.isEmpty()){
            int temp = (int) que.poll();
            
            for(int i = 1; i < check.length; i++){
                if(check[temp][i] == 1 && visit[i] == false){
                    que.offer(i);
                    visit[i] = true;
                    count++;
                }
            }
        }
    }
}
