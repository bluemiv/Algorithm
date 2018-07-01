package baekjoon.java;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Ex2920 {

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		try {
			String[] input = br.readLine().trim().split(" ");
			int[] data = new int[input.length];
			
			int i;
			for(i=0; i<input.length; i++) {
				data[i] = Integer.parseInt(input[i]);
			}
			int result = 0;
			for(i=1; i<input.length-1; i++) {
				if(data[0] == 1) {
					if(data[i]+1 == data[i+1]) {
						result = 0;
					}else {
						result = 2;
						break;
					}
				}else if(data[0] == 8) {
					if(data[i]-1 == data[i+1]) {
						result = 1;
					}else {
						result = 2;
						break;
					}
				}else {
					result = 2;
					break;
				}
			}
			
			if(result == 0) {
				bw.write("ascending");
			}else if(result == 1) {
				bw.write("descending");
			}else {
				bw.write("mixed");
			}
			
			
			bw.flush();
			br.close();
			bw.close();
		} catch (Exception e) {
			// TODO: handle exception
		}
	}
}
