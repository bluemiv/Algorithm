package Ex5;

import java.io.*;

public class Ex5622_1 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String dial = br.readLine().toUpperCase();
        String[] numbers = {"ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"};

        int sum = dial.length(); // 결과

        int i, j;
        for (i = 0; i < dial.length(); i++) {
            char temp = dial.charAt(i);
            for (j = 0; j < numbers.length; j++) {
                if (numbers[j].contains(temp + "")) {
                    sum += j + 2; // 다이얼이 2부터 시작하므로 +2를 해준다.
                    break;
                }
            }// end for
        }// end for

        // Display
        bw.write(sum + "");

        bw.flush();
        bw.close();
        br.close();
    }
}
