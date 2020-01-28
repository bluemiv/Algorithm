import sys

def solution2(arr, target):
    """시간복잡도 O(n^2), 공간복잡도 O(n)"""
    for i, item in enumerate(arr):
        new_target = target - item
        
        for j, item2 in enumerate(arr):
            if new_target == item2:
                return (i, j)
                
    return tuple()


def solution(arr, target):
    """시간복잡도 O(n), 공간복잡도 O(n)
    
    시간복잡도를 줄이기 위해 dictionary를 이용.
    key값을 가지고 value를 가지고 오기 때문에,
    시간복잡도는 O(1)로 연산 됨.
    """
    _dict = dict()

    for i, item in enumerate(arr):
        if _dict.get(target-item, None) is None:
            _dict[item] = i
        else:
            return (_dict[target-item], i)

    return tuple()


if __name__ == "__main__":
    arr = list(map(lambda x: int(x.strip()), sys.stdin.readline().split(",")))
    target = int(sys.stdin.readline())
    rst = solution(arr, target)
    print(rst)
