package exam;

import java.io.*;

public class Ex10039 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int sum = 0, temp = 0;
        int i;
        for (i = 0; i < 5; i++) {
            temp = Integer.parseInt(br.readLine());
            if (temp < 40) temp = 40;
            sum += temp;
        }
        bw.write(sum / 5 + "");

        bw.flush();
        br.close();
        bw.close();
    }
}
