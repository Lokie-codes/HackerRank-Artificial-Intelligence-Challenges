def nextMove(n,r,c,grid):
    for row in grid:
        if 'p' in row:          # If princess is in the row
            px = row.index('p') # Column number of princess
            py = grid.index(row)# Row number of princess
            mx = c              # Column number of bot
            my = r              # Row number of bot
            # print(f"Location of Princess : ({px}, {py})")
            # print(f"Location of Bot      : ({mx}, {my})")
        # for cell in row:
        #     print(cell)
    if mx < px:             # bot is behind the princess
        return "RIGHT"
    elif mx > px:           # bot is in front of princess
        return "LEFT"
    elif my < py:             # bot is below the princess
        return "DOWN"
    else:           # bot is above the princess
        return "UP"
    return ""

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))