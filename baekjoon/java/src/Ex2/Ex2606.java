package Ex2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Ex2606 {

    private static int result = 0;
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));

        // 컴퓨터 수
        final int n = Integer.parseInt(br.readLine());
        // 간선 개수
        int v = Integer.parseInt(br.readLine());

        // 연결 정보를 담을 콜렉션
        final ArrayList<Integer>[] list = new ArrayList[n+1];
        for(int i=0; i<n+1; i++)
            list[i] = new ArrayList<>();
        while(v-- > 0) {
            final StringTokenizer st = new StringTokenizer(br.readLine());
            final int[] num = {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
            list[num[0]].add(num[1]);
            list[num[1]].add(num[0]);
        }

        dfs(list, 1, new boolean[n+1]);
        System.out.println(result);
    }

    public static void dfs(ArrayList<Integer>[] list, int start, boolean[] visited) {
        visited[start] = true;
        for(int i=0; i<list[start].size(); i++) {
            final int next = list[start].get(i);
            if(!visited[next]) {
                result++;
                dfs(list, next, visited);
            }
        }
    }
}
