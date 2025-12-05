def parse_ranges_and_ids(filename):
	with open(filename, 'r') as f:
		lines = [line.strip() for line in f if line.strip() != '']
	split_idx = 0
	for i, line in enumerate(lines):
		if '-' not in line:
			split_idx = i
			break
	ranges = []
	for line in lines[:split_idx]:
		start, end = map(int, line.split('-'))
		ranges.append((start, end))
	ids = [int(line) for line in lines[split_idx:]]
	return ranges, ids

def is_fresh(ingredient_id, ranges):
	for start, end in ranges:
		if start <= ingredient_id <= end:
			return True
	return False

def main():
	ranges, ids = parse_ranges_and_ids('day5/day5.text')
	fresh_count = 0
	for ingredient_id in ids:
		if is_fresh(ingredient_id, ranges):
			fresh_count += 1
	print("Number of fresh ingredient IDs:", fresh_count)

if __name__ == "__main__":
	main()
