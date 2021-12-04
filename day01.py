#!/usr/bin/env python
## https://adventofcode.com/2021/day/1/input

filename = "input-day01.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# with open(filename) as file:
#     while (line := file.readline().rstrip()):
#         print(line)

print(f'line count: {len(lines)}')

def part1():
    print('\n### Part 1 ###')

    inc = 0
    dec = 0

    for idx, val in enumerate(lines):
        # print(idx, val)
        if idx == 0:
            inc += 1
        else:
            if val > lines[idx-1]:
                inc += 1
                # print(idx, val, "inc")
                # results.append("inc")
            else:
                dec += 1
                # print(idx, val, "dec")

    print(f'Increased: {inc}')
    print(f'Decreased: {dec}')


def part2():
    print('\n### Part 2 ###')
    inc = 0
    dec = 0
    sum = []

    for idx, val in enumerate(lines):
        if idx+2 < len(lines)-1:
            s = 0
            s = int(lines[idx]) + int(lines[idx+1]) + int(lines[idx+2])
            # print(idx, val, s)
            sum.append(s)

    # print(sum)

    for idx, val in enumerate(sum):
        if idx == 0:
            inc += 1
        else:
            if val > sum[idx-1]:
                inc += 1
            else:
                dec += 1

    print(f'Increased: {inc}')
    print(f'Decreased: {dec}')

part1()
part2()