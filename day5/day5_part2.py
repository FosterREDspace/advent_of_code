def parse_ranges(filename):
	with open(filename, 'r') as f:
		lines = [line.strip() for line in f if line.strip() != '']
	ranges = []
	for line in lines:
		if '-' in line:
			start, end = map(int, line.split('-'))
			ranges.append((start, end))
		else:
			break
	return ranges


def merge_ranges(ranges):
	if not ranges:
		return []
	ranges.sort()
	merged = [ranges[0]]
	for current in ranges[1:]:
		last_start, last_end = merged[-1]
		curr_start, curr_end = current
		if curr_start <= last_end:
			merged[-1] = (last_start, max(last_end, curr_end))
		else:
			merged.append(current)
	return merged

def main():
	ranges = parse_ranges('day5/day5.text')
	merged = merge_ranges(ranges)
	total_fresh = sum(end - start + 1 for start, end in merged)
	print("Total number of unique fresh ingredient IDs:", total_fresh)

if __name__ == "__main__":
	main()
