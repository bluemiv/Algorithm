package Ex1;

import java.io.*;
import java.util.StringTokenizer;

public class Ex15652 {
    private final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private final static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static int n;
    private static int m;

    public static void main(String[] args) throws IOException {
        final StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        sequence(new int[m], 0);

        bw.flush();
    }

    private static void sequence(final int[] arr, final int choose) throws IOException {
        // End Point
        if(choose == m) {
            for(int num : arr) {
                bw.write(num + " ");
            }
            bw.newLine();
            return;
        }

        for(int i=1; i<=n; i++) {
            // 두번째 뽑기부터는 이전에 뽑은 값보다 크거나 같아야 함
            if(choose > 0 && arr[choose-1] > i)
                continue;

            // 뽑고, choose 값을 +1 카운팅해줌
            arr[choose] = i;
            sequence(arr, choose + 1);
        }
    }
}
