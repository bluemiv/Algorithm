package Ex1;

import java.io.*;

public class Ex10989 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[] numbers = new int[10001];

        int i;
        for (i = 0; i < n; i++) {
            numbers[Integer.parseInt(br.readLine())]++;
        }

        int j;
        for (i = 1; i <= 10000; i++) {
            int cnt = numbers[i];
            if (cnt != 0) {

                for (j = 0; j < cnt; j++) {
                    bw.write(i + "\n");
                }// end for
            }// end if
        }// end for

        bw.flush();
        bw.close();
        br.close();
    }
}
