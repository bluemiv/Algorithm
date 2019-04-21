package baekjoon.java01;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Ex10828 {

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			int n = Integer.parseInt(br.readLine());
			MyStack stack = new MyStack();
			String input = "";
			while(n-->0) {
				input = br.readLine();
				if(input.toLowerCase().contains("push")) {
					int item = Integer.parseInt(input.split(" ")[1]);
					stack.push(item);
				}else if(input.toLowerCase().contains("pop")) {
					System.out.println(stack.pop());
				}else if(input.toLowerCase().contains("size")) {
					System.out.println(stack.size());
				}else if(input.toLowerCase().contains("empty")) {
					System.out.println(stack.empty());
				}else if(input.toLowerCase().contains("top")) {
					System.out.println(stack.top());
				}else{
					return;
				}
			}
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		
	}
	
}

class MyStack {
/*
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
*/
	ArrayList<Object> data;
	MyStack(){
		data = new ArrayList<Object>();
	}
	
	void push(Object item) {
		// 값이 없을때
		if(item == null) {
			return;
		}
		data.add(item);
//		System.out.println("item:" + item);
	}
	
	Object pop() {
		// stack에 값이 없는경우
		if(data.isEmpty()) {
			return -1;
		}
		
		return data.remove(data.size()-1);
	}

	int size() {
		return data.size();
	}
	
	int empty() {
		// 비어있는 경우
		if(data.isEmpty()) return 1;
		
		// 안 비어있는 경우
		return 0;
	}
	Object top() {
		if(data.isEmpty()) return -1;
		return data.get(data.size()-1);
	}
}
