import sys
num = int(sys.stdin.readline())
words = []
for _ in range(num):
    words.append(sys.stdin.readline().rstrip())

words.sort()
count = 0

for i in range(num):
    if i == num - 1:
        count += 1
    else:
        if not words[i+1].startswith(words[i]):
            count += 1

print(count)