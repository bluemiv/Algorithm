package Ex1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Ex1260 {
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final StringTokenizer st = new StringTokenizer(br.readLine());
        final int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        final int initPoint = Integer.parseInt(st.nextToken());

        final ArrayList<Integer>[] list = new ArrayList[n+1];
        for(int i=0; i<n+1; i++) {
            list[i] = new ArrayList<Integer>();
        }
        while(m-- > 0) {
            final StringTokenizer st2 = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st2.nextToken());
            int num2 = Integer.parseInt(st2.nextToken());
            list[num].add(num2);
            list[num2].add(num);
        }
        for(int i=0; i<n+1; i++) {
            Collections.sort(list[i]);
        }

        dfs(list, initPoint, new boolean[n+1]);
        System.out.println();

        bfs(list, initPoint, new LinkedList<>(), new boolean[n+1]);
    }

    public static void dfs(ArrayList<Integer>[] list, int initPoint, boolean[] visit) {
        System.out.print(initPoint + " ");
        visit[initPoint] = true;
        for(int i=0; i<list[initPoint].size(); i++) {
            final int nextPoint = list[initPoint].get(i);
            if(!visit[nextPoint]) {
                dfs(list, nextPoint, visit);
            }
        }
    }

    public static void bfs(ArrayList<Integer>[] list, int initPoint, Queue<Integer> q, boolean[] visit) {
        q.add(initPoint);
        while(!q.isEmpty()) {
            final int currentPoint = q.poll();
            System.out.print(currentPoint + " ");
            visit[currentPoint] = true;
            for(int i=0; i<list[currentPoint].size(); i++) {
                final int nextPoint = list[currentPoint].get(i);
                if(!visit[nextPoint]) {
                    visit[nextPoint] = true;
                    q.add(nextPoint);
                }
            }
        }
    }
}
