package baekjoon.java;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Ex1110 {

	public static void main(String[] args) {
		int cnt = 0;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			// n 설정
			String n = br.readLine();
			if(n.length() < 2) n = "0" + n;

			int first = n.charAt(0) - 48;
			int second = n.charAt(1) - 48;
			
			String new_n="";
			while(!n.equals(new_n)) {
				if(!new_n.equals("")) {
					first = new_n.charAt(0) - 48;
					second = new_n.charAt(1) - 48;
				}
				int sum = first + second;
				
				new_n = second + "" + (sum % 10);
				
				cnt++;
			}
			
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		System.out.print(cnt);
	}
}
