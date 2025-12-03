pairs = []
with open('day2/day2key.text', 'r') as f:
	content = f.read().strip()
	groups = content.split(',')
	for group in groups:
		start, end = group.split('-')
		pairs.append((int(start), int(end)))

def is_repeated_sequence(n):
	s = str(n)
	l = len(s)
	for size in range(1, l // 2 + 1):
		if l % size == 0:
			part = s[:size]
			if part * (l // size) == s:
				return True
	return False

invalid_sum = 0
for start, end in pairs:
	for num in range(start, end + 1):
		if is_repeated_sequence(num):
			invalid_sum += num
print("Sum of all invalid IDs:", invalid_sum)


