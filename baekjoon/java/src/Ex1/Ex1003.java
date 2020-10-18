package Ex1;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Ex1003 {
    // 피보나치 함수
    private static int[] dp;

    private static int fibonacci(int n) {
        if (n <= 1) {
            dp[n] = n;
            return n;
        }

        if (dp[n] > 0) {
            return dp[n];
        }

        return dp[n] = fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {
//		double startTime = System.currentTimeMillis();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            int testCase = Integer.parseInt(br.readLine());
            while (testCase-- > 0) {
                int n = Integer.parseInt(br.readLine());
                if (n == 0) {
                    System.out.println("1 0");
                } else if (n == 1) {
                    System.out.println("0 1");
                } else {
                    dp = new int[n + 1];
                    fibonacci(n);
                    System.out.println(dp[n - 1] + " " + dp[n]);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
//			double endTime = System.currentTimeMillis();
//			System.out.println(endTime - startTime);
        }
    }

}
