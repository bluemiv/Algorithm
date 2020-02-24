package recursive;

import java.util.Stack;

public class PowerSet {
    private static final int n = 5;
    private static final char[] characters = {'A', 'B', 'C', 'D', 'E'};

    public static void main(String[] args) {
        final Stack<Integer> stack = new Stack<>();
        search(stack, 1);

        final Stack<Character> stack2 = new Stack<>();
        search2(stack2, 0);
    }

    private static void search(Stack<Integer> stack, int k) {
        if(k >= n + 1) {
            System.out.println(stack.toString()); // 부분 집합을 출력한다.
        } else {
            // 1. k를 부분집합에 포함한다.
            stack.add(k);
            search(stack, k + 1);

            // 2. k를 부분집합에 포함하지 않는다.
            stack.pop();
            search(stack, k + 1);
        }
    }

    private static void search2(Stack<Character> stack, int k) {
        if(k >= characters.length) {
            System.out.println(stack.toString());
        } else {
            stack.push(characters[k]);
            search2(stack, k+1);

            stack.pop();
            search2(stack, k+1);
        }
    }
}
