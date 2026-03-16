ip = input().strip()

if "::" in ip:
    left, right = ip.split("::")
    left_parts = left.split(":") if left else []
    right_parts = right.split(":") if right else []

    missing = 8 - (len(left_parts) + len(right_parts))
    parts = left_parts + (["0"] * missing) + right_parts
else:
    parts = ip.split(":")

parts = [p.zfill(4) for p in parts]

print(":".join(parts))