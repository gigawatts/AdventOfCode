#!/usr/bin/env python
## https://adventofcode.com/2021/day/2/input

filename = "input-day02.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

print(f'line count: {len(lines)}')


def part1():
    print('\n### Part 1 ###')

    horizontal = 0  # forward + x
    depth = 0  # down + x  # up - x

    for idx, val in enumerate(lines):
        # print(idx, val)
        line = val.split(' ',2)
        dir = line[0]
        units = int(line[1])
        # print(f'direction: {dir}  units: {units}')
        if dir == 'forward':
            horizontal += units
        if dir == 'down':
            depth += units
        if dir == 'up':
            depth -= units

    ans = horizontal * depth
    print(f'Horizontal: {horizontal}')
    print(f'Depth: {depth}')
    print(f'Answer: {ans}')



def part2():
    print('\n### Part 2 ###')

    horizontal = 0
    depth = 0
    aim = 0

    for idx, val in enumerate(lines):
        line = val.split(' ',2)
        dir = line[0]
        units = int(line[1])

        if dir == 'forward':
            horizontal += units
            depth += (aim * units)
        if dir == 'down':
            aim += units
        if dir == 'up':
            aim -= units

    ans = horizontal * depth
    print(f'Horizontal: {horizontal}')
    print(f'Depth: {depth}')
    print(f'Answer: {ans}')


part1()
part2()