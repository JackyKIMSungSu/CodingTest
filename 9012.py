import sys

input = sys.stdin.readline
num = int(input())
vps_list = []
for _ in range(num):
    input = sys.stdin.readline
    vps_list.append(input().rstrip())

def check_vps(vps):
    stack = []
    for char in vps:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return 'NO'
            stack.pop()
            
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'
    
def solve():
    for vps in vps_list:
        print(check_vps(vps))
    
    return

if __name__ == "__main__":
    solve()