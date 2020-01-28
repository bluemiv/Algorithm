package exam;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Ex8958 {

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int t = Integer.parseInt(br.readLine());
            while (t-- > 0) {
                String input = br.readLine();
                int cnt = 0, sum = 0;
                int i;
                for (i = 0; i < input.length(); i++) {
                    if (input.charAt(i) == 'O') {
                        cnt++;
                        sum += cnt;
                    } else {
                        cnt = 0;
                    }
                } // end for
                bw.write(sum + "\n");
            } // end while
            bw.flush();

            br.close();
            bw.close();
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }
    }
}
