def largest_two_digit(nums):
	max_num = 0
	n = len(nums)
	for i in range(n - 1):
		tens = nums[i]
		ones = max(nums[i+1:])
		num = 10 * tens + ones
		if num > max_num:
			max_num = num
	return max_num

def main():
	with open("day3/day3.text", "r") as f:
		lines = f.readlines()
	number_tuples = [tuple(int(char) for char in line.strip()) for line in lines]
	largest_numbers = [largest_two_digit(tup) for tup in number_tuples]
	total = 0
	for num in largest_numbers:
		total += num
		print(num)
	print("Total output:",total)
	
if __name__ == "__main__":
	main()
