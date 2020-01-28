import time
# 문자열 펠린드롬
def str_pelindrome(word):
    return str(word) == str(word)[::-1]

# 정수형 펠린드롬
def pelindrome(num):
    if num < 0:
        return False  # 음수는 무조건 False

    pe = 0
    tmp = num
    while tmp > 0:
        pe *= 10
        pe += tmp % 10
        tmp //= 10

    return num == pe

# main
if __name__ ==  "__main__":
    start = time.time()
    test_case = [12345, -101, 12421]

    for test in test_case:
        print("Input:", test,"| Output:", pelindrome(test))
    
    end = time.time()
    print(start, end, end - start)