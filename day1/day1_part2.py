
def solve():
    instructions = []
    with open('day1/lock.text', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                letter = line[0]
                number = int(line[1:])
                instructions.append((letter, number))

    current = 50
    zero_passes = 0

    for letter, number in instructions:
        if letter == 'R':          
            hits = (current + number) // 100
            zero_passes += hits
            current = (current + number) % 100

        elif letter == 'L':
            if current == 0:
                hits = number // 100
            else:
                if number >= current:
                    hits = (number - current) // 100 + 1
                else:
                    hits = 0
            
            zero_passes += hits
            current = (current - number) % 100

    print("Final Password:", zero_passes)

if __name__ == "__main__":
    solve()
