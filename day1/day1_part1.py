result = []
with open('day1/lock.text', 'r') as f:
	for line in f:
		line = line.strip()
		if line:
			letter = line[0]
			number = int(line[1:])
			result.append((letter, number))

current = 50
zero_counter = 0
for letter, number in result:
	if letter == 'R':
		current = (current + number) % 100
	elif letter == 'L':
		current = (current - number) % 100
	if current == 0:
		zero_counter += 1

print("Final value:", current)
print("Landed on 0:" , zero_counter, "times")
