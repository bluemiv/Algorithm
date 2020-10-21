package Ex1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ex1035 {
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int decimal = Integer.parseInt(br.readLine(), 16); // 10진수로 변환
        System.out.printf("%o", decimal);
    }
}