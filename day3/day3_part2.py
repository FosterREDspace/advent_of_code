def largest_k_digit_subsequence(digits, k):
	stack = []
	to_remove = len(digits) - k
	for digit in digits:
		while stack and to_remove > 0 and stack[-1] < digit:
			stack.pop()
			to_remove -= 1
		stack.append(digit)
	return stack[:k]

def main():
	with open("day3/day3.text", "r") as f:
		lines = f.readlines()
	k = 12
	total = 0
	for line in lines:
		digits = [int(char) for char in line.strip()]
		largest_digits = largest_k_digit_subsequence(digits, k)
		num = int(''.join(str(d) for d in largest_digits))
		print(num)
		total += num
	print("Total output:",total)

if __name__ == "__main__":
	main()
