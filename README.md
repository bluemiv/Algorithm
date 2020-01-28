# 알고리즘 문제 풀이

## 1. 백준
- Site: [https://www.acmicpc.net/](https://www.acmicpc.net/)

## 2. 매일프로그래밍
- Site: [https://mailprogramming.com/](https://mailprogramming.com/)

### 2.1. 문제

#### 11번.

길이가 같은 두 문자열(`string`) `A` 와 `B`가 주어지면, `A` 가 `B` 로 1:1 암호화 가능한지 찾으시오.

Given two strings of equal length, check if two strings can be encrypted 1 to 1.

**예제**

```javascript
Input: "EGG", "FOO"
Output: True // E->F, G->O
```

```javascript
Input: "ABBCD", "APPLE"
Output: True // A->A, B->P, C->L, D->E
```

```javascript
Input: "AAB", "FOO"
Output: False
```

#### 10번.

정수 배열(`int array`)과 정수 `N`이 주어지면, `N`번째로 큰 배열 원소를 찾으시오.

Given an integer array and integer N, find the Nth largest element in the array.

**예제**

```javascript
Input: [-1, 3, -1, 5, 4], 2
Output: 4
```

```javascript
Input: [2, 4, -2, -3, 8], 1
Output: 8
```

```javascript
Input: [-5, -3, 1], 3
Output: -5
```

#### 9번.

정수 배열(`int array`)이 주어지면 `0`이 아닌 정수 순서를 유지하며 모든 `0`을 배열 오른쪽 끝으로 옮기시오. 단, 시간복잡도는 `O(n)`, 공간복잡도는 `O(1)`여야 합니다.  

**예제**
```javascript
Input: [0, 5, 0, 3, -1]
Output: [5, 3, -1, 0, 0]
```

```javascript
Input: [3, 0, 3]
Output: [3, 3, 0]
```


#### 8번.
간격(`interval`)로 이루어진 배열이 주어지면, 겹치는 간격 원소들을 합친 새로운 배열을 만드시오. 간격은 시작과 끝으로 이루어져 있으며 시작은 끝보다 작거나 같습니다.  

Given a list of intervals, merge intersecting intervals.  

**예제**
```javascript
Input: {{2,4}, {1,5}, {7,9}}
Output: {{1,5}, {7,9}}
```

```javascript
Input: {{3,6}, {1,3}, {2,4}}
Output: {{1,6}}
```

#### 7번.

정수 배열과 타겟 숫자가 주어지면, 합이 타겟값이 되는 두 원소의 인덱스를 찾으시오. 단, 시간복잡도 `O(n)` 여야 합니다.  

Given an array of integers and a target integer, find two indexes of the array element that sums to the target number.  

**예제**
```javascript
Input: [2, 5, 6, 1, 10], 타겟 8
Output: [0, 2] // 배열[0] + 배열[2] = 8
```

#### 6번.

주어진 `string` 에 모든 단어를 거꾸로 하시오.  

Reverse all the words in the given string.  

**예제**
```javascript
Input: "abc 123 apple"
Output: "cba 321 elppa"
```

#### 5번.

정수 `n`이 주어지면, `n`개의 여는 괄호 `"("`와 `n`개의 닫는 괄호 `")"`로 만들 수 있는 괄호 조합을 모두 구하시오. (시간 복잡도 제한 없습니다).  

Given an integer N, find the number of possible balanced parentheses with N opening and closing brackets.  

**예제**
```javascript
Input: 1
Output: ["()"]
```

```javascript
Input: 2
Output: ["(())", "()()"]
```

```javascript
Input: 3
Output: ["((()))", "(()())", "()(())", "(())()", "()()()"]
```

#### 4번.

문자열 배열(`string array`)이 주어지면, 제일 긴 공통된 접두사(`prefix`)의 길이를 찾으시오.  

Given an array of strings, find the longest common prefix of all strings.  

**예제**
```javascript
Input: ["apple", "apps", "ape"]
Output: 2 // "ap"
```

```javascript
Input: ["hawaii", "happy"]
Output: 2 // "ha"
```

```javascript
Input: ["dog", "dogs", "doge"]
Output: 3 // "dog"
```

#### 3번.

피보나치 배열은 `0`과 `1`로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다. 정수 `N`이 주어지면, `N`보다 작은 모든 짝수 피보나치 수의 합을 구하여라.  

Fibonacci sequence starts with 0 and 1 where each fibonacci number is a sum of two previous fibonacci numbers. Given an integer N, find the sum of all even fibonacci numbers.  

**예제**
```javascript
Input: N = 12
Output: 10 // 0, 1, 2, 3, 5, 8 중 짝수인 2 + 8 = 10.
```


#### 2번.

정수 배열(`int array`)가 주어지면 가장 큰 이어지는 원소들의 합을 구하시오. 단, 시간복잡도는 `O(n)`.  

Given an integer array, find the largest consecutive sum of elements.  

**예제**
```javascript
Input: [-1, 3, -1, 5]
Output: 7 // 3 + (-1) + 5
```

```javascript
Input: [-5, -3, -1]
Output: -1 // -1
```

```javascript
Input: [2, 4, -2, -3, 8]
Output: 9 // 2 + 4 + (-2) + (-3) + 8
```


#### 1번.

정수(`int`)가 주어지면, 팰린드롬(`palindrome`)인지 알아 내시오. 팰린드롬이란, 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어를 말합니다. 단, 정수를 문자열로 바꾸면 안됩니다.  


**예제**

```javascript
Input: 12345
Output: false
```

```javascript
Input: -101
Output: false
```

```javascript
Input: 12421
Output: true
```

