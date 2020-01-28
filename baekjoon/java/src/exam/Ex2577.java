package exam;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Ex2577 {

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            String[] input = new String[3];
            input[0] = br.readLine();
            input[1] = br.readLine();
            input[2] = br.readLine();

            int mul = 1;
            int i;
            for (i = 0; i < 3; i++) {
                mul *= Integer.parseInt(input[i]);
            }
//			System.out.println(mul);

            int[] check = new int[10];
            while (mul > 0) {
                check[mul % 10]++;
                mul /= 10;
            }

            for (i = 0; i < 10; i++) {
                System.out.println(check[i]);
            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }
    }
}
