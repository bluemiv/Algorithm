package Ex1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ex1023 {
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final String input = br.readLine();
        final String[] nums = input.split("\\.");

        System.out.println(nums[0]);
        System.out.println(Integer.parseInt(nums[1]));
    }
}
