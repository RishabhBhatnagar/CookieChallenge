def neighbour_count(cookie, x, y, choco_chip, m, n):
    if (x<m and y<n) and (x>=0 and y>=0):
        if cookie[x][y] == choco_chip:
            # current chip is chocolate chip.
            # counting current chip.
            neighbour_count.count += 1
            # replacing current cell value to non choco chip value
            cookie[x][y] = 1-choco_chip
            
            # running this algo for neighbouring cells.
            neighbour_count(cookie, x+1, y,   choco_chip, m, n) # right
            neighbour_count(cookie, x-1, y,   choco_chip, m, n) # left
            neighbour_count(cookie, x,   y+1, choco_chip, m, n) # top
            neighbour_count(cookie, x,   y-1, choco_chip, m, n) # down
                  
    return neighbour_count.count

def main(cookie, choco_chip):
    m, n = len(cookie), len(cookie[0])
    for i, row in enumerate(cookie):
        for j, col in enumerate(row):
            if col == choco_chip:      # checking if curent_cell is a choco_chip
                neighbour_count.count = 0
                yield neighbour_count(cookie, i, j, choco_chip, m, n)


if __name__ == '__main__':
    choco_chip = 1
    cookie_string = """010000
                       101101
                       011011
                       100100
                       000000"""
    cookie = [[int(chip) for chip in row.strip()] for row in cookie_string.split('\n')]
    print(list(main(cookie, choco_chip)))
