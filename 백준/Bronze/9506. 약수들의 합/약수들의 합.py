while True:
    n = int(input())
    if n == -1:
        break

    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)

    print(f"{n} = {' + '.join(map(str, arr))}" if sum(arr) == n else f"{n} is NOT perfect.")
