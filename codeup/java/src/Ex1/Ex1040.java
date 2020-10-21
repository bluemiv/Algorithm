package Ex1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Ex1039 {
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final StringTokenizer st = new StringTokenizer(br.readLine());
        final long[] nums = {Long.parseLong(st.nextToken()), Long.parseLong(st.nextToken())};
        System.out.println(nums[0] + nums[1]);
    }
}