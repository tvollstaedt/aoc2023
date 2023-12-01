def part1(input: str):
    num_sum = 0
    for line in input.split():
        numbers = [int(num) for num in line if num.isdigit()]
        num_sum += int(str(numbers[0]) + str(numbers[-1])) if len(numbers) > 0 else 0
    return num_sum


def part2(input: str):
    number_map = {
        'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r',
        'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'ei8t', 'nine': 'ni9e'
    }
    for number in number_map:
        input = input.replace(number, number_map[number])
    return part1(input)
