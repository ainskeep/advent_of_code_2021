import helpers

lines = helpers.read_input()

master_dict = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4', 'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}

print("Part 1")
count = 0
for line in lines:
    display = line.split('|')[-1].split()

    for number in display:
        # 1 7 4 8
        if len(number) in [2, 3, 4, 7]:
            count += 1


print(f"Count: {count}")

print("Part 2")

def decode(decoder):
    decoder_map = {}
    # first, find the unique numbers
    one, two, three, four, five, six, seven, eight, nine = '', '', '', '', '', '', '', '', ''

    one = list(filter(lambda number: len(number) == 2, decoder))[0]
    four = list(filter(lambda number: len(number) == 4, decoder))[0]
    seven = list(filter(lambda number: len(number) == 3, decoder))[0]
    eight = list(filter(lambda number: len(number) == 7, decoder))[0]

    nums_with_len_five = list(filter(lambda number: len(number) == 5, decoder))
    nums_with_len_six = list(filter(lambda number: len(number) == 6, decoder))

    for num in nums_with_len_five:
        if len(set(num) - set(one)) == 3:
            three = num

    for num in nums_with_len_six:
        if len(set(num) - set(three)) == 1:
            nine = num


    decoder_map['a'] = [char for char in list(seven) if char not in list(one)][0]

    decoder_map['g'] = list(set(nine) - set(four) - set(decoder_map['a']))[0]
    decoder_map['b'] = list(set(four) - set(three))[0]

    for num in nums_with_len_five:
        b = decoder_map['b']
        if b in num:
            five = num

    for num in nums_with_len_five:
        if num != five and num != three:
            two = num

    decoder_map['f'] = list(set(one) - set(two))[0]
    decoder_map['c'] = list(set(one) - set(decoder_map['f']))[0]
    decoder_map['d'] = list(set(four) - set(seven) - set(decoder_map['b']))[0]
    decoder_map['e'] = list(set(eight) - set(nine))[0]

    return decoder_map

total = 0
for line in lines:
    decoder, display = line.split('|')

    display = display.split()
    decoder = decoder.split()


    decoder_map = decode(decoder)
    inv_decoder_map = {v: k for k, v in decoder_map.items()}
    display_val = ''
    for num in display:
        decoded_num = ''
        for char in num:
            decoded_num += inv_decoder_map[char]

        decimal_number = master_dict[''.join(sorted(decoded_num))]
        display_val += decimal_number

    total += int(display_val)


print(f"Total {total}")


