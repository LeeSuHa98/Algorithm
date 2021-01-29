import java.util.Scanner;

public class Sequence {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num;

        num = sc.nextInt();
        sc.close();

        System.out.println(honeyComb(num));
    }
    public static int honeyComb(int index){
        int count = 2;
        int layer = 1;

        if(index == 1){
            return 1;
        }
        
        while(index >= count){
            count += 6 * layer;
            layer++;
        }

        return layer;
    }
}
