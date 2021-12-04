#!/usr/bin/env python
## https://adventofcode.com/2021/day/3/input

filename = "input-day03.txt"
# filename = "sample-day03.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

print(f'line count: {len(lines)}')


def part1():
    print('\n### Part 1 ###')

    zero_list = []
    one_list = []
    length = len(lines[0])
    for b in range(0, length):
        zero_count = 0
        one_count = 0

        for idx, val in enumerate(lines):
            if val[b] == str(0):
                zero_count += 1
            elif val[b] == str(1):
                one_count += 1
        
        zero_list.append(zero_count)
        one_list.append(one_count)

    print(f'zeros  : {zero_list}')
    print(f'ones   : {one_list}')

    gamma = ""
    epsilon = ""
    for b in range(0, length):
        if zero_list[b] > one_list[b]:
            gamma += str(0)
            epsilon += str(1)
        elif zero_list[b] < one_list[b]:
            gamma += str(1)
            epsilon += str(0)
    
    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)
    ans = gamma_dec * epsilon_dec
    print(f'gamma  : {gamma} = {gamma_dec}')
    print(f'epsilon: {epsilon} = {epsilon_dec}')
    print(f'Answer : {ans}')


def part2():
    print('\n### Part 2 ###')
    length = len(lines[0])
    blanks = ' ' * length
    
    #### Oxygen Generator Rating ############################
    print("Calculating Oxygen generator rating")
    oxy_lines = lines[:]
    oxy_result = 0
    oxy_zero_list = []
    oxy_one_list = []
        
    for b in range(0, length):
        print(f'## bit {b} of {length-1}')
        oxy_zero_count = 0
        oxy_one_count = 0

        for idx, val in enumerate(oxy_lines):
            if val[b] == str(0):
                oxy_zero_count += 1
            elif val[b] == str(1):
                oxy_one_count += 1
        
        oxy_zero_list.append(oxy_zero_count)
        oxy_one_list.append(oxy_one_count)
        print(f'zeros  : {oxy_zero_list}')
        print(f'ones   : {oxy_one_list}')

        oxy_temp = oxy_lines
        while(blanks in oxy_temp) :
            oxy_temp.remove(blanks)
        oxy_temp_length = len(oxy_temp)
        
        print(f'cleaned oxygen list length: {oxy_temp_length}')
        print(oxy_lines)

        if oxy_temp_length > 1:

            if oxy_zero_list[b] > oxy_one_list[b]:
                print(f'zero most common at bit {b}')
                ## keep only lines with a 0 at this bit position, delete lines with 1
                for idx2, val2 in enumerate(oxy_lines):
                    if val2[b] == str(0):
                        print(f'saving  {oxy_lines[idx2]}')
                        # oxy_result.append(oxy_lines[idx2])
                    else:
                        print(f'erasing {oxy_lines[idx2]}')
                        oxy_lines[idx2] = blanks

            elif oxy_zero_list[b] < oxy_one_list[b]:
                print(f'one most common at bit {b}')
                ## keep only lines with a 1 at this bit position
                for idx2, val2 in enumerate(oxy_lines):
                    if val2[b] == str(1):
                        print(f'saving  {oxy_lines[idx2]}')
                        # oxy_result.append(oxy_lines[idx2])
                    else:
                        print(f'erasing {oxy_lines[idx2]}')
                        oxy_lines[idx2] = blanks
            
            else:
                print(f'equal number of zeros and ones at bit {b}')
                ## keep only lines with a 1 at this bit position
                for idx2, val2 in enumerate(oxy_lines):
                    if val2[b] == str(1):
                        print(f'saving  {oxy_lines[idx2]}')
                        # oxy_result.append(oxy_lines[idx2])
                    else:
                        print(f'erasing {oxy_lines[idx2]}')
                        oxy_lines[idx2] = blanks


        else:
            print('Only one line left!')
            print(oxy_lines[0])

        if b == length-1:
            print("last bit")
            while(blanks in oxy_lines) :
                oxy_lines.remove(blanks)
            print(f'oxy result: {oxy_lines}')
            oxy_result = oxy_lines[0]



    #### CO2 Scrubber Rating ############################
    print("Calculating CO2 scrubber rating")
    co2_lines = lines[:]
    co2_result = 0
    co2_zero_list = []
    co2_one_list = []
    b=0

    for b in range(0, length):
        print(f'## bit {b} of {length-1}')
        co2_zero_count = 0
        co2_one_count = 0

        for idx, val in enumerate(co2_lines):
            if val[b] == str(0):
                co2_zero_count += 1
            elif val[b] == str(1):
                co2_one_count += 1
        
        co2_zero_list.append(co2_zero_count)
        co2_one_list.append(co2_one_count)
        print(f'zeros  : {co2_zero_list}')
        print(f'ones   : {co2_one_list}')

        co2_temp = co2_lines
        while(blanks in co2_temp) :
            co2_temp.remove(blanks)
        co2_temp_length = len(co2_temp)
        
        print(f'cleaned co2 list length: {co2_temp_length}')
        print(co2_lines)

        if co2_temp_length > 1:

            if co2_zero_list[b] < co2_one_list[b]:
                print(f'zero least common at bit {b}')
                ## keep only lines with a 0 at this bit position, delete lines with 1
                for idx2, val2 in enumerate(co2_lines):
                    if val2[b] == str(0):
                        print(f'saving  {co2_lines[idx2]}')
                        # co2_result.append(co2_lines[idx2])
                    else:
                        print(f'erasing {co2_lines[idx2]}')
                        co2_lines[idx2] = blanks

            elif co2_zero_list[b] > co2_one_list[b]:
                print(f'one least common at bit {b}')
                ## keep only lines with a 1 at this bit position
                for idx2, val2 in enumerate(co2_lines):
                    if val2[b] == str(1):
                        print(f'saving  {co2_lines[idx2]}')
                        # co2_result.append(co2_lines[idx2])
                    else:
                        print(f'erasing {co2_lines[idx2]}')
                        co2_lines[idx2] = blanks
            
            else:
                print(f'equal number of zeros and ones at bit {b}')
                ## keep only lines with a 0 at this bit position
                for idx2, val2 in enumerate(co2_lines):
                    if val2[b] == str(0):
                        print(f'saving  {co2_lines[idx2]}')
                        # co2_result.append(co2_lines[idx2])
                    else:
                        print(f'erasing {co2_lines[idx2]}')
                        co2_lines[idx2] = blanks


        else:
            print('Only one line left!')
            print(co2_lines[0])

        if b == length-1:
            print("last bit")
            while(blanks in co2_lines) :
                co2_lines.remove(blanks)
            print(f'co2 result: {co2_lines}')
            co2_result = co2_lines[0]



    #### Final results #####################################
    oxy_result_dec = int(oxy_result, 2)
    co2_result_dec = int(co2_result, 2)
    ans = oxy_result_dec * co2_result_dec
    print(f'Oxygen Generator Rating: {oxy_result} = {oxy_result_dec}')
    print(f'CO2 Scrubber Rating: {co2_result} = {co2_result_dec}')
    print(f'Answer: {ans}')

part1()
part2()