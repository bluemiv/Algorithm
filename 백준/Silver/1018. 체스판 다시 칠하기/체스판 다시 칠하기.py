n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(input()))

wb_row = ["W" if i % 2 == 0 else "B" for i in range(m)]
bw_row = ["B" if i % 2 == 0 else "W" for i in range(m)]

wb_board = []
for i in range(n):
    wb_board.append(wb_row if i % 2 == 0 else bw_row)

bw_board = []
for i in range(n):
    bw_board.append(bw_row if i % 2 == 0 else wb_row)

ret = 8 * 8
for dy in range(n - 8 + 1):
    for dx in range(m - 8 + 1):
        wb_cnt = 0
        bw_cnt = 0
        for i in range(dy, dy + 8):
            for j in range(dx, dx + 8):
                if board[i][j] != wb_board[i][j]:
                    wb_cnt += 1
                if board[i][j] != bw_board[i][j]:
                    bw_cnt += 1
        tmp = min(wb_cnt, bw_cnt)
        ret = min(ret, tmp)
print(ret)
