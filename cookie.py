cookie_string = """
                010000
                101101
                011011
                100100
                000000
                """
cookie_rows = [i.strip() for i in cookie_string.split('\n') if i.strip()]
cookie = []
for row in cookie_rows:
    cookie.append([int(chip) for chip in row])


def neighbour_count(cookie, x, y, cookie_type, m, n):
    if (x<m and y<n) and (x>=0 and y>=0):
        if cookie[x][y] == cookie_type:
            neighbour_count.count += 1
            cookie[x][y] = 1-cookie_type
            neighbour_count(cookie, x+1, y,   cookie_type, m, n)
            neighbour_count(cookie, x-1, y,   cookie_type, m, n)
            neighbour_count(cookie, x,   y+1, cookie_type, m, n)
            neighbour_count(cookie, x,   y-1, cookie_type, m, n)            
    return neighbour_count.count


m, n = len(cookie), len(cookie[0])
for i, row in enumerate(cookie):
    for j, col in enumerate(row):
        if col == 1:
            neighbour_count.count = 0
            print(neighbour_count(cookie, i, j, 1, m, n))
