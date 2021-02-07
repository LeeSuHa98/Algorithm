import java.util.*;
import java.io.*;

public class Pythagoras {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while(true){
            StringTokenizer st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if(a == 0 && b == 0 && c == 0){
                break;
            }

           int numA = a*a;
           int numB = b*b;
           int numC = c*c;

            if(numA + numB == numC || numA + numC == numB || numB + numC == numA){
                sb.append("right").append("\n");
            }
            else{
                sb.append("wrong").append("\n");
            }
        }

        System.out.println(sb);
    }
}
