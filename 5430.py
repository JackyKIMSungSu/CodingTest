import sys
import ast

case = int(sys.stdin.readline())
for _ in range(case):
    fun_list = sys.stdin.readline().rstrip()
    list_num = int(sys.stdin.readline())
    num_list = ast.literal_eval(sys.stdin.readline().rstrip())
    # print(fun_list[1], list_num, num_list)
    reverse = False
    for fun in fun_list:
        if fun == 'R':
            reverse = not reverse
        elif fun == 'D':
            if not num_list:
                print('error')
                break
            else:
                if reverse:
                    num_list.pop()
                else:
                    num_list.pop(0)
    else:
        if reverse:
            num_list.reverse()
        print(num_list)