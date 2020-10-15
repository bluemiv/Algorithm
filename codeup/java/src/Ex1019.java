import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ex1019 {
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final String input = br.readLine();
        final String[] dateInfo = input.split("\\.");
        final String year = parsingYear(dateInfo[0]);
        final String month = parsingMonth(dateInfo[1]);
        final String date = parsingMonth(dateInfo[2]);
        System.out.printf("%s.%s.%s", year, month, date);
    }

    public static String parsingYear(String num) {
        if (num.length() == 2) {
            return "00" + num;
        }
        return num;
    }

    public static String parsingMonth(String num) {
        if (num.length() == 1) {
            return "0" + num;
        }
        return num;
    }
}

