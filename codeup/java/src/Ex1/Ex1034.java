package Ex1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ex1034 {
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long num = Long.parseLong(br.readLine());

        int sum = 0; // 결과값
        int k = 0; // 자리수
        while (num != 0) {
            // 8의 제곱수를 곱한다. (8^0, 8^1, ....)
            sum += (num % 10) * Math.pow(8, k);

            // 자리수를 증가 시킨다.
            k++;
            num /= 10;
        }
        System.out.println(sum);
    }
}
