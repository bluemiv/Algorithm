package Ex1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ex1024 {
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final char[] arr = br.readLine().toCharArray();
        for(char c : arr) {
            System.out.println("'" + c + "'");
        }
    }
}
