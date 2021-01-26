import java.util.Scanner;

public class GroupWordChecker {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        // 그룹단어 세는 count
        int count = 0;
        // 입력할 단어 수
        int N = sc.nextInt();

        // 단어 수 만큼 단어 입력
        for (int i = 0; i < N; i++) {
            if (check() == true) {
                count++;
            }
        }

        System.out.println(count);
    }

    // 그룹단어인지 아닌지 체크하는 함수
    public static boolean check() {
        // 26개의 알파벳을 비교해줄 변수
        boolean[] check = new boolean[26];
        // 이전 단어 체크
        // prev가 같으면 중복검사 안함
        // prev가 다르면 중복검사
        int prev = 0;

        String str = sc.next();

        for (int i = 0; i < str.length(); i++) {
            // i번째 단어 속 문자 저장
            int now = str.charAt(i);

            // 이전 문자와 현재 문자가 같지 않다면 ? 중복검사 해야함
            if (prev != now) {
                // 처음 나오는 단어라면
                if (check[now - 'a'] == false) {
                    check[now - 'a'] = true;
                    prev = now;
                }
                // 나온 적 있으면 함수 종료
                else {
                    return false;
                }
            }
            //이전 문자와 현재 문자가 같다면 ?
            else{
                continue;
            }
        }
        return true;
    }
}
