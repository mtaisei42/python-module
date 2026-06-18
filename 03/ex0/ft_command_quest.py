import sys

print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
total = len(sys.argv)
if total == 1:
    print("No arguments provided!")
else:
    print(f"Arguments received: {total-1}")
    for i in range(1,total):
        print(f"Arguments {i}: {sys.argv[i]}")
print(f"Total arguments: {total}")
