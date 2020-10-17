package Ex1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ex1025 {
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final char[] input = br.readLine().toCharArray();

        for(int i=0; i<input.length; i++) {
            int temp = (int) ((input[i] - '0') * Math.pow(10, input.length-i-1));
            System.out.printf("[%s]\n", temp);
        }
    }
}
