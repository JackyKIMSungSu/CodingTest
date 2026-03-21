import sys
import re
# input = sys.stdin.readline

line = input().replace(',', '').rstrip(';\n').split()

# 입력받은 선언을 타입과 변수명으로 나눠서 사용
t, vars = line[0], line[1:]

# 변수명과 기호(&, *, [])를 분리하는 패턴
pattern = re.compile(r'([a-zA-Z]+)|([^a-zA-Z]+)')

for v in vars:
    p = pattern.findall(v)
    p = [''.join(x) for x in p]

    # 변수 타입을 먼저 붙이고 기호를 붙여나감
    ans = t
    ans += p[-1][::-1].replace('][', '[]') if len(p) == 2 else ''
    # ']['를 '[]'로 치환하는 이유:
    # 각 기호를 역순으로 붙이고 있기 때문에 뒤집힌 괄호를 교정

    print(f'{ans} {p[0]};')
