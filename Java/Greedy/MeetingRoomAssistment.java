import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class MeetingRoomAssistment {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[][] meetingSchedule = new int[N][2];

        for(int i = 0; i < N; i++){
            meetingSchedule[i][0] = sc.nextInt();
            meetingSchedule[i][1] = sc.nextInt();
        }

        Arrays.sort(meetingSchedule, new Comparator<int[]>() {
			
			@Override
			public int compare(int[] o1, int[] o2) {
				
				// 종료시간이 같을 경우 시작시간이 빠른순으로 정렬해야한다.  
				if(o1[1] == o2[1]) {
					return o1[0] - o2[0];
				}
				
				return o1[1] - o2[1];
			}
        });

        //이전 
        int preEndTime = 0;
        int count = 0;

        for(int i = 0; i < N; i++) {
            if(preEndTime <= meetingSchedule[i][0]){
                preEndTime = meetingSchedule[i][1];
                count++;
            }
        }
    
        System.out.println(count);
    }
}
