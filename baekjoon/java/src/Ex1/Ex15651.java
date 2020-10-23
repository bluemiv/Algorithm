package Ex1;

import java.io.*;
import java.util.StringTokenizer;

public class Ex15651 {

    private static int n;
    private static int m;
    private static int choose = 0;
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        sequence(new int[m], 0);

        bw.flush();
    }

    public static void sequence(final int[] arr, int choose) throws IOException {
        // End Point
        if(choose == m) {
            for(int num : arr) {
                bw.write(num + " ");
            }
            bw.newLine();
            return;
        }

        for(int i=1; i<=n; i++) {
            arr[choose] = i;
            sequence(arr, choose+1);
        }
    }
}
