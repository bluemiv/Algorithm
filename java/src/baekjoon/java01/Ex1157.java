package baekjoon.java01;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ex1157 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine().trim().toUpperCase();

		int[] cnt = new int[26]; // a-z
		int i;
		for(i=0; i<input.length(); i++) {
			cnt[input.charAt(i)-65]++;
		}
		
		int max = Integer.MIN_VALUE;
		for(i=0; i<26; i++) {
			if(cnt[i] > max) {
				max = cnt[i];
			}
		}
		
		StringBuilder sb = new StringBuilder();
		int check = -1;
		for(i=0; i<26; i++) {
			if(cnt[i] == max) {
				if(check != -1) {
					sb.append("?");
					System.out.print(sb.toString());
					return;
				}
				check = i;
			}
		}
			
		sb.append((char)(check+65));
		System.out.print(sb.toString());
		
	}
}
