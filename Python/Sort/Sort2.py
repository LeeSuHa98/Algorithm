import sys

N = int(input())
arr = [int(sys.stdin.readline()) for _ in range(N)]
sys.stdout.write("\n".join(map(str, sorted(arr))))