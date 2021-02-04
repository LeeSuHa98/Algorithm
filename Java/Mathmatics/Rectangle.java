import java.util.Scanner;

public class Rectangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x, y, w, h;

        x = sc.nextInt();
        y = sc.nextInt();
        w = sc.nextInt();
        h = sc.nextInt();

        sc.close();

        int xMin = Math.min(x, (w-x));
        int yMin = Math.min(y, (h-y));
        
        System.out.println(Math.min(xMin, yMin));
    }
}
