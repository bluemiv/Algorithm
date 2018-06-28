package baekjoon.java;

public class Ex4673 {

	private static boolean[] check = new boolean[10000];
	public static void main(String[] args) {
		int i;
		for(i=1; i<10000; i++) {
			d(i);
		}
		
		for(i=1; i<10000; i++) {
			if(!check[i]) {
				System.out.println(i);
			}
		}
	}
	
	private static int d(int n) {
		
		int sum = 0;
		if(n<10) {
			// 1의자리
			sum = 2*n;
			check[sum]= true;
			
		}else if(n >=10 & n<100) {
			// 10의 자리
			int[] num = new int[2]; // 33
			num[0] = n/10; // 3
			num[1] = n%10; // 3
			sum = n + num[0] + num[1]; // 33 + 3 + 3 = 39
			check[sum] = true;
			
		}else if(n >=100 & n<1000) {
			// 100의 자리
			int[] num = new int[3]; // 120
			num[0] = n/100; // 1
			num[1] = (n%100)/10; // 2
			num[2] = n%10; // 0
			sum = n + num[0] + num[1] + num[2]; // 120 + 1 + 2 + 0 = 123
			check[sum] = true;
			
		}else if(n >=1000 & n<10000) {
			// 1000의 자리
			int[] num = new int[4]; // 9913
			num[0] = n/1000; // 9
			num[1] = (n%1000)/100; // 9
			num[2] = (n%100)/10; // 1
			num[3] = n%10; // 3
			sum = n + num[0] + num[1] + num[2] + num[3]; // 9913 + 9 + 9 + 1 + 3 = 9935
			if(sum >= 10000) {
				return 0;
			}
			check[sum] = true;
			
		}else {
			return 0;
		}
		return d(sum);
	}
}
