import java.util.Scanner;


public class Word {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String N = sc.next().toLowerCase();
        
        int[] alphabet = new int[26];

        for(int i = 0; i < N.length(); i++){
            int count = N.charAt(i) - 'a';
            alphabet[count]++;
        }

        int max = -1;
        char c = '?';

        for(int i = 0; i < alphabet.length; i++){
            if(max < alphabet[i]){
                max = alphabet[i];
                c = (char) (i + 65);
            }
            else if(max == alphabet[i]){
                c = '?';
            }
        }
        
        System.out.println(c);

        sc.close();
    }
}
