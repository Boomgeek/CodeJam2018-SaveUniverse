def swap(c, i, j):
    c = list(c)
    c[i], c[j] = c[j], c[i]
    return ''.join(c)


def swapProgram(program):
    reverseProgram = program[::-1]
    for i, char in enumerate(reverseProgram):
        preChar = reverseProgram[i-1]
        if i != 0 and (char == 'C' and preChar == 'S'):
            return swap(reverseProgram, i, i-1)[::-1]
    return program


def calculateDamage(program):
    damage = 0
    strength = 1
    for i in range(0, len(program)):
        if program[i] == 'S':
            damage += strength
        else:
            strength += strength
    return damage


def calMinDamage(program):
    return program.count('S')


def savingUniverse(shield, program):
    minDm = calMinDamage(program)
    currentDm = calculateDamage(program)

    if shield < minDm:
        return "IMPOSSIBLE"
    elif currentDm <= shield:
        return 0

    count = 1
    while True:
        program = swapProgram(program)
        nowDm = calculateDamage(program)
        if nowDm <= shield:
            break
        else:
            count += 1
    return count


def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        # read a list of integers, 2 in this case
        n, m = [s for s in input().split(" ")]

        # process
        print('Case #{0}: {1}'.format(i, savingUniverse(int(n), m)))


if __name__ == "__main__":
    main()
