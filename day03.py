#!/usr/bin/env python
## https://adventofcode.com/2021/day/3/input

filename = "input-day03.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

print(f'line count: {len(lines)}')


def part1():
    print('\n### Part 1 ###')

    zero_list = []
    one_list = []
    for b in range(0, 12):
        zero_count = 0
        one_count = 0

        for idx, val in enumerate(lines):
            if val[b] == str(0):
                zero_count += 1
            elif val[b] == str(1):
                one_count += 1
        
        zero_list.append(zero_count)
        one_list.append(one_count)

    print(f'zeros: {zero_list}')
    print(f'ones : {one_list}')

    gamma = ""
    epsilon = ""
    for b in range(0, 12):
        if zero_list[b] > one_list[b]:
            gamma += str(0)
            epsilon += str(1)
        elif zero_list[b] < one_list[b]:
            gamma += str(1)
            epsilon += str(0)
    
    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)
    ans = gamma_dec * epsilon_dec
    print(f'gamma: {gamma} {gamma_dec}')
    print(f'epsilon: {epsilon} {epsilon_dec}')
    print(f'Answer: {ans}')



def part2():
    print('\n### Part 2 ###')


    print(f'Answer: {ans}')


part1()
part2()