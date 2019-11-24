n = int(input())
# hight = 2 * n + 2
# dot1stloop = n
# 1st line n+1 "." on each side, N*2 + 1 * "-" in the middle
# 2nd line dots, // on each side + n * 2 - 1 "-"
# 3rd line dots, // on each side, n*2 + 1 "-"
# middle line not including // and \\ is n*4 - 1 characters, stop! in the middle -> dashes each side = n*4 -1 - 5 //2

mid_dash = ((n*4)-6)//2
dot_1st_line = n + 1
dash_1st_line = n * 2 + 1
dash_1st_loop = n * 2 - 1
dot_1st_loop = n
row2 = 1
dot2nd_loop = row2
dash_2nd_loop = n*4 - 3

print(dot_1st_line * "." + dash_1st_line * "-" + dot_1st_line * ".")
for row in range(n):
    print(dot_1st_loop * "." + "//" + dash_1st_loop * "-" + "\\\\" + dot_1st_loop * ".")
    dot_1st_loop -=1
    dash_1st_loop += 2
print("//" + mid_dash * "-" + "STOP!" + mid_dash * "-" + "\\\\")
print("\\\\" + ((n*4)-1) * '-' + "//")

for row2 in range(1, n):
        print(dot2nd_loop * "." + "\\\\" + dash_2nd_loop * "-" + "//" + dot2nd_loop * ".")
        dot2nd_loop +=1
        dash_2nd_loop -=2



