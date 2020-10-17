package Ex1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ex1027 {
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final String[] date = br.readLine().split("\\.");
        System.out.printf("%s-%s-%s", date[2], date[1], date[0]);
    }
}
