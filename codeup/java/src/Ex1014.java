import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ex1014 {
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final Float floatNum = Float.parseFloat(br.readLine());
        System.out.printf("%.2f", floatNum);
    }
}

