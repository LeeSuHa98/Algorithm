import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class DfsBfs {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    //방문 기록
    public static boolean[] visit;
    // 정점의 번호
    public static int[][] check;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception{
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());

        // 정점의 개수
        int N = Integer.parseInt(stringTokenizer.nextToken());
        // 간선의 개수
        int M = Integer.parseInt(stringTokenizer.nextToken());
        // 첫 정점의 번호
        int V = Integer.parseInt(stringTokenizer.nextToken());

        check = new int[N + 1][N + 1];
        
        // 정점들간의 연결
        for (int i = 1; i < M+1; i++) {
            stringTokenizer = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(stringTokenizer.nextToken());
            int b = Integer.parseInt(stringTokenizer.nextToken());

            check[a][b] = 1;
            check[b][a] = 1;
        }

        visit = new boolean[N+1];
        dfs(V);

        sb.append("\n");

        visit = new boolean[N+1];
        bfs(V);

        System.out.println(sb);

        br.close();
    }

    public static void dfs(int vertex) {
        visit[vertex] = true;
        sb.append(vertex + " ");

        if(vertex == check.length){
            return;
        }
        for(int i = 1; i < check.length; i++){
            if(check[vertex][i] == 1 && visit[i] == false){
                dfs(i);
            }
        }
    }

    public static void bfs(int vertex){
        Queue que = new LinkedList<Integer>();

        que.add(vertex);
        visit[vertex] = true;

        while(!que.isEmpty()){
            int temp = (int) que.peek();
            int num = (int) que.poll();

            sb.append(num + " ");
            
            for(int i = 1; i < check.length; i++){
                if(check[temp][i] == 1 && visit[i] == false){
                    que.add(i);
                    visit[i] = true;
                }
            }
        }
        sb.append("\n");
    }
}
