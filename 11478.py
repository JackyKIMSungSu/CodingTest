import sys

str1 = sys.stdin.readline().rstrip()

subset = set()

for i in range(len(str1)):
    subset.add(str1[i])
    for j in range(i+1, len(str1)+1):
        subset.add(str1[i:j])   

print(len(subset))