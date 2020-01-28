package exam;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Ex4344 {

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            // 테스트 케이스
            int t = Integer.parseInt(br.readLine());

            int n; // 학생 수
            int sum; // 총 합
            int[] score;
            double avg; // 반 평균
            while (t-- > 0) {
                String[] input = br.readLine().trim().split(" ");
                n = Integer.parseInt(input[0]);
                score = new int[n];

                int i;
                sum = 0;
                for (i = 1; i < n + 1; i++) {
                    score[i - 1] = Integer.parseInt(input[i]);
                    sum += score[i - 1];
                }
//				System.out.println("sum:"+sum);
                avg = (double) sum / n;
//				System.out.println("avg:"+avg);
                // 반평균을 넘는 학생의 비율 구하기
                int cnt = 0;
                for (i = 0; i < n; i++) {
                    if (score[i] > avg) {
//						System.out.print(score[i]);
                        cnt++;
                    }
                }

                System.out.printf("%.3f%%\n", ((double) cnt / n) * 100);
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }
    }
}
