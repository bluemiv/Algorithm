package Ex1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ex1019 {
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final String input = br.readLine();

        // 점(.)으로 문자열을 split 한다.
        final String[] dateInfo = input.split("\\.");

        // 알맞은 형태로 파싱(parsing) 해준다.
        final String year = parsingYear(dateInfo[0]);
        final String month = parsingMonth(dateInfo[1]);
        final String date = parsingMonth(dateInfo[2]);
        System.out.printf("%s.%s.%s", year, month, date);
    }

    /**
     * 4자리로 바꿔준다.
     * @param num 연도
     * @return 2자리의 연도
     */
    public static String parsingYear(String num) {
        final int YEAR_LEN = 4;
        String result = num;
        for(int i=0; i<YEAR_LEN - num.length(); i++) {
               result = "0" + result;
        }
        return result;
    }

    /**
     * 2자리로 바꿔준다.
     * @param num 월 또는 일
     * @return 2자리의 월 또는 일
     */
    public static String parsingMonth(String num) {
        if(num.length() == 1) {
            return "0" + num;
        }
        return num;
    }
}

