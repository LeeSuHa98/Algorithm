import java.util.Scanner;

public class SugarDeliveryService {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("배달해야할 물건의 무게는 ? ");
        int N = sc.nextInt();

        int quotient_5 = N / 5;
        int quotient_3 = 0;
        
        int remainder_5 = N % 5;

        while(quotient_5 >= 0){
            if(remainder_5 % 3 == 0){
                quotient_3 = remainder_5 / 3;
                remainder_5 = remainder_5 % 3;
                break;
            }

            remainder_5 = remainder_5 + 5;
            quotient_5 = quotient_5 - 1;
        }

        if(remainder_5 < 0){
            System.out.println("-1");
        }

        System.out.println(quotient_5 + quotient_3); 
    }
}
