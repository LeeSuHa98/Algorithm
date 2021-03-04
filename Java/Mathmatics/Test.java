import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;


public class Test {
    // public static boolean visit;
    // public static char[][] check;

    // public static void main(String[] args) throws IOException{
    //     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    //     StringBuilder sb = new StringBuilder();
    //     StringTokenizer st = new StringTokenizer(br.readLine()," ");

    //     String K = st.nextToken();
    //     int N = Integer.parseInt(br.readLine());

    //     check = new char[N][N];

    //     for(int i = 1; i < N+1; i++){
    //         st = new StringTokenizer(br.readLine());

    //         String a = st.nextToken();
    //         String b = st.nextToken();

    //         check[i][b] = 
    //     }
    // }
    public static void main(String[] args) throws IOException {
 
		Scanner sc = new Scanner(System.in);
        int n= sc.nextInt();
        

        int[] arr = new int[n];
        for (int i = 0; i <n ; i++) {
            arr[i] = sc.nextInt();
        }

        int max = 0;
        Arrays.sort(arr);

        int left =1;
        int right =arr[n-1];
        long height =0;
        int mid =0;
        int ans=0;

        int result = 0;
        while(left <= right){

            height =0;
            mid =(left+right)/2;

            for (int i = 0; i <n ; i++) {
                if(arr[i]>=mid) {
                    result += arr[i];
                }
            }
            
            if(right < left){

                left = mid + 1;
            }else {
                right = mid-1;

            }
        }
        System.out.println(result);
    }
}
