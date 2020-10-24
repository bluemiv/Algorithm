package Ex7;

import java.io.*;
import java.util.*;

public class Ex7576 {
    // 상하좌우 이동을 위한 정수형 배열 생성
    private static final int[] deltaX = {1, -1, 0, 0};
    private static final int[] deltaY = {0, 0, 1, -1};

    // 콘솔 입출력
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int[][] matrix;
    private static int m;
    private static int n;

    private static final int NOT_RIPE = 0;

    public static void main(String[] args) throws IOException {
        final StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        matrix = new int[n][m];

        for(int i=0; i<n; i++) {
            final StringTokenizer tempSt = new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++) {
                matrix[i][j] = Integer.parseInt(tempSt.nextToken());
            }
        }

        int result = bfs();

        // 결과 출력
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if (matrix[i][j] == NOT_RIPE) {
                    bw.write("-1");
                    bw.flush();
                    return;
                }
            }
        }
        bw.write(result + "");
        bw.flush();
    }

    private static int bfs() {
        final Queue<Map<String, Integer>> q = new LinkedList<>();

        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(matrix[i][j] == 1) {
                    final Map<String, Integer> initPoint = new HashMap<>();
                    initPoint.put("x", i);
                    initPoint.put("y", j);
                    initPoint.put("day", 0);
                    q.offer(initPoint);
                }
            }
        }

        int day = 0;
        while(!q.isEmpty()) {
            final Map<String, Integer> curPoint = q.poll();
            day = curPoint.get("day");

            for(int i=0; i<4; i++) {
                final int nextX = curPoint.get("x") + deltaX[i];
                final int nextY = curPoint.get("y") + deltaY[i];

                if(nextX >= 0 && nextX < n && nextY >= 0 && nextY < m) {
                    if(matrix[nextX][nextY] == NOT_RIPE) {
                        matrix[nextX][nextY] = matrix[curPoint.get("x")][curPoint.get("y")] + 1;

                        final Map<String, Integer> nextPoint = new HashMap<>();
                        nextPoint.put("x", nextX);
                        nextPoint.put("y", nextY);
                        nextPoint.put("day", curPoint.get("day") + 1);
                        q.offer(nextPoint);
                    }
                }
            }
        }
        return day;
    }
}
