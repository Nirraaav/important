import sys

sys.set_int_max_str_digits(100000000)

t = [2]
N = int(input())
for _ in range(N):
	t.append(t[-1] * (t[-1] - 1) + 1)

h = sum(1/(x - 1) for x in t)
print(len(str(t[-1])))
print(h)