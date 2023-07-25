
def draw_star(n, row, col):
    if n == 3 and row < size and col <size:
       str_list[row][col] = "*"
       str_list[row][col+1] = "*"
       str_list[row][col+2] = "*"
       str_list[row+1][col] = "*"
       #str_list[row+1][col+1] = " "
       str_list[row+1][col+2] = "*"
       str_list[row+2][col] = "*"
       str_list[row+2][col+1] = "*"
       str_list[row+2][col+2] = "*"
    else:
        draw_star(n/3, int(row), int(col))
        draw_star(n/3, int(row + n/3), int(col))
        draw_star(n/3, int(row + n/3 * 2), int(col))
        draw_star(n/3, int(row), int(col + n/3))
        #draw_star(n/3, int(row + n/3), int(col + n/3))
        draw_star(n/3, int(row + n/3 * 2), int(col + n/3))
        draw_star(n/3, int(row), int(col + n/3 * 2))
        draw_star(n/3, int(row + n/3), int(col + n/3 * 2))
        draw_star(n/3, int(row + n/3 * 2), int(col + n/3 * 2))
    

n = int(input())
str_list = [[" " for _ in range(n)] for _ in range(n)]
size = len(str_list)
draw_star(n, 0, 0)
for idx in range(len(str_list)):
    print("".join(str_list[idx]))