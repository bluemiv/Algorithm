package Ex1;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Ex1065 {

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            int n = Integer.parseInt(br.readLine());
            int cnt = 0; // result

            if (n < 100) {
                // 첫째 자리, 둘째 자리
                cnt = n;
            } else if (n >= 100 & n <= 1000) {
                if (n == 1000) {
                    n = 999;
                }
                // 셋째 자리
                cnt = 99;
                int i;
                int[] num;
                for (i = 100; i <= n; i++) {
                    num = new int[]{i / 100, (i % 100) / 10, i % 10};
//					System.out.println(num[0]+","+num[1]+","+num[2]);
                    int ad = num[1] - num[0];
                    if (ad == (num[2] - num[1])) {
                        // 등차수열이다
                        cnt++;
                    }
                }// end for
            }// end if

            System.out.println(cnt);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
