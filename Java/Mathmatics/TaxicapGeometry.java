import java.util.Scanner;

public class TaxicapGeometry {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double R = sc.nextDouble();

        sc.close();

        //유클리드 기하학 pi*R^2
        double uclid = R*R*Math.PI;
        //택시 기하학 2*R^2
        double taxicap = R*R*2;

        System.out.println(uclid);
        System.out.println(taxicap);
    }
}