import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Test {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String x = br.readLine();

        int bumbCount = 0;
        int defenceCount = 0;

        for(int i = 0; i < x.length(); i++){
            if(x.charAt(i) == '('){
                bumbCount++;
            }
            else if(x.charAt(i) == ')'){
                defenceCount++;
            }
        }

        if(defenceCount == bumbCount){
            System.out.println("YES");
        }
        else if(defenceCount > bumbCount || defenceCount < bumbCount){
            System.out.println("NO");
        }
    }
}
