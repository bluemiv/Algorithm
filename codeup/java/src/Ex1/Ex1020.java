package Ex1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ex1020 {
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final String input = br.readLine();
        
        // 하이폰(-)으로 split
        final String[] numbers = input.split("-");
        
        // String.join()으로 재결합
        System.out.println(String.join("", numbers));
    }
}

