package exam;

import java.io.*;

public class Ex2675 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            String[] temp = br.readLine().trim().split(" ");
            int r = Integer.parseInt(temp[0]);
            String s = temp[1];
            int i, j;
            for (i = 0; i < s.length(); i++) {
                for (j = 0; j < r; j++) {
                    bw.write(s.charAt(i));
                }
            }
            bw.write("\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
